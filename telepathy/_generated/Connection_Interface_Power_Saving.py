# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright © 2007-2010 Collabora Limited 

    This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Library General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
  
"""

import dbus.service


class ConnectionInterfacePowerSaving(dbus.service.Interface):
    """\
      Some protocols support mechanisms for reducing bandwidth usage—and
        hence power usage, on mobile devices—when the user is not directly
        interacting with their IM client. For instance, Google Talk's XMPP
        server supports queueing incoming presence updates at the client's
        instruction; the client can instruct the server to deliver all
        outstanding presence updates at a later time. This interface may be
        used to instruct the connection manager to enable and disable such
        protocol-level features when a screensaver is activated, the device
        screen is locked, and so on, by calling the
        SetPowerSaving method.

      Enabling power saving SHOULD NOT change behaviour in any way
        that is noticable to a user not actively interacting with their client.
        For example, delaying presence updates somewhat is unlikely to be
        noticed by a user not staring at their device waiting for a contact to
        come online; on the other hand, requesting that the server queue
        incoming messages would be noticable by the user, so is not an
        acceptable effect of calling
        SetPowerSaving.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.PowerSaving')

    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.PowerSaving', in_signature='b', out_signature='')
    def SetPowerSaving(self, Activate):
        """
        Turn power saving mode on or off.

        
          Depending on the device's activity level, the
            connection can have its power saving mode turned on or off.
        

        Errors raised by this method indicate that power saving could not be
          enabled, which SHOULD NOT generally be treated as fatal.

        
          If the CM cannot switch modes, either because of the
          protocol (NotImplemented), or because of the service
          (NotAvailable), Mission Control (or whoever manages this)
          should be made aware. The error could be ignored or, in the extreme,
          be fascist and disconnect the account.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.PowerSaving', signature='b')
    def PowerSavingChanged(self, Active):
        """
        The PowerSavingActive
        property changed.
      
        """
        pass
  