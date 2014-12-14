# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2008-2009 Collabora Limited
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
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
  
"""

import dbus.service


class ChannelTypeStreamTube(dbus.service.Interface):
    """\
      A stream tube is a transport for ordered, reliable data transfer,
        similar to SOCK_STREAM sockets.

      When offering a stream tube, the initiating client creates a local
        listening socket and offers it to the recipient client using the
        Offer method.  When a
        recipient accepts a stream tube using the
        Accept method, the
        recipient's connection manager creates a new local listening socket.
        Each time the recipient's client connects to this socket, the
        initiator's connection manager proxies this connection to the
        originally offered socket.

    """

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.StreamTube', in_signature='uvua{sv}', out_signature='')
    def Offer(self, address_type, address, access_control, parameters):
        """
        Offer a stream tube exporting the local socket specified.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.StreamTube', in_signature='uuv', out_signature='v')
    def Accept(self, address_type, access_control, access_control_param):
        """
        Accept a stream tube that's in the "local pending" state. The
        connection manager will attempt to open the tube. The tube remains in
        the "local pending" state until the TubeChannelStateChanged
        signal is emitted.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.StreamTube', signature='uvu')
    def NewRemoteConnection(self, Handle, Connection_Param, Connection_ID):
        """
        Emitted each time a participant opens a new connection to its
        socket.

        This signal is only fired on the offering side.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.StreamTube', signature='u')
    def NewLocalConnection(self, Connection_ID):
        """
        Emitted when the tube application connects to the CM's socket.

        This signal is only fired on the accepting side.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.StreamTube', signature='uss')
    def ConnectionClosed(self, Connection_ID, Error, Message):
        """
        Emitted when a connection has been closed.
      
        """
        pass
  