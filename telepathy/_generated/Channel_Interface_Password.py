# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""
Copyright © 2005-2009 Collabora Limited
Copyright © 2005-2009 Nokia Corporation
Copyright © 2006 INdT
  

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


class ChannelInterfacePassword(dbus.service.Interface):
    """\
      Interface for channels that may have a password set that users need
    to provide before being able to join, or may be able to view or change
    once they have joined the channel.

    The GetPasswordFlags method and the
    associated PasswordFlagsChanged
    signal indicate whether the channel has a password, whether the user
    must now provide it to join, and whether it can be viewed or changed
    by the user.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Channel.Interface.Password')

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Password', in_signature='', out_signature='u')
    def GetPasswordFlags(self):
        """
        Returns the bitwise-OR of the flags relevant to the password on this
        channel.  The user interface can use this to present information about
        which operations are currently valid.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Password', in_signature='s', out_signature='b')
    def ProvidePassword(self, Password):
        """
        Provide the password so that the channel can be joined. Must be
        called with the correct password in order for channel joining to
        proceed if the 'provide' password flag is set.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.Password', signature='uu')
    def PasswordFlagsChanged(self, Added, Removed):
        """
        Emitted when the flags as returned by
        GetPasswordFlags are changed.
        The user interface should be updated as appropriate.
      
        """
        pass
  