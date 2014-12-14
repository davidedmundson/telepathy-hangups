# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright (C) 2005-2008 Collabora Limited 
 Copyright (C) 2005-2008 Nokia Corporation 
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


class ChannelInterfaceHold(dbus.service.Interface):
    """\
      Interface for channels where you may put the channel on hold.
        This only makes sense for channels where
        you are streaming media to or from the members. (To see whether the
        other participant has put you on hold, see CallState.)

      If you place a channel on hold, this indicates that you do not wish
        to be sent media streams by any of its members and will be ignoring
        any media streams you continue to receive. It also requests that the
        connection manager free up any resources that are only needed for
        an actively used channel (e.g. in a GSM or PBX call, it will be
        necessary to place an active call on hold before you can start
        another call).
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Channel.Interface.Hold')

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Hold', in_signature='', out_signature='uu')
    def GetHoldState(self):
        """
        Return whether the local user has placed the channel on hold.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Hold', in_signature='b', out_signature='')
    def RequestHold(self, Hold):
        """
        Request that the channel be put on hold (be instructed not to send
          any media streams to you) or be taken off hold.

        If the connection manager can immediately tell that the requested
          state change could not possibly succeed, this method SHOULD
          return the NotAvailable error. If the requested state is the
          same as the current state, this method SHOULD return successfully
          without doing anything.

        Otherwise, this method SHOULD immediately set the hold state to
          Local_Hold_State_Pending_Hold or Local_Hold_State_Pending_Unhold
          (as appropriate), emitting
          HoldStateChanged if this is a change,
          and return successfully.

        The eventual success or failure of the request is indicated by a
          subsequent HoldStateChanged signal, changing the hold state to
          Local_Hold_State_Held or Local_Hold_State_Unheld.

        If the channel has multiple streams, and the connection manager
          succeeds in changing the hold state of one stream but fails to
          change the hold state of another, it SHOULD attempt to revert
          all streams to their previous hold states.

        The following state transitions SHOULD be used, where
          appropriate:

        
          Successful hold:
            (Unheld, any reason) → (Pending_Hold, Requested) →
            (Held, Requested)
          
          Successful unhold:
            (Held, any reason) → (Pending_Unhold, Requested) →
            (Unheld, Requested)
          
          Attempting to unhold fails at the first attempt to acquire a
            resource:
            (Held, any reason) → (Pending_Unhold, Requested) →
            (Held, Resource_Not_Available)
          
          Attempting to unhold acquires one resource, but fails to acquire
            a second, and takes time to release the first:
            (Held, any reason) → (Pending_Unhold, Requested) →
            (Pending_Hold, Resource_Not_Available) →
            (Held, Resource_Not_Available)
          
        
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.Hold', signature='uu')
    def HoldStateChanged(self, HoldState, Reason):
        """
        Emitted to indicate that the hold state has changed for this channel.
        This may occur as a consequence of you requesting a change with
        RequestHold, or the state changing as a
        result of a request from
        another process.
      
        """
        pass
  