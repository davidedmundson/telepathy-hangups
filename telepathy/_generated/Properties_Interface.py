# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright (C) 2005-2007 Collabora Limited 
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


class PropertiesInterface(dbus.service.Interface):
    """\
      Interface for channels and other objects, to allow querying and setting
    properties. ListProperties returns which properties are valid for
    the given channel, including their type, and an integer handle used to
    refer to them in GetProperties, SetProperties, and the PropertiesChanged
    signal. The values are represented by D-Bus variant types, and are
    accompanied by flags indicating whether or not the property is readable or
    writable.

    Each property also has a flags value to indicate what methods are
    available. This is a bitwise OR of PropertyFlags values.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Properties')

    @dbus.service.method('org.freedesktop.Telepathy.Properties', in_signature='au', out_signature='a(uv)')
    def GetProperties(self, Properties):
        """
        Returns an array of (identifier, value) pairs containing the current
        values of the given properties.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Properties', in_signature='', out_signature='a(ussu)')
    def ListProperties(self):
        """
        Returns a dictionary of the properties available on this channel.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Properties', in_signature='a(uv)', out_signature='')
    def SetProperties(self, Properties):
        """
        Takes an array of (identifier, value) pairs containing desired
          values to set the given properties. In the case of any errors, no
          properties will be changed. When the changes have been acknowledged
          by the server, the PropertiesChanged signal will be emitted.

        All properties given must have the PROPERTY_FLAG_WRITE flag, or
        PermissionDenied will be returned. If any variants are of the wrong
        type, NotAvailable will be returned.  If any given property identifiers
        are invalid, InvalidArgument will be returned.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Properties', signature='a(uv)')
    def PropertiesChanged(self, Properties):
        """
        Emitted when the value of readable properties has changed.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Properties', signature='a(uu)')
    def PropertyFlagsChanged(self, Properties):
        """
        Emitted when the flags of some room properties have changed.
      
        """
        pass
  