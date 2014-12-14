# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright (C) 2007 Collabora Limited 

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


class ChannelInterfaceChatState(dbus.service.Interface):
    """\
      An interface for channels for receiving notifications of remote contacts'
      state, and for notifying remote contacts of the local state.

      Clients should assume that a contact's state is Channel_Chat_State_Inactive
      unless they receive a notification otherwise.

      The Channel_Chat_State_Gone state is treated differently to other states:
      
        It may not be used for multi-user chats
        It may not be explicitly sent
        It should be automatically sent when the channel is closed
        It must not be sent to the peer if a channel is closed without being used
        Receiving it must not cause a new channel to be opened
      

      The different states are defined by XEP-0085, but may be applied to any suitable protocol.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Channel.Interface.ChatState')

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.ChatState', in_signature='u', out_signature='')
    def SetChatState(self, State):
        """
        Set the local state and notify other members of the channel that it
        has changed.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.ChatState', signature='uu')
    def ChatStateChanged(self, Contact, State):
        """
        Emitted when the state of a member of the channel has changed.
        This includes local state.
      
        """
        pass
  