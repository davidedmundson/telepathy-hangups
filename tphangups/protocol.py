import telepathy
import dbus

from .connection import HangupsConnection

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