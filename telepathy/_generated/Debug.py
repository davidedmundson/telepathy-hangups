# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright (C) 2009 Collabora Ltd.

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


class Debug(dbus.service.Object):
    """\
      An interface for providing debug messages.

      This interface is primarily provided by one object per
      service, at the path /org/freedesktop/Telepathy/debug.
    """

    @dbus.service.method('org.freedesktop.Telepathy.Debug', in_signature='', out_signature='a(dsus)')
    def GetMessages(self):
        """
        Retrieve buffered debug messages. An implementation could have a
        limit on how many message it keeps and so the array returned from
        this method should not be assumed to be all of the messages in
        the lifetime of the service.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Debug', signature='dsus')
    def NewDebugMessage(self, time, domain, level, message):
        """
        Emitted when a debug messages is generated if the
        Enabled property is set to TRUE.
      
        """
        pass
  