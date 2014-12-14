# telepathy-python - Base classes defining the interfaces of the Telepathy framework
#
# Copyright (C) 2005, 2006 Collabora Limited
# Copyright (C) 2005, 2006 Nokia Corporation
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from telepathy._generated.interfaces import *

# Backwards compatibility
CONN_MGR_INTERFACE = CONNECTION_MANAGER
CONN_INTERFACE = CONNECTION
CHANNEL_INTERFACE = CHANNEL
CHANNEL_HANDLER_INTERFACE = CHANNEL_HANDLER

# More backwards compatibility
CONN_INTERFACE_ALIASING = CONNECTION_INTERFACE_ALIASING
CONN_INTERFACE_AVATARS = CONNECTION_INTERFACE_AVATARS
CONN_INTERFACE_CAPABILITIES = CONNECTION_INTERFACE_CAPABILITIES
CONN_INTERFACE_PRESENCE = CONNECTION_INTERFACE_PRESENCE
CONN_INTERFACE_RENAMING = CONNECTION_INTERFACE_RENAMING
