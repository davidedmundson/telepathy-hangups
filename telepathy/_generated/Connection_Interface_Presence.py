# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""
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
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
  
"""

import dbus.service


class ConnectionInterfacePresence(dbus.service.Interface):
    """\

      This interface is for services which have a concept of presence which
        can be published for yourself and monitored on your contacts.
        Telepathy's definition of presence is based on that used by
        the Galago project.

    Presence on an individual (yourself or one of your contacts) is modelled as
    a last activity time along with a set of zero or more statuses, each of
    which may have arbitrary key/value parameters. Valid statuses are defined
    per connection, and a list of them can be obtained with the
    GetStatuses method.

    (The SimplePresence interface which replaces this one restricts
      presences to one status per contact, with an optional message, which is
      in practice all that was implemented on this interface.)

    Each status has an arbitrary string identifier which should have an agreed
    meaning between the connection manager and any client which is expected to
    make use of it. The well-known values defined by the SimplePresence
      interface SHOULD be used where possible

    As well as these well-known status identifiers, every status also has a
    numerical type value chosen from
    Connection_Presence_Type which can be used by the client
    to classify even unknown statuses into different fundamental types.

    These numerical types exist so that even if a client does not understand
    the string identifier being used, and hence cannot present the presence to
    the user to set on themselves, it may display an approximation of the
    presence if it is set on a contact.

    The dictionary of variant types allows the connection manager to exchange
    further protocol-specific information with the client. It is recommended
    that the string (s) argument 'message' be interpreted as an optional
    message which can be associated with a presence status.

    If the connection has a 'subscribe' contact list,
    PresenceUpdate signals should be emitted to
    indicate changes of contacts on this list, and should also be emitted for
    changes in your own presence. Depending on the protocol, the signal may
    also be emitted for others such as people with whom you are communicating,
    and any user interface should be updated accordingly.

    On some protocols, RequestPresence may
    only succeed on contacts on your 'subscribe' list, and other contacts will
    cause a PermissionDenied error.  On protocols where there is no 'subscribe'
    list, and RequestPresence succeeds, a client may poll the server
    intermittently to update any display of presence information.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.Presence')

    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Presence', in_signature='sa{sv}', out_signature='')
    def AddStatus(self, Status, Parameters):
        """
        Request that a single presence status is published for the user, along
        with any desired parameters. Changes will be indicated by
        PresenceUpdate signals being emitted.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Presence', in_signature='', out_signature='')
    def ClearStatus(self):
        """
        Request that all of a user's presence statuses be removed. Be aware
        that this request may simply result in the statuses being replaced by a
        default available status. Changes will be indicated by
        PresenceUpdate signals being emitted.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Presence', in_signature='au', out_signature='a{u(ua{sa{sv}})}')
    def GetPresence(self, Contacts):
        """
        Get presence previously emitted by
        PresenceUpdate for the given contacts.
        Data is returned in the same structure as the PresenceUpdate signal.
        Using this method in favour of
        RequestPresence has the advantage that
        it will not wake up each client connected to the PresenceUpdate signal.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Presence', in_signature='', out_signature='a{s(ubba{ss})}')
    def GetStatuses(self):
        """
        Get a dictionary of the valid presence statuses for this connection.
        This is only available when online because only some statuses will
        be available on some servers.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Presence', in_signature='s', out_signature='')
    def RemoveStatus(self, Status):
        """
        Request that the given presence status is no longer published for the
        user. Changes will be indicated by
        PresenceUpdate signals being emitted. As
        with ClearStatus, removing a status may
        actually result in it being replaced by a default available status.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Presence', in_signature='au', out_signature='')
    def RequestPresence(self, Contacts):
        """
        Request the presence for contacts on this connection. A PresenceUpdate
        signal will be emitted when they are received. This is not the same as
        subscribing to the presence of a contact, which must be done using the
        'subscription' ContactList,
        and on some protocols presence information may not be available unless
        a subscription exists.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Presence', in_signature='u', out_signature='')
    def SetLastActivityTime(self, Time):
        """
        Request that the recorded last activity time for the user be updated on
        the server.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Presence', in_signature='a{sa{sv}}', out_signature='')
    def SetStatus(self, Statuses):
        """
        Request that the user's presence be changed to the given statuses
          and desired parameters. Changes will be reflected by
          PresenceUpdate
          signals being emitted.

        Statuses whose Connection_Presence_Type
          is Offline, Error or Unknown MUST NOT be passed to this
          function. Connection managers SHOULD reject these statuses.

        
          The same rationale as for SimplePresence.SetPresence
            applies.
        

        On certain protocols, this method may be
          called on a newly-created connection which is still in the
          DISCONNECTED state, and will sign on with the requested status.
          If the requested status is not available after signing on,
          NotAvailable will be returned and the connection will remain
          offline, or if the protocol does not support signing on with
          a certain status, Disconnected will be returned.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.Presence', signature='a{u(ua{sa{sv}})}')
    def PresenceUpdate(self, Presence):
        """
        This signal should be emitted when your own presence has been changed,
        or the presence of the member of any of the connection's channels has
        been changed, or when the presence requested by
        RequestPresence is available.
      
        """
        pass
  