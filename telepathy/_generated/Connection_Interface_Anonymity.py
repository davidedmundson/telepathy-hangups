# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2008-2010 Nokia Corporation
Copyright © 2010 Collabora Ltd.

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


class ConnectionInterfaceAnonymity(dbus.service.Interface):
    """\
      An interface to support anonymity settings on a per-connection basis.
        This defines what personal identifying information a remote contact
        may or may not see.  For example, GSM might use this for CLIR, while
        SIP might use this for privacy service requests.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.Anonymity')

    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.Anonymity', signature='u')
    def AnonymityModesChanged(self, Modes):
        """
        Emitted when the anonymity mode has changed.
      
        """
        pass
  