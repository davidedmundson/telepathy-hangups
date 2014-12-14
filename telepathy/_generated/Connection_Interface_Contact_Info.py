# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright (C) 2008 Collabora Limited 
 Copyright (C) 2008 Nokia Corporation 

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


class ConnectionInterfaceContactInfo(dbus.service.Interface):
    """\
      An interface for requesting information about a contact on a given
        connection. Information is represented as a list of
        Contact_Info_Fields forming a
        structured representation of a vCard (as defined by RFC 2426), using
        field names and semantics defined therein.

      On some protocols, information about your contacts is pushed to you,
        with change notification; on others, like XMPP, the client must
        explicitly request the avatar, and has no way to tell whether it has
        changed without retrieving it in its entirety. This distinction is
        exposed by ContactInfoFlags containing
        the Push flag.

      On protocols with the Push flag set, UIs can connect to
        ContactInfoChanged, call
        GetContactInfo once at login for the set
        of contacts they are interested in, and then be sure they will receive
        the latest contact info. On protocols like XMPP, clients can do the
        same, but will receive (at most) opportunistic updates if the info is
        retrieved for other reasons. Clients may call
        RequestContactInfo or
        RefreshContactInfo to force a contact's
        info to be updated, but MUST NOT do so unless this is either in
        response to direct user action, or to refresh their own cache after a
        number of days.

      
        We don't want clients to accidentally cause a ridiculous amount of
          network traffic.
      
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.ContactInfo')

    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactInfo', in_signature='au', out_signature='a{ua(sasas)}')
    def GetContactInfo(self, Contacts):
        """
        Request information on several contacts at once.  This SHOULD only
        return cached information, omitting handles for which no information is
        cached from the returned map.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactInfo', in_signature='au', out_signature='')
    def RefreshContactInfo(self, Contacts):
        """
        Retrieve information for the given contact, requesting it from the
        network if an up-to-date version is not cached locally. This method
        SHOULD return immediately, emitting
        ContactInfoChanged when the contacts'
        updated contact information is returned.

        
          This method allows a client with cached contact information to
          update its cache after a number of days.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactInfo', in_signature='u', out_signature='a(sasas)')
    def RequestContactInfo(self, Contact):
        """
        Retrieve information for a contact, requesting it from the network if
        it is not cached locally.

        
          This method is appropriate for an explicit user request to show
          a contact's information; it allows a UI to wait for the contact
          info to be returned.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactInfo', in_signature='a(sasas)', out_signature='')
    def SetContactInfo(self, ContactInfo):
        """
        Set new contact information for this connection, replacing existing
        information.  This method is only suppported if
        ContactInfoFlags contains
        Can_Set, and may only be passed fields conforming to
        SupportedFields.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.ContactInfo', signature='ua(sasas)')
    def ContactInfoChanged(self, Contact, ContactInfo):
        """
        Emitted when a contact's information has changed or been received for
        the first time on this connection.
      
        """
        pass
  