# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright (C) 2005, 2006, 2008 Collabora Limited 
 Copyright (C) 2005, 2006, 2008 Nokia Corporation 
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


class ConnectionInterfaceContactCapabilities(dbus.service.Interface):
    """\
      Contact capabilities describe the channel classes which may be
        created with a given contact in advance of attempting to create a
        channel. Each capability represents a commitment by the
        connection manager that it will ordinarily be able to create a channel
        with a contact when given a request with the properties defined by the
        channel class.

      Capabilities pertain to particular contact handles, and represent
        activities such as having a text chat, a voice call with the user or a
        stream tube of a defined type.

      This interface also enables user interfaces to notify the connection
        manager what capabilities to advertise for the user to other contacts.
        This is done by using the
        UpdateCapabilities method.

      
        XMPP is a major user of this interface: XMPP contacts will not,
          in general, be callable using VoIP unless they advertise suitable
          Jingle capabilities.

        Many other protocols also have some concept of capability flags,
          which this interface exposes in a protocol-independent way.
      
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.ContactCapabilities')

    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactCapabilities', in_signature='a(saa{sv}as)', out_signature='')
    def UpdateCapabilities(self, Handler_Capabilities):
        """
        Alter the connection's advertised capabilities to include
          the intersection of the given clients' capabilities with what the
          connection manager is able to implement.

        On connections managed by the ChannelDispatcher, processes other
          than the ChannelDispatcher SHOULD NOT call this method, and the
          ChannelDispatcher SHOULD use this method to advertise the
          capabilities of all the registered Client.Handler
          implementations.On connections not managed by the ChannelDispatcher,
          clients MAY use this method directly, to indicate the channels they
          will handle and the extra capabilities they have.

        Upon a successful invocation of this method, the connection manager
          will only emit the
          ContactCapabilitiesChanged signal
          for the user's SelfHandle
          if, in the underlying protocol, the new capabilities are distinct
          from the previous state.

        
          The connection manager will essentially intersect the provided
            capabilities and the channel classes it implements. Therefore,
            certain properties which are never fixed for a channel class
            (such as the target handle, or the Parameters property of a tube
            channel) will almost certainly not be advertised.
        

        This method MAY be called on a newly-created connection while it
          is still in the DISCONNECTED state, to request that when the
          connection connects, it will do so with the appropriate
          capabilities. Doing so MUST NOT fail.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactCapabilities', in_signature='au', out_signature='a{ua(a{sv}as)}')
    def GetContactCapabilities(self, Handles):
        """
        Returns an array of requestable channel classes for the given
          contact handles, representing the channel requests that are
          expected to succeed.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.ContactCapabilities', signature='a{ua(a{sv}as)}')
    def ContactCapabilitiesChanged(self, caps):
        """
        Announce that there has been a change of capabilities on the
          given handles. A single signal can be emitted for several
        contacts.

        
          The underlying protocol can get several contacts' capabilities at
            the same time.
        

      
        """
        pass
  