# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2009-2010 Collabora Ltd.

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


class ProtocolInterfacePresence(dbus.service.Interface):
    """\
      An interface for protocols where it might be possible to set the
        user's presence, and the supported presence types can be predicted
        before connecting.

      
        This allows UIs to show or hide presence types that aren't
          always supported, such as "invisible", while not online.
      

      The properties on this interface SHOULD be cached in the
        .manager file, in the
        [Protocol proto]
        group. For each status s in
        Statuses, that group should
        contain a key of the form status-s whose value
        is the Connection_Presence_Type as an ASCII
        decimal integer, followed by a space-separated sequence of tokens
        from the following set:

      
        settable
        If present, the user can set this status on themselves using
          SetPresence; this corresponds to May_Set_On_Self
          in the Simple_Status_Spec struct.

        message
        If present, the user can set a non-empty message for this status;
          this corresponds to Can_Have_Message in the
          Simple_Status_Spec struct.
      

      Unrecognised tokens MUST be ignored.

      For instance, an XMPP connection manager might have this
        .manager file:

[Protocol jabber]
Interfaces=org.freedesktop.Telepathy.Protocol.Interface.Presence;
param-account=s required
param-password=s required
status-offline=1
status-unknown=7
status-error=8
status-hidden=5 settable message
status-xa=4 settable message
status-away=3 settable message
status-dnd=6 settable message
status-available=2 settable message
status-chat=2 settable message


      which corresponds to these property values (using a Python-like
        syntax):

Statuses = {
    'offline': (OFFLINE, False, False),
    'unknown': (UNKNOWN, False, False),
    'error': (ERROR, False, False),
    'hidden': (HIDDEN, True, True),
    'xa': (EXTENDED_AWAY, True, True),
    'away': (AWAY, True, True),
    'dnd': (BUSY, True, True),
    'available': (AVAILABLE, True, True),
    'chat': (AVAILABLE, True, True),
}

    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Protocol.Interface.Presence')
