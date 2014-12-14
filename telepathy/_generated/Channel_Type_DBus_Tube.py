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


class ChannelTypeDBusTube(dbus.service.Interface):
    """\
      A D-Bus tube is an ordered reliable transport, for transporting D-Bus
        traffic.

      For each D-Bus tube, the connection manager listens on a D-Bus
        server address, as detailed in the D-Bus specification. On this
        address, it emulates a bus upon which each tube participant appears
        as an endpoint.

      The objects and interfaces which are expected to exist on the
        emulated bus depend on the well-known name; typically, either the
        participant who initiated the tube is expected to export the same
        objects/interfaces that would be exported by a service of that name
        on a bus, or all participants are expected to export those
        objects/interfaces.

      In a multi-user context (Handle_Type_Room) the tube behaves
        like the D-Bus bus daemon, so participants can send each other
        private messages, or can send broadcast messages which are
        received by everyone in the tube (including themselves).
        Each participant has a D-Bus unique name; connection managers
        MUST prevent participants from sending messages with the wrong
        sender unique name, and SHOULD attempt to avoid participants
        receiving messages not intended for them.

      In a 1-1 context (Handle_Type_Contact) the tube behaves like
        a peer-to-peer D-Bus connection - arbitrary D-Bus messages with
        any sender and/or destination can be sent by each participant,
        and each participant receives all messages sent by the other
        participant.

    """

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.DBusTube', in_signature='a{sv}u', out_signature='s')
    def Offer(self, parameters, access_control):
        """
        Offers a D-Bus tube providing the service specified.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.DBusTube', in_signature='u', out_signature='s')
    def Accept(self, access_control):
        """
        Accept a D-Bus tube that's in the "local pending" state. The
        connection manager will attempt to open the tube. The tube remains in
        the "local pending" state until the TubeChannelStateChanged
        signal is emitted.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.DBusTube', signature='a{us}au')
    def DBusNamesChanged(self, Added, Removed):
        """
        Emitted on a multi-user (i.e. Handle_Type_Room) D-Bus tube when a
        participant opens or closes the tube.  This provides change
        notification for the DBusNames property.
      
        """
        pass
  