# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright (C) 2008 Collabora Limited
Copyright (C) 2008 Nokia Corporation

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


class ConnectionInterfaceRequests(dbus.service.Interface):
    """\
      An enhanced version of the Telepathy connection interface, which can
        represent bundles of channels that should be dispatched together, and
        does not assume any particular properties by which channels are
        uniquely identifiable.

      If this interface is implemented on a connection, then
        NewChannels MUST be emitted for
        all new channels, even those created with RequestChannel.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.Requests')

    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Requests', in_signature='a{sv}', out_signature='oa{sv}')
    def CreateChannel(self, Request):
        """
        Request that an entirely new channel is created.

        
          There is deliberately no flag corresponding to the
            suppress_handler argument to
            Connection.RequestChannel,
            because passing a FALSE value for that argument is deprecated.
            Requests made using this interface always behave as though
            suppress_handler was TRUE.
        

      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Requests', in_signature='a{sv}', out_signature='boa{sv}')
    def EnsureChannel(self, Request):
        """
        Request that channels are ensured to exist.

        
          The connection manager is in the best position to determine which
            existing channels could satisfy which requests.
        

      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.Requests', signature='a(oa{sv})')
    def NewChannels(self, Channels):
        """
        New channels have been created. The connection manager SHOULD emit
          a single signal for any group of closely related channels that are
          created at the same time, so that the channel dispatcher can try to
          dispatch them to a handler as a unit.

        In particular, if additional channels are created as a side-effect
          of a call to CreateChannel,
          these channels SHOULD appear in the same NewChannels signal as
          the channel that satisfies the request.

        
          Joining a MUC Tube in XMPP requires joining the corresponding
            MUC (chatroom), so a Text
            channel can be created as a side-effect.
        

        Every time NewChannels is emitted, it MUST be followed by
          a Connection.NewChannel
          signal for each channel.

        
          The double signal emission is for the benefit of older Telepathy
            clients, which won't be listening for NewChannels.

          The more informative NewChannels signal comes first so that
            clients that did not examine the connection to find
            out whether Requests is supported will see the more informative
            signal for each channel first, and then ignore the less
            informative signal because it announces a new channel of which
            they are already aware.
        
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.Requests', signature='o')
    def ChannelClosed(self, Removed):
        """
        Emitted when a channel is closed and hence disappears from the
        Channels property.

        
          This is redundant with the Closed
          signal on the channel itself, but it does provide full change
          notification for the Channels property.
        
      
        """
        pass
  