# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright (C) 2005-2008 Collabora Limited 
 Copyright (C) 2005, 2006 Nokia Corporation 
 Copyright (C) 2006 INdT 

    This library is free software; you can redistribute it and/or modify it
      under the terms of the GNU Lesser General Public License as published by
      the Free Software Foundation; either version 2.1 of the License, or (at
      your option) any later version.

    This library is distributed in the hope that it will be useful, but
      WITHOUT ANY WARRANTY; without even the implied warranty of
      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser
      General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
      along with this library; if not, write to the Free Software Foundation,
      Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
  
"""

import dbus.service


class ConnectionInterfaceContacts(dbus.service.Interface):
    """\
      This interface allows many attributes of many contacts to be
        obtained in a single D-Bus round trip.

      Each contact attribute has an string identifier
        (Contact_Attribute), which is namespaced
        by the D-Bus interface which defines it.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.Contacts')

    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Contacts', in_signature='auasb', out_signature='a{ua{sv}}')
    def GetContactAttributes(self, Handles, Interfaces, Hold):
        """
        Return any number of contact attributes for the given handles.
      
        """
        raise NotImplementedError
  