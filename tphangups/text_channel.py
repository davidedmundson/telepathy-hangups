import telepathy
import dbus

#this implements ChannelTypeText which is almost all entirely deprecated
#we should update channel.py to implement InterfaceMessages copying and pasting code from Butterfly

class HangupsTextChannel(telepathy.server.ChannelTypeText,
        telepathy.server.ChannelInterfaceChatState):

    #TODO probably pass the conversation object from Hangups client
    def __init__(self, conn, manager, props, object_path=None):
        telepathy.server.ChannelTypeText.__init__(self, conn, manager, props,
                    object_path=object_path)

        self._implement_property_get(telepathy.CHANNEL_INTERFACE_MESSAGES, {
            'SupportedContentTypes': lambda: ["text/plain"] ,
            'MessagePartSupportFlags': lambda: 0,
            'DeliveryReportingSupport': lambda: telepathy.DELIVERY_REPORTING_SUPPORT_FLAG_RECEIVE_FAILURES,
            'PendingMessages': lambda: dbus.Array(self._pending_messages.values(), signature='aa{sv}')
            })

        self._add_immutables({
            'SupportedContentTypes': telepathy.CHANNEL_INTERFACE_MESSAGES,
            'MessagePartSupportFlags': telepathy.CHANNEL_INTERFACE_MESSAGES,
            'DeliveryReportingSupport': telepathy.CHANNEL_INTERFACE_MESSAGES,
            })

    @dbus.service.method(telepathy.CHANNEL_TYPE_TEXT, in_signature='us', out_signature='',
                         async_callbacks=('_success', '_error'))
    def Send(self, message_type, text, _success, _error):
        print ("NEW MESSAGE " + text)
        self.Received(15, 34234234, 2, 0 , 0, "Hello!")
