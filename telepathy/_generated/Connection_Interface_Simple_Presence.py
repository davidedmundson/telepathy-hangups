# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright (C) 2005-2008 Collabora Limited 
 Copyright (C) 2005, 2006 Nokia Corporation 
 Copyright (C) 2006 INdT 

    This library is free software; you can redistribute it and/or modify it
      under the terms of the GNU Lesser General Public License as published by
      the Free Software Foundation; either version 2.1 of the License, or (at
      your option) any later version.

    This library is distributed in the hope that it will be useful, but
      WITHOUT ANY WARRANTY; without even the implied warranty of
      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser
      General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
      along with this library; if not, write to the Free Software Foundation,
      Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
  
"""

import dbus.service


class ConnectionInterfaceSimplePresence(dbus.service.Interface):
    """\
      This interface is for services which have a concept of presence which
        can be published for yourself and monitored on your contacts.

      Presence on an individual (yourself or one of your contacts) is
        modelled as a status and a status message. Valid statuses are defined
        per connection, and a list of those that can be set on youself
        can be obtained from the
        Statuses
        property.

      Each status has an arbitrary string identifier which should have an
        agreed meaning between the connection manager and any client which is
        expected to make use of it. The following well-known values should be
        used where possible to allow clients to identify common choices:

      
        
          status identifier
          Connection_Presence_Type
          comments
        
        
          available
          Connection_Presence_Type_Available
          
        
        
          away
          Connection_Presence_Type_Away
          
        
        
          brb
          Connection_Presence_Type_Away
          Be Right Back (a more specific form of Away)
        
        
          busy
          Connection_Presence_Type_Busy
          
        
        dnd
          Connection_Presence_Type_Busy
          Do Not Disturb (a more specific form of Busy)
        
        
          xa
          Connection_Presence_Type_Extended_Away
          Extended Away
        
        
          hidden
          Connection_Presence_Type_Hidden
          Also known as "Invisible" or "Appear Offline"
        
        
          offline
          Connection_Presence_Type_Offline
          
        
        
          unknown
          Connection_Presence_Type_Unknown
          special, see below
        
        
          error
          Connection_Presence_Type_Error
          special, see below
        
      

      As well as these well-known status identifiers, every status also has
        a numerical type value chosen from
        Connection_Presence_Type which can be
        used by the client to classify even unknown statuses into different
        fundamental types.

      These numerical types exist so that even if a client does not
        understand the string identifier being used, and hence cannot present
        the presence to the user to set on themselves, it may display an
        approximation of the presence if it is set on a contact.

      As well as the normal status identifiers, there are two special ones
        that may be present: 'unknown' with type Unknown and 'error' with type
        Error. 'unknown' indicates that it is impossible to determine the
        presence of a contact at this time, for example because it's not on the
        'subscribe' list and the protocol only allows one to determine the
        presence of contacts you're subscribed to. 'error' indicates that there
        was a failure in determining the status of a contact.

      If the connection has a 'subscribe' contact list,
        PresencesChanged
        signals should be emitted to indicate changes of contacts on this list,
        and should also be emitted for changes in your own presence. Depending
        on the protocol, the signal may also be emitted for others such as
        people with whom you are communicating, and any user interface should
        be updated accordingly.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.SimplePresence')

    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.SimplePresence', in_signature='ss', out_signature='')
    def SetPresence(self, Status, Status_Message):
        """
        Request that the presence status and status message are published for
          the connection.  Changes will be indicated by
          PresencesChanged
          signals being emitted.

        This method may be called on a newly-created connection while it
          is still in the DISCONNECTED state, to request that when the
          connection connects, it will do so with the selected status.

        In DISCONNECTED state the
          Statuses
          property will indicate which statuses are allowed to be set
          while DISCONNECTED (none, if the Connection Manager doesn't allow
          this). This value MUST NOT be cached, as the set of allowed
          presences might change upon connecting.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.SimplePresence', in_signature='au', out_signature='a{u(uss)}')
    def GetPresences(self, Contacts):
        """
        Get presence previously emitted by
        PresencesChanged for the given
        contacts. Data is returned in the same structure as the
        PresencesChanged signal; no additional network requests are made.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.SimplePresence', signature='a{u(uss)}')
    def PresencesChanged(self, Presence):
        """
        This signal should be emitted when your own presence has been changed,
        or the presence of the member of any of the connection's channels has
        been changed.
      
        """
        pass
  