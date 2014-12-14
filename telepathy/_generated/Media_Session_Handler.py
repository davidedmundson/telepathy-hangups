# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright (C) 2005, 2006 Collabora Limited 
 Copyright (C) 2005, 2006 Nokia Corporation 
 Copyright (C) 2006 INdT 

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


class MediaSessionHandler(dbus.service.Object):
    """\
      An media session handler is an object that handles a number of synchronised
    media streams.
    """

    @dbus.service.method('org.freedesktop.Telepathy.Media.SessionHandler', in_signature='us', out_signature='')
    def Error(self, Error_Code, Message):
        """
        Informs the connection manager that an error occured in this session.
        If used, the connection manager must terminate the session and all of
        the streams within it, and may also emit a StreamError
        signal on the channel for each stream within the session.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Media.SessionHandler', in_signature='', out_signature='')
    def Ready(self):
        """
        Inform the connection manager that a client is ready to handle
        this session handler (i.e. that it has connected to the
        NewStreamHandler signal and done any
        other necessary setup).
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Media.SessionHandler', signature='ouuu')
    def NewStreamHandler(self, Stream_Handler, ID, Media_Type, Direction):
        """
        Emitted when a new stream handler has been created for this
        session.
      
        """
        pass
  