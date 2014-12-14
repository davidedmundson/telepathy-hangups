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
      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
      02110-1301, USA.
  
"""

import dbus.service


class ClientHandler(dbus.service.Object):
    """\
      Handlers are the user interface for a channel. They turn an abstract
        Telepathy channel into something the user wants to see, like a text
        message stream or an audio and/or video call.

      For its entire lifetime, each channel on a connection known to the
        channel dispatcher is either being processed by the channel dispatcher,
        or being handled by precisely one Handler.

      Because each channel is only handled by one Handler, handlers may
        perform actions that only make sense to do once, such as acknowledging
        Text
        messages, doing the actual streaming for StreamedMedia
        channels with the MediaSignalling
        interface, or transferring the file in FileTransfer
        channels.

      When a new incoming channel (one with
        Requested
        = FALSE) is offered to
        Approvers
        by the channel dispatcher, it also offers the Approvers a list of all
        the running or activatable handlers whose
        HandlerChannelFilter property
        (possibly as cached in the .client file) indicates that they
        are able to handle the channel. The Approvers can choose one of
        those channel handlers to handle the channel.

      When a new outgoing channel (one with
        Requested
        = TRUE) appears, the channel dispatcher passes it to an appropriate
        channel handler automatically.
      

    """

    @dbus.service.method('org.freedesktop.Telepathy.Client.Handler', in_signature='ooa(oa{sv})aota{sv}', out_signature='')
    def HandleChannels(self, Account, Connection, Channels, Requests_Satisfied, User_Action_Time, Handler_Info):
        """
        Called by the channel dispatcher when this client should handle these
          channels, or when this client should present channels that it is already
          handling to the user (e.g. bring them into the foreground).

        
          Clients are expected to know what channels they're already handling,
            and which channel object path corresponds to which window or tab.
            This can easily be done using a hash table keyed by channels' object
            paths.
        

        This method can raise any D-Bus error. If it does, the
          handler is assumed to have failed or crashed, and the channel
          dispatcher MUST recover in an implementation-specific way; it MAY
          attempt to dispatch the channels to another handler, or close the
          channels.

        If closing the channels, it is RECOMMENDED that the channel
          dispatcher attempts to close the channels using
          Channel.Close,
          but resorts to calling
          Channel.Interface.Destroyable.Destroy
          (if available) or ignoring the channel (if not) if the same handler
          repeatedly fails to handle channels.

        After HandleChannels returns successfully, the client process is
          considered to be responsible for the channel until it its unique
          name disappears from the bus.

        
          If a process has multiple Client bus names - some temporary and
            some long-lived - and drops one of the temporary bus names in order
            to reduce the set of channels that it will handle, any channels
            that it is already handling should remain unaffected.
        
      
        """
        raise NotImplementedError
  