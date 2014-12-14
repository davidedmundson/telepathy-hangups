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


class ChannelTypeContactSearch(dbus.service.Interface):
    """\
      A channel type for searching server-stored user directories. A new
        channel should be requested by a client for each search attempt, and
        closed when the search is completed or the required result has been
        found. Channels of this type should have TargetHandleType
        None (and hence TargetHandle 0 and
        TargetID
        ""). Requests for channels of this type need only
        optionally specify the Server property
        (if it is an allowed property in the connection's RequestableChannelClasses).

      Before searching, the
        AvailableSearchKeys property should be
        inspected to determine the valid search keys which can be provided to
        the Search method. A search request is
        then started by providing some of these terms to the Search method, and
        the SearchState will change from
        Not_Started to In_Progress.  As results are
        returned by the server, the
        SearchResultReceived signal is emitted
        for each contact found; when the search is complete, the search state
        will be set to Completed. If the search fails after Search
        has been called, the state will change to Failed.  A
        running search can be cancelled by calling
        Stop.

      If the protocol supports limiting the number of results returned by a
        search and subsequently requesting more results, after
        Limit results have been received the
        search state will be set to More_Available. Clients may
        call More to request another
        Limit results. If allowed by the
        connection manager, clients may specify the "page size" by specifying
        Limit when calling
        CreateChannel.
        

      The client should call the channel's Close
        method when it is finished with the channel.

      Each channel can only be used for a single search; a new channel
        should be requested for each subsequent search. Connection managers
        MUST support multiple ContactSearch channels being open at once (even
        to the same server, if applicable).

      It does not make sense to request this channel type using EnsureChannel;
        clients SHOULD request channels of this type using
        CreateChannel
        instead.

      
        A contact search channel that is already in use for a different
          search isn't useful.
      
    """

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.ContactSearch', in_signature='a{ss}', out_signature='')
    def Search(self, Terms):
        """
        Send a request to start a search for contacts on this connection. This
        may only be called while the SearchState
        is Not_Started; a valid search request will cause the
        SearchStateChanged signal to be emitted
        with the state In_Progress.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.ContactSearch', in_signature='', out_signature='')
    def More(self):
        """
        Request that a search in SearchState
        More_Available move back to state In_Progress
        and continue listing up to Limit more results.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.ContactSearch', in_signature='', out_signature='')
    def Stop(self):
        """
        Stop the current search. This may not be called while the
          SearchState is Not_Started. If called
          while the SearchState is In_Progress,
          SearchStateChanged will be emitted,
          with the state Failed and the error
          org.freedesktop.Telepathy.Error.Cancelled.

        Calling this method on a search in state Completed or Failed
          succeeds, but has no effect.

        
          Specifying Stop to succeed when the search has finished means that
            clients who call Stop just before receiving
            SearchStateChanged don't have to
            handle a useless error.
        

        Depending on the protocol, the connection manager may not be
          able to prevent the server from sending further results after this
          method returns; if this is the case, it MUST ignore any further
          results.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.ContactSearch', signature='usa{sv}')
    def SearchStateChanged(self, State, Error, Details):
        """
        Emitted when the SearchState property
          changes. The implementation MUST NOT make transitions other than the
          following:

        
          Not_Started → In_Progress
          In_Progress → More_Available
          More_Available → In_Progress
          In_Progress → Completed
          In_Progress → Failed
        
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.ContactSearch', signature='a{sa(sasas)}')
    def SearchResultReceived(self, Result):
        """
        Emitted when a some search results are received from the server.
        This signal can be fired arbitrarily many times so clients MUST NOT
        assume they'll get only one signal.
      
        """
        pass
  