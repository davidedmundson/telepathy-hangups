# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2009-2010 Collabora Ltd.

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


class ProtocolInterfaceAvatars(dbus.service.Interface):
    """\
      An interface for protocols where it might be possible to set the
        user's avatar, and the expected size limits and supported MIME types
        are known before connecting.

      
        If the avatar requirements cannot be discovered while offline,
          it's impossible to avoid setting the Account's Avatar property to an unsupported avatar.
      

      Each property on this interface SHOULD be cached in the
        .manager file, using a key of the same name as the
        property in the [Protocol proto]
        group. All properties are encoded in ASCII decimal in the obvious
        way, except for
        SupportedAvatarMIMETypes which is
        encoded as a sequence of strings each followed by a semicolon
        (as for the "localestrings" type in the Desktop Entry
        Specification).

      For instance, an XMPP connection manager might have this
        .manager file:

[Protocol jabber]
Interfaces=org.freedesktop.Telepathy.Protocol.Interface.Avatars;
param-account=s required
param-password=s required
SupportedAvatarMIMETypes=image/png;image/jpeg;image/gif;
MinimumAvatarHeight=32
RecommendedAvatarHeight=64
MaximumAvatarHeight=96
MinimumAvatarWidth=32
RecommendedAvatarWidth=64
MaximumAvatarWidth=96
MaximumAvatarBytes=8192

    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Protocol.Interface.Avatars')
