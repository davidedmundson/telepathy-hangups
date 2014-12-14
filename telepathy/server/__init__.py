"""
telepathy-python - Base classes defining the interfaces of the Telepathy framework

Copyright (C) 2005, 2006 Collabora Limited
Copyright (C) 2005, 2006 Nokia Corporation
Copyright (C) 2006 INdT

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
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

from telepathy.server.connmgr import *
from telepathy.server.conn import *
from telepathy.server.channel import *
from telepathy.server.channelmanager import *
from telepathy.server.debug import *
from telepathy.server.handle import *
from telepathy.server.media import *
from telepathy.server.properties import *
from telepathy.server.protocol import *

from telepathy._generated.Client_Observer import ClientObserver as Observer
from telepathy._generated.Client_Approver import ClientApprover as Approver
from telepathy._generated.Client_Handler import ClientHandler as Handler
from telepathy._generated.Client_Interface_Requests import ClientInterfaceRequests

from telepathy import version, __version__
