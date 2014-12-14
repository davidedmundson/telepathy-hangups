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


class ConnectionInterfaceClientTypes(dbus.service.Interface):
    """\
      An interface on connections to support protocols which allows users to
        subscribe to the client types of their contacts.

      One can connect to instant messaging networks on a huge variety of
        devices, from PCs, to phones to consoles. It can be useful for users
        to know what kind of device a contact is using so that he or she
        can decide not to send that big file or start a video chat. This
        interface exposes exactly this information for clients to display.

      The client types are represented in strings, using the values
        
        documented by the XMPP registrar with some additional types
        added for other protocols. A contact can set one or more client types
        so this interface returns a list of strings to denote client types
        for a contact. The well-known client types to be used are:

      
        bot
        console (minimal non-GUI client used on dumb terminals or
          text-only screens, not a games console)
        handheld
        pc
        phone
        web

      

      If the empty list is given as the client types, this means that
        details about the contact's client types are unknown. If there are
        multiple resources of a contact online at one point in time, the
        client types of the most available resource will be returned. In
        other words, the returned client types are those for the resource whose
        presence will be retreived using the
        SimplePresence
        interface.

      For example, if a contact has two resources:

      
        their phone, with presence "available"; and
        their pc, with presence "busy";
      

      then the methods in this interface will return an array (with
      one element: "phone") as the client types because that is the more
      available resource. If at some later time the contact's phone's presence
      changes to "away", the
      ClientTypesUpdated signal will
      notify that the contact's client types attribute has changed from
      ["phone"] to ["pc"],
      because "busy" is a more available presence than "away".

    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.ClientTypes')

    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ClientTypes', in_signature='au', out_signature='a{uas}')
    def GetClientTypes(self, Contacts):
        """
        Return the client types of the given contacts, if they are
        already known. If any of the given contacts' client types are
        not known, request their current client types, but return
        immediately without waiting for a reply; if a reply with a
        non-empty client type array is later received for those
        contacts, the
        ClientTypesUpdated signal will
        be emitted for them.

        
          This method is appropriate for "lazy" client type finding, for instance
          displaying the client types (if available) of everyone in your contact
          list.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ClientTypes', in_signature='u', out_signature='as')
    def RequestClientTypes(self, Contact):
        """
        Return the current client types of the given contact. If necessary, make
        a request to the server for up-to-date information, and wait for a
        reply.

        
          This method is appropriate for use in a "Contact Information..."
          dialog; it can be used to show progress information (while waiting
          for the method to return), and can distinguish between various error
          conditions.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.ClientTypes', signature='uas')
    def ClientTypesUpdated(self, Contact, Client_Types):
        """
        Emitted when a contact's client types change or become known.
      
        """
        pass
  