# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2005-2009 Collabora Limited
Copyright © 2005-2009 Nokia Corporation
Copyright © 2006 INdT

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


class Channel(dbus.service.Object):
    """\
    All communication in the Telepathy framework is carried out via channel
    objects which are created and managed by connections. This interface must
    be implemented by all channel objects, along with one single channel type,
    such as Channel.Type.ContactList
    which represents a list of people (such as a buddy list) or Channel.Type.Text which
    represents a channel over which textual messages are sent and received.

    Each Channel's object path MUST start with the object path of
      its associated Connection, followed
      by '/'. There MAY be any number of additional object-path components,
      which clients MUST NOT attempt to parse.

    
      This ensures that Channel object paths are unique, even between
        Connections and CMs, because Connection object paths are
        guaranteed-unique via their link to the well-known bus name.

      If all connection managers in use are known to comply with at least
        spec version 0.17.10, then the Connection's object path can
        even be determined from the Channel's without any additional
        information, by taking the first 7 components.
    

    Each channel has a number of immutable properties (which cannot vary
      after the channel has been announced with NewChannels),
      provided to clients in the
      ObserveChannels,
      AddDispatchOperation and
      HandleChannels
      methods to permit immediate identification of the channel. This interface
      contains immutable properties common to all channels. In brief:

    
      ChannelType specifies the kind of
        communication carried out on this channel;
      TargetHandleType,
        TargetHandle and
        TargetID specify the entity with which
        this channel communicates, such as the other party in a 1-1 call, or
        the name of a multi-user chat room;
      InitiatorHandle and
        InitiatorID specify who created this
        channel;
      Requested indicates whether the local
        user requested this channel, or whether it is an incoming call, a text
        conversation started by a remote contact, a chatroom invitation,
        etc.
    

    Other optional Interfaces can be
      implemented to indicate other available
      functionality, such as Channel.Interface.Group
      if the channel contains a number of contacts, Channel.Interface.Password
      to indicate that a channel may have a password set to require entry, and
      Channel.Interface.ChatState
      for typing notifications. The interfaces implemented may not vary after
      the channel has been created. These other interfaces (along with the
      interface named by ChannelType) may
      themselves specify immutable properties to be announced up-front along
      with the properties on this interface.

    Some channels are “anonymous”, with
      TargetHandleType set to None,
      which indicates that the channel is defined by some other properties. For
      instance, transient ad-hoc chat rooms may be defined only by their members (as visible
      through the Group
      interface), and ContactSearch
      channels represent a single search attempt for a particular Server.

    Specific connection manager implementations may implement channel types and
    interfaces which are not contained within this specification in order to
    support further functionality. To aid interoperability between client and
    connection manager implementations, the interfaces specified here should be
    used wherever applicable, and new interfaces made protocol-independent
    wherever possible. Because of the potential for 3rd party interfaces adding
    methods or signals with conflicting names, the D-Bus interface names should
    always be used to invoke methods and bind signals.
    """

    @dbus.service.method('org.freedesktop.Telepathy.Channel', in_signature='', out_signature='')
    def Close(self):
        """
        Request that the channel be closed. This is not the case until
        the Closed signal has been emitted, and
        depending on the connection
        manager this may simply remove you from the channel on the server,
        rather than causing it to stop existing entirely. Some channels
        such as contact list channels may not be closed.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel', in_signature='', out_signature='s')
    def GetChannelType(self):
        """
        Returns the interface name for the type of this channel.  Clients
        SHOULD use the ChannelType property
        instead, falling back to this method only if necessary.

        
          The GetAll method lets clients retrieve all properties in one
          round-trip.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel', in_signature='', out_signature='uu')
    def GetHandle(self):
        """
        Returns the handle type and number if this channel represents a
        communication with a particular contact, room or server-stored list, or
        zero if it is transient and defined only by its contents. Clients
        SHOULD use the TargetHandle and
        TargetHandleType properties instead,
        falling back to this method only if necessary.

        
          The GetAll method lets clients retrieve all properties in one
          round-trip.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel', in_signature='', out_signature='as')
    def GetInterfaces(self):
        """
        Get the optional interfaces implemented by the channel.
        Clients SHOULD use the Interfaces
        property instead, falling back to this method only if necessary.

        
          The GetAll method lets clients retrieve all properties in one
          round-trip.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel', signature='')
    def Closed(self):
        """
        Emitted when the channel has been closed. Method calls on the
        channel are no longer valid after this signal has been emitted,
        and the connection manager may then remove the object from the bus
        at any point.
      
        """
        pass
  