# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2008-2009 Collabora Ltd.
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
      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
      02110-1301, USA.
  
"""

import dbus.service


class ClientApprover(dbus.service.Object):
    """\
      Approvers are clients that notify the user that new channels have
        been created by a contact, and allow the user to accept or reject
        those channels. The new channels are represented by a ChannelDispatchOperation
        object, which is passed to the
        AddDispatchOperation method.

      
        For instance, Empathy's tray icon, or the answer/reject window
          seen when a Maemo device receives a VoIP call, should be
          Approvers.
      

      Approvers can also select which channel handler will be used for the
        channel, for instance by offering the user a list of possible
        handlers rather than just an accept/reject choice.
        However, the Channel Dispatcher must be able to prioritize
        possible handlers on its own using some reasonable heuristic,
        probably based on user configuration.

      It is possible (and useful) to have an approver and
        a channel handler in the same process; this is particularly useful
        if a channel handler wants to claim responsibility for particular
        channels itself.

      All approvers are notified simultaneously. For instance, in a
        desktop system, there might be one approver that displays a
        notification-area icon, one that is part of a contact list
        window and highlights contacts there, and one that is part
        of a full-screen media player.

      Any approver can approve the handling of a channel dispatch operation
        with a particular channel handler by calling the HandleWith
        method. Approvers can also attempt to Claim
        channels; if this succeeds, the approver may handle the channels
        itself (if it is also a Handler), or close the channels in order to
        reject them.

      At the D-Bus level, there is no "reject" operation: approvers wishing
        to reject channels SHOULD call the Claim method, then (if it succeeds)
        close the channels in any way they see fit.

      The first approver to reply gets its decision acted on; any other
        approvers that reply at approximately the same time will get a D-Bus
        error, indicating that the channel has already been dealt with.

      Approvers should usually prompt the user and ask for
        confirmation, rather than dispatching the channel to a handler
        straight away.
    """

    @dbus.service.method('org.freedesktop.Telepathy.Client.Approver', in_signature='a(oa{sv})oa{sv}', out_signature='')
    def AddDispatchOperation(self, Channels, DispatchOperation, Properties):
        """
        Called by the channel dispatcher when a ChannelDispatchOperation
          in which the approver has registered an interest is created,
          or when the approver starts up while such channel dispatch
          operations already exist.

        The channel dispatcher SHOULD call this method on all approvers
          at the same time. If an approver returns an error from this method,
          the approver is assumed to be faulty.

        If no approvers return from this method
          successfully (including situations where there are no matching
          approvers at all), the channel dispatcher SHOULD consider this
          to be an error, and recover by dispatching the channel to the
          most preferred handler.

        
          Processes that aren't approvers (or don't at least ensure that there
          is some approver) probably shouldn't be making connections
          anyway, so there should always be at least one approver running.
        
      
        """
        raise NotImplementedError
  