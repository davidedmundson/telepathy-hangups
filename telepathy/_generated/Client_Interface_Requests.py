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


class ClientInterfaceRequests(dbus.service.Interface):
    """\
      This interface can be implemented by a Handler to be notified about
        requests for channels that it is likely to be asked to handle.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Client.Interface.Requests')

    @dbus.service.method('org.freedesktop.Telepathy.Client.Interface.Requests', in_signature='oa{sv}', out_signature='')
    def AddRequest(self, Request, Properties):
        """
        Called by the ChannelDispatcher to indicate that channels have been
          requested, and that if the request is successful, they will probably
          be handled by this Handler. The ChannelDispatcher SHOULD only
          call this method on one handler per request.

        
          This allows the UI to start preparing to handle the channels
            in advance (e.g. render a window with an "in progress" message),
            improving perceived responsiveness.

          The use of "probably" is because you can't necessarily tell from
            a channel request which handler will handle particular channels.
            A reasonable heuristic would be to match the request against the
            HandlerChannelFilter,
            and respect the preferred handler (if any).
        

        If the request succeeds and is given to the expected Handler,
          the Requests_Satisfied parameter to
          HandleChannels
          can be used to match the channel to a previous AddRequest call.

        
          This lets the UI direct the channels to the window that it
            already opened.
        

        If the request fails, the expected handler is notified by the
          channel dispatcher calling its
          RemoveRequest method.

        
          This lets the UI close the window or display the error.
        

        The channel dispatcher SHOULD remember which handler was notified,
          and if the channel request succeeds, it SHOULD dispatch the channels
          to the expected handler, unless the channels do not match that
          handler's HandlerChannelFilter.
          If the channels are not dispatched to the expected handler, the
          handler that was expected is notified by the channel dispatcher
          calling its RemoveRequest method
          with the NotYours error.

        
          Expected handling is for the UI to close the window it
            previously opened.
        

        Handlers SHOULD NOT return an error from this method; errors
          returned from this method SHOULD NOT alter the channel dispatcher's
          behaviour.

        
          Calls to this method are merely a notification.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Client.Interface.Requests', in_signature='oss', out_signature='')
    def RemoveRequest(self, Request, Error, Message):
        """
        Called by the ChannelDispatcher to indicate that a request
          previously passed to AddRequest
          has failed and should be disregarded.

        Handlers SHOULD NOT return an error from this method; errors
          returned from this method SHOULD NOT alter the channel dispatcher's
          behaviour.

        
          Calls to this method are merely a notification.
        
      
        """
        raise NotImplementedError
  