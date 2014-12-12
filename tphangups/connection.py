import telepathy

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

        handle = self.create_handle(telepathy.HANDLE_TYPE_CONTACT, "self")
        self.set_self_handle(handle)

        self._channel_manager = HangupsChannelManager(self, protocol)

    def Connect(self):
        if self._status == telepathy.CONNECTION_STATUS_DISCONNECTED:
            #FIXME set to connecting..then actually connect
            self.StatusChanged(telepathy.CONNECTION_STATUS_CONNECTED, telepathy.CONNECTION_STATUS_REASON_REQUESTED)
            print ("connect")

            handle = self.create_handle(telepathy.HANDLE_TYPE_CONTACT, "monkeyface")

            #making a text channel
            props = props = {
                telepathy.CHANNEL_INTERFACE + '.ChannelType': telepathy.CHANNEL_TYPE_TEXT,
                telepathy.CHANNEL_INTERFACE + '.TargetHandle': handle.id,
                telepathy.CHANNEL_INTERFACE + '.TargetHandleType': telepathy.HANDLE_TYPE_CONTACT,
                telepathy.CHANNEL_INTERFACE + '.Requested': True
                }

            self._channel_manager.channel_for_props(props, signal=True)


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

class HangupsChannelManager(telepathy.server.ChannelManager):
    def __init__(self, connection, protocol):
        self._connection = connection
        self._protocol = protocol
        telepathy.server.ChannelManager.__init__(self, connection)
        self.set_requestable_channel_classes(protocol.requestable_channels)
        self.implement_channel_classes(telepathy.CHANNEL_TYPE_TEXT, self._get_text_channel)

    def _get_text_channel(self, props):
        print ("Making new text channel")
        return HangupsTextChannel(self._connection, self._manager, props)
