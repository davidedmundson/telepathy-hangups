# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright (C) 2010 Collabora Ltd.

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


class ChannelInterfaceSecurable(dbus.service.Interface):
    """\
      This interface exists to expose security information about
        Channels. The two
        properties are sometimes immutable and can be used to make
        decisions on how cautious to be about transferring sensitive
        data. The special case of ServerAuthentication
        channels is one example of where the two properties are
        immutable.

      For example, clients MAY use these properties to decide
        whether the PLAIN mechanism is acceptable for a
        SASLAuthentication
        channel.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Channel.Interface.Securable')
