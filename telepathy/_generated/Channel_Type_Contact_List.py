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


class ChannelTypeContactList(dbus.service.Interface):
    """\
      A channel type for representing a list of people on the server which is
    not used for communication. This is intended for use with the interface
    Channel.Interface.Group
    for managing buddy lists and privacy lists
    on the server. This channel type has no methods because all of the
    functionality it represents is available via the group interface.

    There are currently two types of contact list:
    HANDLE_TYPE_LIST is a "magic" server-defined list, and
    HANDLE_TYPE_GROUP is a user-defined contact group.

    For server-defined lists like the subscribe list, singleton instances
    of this channel type should be created by the connection manager at
    connection time if the list exists on the server, or may be requested
    by using the appropriate handle.  These handles can be obtained using
    RequestHandles
    with a Handle_Type of HANDLE_TYPE_LIST and one of the
    following identifiers:

    
      subscribe - the group of contacts for whom you receive presence
      publish - the group of contacts who may receive your presence
      hide - a group of contacts who are on the publish list but are temporarily disallowed from receiving your presence
      allow - a group of contacts who may send you messages
      deny - a group of contacts who may not send you messages
      stored - on protocols where the user's contacts are stored, this
      contact list contains all stored contacts regardless of subscription
      status.
    

    A contact can be in several server-defined lists. All lists are optional
    to implement. If RequestHandles
    or RequestChannel
    for a particular contact list raises an error, this indicates that the
    connection manager makes no particular statement about the list's contents;
    clients MUST NOT consider this to be fatal.

    If a client wants to list all of a user's contacts, it is appropriate to
    use the union of the subscribe, publish and stored lists, including the
    local and remote pending members.

    For example in XMPP, contacts who have the subscription type "none",
    "from", "to" and "both" can be respectively in the lists:

    
      "none": stored
      "from": stored and publish
      "to": stored and subscribe
      "both": stored, publish and subscribe
    

    These contact list channels may not be closed.

    For user-defined contact groups, instances of this channel type should
    be created by the connection manager at connection time for each group
    that exists on the server. New, empty groups can be created by calling
    RequestHandles
    with a Handle_Type of HANDLE_TYPE_GROUP and with the
    name set to the human-readable UTF-8 name of the group.

    User-defined groups may be deleted by calling Close on the
    channel, but only if
    the group is already empty. Closing a channel to a non-empty group is
    not allowed; its members must be set to the empty set first.

    On some protocols (e.g. XMPP) empty groups are not represented on the
    server, so disconnecting from the server and reconnecting might cause
    empty groups to vanish.
    """
