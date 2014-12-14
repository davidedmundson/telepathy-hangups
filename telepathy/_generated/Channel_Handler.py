# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright (C) 2007-2008 Collabora Limited

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


class ChannelHandler(dbus.service.Object):
    """\
      An interface exported by Mission Control 4 client applications which
        are able to handle incoming channels.
    """

    @dbus.service.method('org.freedesktop.Telepathy.ChannelHandler', in_signature='sosouu', out_signature='')
    def HandleChannel(self, Bus_Name, Connection, Channel_Type, Channel, Handle_Type, Handle):
        """
        Called when a channel handler should handle a new channel.
      
        """
        raise NotImplementedError
  