#!/usr/bin/python

import telepathy
import gobject
import dbus

from dbus.mainloop.glib import DBusGMainLoop

import sys

class HangupsConnectionManager(telepathy.server.ConnectionManager):
    def __init__(self):
        print ("Making manager")
        telepathy.server.ConnectionManager.__init__(self, 'hangups')
        self._implement_protocol('hangouts', HangupsProtocol) #protocol is still hangouts, _NOT_ hangups


class HangupsProtocol(telepathy.server.Protocol,
                      telepathy.server.ProtocolInterfacePresence):
    _proto_ = "hangouts"
    _englishName = "Google Hangouts"
    _vcard_field = ""
    _icon = "" #FIXME


    _mandatory_parameters = {"account" : "s"}

    _supported_interfaces = [
            telepathy.CONNECTION_INTERFACE_ALIASING,
            telepathy.CONNECTION_INTERFACE_AVATARS,
            telepathy.CONNECTION_INTERFACE_SIMPLE_PRESENCE,
            telepathy.CONNECTION_INTERFACE_CONTACTS
        ]

    _statuses = {
            "online":(
                telepathy.CONNECTION_PRESENCE_TYPE_AVAILABLE,
                True, True),
            "offline":(
                telepathy.CONNECTION_PRESENCE_TYPE_OFFLINE,
                True, False)
            }

    #claim to support 1-1 text messages
    _requestable_channel_classes = [
        ({telepathy.CHANNEL_INTERFACE + '.ChannelType': dbus.String(telepathy.CHANNEL_TYPE_TEXT),
          telepathy.CHANNEL_INTERFACE + '.TargetHandleType': dbus.UInt32(telepathy.HANDLE_TYPE_CONTACT)},
         [telepathy.CHANNEL_INTERFACE + '.TargetHandle',
          telepathy.CHANNEL_INTERFACE + '.TargetID'])]


    def __init__(self, connection_manager):
        print ("Making protocol")
        telepathy.server.Protocol.__init__(self, connection_manager, 'hangouts')
        telepathy.server.ProtocolInterfacePresence.__init__(self)

    def create_connection(self, connection_manager, parameters):
        return HangupsConnection(self, connection_manager, parameters)

    def NormalizeContact(self, contactId):
        return "BLAH"+contactId


class HangupsConnection(telepathy.server.Connection,
        telepathy.server.ConnectionInterfaceRequests,
        telepathy.server.ConnectionInterfaceSimplePresence): #all other Ifaces here too

    def __init__(self, protocol, manager, parameters):
        print ("Making Connection")
        protocol.check_parameters(parameters)
        account = str("DAVE")
        #parameters['account']

        telepathy.server.Connection.__init__(self, 'hangouts', account,
                'hangups', protocol)
        telepathy.server.ConnectionInterfaceRequests.__init__(self)
        telepathy.server.ConnectionInterfaceSimplePresence.__init__(self)

        self._channel_manager = HangupsChannelManager(self, protocol)

        #making a text channel
        props = props = {
            telepathy.CHANNEL_INTERFACE + '.ChannelType': telepathy.CHANNEL_TYPE_TEXT,
            telepathy.CHANNEL_INTERFACE + '.TargetHandle': 0,
            telepathy.CHANNEL_INTERFACE + '.TargetHandleType': telepathy.HANDLE_TYPE_CONTACT,
            telepathy.CHANNEL_INTERFACE + '.Requested': True
            }

        #self._channel_manager.channel_for_props(props, signal=True, call=True)


    def Connect(self):
        if self._status == telepathy.CONNECTION_STATUS_DISCONNECTED:
            #FIXME set to connecting..then actually connect
            self.StatusChanged(telepathy.CONNECTION_STATUS_CONNECTED, telepathy.CONNECTION_STATUS_REASON_REQUESTED)
            print ("connect")

    def Disconnect(self):
        self.__disconnect_reason = telepathy.CONNECTION_STATUS_REASON_REQUESTED
        print ("disconnect request")
        #FIXME


class HangupsChannelManager(telepathy.server.ChannelManager):
    def __init__(self, connection, protocol):
        telepathy.server.ChannelManager.__init__(self, connection)
        self.set_requestable_channel_classes(protocol.requestable_channels)
        self.implement_channel_classes(telepathy.CHANNEL_TYPE_TEXT, self._get_text_channel)

    def _get_text_channel(self, props):
        print ("Making new text channel")


class HangupsTextChannel(telepathy.server.ChannelTypeText,
        telepathy.server.ChannelInterfaceChatState):

    #TODO probably pass the conversation object from Hangups client
    def __init__(self, conn, manager, props, object_path=None):
        telepathy.server.ChannelTypeText.__init__(self, conn, manager, props,
                    object_path=object_path)

        self._implement_property_get(CHANNEL_INTERFACE_MESSAGES, {
            'SupportedContentTypes': lambda: ["text/plain"] ,
            'MessagePartSupportFlags': lambda: 0,
            'DeliveryReportingSupport': lambda: telepathy.DELIVERY_REPORTING_SUPPORT_FLAG_RECEIVE_FAILURES,
            'PendingMessages': lambda: dbus.Array(self._pending_messages2.values(), signature='aa{sv}')
            })

        self._add_immutables({
            'SupportedContentTypes': CHANNEL_INTERFACE_MESSAGES,
            'MessagePartSupportFlags': CHANNEL_INTERFACE_MESSAGES,
            'DeliveryReportingSupport': CHANNEL_INTERFACE_MESSAGES,
            })

if __name__ == '__main__':

    #this is a collection of black magic.
    dbus.set_default_main_loop(dbus.mainloop.glib.DBusGMainLoop())
    manager = HangupsConnectionManager()
    mainloop = gobject.MainLoop(is_running=True)
    mainloop.run()