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


class ConnectionInterfaceCellular(dbus.service.Interface):
    """\
      This interface is for various cellular things (GSM and/or CDMA) that
        aren't really applicable to other protocols.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.Cellular')

    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.Cellular', signature='s')
    def IMSIChanged(self, IMSI):
        """
        Emitted when the IMSI for the connection changes.  This sort of thing
        is rare, but could happen on cellular phones that allow hot-swapping
        of SIM cards.  In the case of SIM swapping, this signal would be
        emitted twice; the first time while the SIM is being ejected (with an
        empty string), and the second time after a new SIM has been inserted
        (assuming that the IMSI can be determined from the new SIM).
      
        """
        pass
  