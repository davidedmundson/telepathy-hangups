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


class ChannelInterfaceServicePoint(dbus.service.Interface):
    """\
      An interface for channels
        that can indicate when/if they are connected to some form
        of service point.  For example, when
        dialing 9-1-1 in the US, a GSM modem/network will recognize that as
        an emergency call, and inform higher levels of the stack that the
        call is being handled by an emergency service.  In this example,
        the call is handled by a Public Safety Answering Point (PSAP) which is labeled
        as "urn:service:sos".  Other networks and protocols may handle this
        differently while still using this interface.

      Note that while the majority of examples given in this
        documentation are for GSM calls, they could just as easily be
        SIP calls, GSM SMS's, etc.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Channel.Interface.ServicePoint')

    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.ServicePoint', signature='(us)')
    def ServicePointChanged(self, Service_Point):
        """
        Emitted when a channel changes the service point that it's connected to.  This
        might be a new call being connected to a service, a call connected to
        a service being routed to a different service
        (ie, an emergency call being routed from a generic emergency PSAP to
        a poison control PSAP), or any number of other things.

        Note that this should be emitted as soon as the CM has been notified
        of the switch, and has updated its internal state.  The CM MAY still
        be in the process of connecting to the new service point.
      
        """
        pass
  