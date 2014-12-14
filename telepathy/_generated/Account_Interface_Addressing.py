# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2010 Collabora Ltd

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


class AccountInterfaceAddressing(dbus.service.Interface):
    """\
      Some accounts can be used for multiple protocols; for instance, SIP
        and Skype accounts can often be used to contact the PSTN, MSN and
        Yahoo accounts can contact each other, and XMPP accounts can
        potentially contact many protocols via a transport.
      However, if the user does not intend to make use of this functionality,
        user interfaces can improve clarity by not displaying it: for instance,
        if a user prefers to call phone numbers via a particular SIP account,
        when an address book displays a contact with a phone number, it is
        desirable to display a "call with SIP" button for that account, but
        avoid displaying similar buttons for any other configured SIP or
        Skype accounts.
      The purpose of this interface is to allow this "for use with" information
        to be recorded and retrieved.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Account.Interface.Addressing')

    @dbus.service.method('org.freedesktop.Telepathy.Account.Interface.Addressing', in_signature='sb', out_signature='')
    def SetURISchemeAssociation(self, URI_Scheme, Association):
        """
        Associate (or disassociate) an account with a particular
          URI addressing scheme, (such as 'tel' for telephony)
      
        """
        raise NotImplementedError
  