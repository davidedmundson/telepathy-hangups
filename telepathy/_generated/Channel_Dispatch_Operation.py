# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2008-2009 Collabora Ltd.
Copyright © 2008-2009 Nokia Corporation

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
      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
      MA 02110-1301, USA.
  
"""

import dbus.service


class ChannelDispatchOperation(dbus.service.Object):
    """\
      A channel dispatch operation is an object in the ChannelDispatcher
        representing a batch of unrequested channels being announced to
        client
        Approver
        processes.

      These objects can result from new incoming channels or channels
        which are automatically created for some reason, but cannot result
        from outgoing requests for channels.

      More specifically, whenever the
        Connection.Interface.Requests.NewChannels
        signal contains channels whose
        Requested
        property is false, or whenever the
        Connection.NewChannel
        signal contains a channel with suppress_handler false,
        one or more ChannelDispatchOperation objects are created for those
        channels.

      (If some channels in a NewChannels signal are in different bundles,
        this is an error. The channel dispatcher SHOULD recover by treating
        the NewChannels signal as if it had been several NewChannels signals
        each containing one channel.)

      First, the channel dispatcher SHOULD construct a list of all the
        Handlers
        that could handle all the channels (based on their HandlerChannelFilter
        property), ordered by
        priority in some implementation-dependent way. If there are handlers
        which could handle all the channels, one channel dispatch operation
        SHOULD be created for all the channels. If there are not, one channel
        dispatch operation SHOULD be created for each channel, each with
        a list of channel handlers that could handle that channel.

      If no handler at all can handle a channel, the channel dispatcher
        SHOULD terminate that channel instead of creating a channel dispatcher
        for it. It is RECOMMENDED that the channel dispatcher closes
        the channels using Channel.Interface.Destroyable.Destroy
        if supported, or Channel.Close
        otherwise. As a special case, the channel dispatcher SHOULD NOT close
        ContactList
        channels, and if Close fails, the channel dispatcher SHOULD ignore
        that channel.

      
        ContactList channels are strange. We hope to replace them with
          something better, such as an interface on the Connection, in a
          future version of this specification.
      

      When listing channel handlers, priority SHOULD be given to
        channel handlers that are already handling channels from the same
        bundle.

      If a handler with BypassApproval
        = True could handle all of the channels in the dispatch
        operation, then the channel dispatcher SHOULD call HandleChannels
        on that handler, and (assuming the call succeeds) emit
        Finished and stop processing those
        channels without involving any approvers.

      
        Some channel types can be picked up "quietly" by an existing
          channel handler. If a Text
          channel is added to an existing bundle containing a StreamedMedia
          channel, there shouldn't be
          any approvers, flashing icons or notification bubbles, if the
          the UI for the StreamedMedia channel can just add a text box
          and display the message.
      

      Otherwise, the channel dispatcher SHOULD send the channel dispatch
        operation to all relevant approvers (in parallel) and wait for an
        approver to claim the channels or request that they are handled.
        See
        AddDispatchOperation
        for more details on this.

      Finally, if the approver requested it, the channel dispatcher SHOULD
        send the channels to a handler.
    """

    @dbus.service.method('org.freedesktop.Telepathy.ChannelDispatchOperation', in_signature='s', out_signature='')
    def HandleWith(self, Handler):
        """
        Called by an approver to accept a channel bundle and request that
          the given handler be used to handle it.

        If successful, this method will cause the ChannelDispatchOperation
          object to disappear, emitting
          Finished.

        However, this method may fail because the dispatch has already been
          completed and the object has already gone. If this occurs, it
          indicates that another approver has asked for the bundle to be
          handled by a particular handler. The approver MUST NOT attempt
          to interact with the channels further in this case, unless it is
          separately invoked as the handler.

        Approvers which are also channel handlers SHOULD use
          Claim instead
          of HandleWith to request that they can handle a channel bundle
          themselves.

        (FIXME: list some possible errors)

        If the channel handler raises an error from HandleChannels,
          this method
          MAY respond by raising that same error, even if it is not
          specifically documented here.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.ChannelDispatchOperation', in_signature='', out_signature='')
    def Claim(self):
        """
        Called by an approver to claim channels for handling
          internally. If this method is called successfully, the process
          calling this method becomes the handler for the channel, but
          does not have the HandleChannels
          method called on it.

        Clients that call Claim on channels but do not immediately
          close them SHOULD implement the Handler interface and its
          HandledChannels
          property.

        Approvers wishing to reject channels MUST call this method to
          claim ownership of them, and MUST NOT call
          Close
          on the channels unless/until this method returns successfully.

        
          The channel dispatcher can't know how best to close arbitrary
            channel types, so it leaves it up to the approver to do so.
            For instance, for Text channels it is necessary
            to acknowledge any messages that have already been displayed to
            the user first - ideally, the approver would display and then
            acknowledge the messages - or to call Channel.Interface.Destroyable.Destroy
            if the destructive behaviour of that method is desired.

          Similarly, an Approver for StreamedMedia channels can close the
            channel with a reason (e.g. "busy") if desired. The channel
            dispatcher, which is designed to have no specific knowledge
            of particular channel types, can't do that.
        

        If successful, this method will cause the ChannelDispatchOperation
          object to disappear, emitting
          Finished, in the same way as for
          HandleWith.

        This method may fail because the dispatch operation has already
          been completed. Again, see HandleWith for more details. The approver
          MUST NOT attempt to interact with the channels further in this
          case.

        (FIXME: list some other possible errors)
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.ChannelDispatchOperation', in_signature='sx', out_signature='')
    def HandleWithTime(self, Handler, UserActionTime):
        """
        A variant of HandleWith allowing the
          approver to pass an user action time. This timestamp will be passed
          to the Handler when HandleChannels
          is called.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.ChannelDispatchOperation', signature='oss')
    def ChannelLost(self, Channel, Error, Message):
        """
        A channel has closed before it could be claimed or handled. If
          this is emitted for the last remaining channel in a channel
          dispatch operation, it MUST immediately be followed by
          Finished.

        This signal MUST NOT be emitted until all Approvers that were
          invoked have returned (successfully or with an error) from
          their AddDispatchOperation
          method.

        
          This means that Approvers can connect to the ChannelLost signal
            in a race-free way. Non-approver processes that discover
            a channel dispatch operation in some way (such as observers)
            will have to follow the usual "connect to signals then recover
            state" model - first connect to ChannelLost and
            Finished,
            then download Channels (and
            on error, perhaps assume that the operation has already
            Finished).
        
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.ChannelDispatchOperation', signature='')
    def Finished(self):
        """
        Emitted when this dispatch operation finishes. The dispatch
          operation is no longer present and further methods must not be
          called on it.

        Approvers that have a user interface SHOULD stop notifying the user
          about the channels in response to this signal; they MAY assume that
          on errors, they would have received
          ChannelLost first.

        Its object path SHOULD NOT be reused for a subsequent dispatch
          operation; the ChannelDispatcher MUST choose object paths
          in a way that avoids immediate re-use.

        
          Otherwise, clients might accidentally call
            HandleWith or
            Claim on a new dispatch operation
            instead of the one they intended to handle.
        

        This signal MUST NOT be emitted until all Approvers that were
          invoked have returned (successfully or with an error) from
          their AddDispatchOperation
          method.

        
          This means that Approvers can connect to the ChannelLost signal
            in a race-free way. Non-approver processes that discover
            a channel dispatch operation in some way (such as observers)
            will have to follow the usual "connect to signals then recover
            state" model - first connect to
            ChannelLost and
            Finished, then download Channels
            (and on error, perhaps assume that the operation has already
            Finished).
        
      
        """
        pass
  