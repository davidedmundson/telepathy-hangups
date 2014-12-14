# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright (C) 2008 Collabora Ltd.
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
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

  
"""

import dbus.service


class AccountInterfaceAvatar(dbus.service.Interface):
    """\
      This interface extends the core Account interface to provide a
        user-settable avatar image.

      
        The avatar could have been a property on the core Account interface,
          but was moved to a separate interface because it is likely to be
          large. This means that clients can safely use GetAll to get
          properties on the core Account interface without flooding the
          session bus with large images.
      

    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Account.Interface.Avatar')

    @dbus.service.signal('org.freedesktop.Telepathy.Account.Interface.Avatar', signature='')
    def AvatarChanged(self):
        """
        Emitted when the Avatar property changes.

        The avatar itself is deliberately not included in this
          signal, to reduce bus traffic in the (likely common) case where no
          running application cares about the user's own avatar.
      
        """
        pass
  