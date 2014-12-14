# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2008-2009 Collabora Limited
Copyright © 2008-2009 Nokia Corporation

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


class ChannelInterfaceTube(dbus.service.Interface):
    """\
      A tube is a mechanism for arbitrary data transfer between
      two or more IM users, used to allow applications on the users'
      systems to communicate without having to establish network
      connections themselves. Currently, two types of tube exist:
      Channel.Type.DBusTube and
      Channel.Type.StreamTube. This interface contains
      the properties, signals and methods common to both types of tube;
      you can only create channels of a specific tube type, not of this
      type. A tube channel contains exactly one tube; if you need several
      tubes, you have to create several tube channels.

      Tube channels can be requested for Handle_Type
        Contact (for 1-1 communication) or Room (to communicate with others in
        the room simultaneously).

      As an exception to the usual handling of capabilities, connection managers
        for protocols with capability discovery (such as XMPP) SHOULD advertise the
        capability representing each Tube type that they support
       (Channel.Type.DBusTube and/or
        Channel.Type.StreamTube)
        even if no client has indicated via
        UpdateCapabilities
        that such a tube is supported. They SHOULD also allow clients to offer tubes with any
        Service or
        ServiceName
        to any contact which supports the corresponding tube capability.

      
        This lowers the barrier to entry for those writing new tube
          applications, and preserves interoperability with older versions of
          the Telepathy stack which did not support rich capabilities.
      
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Channel.Interface.Tube')

    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.Tube', signature='u')
    def TubeChannelStateChanged(self, State):
        """
        Emitted when the state of the tube channel changes. Valid state
        transitions are documented with Tube_Channel_State.
      
        """
        pass
  