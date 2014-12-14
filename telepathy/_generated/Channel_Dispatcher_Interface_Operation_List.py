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
      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
      USA.
  
"""

import dbus.service


class ChannelDispatcherInterfaceOperationList(dbus.service.Interface):
    """\
      This interface allows users of the ChannelDispatcher to enumerate
        all the pending dispatch operations, with change notification.

      
        The existence of the
          DispatchOperations property allows a
          newly started approver to pick up existing dispatch operations.

        This is on a separate interface so clients that aren't interested
          in doing this aren't woken up by its signals.
      
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.ChannelDispatcher.Interface.OperationList')

    @dbus.service.signal('org.freedesktop.Telepathy.ChannelDispatcher.Interface.OperationList', signature='oa{sv}')
    def NewDispatchOperation(self, Dispatch_Operation, Properties):
        """
        Emitted when a dispatch operation is added to
          DispatchOperations.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.ChannelDispatcher.Interface.OperationList', signature='o')
    def DispatchOperationFinished(self, Dispatch_Operation):
        """
        Emitted when a dispatch operation finishes (i.e. exactly once per
        emission of ChannelDispatchOperation.Finished).

        
          Strictly speaking this is redundant with
          ChannelDispatchOperation.Finished, but it provides full
          change-notification for the
          DispatchOperations property.
        
      
        """
        pass
  