# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright (C) 2008 Collabora Limited 
 Copyright (C) 2008 Nokia Corporation 

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


class ChannelInterfaceCallState(dbus.service.Interface):
    """\
      An interface for streamed media channels that can indicate call
        progress or call states. The presence of this interface is no guarantee
        that call states will actually be signalled (for instance, SIP
        implementations are not guaranteed to generate status 180 Ringing, so a
        call can be accepted without the Ringing flag ever having been set;
        similarly, Jingle implementations are not guaranteed to send
        <ringing/>).

      To notify the other participant in the call that they are on hold,
        see Hold.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Channel.Interface.CallState')

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.CallState', in_signature='', out_signature='a{uu}')
    def GetCallStates(self):
        """
        Get the current call states for all contacts involved in this call.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.CallState', signature='uu')
    def CallStateChanged(self, Contact, State):
        """
        Emitted when the state of a member of the channel has changed.
      
        """
        pass
  