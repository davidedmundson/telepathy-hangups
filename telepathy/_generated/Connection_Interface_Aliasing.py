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


class ConnectionInterfaceAliasing(dbus.service.Interface):
    """\
      An interface on connections to support protocols where contacts have an
    alias which they can change at will. Provides a method for the user to set
    their own alias, and a signal which should be emitted when a contact's
    alias is changed or first discovered.

    On connections where the user is allowed to set aliases for contacts and
    store them on the server, the GetAliasFlags
    method will have the CONNECTION_ALIAS_FLAG_USER_SET flag set, and the
    SetAliases method may be called on contact
    handles other than the user themselves.

    Aliases are intended to be used as the main displayed name for the
    contact, where available.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.Aliasing')

    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Aliasing', in_signature='', out_signature='u')
    def GetAliasFlags(self):
        """
        Return a bitwise OR of flags detailing the behaviour of aliases on this
        connection.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Aliasing', in_signature='au', out_signature='as')
    def RequestAliases(self, Contacts):
        """
        Request the value of several contacts' aliases at once.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Aliasing', in_signature='au', out_signature='a{us}')
    def GetAliases(self, Contacts):
        """
        Request the value of several contacts' aliases at once. This SHOULD
        only return cached aliases, falling back on the contact identifier
        (i.e. the string corresponding to the handle) if none is present. Also
        if there was no cached alias, a request SHOULD be started of which the
        result is later signalled by
        AliasesChanged.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Aliasing', in_signature='a{us}', out_signature='')
    def SetAliases(self, Aliases):
        """
        Request that the alias of the given contact be changed. Success will be
        indicated by emitting an AliasesChanged
        signal. On connections where the CONNECTION_ALIAS_FLAG_USER_SET flag is
        not set, this method will only ever succeed if the contact is the
        user's own handle (as returned by Connection.GetSelfHandle).
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.Aliasing', signature='a(us)')
    def AliasesChanged(self, Aliases):
        """
        Signal emitted when a contact's alias (or that of the user) is changed.
      
        """
        pass
  