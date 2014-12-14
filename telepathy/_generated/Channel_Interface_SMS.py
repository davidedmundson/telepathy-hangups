# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2008–2010 Nokia Corporation
Copyright © 2010 Collabora Ltd.

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


class ChannelInterfaceSMS(dbus.service.Interface):
    """\
      This interface contains SMS-specific properties for text
        channels.

      The presence of this interface on a channel does not imply that
        messages will be delivered via SMS.

      This interface MAY appear in the
        Interfaces property
        of channels where SMSChannel would be
        immutable and false. It SHOULD appear on channels where
        SMSChannel is immutable and true, and
        also on channels where SMSChannel is
        mutable (i.e. channels that might fall back to sending SMS at any
        time, such as on MSN).

      Handler filters

      A handler for class 0 SMSes should advertise the following filter:

      
{ ...ChannelType:
      ...Text,
  ...TargetHandleType:
      Handle_Type_Contact,
  ...SMS.Flash:
      True,
}

      It should also set its BypassApproval property
        to True, so that it is invoked immediately for new
        channels.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Channel.Interface.SMS')

    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.SMS', signature='b')
    def SMSChannelChanged(self, SMSChannel):
        """
        This signal indicates a change in the
        SMSChannel property.
      
        """
        pass
  