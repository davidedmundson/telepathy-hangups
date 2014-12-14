# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright (C) 2008 Collabora Ltd.
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
      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
      USA.
  
"""

import dbus.service


class ChannelInterfaceDestroyable(dbus.service.Interface):
    """\
      This interface exists to support channels where
        Channel.Close
        is insufficiently destructive. At the moment this means
        Channel.Type.Text,
        but the existence of this interface means that unsupported channels
        can be terminated in a non-channel-type-specific way.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Channel.Interface.Destroyable')

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Destroyable', in_signature='', out_signature='')
    def Destroy(self):
        """
        Close the channel abruptly, possibly with loss of data. The
          connection manager MUST NOT re-create the channel unless/until
          more events occur.

        
          The main motivating situation for this method is that when a Text
            channel with pending messages is closed with Close, it comes back
            as an incoming channel (to avoid a race between Close and an
            incoming message). If Destroy is called on a Text channel, the CM
            should delete all pending messages and close the channel, and
            the channel shouldn't be re-created until/unless another message
            arrives.
        

        Most clients SHOULD call
          Channel.Close
          instead. However, if a client explicitly intends to destroy the
          channel with possible loss of data, it SHOULD call this method
          if this interface is supported (according to the
          Channel.Interfaces
          property), falling back to Close if not.

        In particular, channel dispatchers SHOULD use this method if
          available when terminating channels that cannot be handled
          correctly (for instance, if no handler has been installed for
          a channel type, or if the handler crashes repeatedly).

        Connection managers do not need to implement this interface on
          channels where Close and Destroy would be equivalent.

        
          Callers need to be able to fall back to Close in any case.
        
      
        """
        raise NotImplementedError
  