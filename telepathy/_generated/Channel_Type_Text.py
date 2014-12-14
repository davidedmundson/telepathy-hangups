# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright © 2005-2009 Collabora Limited 
 Copyright © 2005-2009 Nokia Corporation 
 Copyright © 2006 INdT 

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
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
  
"""

import dbus.service


class ChannelTypeText(dbus.service.Interface):
    """\
      A channel type for sending and receiving messages. This channel type
        is primarily used for textual messages, but can also be used for
        formatted text, text with "attachments", or binary messages on some
        protocols.

      Most of the methods and signals on this interface are deprecated,
        since they only support plain-text messages with limited metadata.
        See the mandatory Messages
        interface for the modern equivalents.

      When a message is received, an identifier is assigned and a
        MessageReceived signal emitted, and the message
        is placed in a pending queue represented by the
        PendingMessages property.
        When the Handler
        for a channel has handled the message by showing it to the user
        (or equivalent), it should acknowledge the receipt of that message
        using the AcknowledgePendingMessages
        method, and the message will then be removed from the pending queue.
        Numeric identifiers for received messages may be reused over the
        lifetime of the channel.

      Sending messages can be requested using the
        SendMessage method, which will return
        successfully when the message has been submitted for sending, or
        return an error with no signal emission if there is an immediate
        failure. If a message is submitted for sending but delivery of the
        message later fails, this is indicated by a delivery report, which
        is received in the same way as an incoming message.

      Simple one-to-one chats (such as streams of private messages in
        XMPP or IRC) should be represented by a Text channel whose
        TargetHandleType
        is Handle_Type_Contact. The expected way to
        request such a channel is to set the ChannelType, TargetHandleType,
        and either TargetHandle or TargetID in a call to EnsureChannel.

      Named chat rooms whose identity can be saved and used again later
        (IRC channels, Jabber MUCs) are expected to be represented by Text
        channels with Handle_Type_Room and the Group
        interface. In protocols where a chatroom can be used as a continuation
        of one or more one-to-one chats, these channels should also have the
        Conference
        interface.

      Unnamed, transient chat rooms which cannot be rejoined by their
        unique identifier (e.g. a conversation on MSN which has, or once had,
        three or more participants) are expected to be represented by Text
        channels with Handle_Type_None (and hence TargetHandle 0), the
        Group
        interface, and optionally the
        Conference
        interface.

      On protocols like MSN where a conversation with a user is actually
        just a nameless chat room starting with exactly two members, to which
        more members can be invited, the initial one-to-one conversation
        SHOULD be represented with Handle_Type_Contact. If a third participant
        joins or is invited, this SHOULD be represented by signalling
        a new Conference channel
        with the one-to-one channel in its InitialChannels, migrating the underlying protocol
        object from the one-to-one channel to the Conference channel,
        and creating a new protocol-level conversation if the one-to-one
        channel is re-used. See the Conference interface for more details.

      
        This keeps the presentation of all one-to-one conversations
          uniform, and makes it easier to hand over a conversation from a
          1-1-specific UI to a more elaborate multi-user UI; while it does
          require UIs to understand Conference to follow the
          upgrade, UIs that will deal with XMPP need to understand Conference
          anyway.
      

      If a channel of type Text is closed while it has pending messages,
        the connection manager MUST allow this, but SHOULD open a new channel
        to deliver those messages, signalling it as a new channel with the
        NewChannels
        signal. The new channel should resemble the old channel, but have
        Requested = FALSE regardless of its previous value; the InitiatorHandle
        and InitiatorID should correspond to the sender of one of the pending
        messages.

      
        In effect, this turns this situation, in which a client
          is likely to lose messages:

        
          UI window is closed
          message arrives
          text channel emits Received
          UI calls Close on text channel before it has seen the
            Received signal
          text channel emits Closed and closes
        

        into something nearly equivalent to this situation, which is
          fine:

        
          UI window is closed
          UI calls Close on text channel
          text channel emits Closed and closes
          message arrives
          new text channel is created, connection emits NewChannels
          (the same or a different) UI handles it
        

        Requested must be set to FALSE so the replacement channel
          will be handled by something.

        In practice, connection managers usually implement this by keeping
          the same internal object that represented the old channel, adjusting
          its properties, signalling that it was closed, then immediately
          re-signalling it as a new channel.
      

      As a result, Text channels SHOULD implement Channel.Interface.Destroyable.

      
        This "respawning" behaviour becomes problematic if there is no
          suitable handler for Text channels, or if a particular message
          repeatedly crashes the Text channel handler; a channel dispatcher
          can't just Close() the channel in these situations, because
          it will come back.

        In these situations, the channel dispatcher needs a last-resort
          way to destroy the channel and stop it respawning. It could either
          acknowledge the messages itself, or use the Destroyable interface;
          the Destroyable interface has the advantage that it's not
          channel-type-dependent, so the channel dispatcher only has to
          understand one extra interface, however many channel types
          eventually need a distinction between Close and Destroy.
      

    """

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Text', in_signature='au', out_signature='')
    def AcknowledgePendingMessages(self, IDs):
        """
        Inform the channel that you have handled messages by displaying them to
        the user (or equivalent), so they can be removed from the pending queue.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Text', in_signature='', out_signature='au')
    def GetMessageTypes(self):
        """
        Return an array indicating which types of message may be sent on this
        channel.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Text', in_signature='b', out_signature='a(uuuuus)')
    def ListPendingMessages(self, Clear):
        """
        List the messages currently in the pending queue, and optionally
        remove then all.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Text', in_signature='us', out_signature='')
    def Send(self, Type, Text):
        """
        Request that a message be sent on this channel. When the message has
          been submitted for delivery, this method will return and the
          Sent signal will be emitted. If the
          message cannot be submitted for delivery, the method returns an error
          and no signal is emitted.

        This method SHOULD return before the Sent signal is
          emitted.

        
          When a Text channel implements the Messages
            interface, that "SHOULD" becomes a "MUST".
        
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.Text', signature='')
    def LostMessage(self):
        """
        This signal is emitted to indicate that an incoming message was
        not able to be stored and forwarded by the connection manager
        due to lack of memory.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.Text', signature='uuuuus')
    def Received(self, ID, Timestamp, Sender, Type, Flags, Text):
        """
        Signals that a message with the given id, timestamp, sender, type
        and text has been received on this channel. Applications that catch
        this signal and reliably inform the user of the message should
        acknowledge that they have dealt with the message with the
        AcknowledgePendingMessages method.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.Text', signature='uuus')
    def SendError(self, Error, Timestamp, Type, Text):
        """
        Signals that an outgoing message has failed to send. The error
          will be one of the values from ChannelTextSendError.

        This signal should only be emitted for messages for which
          Sent has already been emitted and
          Send has already returned success.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.Text', signature='uus')
    def Sent(self, Timestamp, Type, Text):
        """
        Signals that a message has been submitted for sending.
      
        """
        pass
  