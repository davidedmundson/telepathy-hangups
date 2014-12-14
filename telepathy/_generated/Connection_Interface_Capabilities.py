# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright (C) 2005, 2006 Collabora Limited 
 Copyright (C) 2005, 2006 Nokia Corporation 
 Copyright (C) 2006 INdT 

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


class ConnectionInterfaceCapabilities(dbus.service.Interface):
    """\
      An interface for connections where it is possible to know what channel
        types may be requested before the request is made to the connection
        object. Each capability represents a commitment by the connection
        manager that it will ordinarily be able to create a channel when given
        a request with the given type and handle.

      Capabilities pertain to particular contact handles, and represent
        activities such as having a text chat or a voice call with the user.
        The activities are represented by the D-Bus interface name of the
        channel type for that activity.

      The generic capability flags are defined by
        Connection_Capability_Flags.

      In addition, channel types may have type specific capability flags of
        their own, which are described in the documentation for each channel
        type.

      This interface also provides for user interfaces notifying the
        connection manager of what capabilities to advertise for the user. This
        is done by using the
        AdvertiseCapabilities method, and deals
        with the
        interface names of channel types and the type specific flags pertaining
        to them which are implemented by available client processes.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.Capabilities')

    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Capabilities', in_signature='a(su)as', out_signature='a(su)')
    def AdvertiseCapabilities(self, Add, Remove):
        """
        Used by user interfaces to indicate which channel types they are able
        to handle on this connection. Because these may be provided by
        different client processes, this method accepts channel types to add
        and remove from the set already advertised on this connection. The type
        of advertised capabilities (create versus invite) is protocol-dependent
        and hence cannot be set by the this method. In the case of a client
        adding an already advertised channel type but with new channel type
        specific flags, the connection manager should simply add the new flags
        to the set of advertised capabilities.

        Upon a successful invocation of this method, the
        CapabilitiesChanged
        signal will be emitted for the user's own handle ( Connection.GetSelfHandle)
        by the connection manager to indicate the changes
        that have been made.  This signal should also be monitored to ensure
        that the set is kept accurate - for example, a client may remove
        capabilities or type specific capability flags when it exits
        which are still provided by another client.

        On connections managed by the ChannelDispatcher,
          this method SHOULD NOT be used by clients other than the
          ChannelDispatcher itself.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Capabilities', in_signature='au', out_signature='a(usuu)')
    def GetCapabilities(self, Handles):
        """
        Returns an array of capabilities for the given contact handles.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.Capabilities', signature='a(usuuuu)')
    def CapabilitiesChanged(self, Caps):
        """
        Announce that there has been a change of capabilities on the
          given handle.

        If the handle is zero, the capabilities refer to the connection
          itself, in some poorly defined way. This usage is deprecated and
          clients should ignore it.
      
        """
        pass
  