# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright (C) 2008 Collabora Ltd.
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


class ConnectionInterfaceLocation(dbus.service.Interface):
    """\
      An interface on connections to support protocols which allow users to
        publish their current geographical location, and subscribe to the
        current location of their contacts.

      This interface is geared strongly towards automatic propagation and
        use of this information, so focuses on latitude, longitude and
        altitude which can be determined by GPS, although provision is also
        included for an optional human-readable description of locations. All
        co-ordinate information is required to be relative to the WGS84
        datum.

      The information published through this interface is intended to have
        the same scope as presence information, so will normally be made
        available to those individuals on the user's "publish" contact list.
        Even so, user interfaces should not automatically publish location
        information without the consent of the user, and it is recommended
        that an option is made available to reduce the accuracy of the
        reported information to allow the user to maintain their privacy.

      Location information is represented using the terminology of XMPP's
        XEP-0080
        or the XEP-0080-derived
        Geoclue API where
        possible.

      Clients of this interface SHOULD register an interest in it by calling
        Connection.AddClientInterest with an argument
        containing the name of this interface,
        before calling any Location method. If they do so, they SHOULD also call
        Connection.RemoveClientInterest after use to allow
        the CM to release resources associated with this interface.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.Location')

    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Location', in_signature='au', out_signature='a{ua{sv}}')
    def GetLocations(self, Contacts):
        """
        Return the current locations of the given contacts, if they are
          already known. If any of the given contacts' locations are not known,
          request their current locations, but return immediately without waiting
          for a reply; if a reply with a non-empty location is later received
          for those contacts, the LocationUpdated
          signal will be emitted for them.

        
          This method is appropriate for "lazy" location finding, for instance
            displaying the location (if available) of everyone in your contact
            list.
        

        For backwards compatibility, if this method is called by a client
          whose "interest count" for this interface, as defined by Connection.AddClientInterest, is zero, the
          Connection SHOULD behave as if AddClientInterest had been called for
          this interface just before that method call. Clients that do not
          explicitly call AddClientInterest SHOULD NOT call Connection.RemoveClientInterest either.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Location', in_signature='u', out_signature='a{sv}')
    def RequestLocation(self, Contact):
        """
        Return the current location of the given contact. If necessary, make
        a request to the server for up-to-date information, and wait for a
        reply.

        
          This method is appropriate for use in a "Contact Information..."
          dialog; it can be used to show progress information (while waiting
          for the method to return), and can distinguish between various error
          conditions.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Location', in_signature='a{sv}', out_signature='')
    def SetLocation(self, Location):
        """
        Set the local user's own location.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.Location', signature='ua{sv}')
    def LocationUpdated(self, Contact, Location):
        """
        Emitted when a contact's location changes or becomes known.
      
        """
        pass
  