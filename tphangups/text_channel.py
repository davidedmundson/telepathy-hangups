import telepathy

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