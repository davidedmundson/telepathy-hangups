# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright © 2005-2009 Collabora Limited 
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


class ChannelTypeRoomList(dbus.service.Interface):
    """\
      A channel type for listing named channels available on the server. Once the
    ListRooms method is called, it emits signals for rooms present on the
    server, until you Close this
    channel. In some cases, it may not be possible
    to stop the deluge of information from the server. This channel should be
    closed when the room information is no longer being displayed, so that the
    room handles can be freed.

    This channel type may be implemented as a singleton on some protocols, so
    clients should be prepared for the eventuality that they are given a
    channel that is already in the middle of listing channels. The
    ListingRooms signal, or
    GetListingRooms method, can be used to check
    this.
    """

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.RoomList', in_signature='', out_signature='b')
    def GetListingRooms(self):
        """
        Check to see if there is already a room list request in progress
        on this channel.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.RoomList', in_signature='', out_signature='')
    def ListRooms(self):
        """
        Request the list of rooms from the server. The
        ListingRooms (True) signal should be
        emitted when this request is being processed,
        GotRooms when any room information is
        received, and ListingRooms (False) when
        the request is complete.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.RoomList', in_signature='', out_signature='')
    def StopListing(self):
        """
        Stop the room listing if it's in progress, but don't close the channel.
        The ListingRooms (False) signal should
        be emitted when the listing stops.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.RoomList', signature='a(usa{sv})')
    def GotRooms(self, Rooms):
        """
        Emitted when information about rooms on the server becomes available.
        The array contains the room handle (as can be passed to the
        RequestChannel
        method with HANDLE_TYPE_ROOM), the channel
        type, and a dictionary containing further information about the
        room as available. The following well-known keys and types are
        recommended for use where appropriate:

        
          handle-name (s)
          The identifier of the room (as would be returned by
            InspectHandles)

          name (s)
          The human-readable name of the room if different from the handle

          description (s)
          A description of the room's overall purpose

          subject (s)
          The current subject of conversation in the room (as would
            be returned by getting the string part of the Subject property)

          members (u)
          The number of members in the room

          password (b)
          True if the room requires a password to enter

          invite-only (b)
          True if you cannot join the room, but must be invited

          room-id (s)
          The human-readable identifier of a chat room (as would be
            returned by getting the RoomID property)

          server (s)
          The DNS name of the server hosting these channels (as would be
            returned by getting the Server property)
        
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.RoomList', signature='b')
    def ListingRooms(self, Listing):
        """
        Emitted to indicate whether or not room listing request is currently
        in progress.
      
        """
        pass
  