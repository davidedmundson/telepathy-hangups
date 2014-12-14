# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2009 Collabora Ltd.
Copyright © 2009 Nokia Corporation

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
      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
      USA.
  
"""

import dbus.service


class ConnectionInterfaceBalance(dbus.service.Interface):
    """\
      In many real-time communication services the user can pay for certain
        services, typically calls to the
        PSTN,
        in advance. In (at least) Skype, it's possible to query the current
        balance in a machine-readable way.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.Balance')

    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.Balance', signature='(ius)')
    def BalanceChanged(self, Balance):
        """
        Emitted when the user's balance has changed.
      
        """
        pass
  