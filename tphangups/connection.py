import telepathy
import dbus

import hangups
import asyncio #maybe want to use gobject event loop? depends on python+dbus

from .text_channel import HangupsTextChannel
from os.path import expanduser


class HangupsConnection(telepathy.server.Connection,
        telepathy.server.ConnectionInterfaceRequests,
        telepathy.server.ConnectionInterfaceSimplePresence,
        telepathy.server.ConnectionInterfaceContacts,
        telepathy.server.ConnectionInterfaceContactList,
        telepathy.server.ConnectionInterfaceAliasing):

    _client = None
    _user_list = None
    _conversation_list = None

    _user_map = {}

    def __init__(self, protocol, manager, parameters):
        print ("Making Connection")
        protocol.check_parameters(parameters)
        account = str("DAVE")
        #parameters['account']

        telepathy.server.Connection.__init__(self, 'hangouts', account,
                'hangups', protocol)
        telepathy.server.ConnectionInterfaceRequests.__init__(self)
        telepathy.server.ConnectionInterfaceSimplePresence.__init__(self)
        telepathy.server.ConnectionInterfaceContacts.__init__(self)
        telepathy.server.ConnectionInterfaceContactList.__init__(self)


        handle = self.create_handle(telepathy.HANDLE_TYPE_CONTACT, "self")

        self.set_self_handle(handle)

        #from simple presence
        self._implement_property_get(
            telepathy.CONNECTION_INTERFACE_SIMPLE_PRESENCE, {
                'Statuses' : lambda: self._protocol.statuses
            })

        self._implement_property_get(
        telepathy.CONNECTION_INTERFACE_CONTACTS, {
            'ContactAttributeInterfaces' : lambda: [telepathy.CONNECTION_INTERFACE_SIMPLE_PRESENCE, telepathy.CONNECTION_INTERFACE_ALIASING],
        })

        self._implement_property_get(
        telepathy.CONNECTION_INTERFACE_CONTACT_LIST, {
            'ContactListState' : lambda: telepathy.constants.CONTACT_LIST_STATE_SUCCESS,
            'ContactListPersists' : lambda: False,
            'CanChangeContactList' : lambda: False,
            'RequestUsesMessage' : lambda: False,
            'DownloadAtConnection' : lambda: True
        })

        self._channel_manager = HangupsChannelManager(self, protocol)

    def Connect(self):
        print ("doing connect")
        if self._status == telepathy.CONNECTION_STATUS_DISCONNECTED:
            self.StatusChanged(telepathy.CONNECTION_STATUS_CONNECTING, telepathy.CONNECTION_STATUS_REASON_REQUESTED)
            cookies = hangups.auth.get_auth(None, None, expanduser("~/.hangups_auth_tmp"))
            self._client = hangups.Client(cookies)
            self._client.on_connect.add_observer(self._on_connect)
            asyncio.async(self._client.connect())

    def Disconnect(self):
        self.__disconnect_reason = telepathy.CONNECTION_STATUS_REASON_REQUESTED
        print ("disconnect request")
        self.client = None

    def _on_connect(self, initial_data):
        print("CONNECTED!!!!!!")
        self._user_list = hangups.UserList(
            self._client, initial_data.self_entity, initial_data.entities,
            initial_data.conversation_participants
        )

        for i in self._user_list._user_dict:
            user = self._user_list._user_dict[i]
            handle = self.create_handle(telepathy.HANDLE_TYPE_CONTACT, user.id_)
            self._user_map[user.id_] = handle

        self._conversation_list = hangups.ConversationList(
            self._client, initial_data.conversation_states, self._user_list,
            initial_data.sync_timestamp)

        self.StatusChanged(telepathy.CONNECTION_STATUS_CONNECTED, telepathy.CONNECTION_STATUS_REASON_REQUESTED)

    def handle(self, handle_type, handle_id):
        self.check_handle(handle_type, handle_id)
        return self._handles[handle_type, handle_id]

    #from SimplePresence
    def GetPresences(self, contacts):
        presences = dbus.Dictionary(signature='u(uss)')
        for handle_id in contacts:
            handle = self.handle(telepathy.HANDLE_TYPE_CONTACT, handle_id)
            contact = handle.name

            presence_type = telepathy.constants.CONNECTION_PRESENCE_TYPE_AVAILABLE
            presence = "online"
            personal_message = ""
            presences[handle] = dbus.Struct((presence_type, presence,
                personal_message), signature='uss')
        return presences

    def SetPresence(self, status, message):
        #pretend to do stuff :)
        pass

    attributes = {
        telepathy.CONNECTION : 'contact-id',
        telepathy.CONNECTION_INTERFACE_SIMPLE_PRESENCE : 'presence',
        telepathy.CONNECTION_INTERFACE_ALIASING : 'alias',
        #telepathy.CONNECTION_INTERFACE_AVATARS : 'token',
        #telepathy.CONNECTION_INTERFACE_CAPABILITIES : 'caps',
        #telepathy.CONNECTION_INTERFACE_CONTACT_CAPABILITIES : 'capabilities'
        }

    #from Contacts - this crap should be in telepathy-python somewhere
    def GetContactAttributes(self, handles, interfaces, hold):
        supported_interfaces = set()
        supported_interfaces.add(telepathy.CONNECTION)
        for interface in interfaces:
            if interface in self.attributes:
                supported_interfaces.add(interface)

        handle_type = telepathy.HANDLE_TYPE_CONTACT
        ret = dbus.Dictionary(signature='ua{sv}')
        for handle in handles:
            ret[handle] = dbus.Dictionary(signature='sv')

        functions = {
            telepathy.CONNECTION :
                lambda x: zip(x, self.InspectHandles(handle_type, x)),
            telepathy.CONNECTION_INTERFACE_SIMPLE_PRESENCE :
                lambda x: self.GetPresences(x).items(),
            telepathy.CONNECTION_INTERFACE_ALIASING :
                lambda x: self.GetAliases(x).items(),
            telepathy.CONNECTION_INTERFACE_AVATARS :
                lambda x: self.GetKnownAvatarTokens(x).items(),
            telepathy.CONNECTION_INTERFACE_CAPABILITIES :
                lambda x: self.GetCapabilities(x).items(),
            telepathy.CONNECTION_INTERFACE_CONTACT_CAPABILITIES :
                lambda x: self.GetContactCapabilities(x).items()
            }

        for interface in supported_interfaces:
            interface_attribute = interface + '/' + self.attributes[interface]
            results = functions[interface](handles)
            for handle, value in results:
                ret[int(handle)][interface_attribute] = value
        return ret

    # from ContactList
    def GetContactListAttributes(self, interfaces, hold):
        all_handles = []
        for (handle_type, handle) in self._handles.keys():
            if handle_type == telepathy.HANDLE_TYPE_CONTACT:
                all_handles.append(handle)
        return self.GetContactAttributes(all_handles, interfaces, hold)


    # from Aliasing
    def GetAliasFlags(self):
        return 0

    def GetAliases(self, handles):
        self.check_connected()
        ret = dbus.Dictionary(signature='us')
        for handle_id in handles:
            handle = self.handle(telepathy.HANDLE_TYPE_CONTACT, handle_id)
            user = self._user_list.get_user(handle.name)
            ret[handle_id] = user.full_name
        return ret

class HangupsChannelManager(telepathy.server.ChannelManager):
    def __init__(self, connection, protocol):
        self._connection = connection
        self._protocol = protocol
        telepathy.server.ChannelManager.__init__(self, connection)
        self.set_requestable_channel_classes(protocol.requestable_channels)
        self.implement_channel_classes(telepathy.CHANNEL_TYPE_TEXT, self._get_text_channel)

    def _get_text_channel(self, props):
        print ("Making new text channel")
        return HangupsTextChannel(self._connection, self._protocol, props)


