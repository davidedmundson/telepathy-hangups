# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""
    Copyright © 2007-2009 Collabora Limited
  

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


class ChannelTypeTubes(dbus.service.Interface):
    """\
      A "tube" is a mechanism for arbitrary data transfer. Two types of
        data transfer are currently specified: D-Bus messages, and streams of
        bytes. Each tube has a service name, which is a string specifying the
        kind of communication that takes place over it, and a dictionary of
        arbitrary parameters. Tube parameters are commonly used for bootstrap
        information such as usernames and passwords. Each tube is identified
        by a locally unique identifier.

       The Tubes channel type may be requested for handles of type
         HANDLE_TYPE_CONTACT and HANDLE_TYPE_ROOM.

       Stream tubes specify listening addresses using pairs of parameters
         with signature 'u', 'v', where the integer 'u' is a member of
         Socket_Address_Type and the v is dependent on the type of address.
    """

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Tubes', in_signature='', out_signature='a{uau}')
    def GetAvailableStreamTubeTypes(self):
        """List the available address types and access-control types
        for stream tubes.
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Tubes', in_signature='', out_signature='au')
    def GetAvailableTubeTypes(self):
        """
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Tubes', in_signature='', out_signature='a(uuusa{sv}u)')
    def ListTubes(self):
        """
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Tubes', in_signature='sa{sv}', out_signature='u')
    def OfferDBusTube(self, Service, Parameters):
        """
        Offers a D-Bus tube providing the service specified.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Tubes', in_signature='sa{sv}uvuv', out_signature='u')
    def OfferStreamTube(self, Service, Parameters, Address_Type, Address, Access_Control, Access_Control_Param):
        """
        Offer a stream tube exporting the local socket specified.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Tubes', in_signature='u', out_signature='s')
    def AcceptDBusTube(self, ID):
        """
        Accept a D-Bus tube that's in the "local pending" state. The
        connection manager will attempt to open the tube. The tube remains in
        the "local pending" state until the TubeStateChanged signal is
        emitted.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Tubes', in_signature='uuuv', out_signature='v')
    def AcceptStreamTube(self, ID, Address_Type, Access_Control, Access_Control_Param):
        """
        Accept a stream tube that's in the "local pending" state. The
        connection manager will attempt to open the tube. The tube remains in
        the "local pending" state until the TubeStateChanged signal is
        emitted.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Tubes', in_signature='u', out_signature='')
    def CloseTube(self, ID):
        """
        Close a tube.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Tubes', in_signature='u', out_signature='s')
    def GetDBusTubeAddress(self, ID):
        """
        For a D-Bus tube, return a string describing the address of the
        private bus.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Tubes', in_signature='u', out_signature='a(us)')
    def GetDBusNames(self, ID):
        """
        For a multi-user (i.e. Handle_Type_Room) D-Bus tube, obtain a mapping
        between contact handles and their unique bus names on this tube.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Tubes', in_signature='u', out_signature='uv')
    def GetStreamTubeSocketAddress(self, ID):
        """
        For a stream tube, obtain the address of the socket used to
        communicate over this tube.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.Tubes', signature='uuusa{sv}u')
    def NewTube(self, ID, Initiator, Type, Service, Parameters, State):
        """
        Emitted when a tube is created.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.Tubes', signature='uu')
    def TubeStateChanged(self, ID, State):
        """
        Emitted when the state of a tube changes.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.Tubes', signature='u')
    def TubeClosed(self, ID):
        """
       Emitted when a tube has been closed. The ID of a closed tube is no
       longer valid. The ID may later be reused for a new tube.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.Tubes', signature='ua(us)au')
    def DBusNamesChanged(self, ID, Added, Removed):
        """
        Emitted on a multi-user (i.e. Handle_Type_Room) D-Bus tube when a
        participant opens or closes the tube.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.Tubes', signature='uu')
    def StreamTubeNewConnection(self, ID, Handle):
        """
        Emitted on a stream tube when a participant opens a new connection
        to its socket.
      
        """
        pass
  