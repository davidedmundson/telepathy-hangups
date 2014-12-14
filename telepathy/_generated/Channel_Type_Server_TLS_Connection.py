# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright © 2010 Collabora Limited 

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


class ChannelTypeServerTLSConnection(dbus.service.Interface):
    """\
      A channel type that carries a TLS certificate between a server
      and a client connecting to it.
      Channels of this kind always have Requested = False,
      TargetHandleType
      = None and TargetHandle
      = 0, and cannot be requested with methods such as CreateChannel.
      Also, they SHOULD be dispatched while the
      Connection
      owning them is in the CONNECTING state.
      In this case, handlers SHOULD accept or reject the certificate, using
      the relevant methods on the provided object, or MAY just Close the channel before doing so, to fall
      back to a non-interactive verification process done inside the CM.
      For example, channels of this kind can pop up while a client is
      connecting to an XMPP server.
    """
