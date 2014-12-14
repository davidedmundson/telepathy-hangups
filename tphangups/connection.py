import telepathy
import dbus

from .text_channel import HangupsTextChannel

class HangupsConnection(telepathy.server.Connection,
        telepathy.server.ConnectionInterfaceRequests,
        telepathy.server.ConnectionInterfaceSimplePresence,
        telepathy.server.ConnectionInterfaceContacts,
        telepathy.server.ConnectionInterfaceContactList): #all other Ifaces here too #fixme, ideally i want a contact manager like the channel manager in tp-python

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
        self.other_dude = self.create_handle(telepathy.HANDLE_TYPE_CONTACT, "otherdude")

        self.set_self_handle(handle)

        #from simple presence
        self._implement_property_get(
            telepathy.CONNECTION_INTERFACE_SIMPLE_PRESENCE, {
                'Statuses' : lambda: self._protocol.statuses
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
        if self._status == telepathy.CONNECTION_STATUS_DISCONNECTED:
            #FIXME set to connecting..then actually connect
            self.StatusChanged(telepathy.CONNECTION_STATUS_CONNECTED, telepathy.CONNECTION_STATUS_REASON_REQUESTED)
            print ("connect")

    def Disconnect(self):
        self.__disconnect_reason = telepathy.CONNECTION_STATUS_REASON_REQUESTED
        print ("disconnect request")
        #FIXME

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
        #telepathy.CONNECTION_INTERFACE_SIMPLE_PRESENCE : 'presence',
        #telepathy.CONNECTION_INTERFACE_ALIASING : 'alias',
        #telepathy.CONNECTION_INTERFACE_AVATARS : 'token',
        #telepathy.CONNECTION_INTERFACE_CAPABILITIES : 'caps',
        #telepathy.CONNECTION_INTERFACE_CONTACT_CAPABILITIES : 'capabilities'
        }

    #from Contacts
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


