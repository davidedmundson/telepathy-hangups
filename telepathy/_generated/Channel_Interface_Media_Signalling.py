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


class ChannelInterfaceMediaSignalling(dbus.service.Interface):
    """\
      An interface for signalling a channel containing synchronised media
        sessions which can contain an arbitrary number of streams. The
        presence of this interface on a Channel indicates that the connection
        manager will not carry out the actual streaming for this channel,
        and that the client handling the channel is responsible for doing
        so; in most cases we recommend doing this by using the
        telepathy-farsight library.

      
        Streaming audio and (particularly) video requires a high level of
          integration with the UI, and having the connection manager act as
          a proxy would be likely to introduce unacceptable latency. As a
          result, audio/video streaming is offloaded into the client
          where possible, as an exception to the general design of
          Telepathy.
      

      The negotiation interface is based on the API of the
        Farsight library.
        This, in turn, is based upon the IETF MMusic ICE drafts, where
        connections are established by signalling potential connection
        candidates to the peer until a usable connection is found, and
        codecs are negotiated with an SDP-style offer and answer. However,
        the principles should be applicable to other media streaming methods
        and the API re-used without difficulty.

      Note that the naming conventions used in the MediaStreamHandler
        and MediaSessionHandler interfaces are rather confusing; methods
        have signal-like names and signals have method-like names, due to
        the API being based rather too closely on that of Farsight. This
        is for historical reasons and will be fixed in a future release
        of the Telepathy specification.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Channel.Interface.MediaSignalling')

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.MediaSignalling', in_signature='', out_signature='a(os)')
    def GetSessionHandlers(self):
        """
        Returns all currently active session handlers on this channel
        as a list of (session_handler_path, type).
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.MediaSignalling', signature='os')
    def NewSessionHandler(self, Session_Handler, Session_Type):
        """
        Signal that a session handler object has been created. The client
        should create a session object and create streams for the streams
        within.
      
        """
        pass
  