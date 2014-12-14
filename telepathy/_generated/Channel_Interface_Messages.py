# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2008–2010 Collabora Ltd.
Copyright © 2008–2010 Nokia Corporation

    This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
USA.
  
"""

import dbus.service


class ChannelInterfaceMessages(dbus.service.Interface):
    """\
      This interface extends the Text
        interface to support more general messages, including:

      
        messages with attachments (like MIME multipart/mixed)
        groups of alternatives (like MIME multipart/alternative)
        delivery reports (which replace Text.SendError),
          addding support for protocols where the message content is not echoed
          back to the sender on failure and for receiving positive
          acknowledgements, as well as ensuring that incoming delivery reports
          are not lost if no client is handling the channel yet;
        any extra types of message we need in future
      

      Incoming messages, outgoing messages, and delivery reports are all
        represented as lists of Message_Part structures,
        with a format reminiscent of e-mail. Messages are sent by calling
        SendMessage; outgoing messages are
        announced to other clients which may be interested in the channel by
        the MessageSent signal. Incoming
        messages and delivery reports are signalled by
        MessageReceived, and are stored in the
        the PendingMessages property until
        acknowledged by calling Text.AcknowledgePendingMessages.
        Only the Handler
        for a channel should acknowledge messages; Observers
        (such as loggers) and Approvers
        for the channel may listen for incoming messages, and send messages of their own, but SHOULD NOT acknowledge messages.

      
        If observers were allowed to acknowledge messages, then messages
          might have been acknowledged before the handler even got to see the
          channel, and hence could not be shown to the user.
      

      If this interface is present, clients that support it SHOULD
        listen for the MessageSent and
        MessageReceived signals, and
        ignore the Sent,
        SendError
        and Received
        signals on the Text interface (which are guaranteed to duplicate
        signals from this interface).

      Although this specification supports formatted (rich-text)
        messages with unformatted alternatives, implementations SHOULD NOT
        attempt to send formatted messages until the Telepathy specification
        has also been extended to cover capability discovery for message
        formatting.

      
        We intend to expose all rich-text messages as XHTML-IM, but on some
        protocols, formatting is an extremely limited subset of that format
        (e.g. there are protocols where foreground/background colours, font
        and size can be set, but only for entire messages).
        Until we can tell UIs what controls to offer to the user, it's
        unfriendly to offer the user controls that may have no effect.
      
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Channel.Interface.Messages')

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Messages', in_signature='aa{sv}u', out_signature='s')
    def SendMessage(self, Message, Flags):
        """
        Submit a message to the server for sending.
          If this method returns successfully, the message has been submitted
          to the server and the MessageSent
          signal is emitted. A corresponding
          Sent
          signal on the Text interface MUST also be emitted.

        This method MUST return before the MessageSent signal is
          emitted.

        
          This means that the process sending the message is the first
            to see the Protocol_Message_Token, and can
            relate the message to the corresponding
            MessageSent signal by comparing
            message tokens (if supported by the protocol).
        

        If this method fails, message submission to the server has failed
          and no signal on this interface (or the Text interface) is
          emitted.

        If this method succeeds, message submission to the server has
          succeeded, but the message has not necessarily reached its intended
          recipient. If a delivery failure is detected later, this is
          signalled by receiving a message whose message-type
          header maps to
          Channel_Text_Message_Type_Delivery_Report.
          Similarly, if delivery is detected to have been successful
          (which is not possible in all protocols), a successful delivery
          report will be signalled.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Messages', in_signature='uau', out_signature='a{uv}')
    def GetPendingMessageContent(self, Message_ID, Parts):
        """
        Retrieve the content of one or more parts of a pending message.
        Note that this function may take a considerable amount of time
        to return if the part's 'needs-retrieval' flag is true; consider
        extending the default D-Bus method call timeout. Additional API is
        likely to be added in future, to stream large message parts.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.Messages', signature='aa{sv}us')
    def MessageSent(self, Content, Flags, Message_Token):
        """
        Signals that a message has been submitted for sending. This
          MUST be emitted exactly once per emission of the Sent
          signal on the Text interface, for backwards-compatibility; clients
          SHOULD ignore the latter if this interface is present, as mentioned
          in the introduction.

        This SHOULD be emitted as soon as the CM determines it's
          theoretically possible to send the message (e.g. the parameters are
          supported and correct).

        
          This signal allows a process that is not the caller of
            SendMessage to log sent messages.
        
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.Messages', signature='au')
    def PendingMessagesRemoved(self, Message_IDs):
        """
        The messages with the given IDs have been removed from the
        PendingMessages list. Clients SHOULD NOT
        attempt to acknowledge those messages.

        
          This completes change notification for the PendingMessages property
          (previously, there was change notification when pending messages
          were added, but not when they were removed).
        
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.Messages', signature='aa{sv}')
    def MessageReceived(self, Message):
        """
        Signals that a message has been received and added to the pending
        messages queue. This MUST be emitted exactly once per emission of the
        Received
        signal on the Text interface, for backwards-compatibility; clients
        SHOULD ignore the latter in favour of this signal if this interface is
        present, as mentioned in the introduction.
      
        """
        pass
  