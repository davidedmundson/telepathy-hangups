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
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

  
"""

import dbus.service


class AccountManager(dbus.service.Object):
    """\
      The account manager is a central service used to store account
        details.

      The current account manager is defined to be the process that owns
        the well-known bus name org.freedesktop.Telepathy.AccountManager on
        the session bus. This process must export an
        /org/freedesktop/Telepathy/AccountManager object with the
        AccountManager interface.

      Until a mechanism exists for making a reasonable automatic choice
        of AccountManager implementation, implementations SHOULD NOT
        register as an activatable service for the AccountManager's
        well-known bus name. Instead, it is RECOMMENDED that some component
        of the user's session will select and activate a particular
        implementation, and that other Telepathy-enabled programs can
        detect whether Telepathy is in use by checking whether the
        AccountManager's well-known name is in use at runtime.
    """

    @dbus.service.method('org.freedesktop.Telepathy.AccountManager', in_signature='sssa{sv}a{sv}', out_signature='o')
    def CreateAccount(self, Connection_Manager, Protocol, Display_Name, Parameters, Properties):
        """
        Request the creation of a new Account. The
        account manager SHOULD NOT allow invalid accounts to be created.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.AccountManager', signature='o')
    def AccountRemoved(self, Account):
        """
        The given account has been removed.

        
          This is effectively change notification for the valid and invalid
          accounts lists. On emission of this signal, the Account indicated
          will no longer be present in either of the lists.
        
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.AccountManager', signature='ob')
    def AccountValidityChanged(self, Account, Valid):
        """
        The validity of the given account has changed. New accounts are
        also indicated by this signal, as an account validity change
        (usually to True) on an account that did not previously exist.

        
          This is effectively change notification for the valid and invalid
          accounts lists.
        
      
        """
        pass
  