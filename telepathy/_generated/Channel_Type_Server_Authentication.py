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


class ChannelTypeServerAuthentication(dbus.service.Interface):
    """\
      The type for a channel representing an authentication step with the
        server. The actual authentication functionality is implemented by
        the additional interface named in
        AuthenticationMethod,
        such as Channel.Interface.SASLAuthentication.

      Future authentication steps also supported by this channel type might
        include solving a captcha and/or agreeing to an EULA or terms-of-use
        document; each of these would be represented by a channel with this
        type, but a different
        AuthenticationMethod.

      Channels of this type will normally be be signalled and dispatched
        while the Connection
        owning them is in the CONNECTING state. They MAY also appear on a
        Connection in the CONNECTED state, for instance if periodic
        re-authentication is required.

      Normally, only one channel of this type will
        exist on a given Connection; if there is more than one, the handler
        must complete authentication with each of them in turn.

      Channels of this type cannot be requested with methods such as
        CreateChannel.
        They always have Requested = False,
        TargetHandleType = None
        and TargetHandle
        = 0.

      While it is CONNECTING, the Connection MUST NOT proceed with
        connection, or signal
        StatusChanged
        to the CONNECTED state, until each channel of this type has either
        been accepted as having a positive result (for instance, on SASL
        channels this is done with the AcceptSASL method), or closed with the Close method.

      
        ServerAuthentication channels normally represent the client
          authenticating itself to the server, but can also be used for the
          server to authenticate itself to the client (i.e. prove that it is
          in fact the desired server and not an imposter). Until the
          authentication handler has confirmed this, connection should not
          continue.
      

      If a channel of this type is closed with the Close method before
        authentication has succeeded, this indicates that the Handler has
        given up its attempts to authenticate or that no Handler is
        available.

      If this occurs, the connection manager MAY attempt to continue
        connection (for instance, performing SASL authentication by using any
        credentials passed to RequestConnection,
        for instance from the Account.Parameters). If this fails
        or has already been tried, the Connection will
        disconnect.

      
        In particular, the ChannelDispatcher will close the
          channel if it cannot find a handler.
      

      When the connection is done with the channel and it is no
        longer needed, it is left open until either the connection state
        turns to DISCONNECTED or the handler closes the channel. The
        channel SHOULD NOT close itself once finished with.
    """
