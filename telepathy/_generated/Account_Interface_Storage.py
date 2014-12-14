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
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

  
"""

import dbus.service


class AccountInterfaceStorage(dbus.service.Interface):
    """\
      
        This interface extends the core Account interface to specify details
        regarding the storage of this account.
      

      
        
          Single-sign-on systems do not generally have directly user-editable
          properties for Accounts, and require the user to visit a specific UI
          to alter their account properties. User interfaces should know not to
          expose these account properties as user-editable, and instead
          redirect the user to the appropriate interface.
        
      

    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Account.Interface.Storage')
