# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright © 2005-2010 Nokia Corporation 
 Copyright © 2005-2010 Collabora Ltd 

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


class ConnectionInterfaceServicePoint(dbus.service.Interface):
    """\
      An interface for connections whose channels may be able to indicate
        specific they are connected to some form
        of service station.  For example, when
        dialing 9-1-1 in the US, a GSM modem/network will recognize that as
        an emergency call, and inform higher levels of the stack that the
        call is being handled by an emergency service.  In this example,
        the call is handled by a Public Safety Answering Point (PSAP) which is labeled
        as "urn:service:sos".  Other networks and protocols may handle this
        differently while still using this interface.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.ServicePoint')

    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.ServicePoint', signature='a((us)as)')
    def ServicePointsChanged(self, Service_Points):
        """
        Emitted when the list of known service points (or their IDs) has
        changed.
      
        """
        pass
  