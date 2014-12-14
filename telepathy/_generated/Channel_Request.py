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
      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
      MA 02110-1301, USA.
  
"""

import dbus.service


class ChannelRequest(dbus.service.Object):
    """\
      A channel request is an object in the ChannelDispatcher representing
        an ongoing request for some channels to be created or found. There
        can be any number of ChannelRequest objects at the same time.

      Its well-known bus name is the same as that of the ChannelDispatcher,
        "org.freedesktop.Telepathy.ChannelDispatcher".

      
        See
          ChannelDispatcher.CreateChannel
          for rationale for ChannelRequest being a separate object.
      

      A channel request can be cancelled by any client (not just the one
        that requested it). This means that the ChannelDispatcher will
        Close
        the resulting channel, or refrain from requesting it at all, rather
        than dispatching it to a handler.
    """

    @dbus.service.method('org.freedesktop.Telepathy.ChannelRequest', in_signature='', out_signature='')
    def Proceed(self):
        """
        Proceed with the channel request.

        
          The client that created this object calls this method
            when it has connected signal handlers for
            Succeeded and
            Failed.
        

        Clients other than the client which created the ChannelRequest
          MUST NOT call this method.

        This method SHOULD return immediately; on success, the request
          might still fail, but this will be indicated asynchronously
          by the Failed signal.

        Proceed cannot fail, unless clients have got the life-cycle
          of a ChannelRequest seriously wrong (e.g. a client calls this
          method twice, or a client that did not create the ChannelRequest
          calls this method). If it fails, clients SHOULD assume that the
          whole ChannelRequest has become useless.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.ChannelRequest', in_signature='', out_signature='')
    def Cancel(self):
        """
        Cancel the channel request. The precise effect depends on the
          current progress of the request.

        If the connection manager has not already been asked to create
          a channel, then Failed is emitted
          immediately, and the channel request is removed.

        If the connection manager has already been asked to create a
          channel but has not produced one yet (e.g. if Connection.Interface.Requests.CreateChannel
          has been called, but has not yet returned), then the
          ChannelDispatcher will remember that the request has been cancelled.
          When the channel appears, it will be closed (if it was newly
          created and can be closed), and will not be dispatched to a
          handler.

        If the connection manager has already returned a channel, but the
          channel has not yet been dispatched to a handler
          then the channel dispatcher will not dispatch that
          channel to a handler. If the channel was newly created for this
          request, the channel dispatcher will close it with Close;
          otherwise, the channel dispatcher will ignore it. In either case,
          Failed will be emitted when processing
          has been completed.

        If Failed is emitted in response to
          this method, the error SHOULD be
          org.freedesktop.Telepathy.Error.Cancelled.

        If the channel has already been dispatched to a handler, then
          it's too late to call this method, and the channel request will
          no longer exist.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.ChannelRequest', signature='ss')
    def Failed(self, Error, Message):
        """
        The channel request has failed. It is no longer present,
          and further methods must not be called on it.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.ChannelRequest', signature='')
    def Succeeded(self):
        """
        The channel request has succeeded. It is no longer present,
          and further methods must not be called on it.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.ChannelRequest', signature='oa{sv}oa{sv}')
    def SucceededWithChannel(self, Connection, Connection_Properties, Channel, Channel_Properties):
        """
        Variant of the Succeeded signal
        allowing to get the channel which has been created.

        This signal MUST be emitted if the
          ChannelDispatcher's
          SupportsRequestHints
          property is true. If supported, it MUST be emitted before
          the Succeeded signal.
      
        """
        pass
  