# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright (C) 2005-2009 Collabora Limited
Copyright (C) 2005-2009 Nokia Corporation
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
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
USA.
  
"""

import dbus.service


class Connection(dbus.service.Object):
    """\
      This models a connection to a single user account on a communication
        service. Its basic capability is to provide the facility to request and
        receive channels of differing types (such as text channels or streaming
        media channels) which are used to carry out further communication.

      In order to allow Connection objects to be discovered by new clients,
        the object path and well-known bus name MUST be of the form
        /org/freedesktop/Telepathy/Connection/cmname/proto/account
        and
        org.freedesktop.Telepathy.Connection.cmname.proto.account
        where:

      
        cmname is the same
          Connection_Manager_Name that appears
          in the connection manager's object path and well-known bus name
        proto is the Protocol name as seen in
          ListProtocols,
          but with "-" replaced with "_" to get a valid
          object path/bus name
        account is some non-empty sequence of ASCII letters,
          digits and underscores not starting with a digit
      

      account SHOULD be formed such that any valid distinct
        connection instance on this protocol has a distinct name. This
        might be formed by including the server name followed by the user
        name (escaped via some suitable mechanism like telepathy-glib's
        tp_escape_as_identifier() function to preserve uniqueness); on
        protocols where connecting multiple times is permissable, a
        per-connection identifier might be necessary to ensure
        uniqueness.

      Clients MAY parse the object path to determine the connection
        manager name and the protocol, but MUST NOT attempt to parse the
        account part. Connection managers MAY use any unique string
        for this part.

    As well as the methods and signatures below, arbitrary interfaces may be
    provided by the Connection object to represent extra connection-wide
    functionality, such as the Connection.Interface.SimplePresence for
    receiving and
    reporting presence information, and Connection.Interface.Aliasing for
    connections where contacts may set and change an alias for themselves.
    These interfaces can be discovered using the
    GetInterfaces method.

    Contacts, rooms, and server-stored lists (such as subscribed contacts,
    block lists, or allow lists) on a service are all represented by
    immutable handles, which are unsigned non-zero integers which are
    valid only for the lifetime of the connection object, and are used
    throughout the protocol where these entities are represented, allowing
    simple testing of equality within clients.

    Zero as a handle value is sometimes used as a "null" value to mean
    the absence of a contact, room, etc.

    Handles have per-type uniqueness, meaning that
    every (handle type, handle number) tuple is guaranteed to be unique within
    a connection and that a handle alone (without its type) is meaningless or
    ambiguous. Connection manager implementations should reference count these
    handles to determine if they are in use either by any active clients or any
    open channels, and may deallocate them when this ceases to be true. Clients
    may request handles of a given type and identifier with the
    RequestHandles method, inspect the entity
    identifier with the InspectHandles
    method, keep handles from being released with
    HoldHandles, and notify that they are no
    longer storing handles with
    ReleaseHandles.
    """

    @dbus.service.method('org.freedesktop.Telepathy.Connection', in_signature='', out_signature='')
    def Connect(self):
        """
        Request that the connection be established. This will be done
          asynchronously and errors will be returned by emitting
          StatusChanged signals.

        Calling this method on a Connection that is already connecting
          or connected is allowed, and has no effect.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection', in_signature='', out_signature='')
    def Disconnect(self):
        """
        Request that the connection be closed. This closes the connection if
        it's not already in DISCONNECTED state, and destroys the connection
        object.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection', in_signature='', out_signature='as')
    def GetInterfaces(self):
        """
        Returns the set of optional interfaces supported by this
          connection. See Interfaces for more
          details.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection', in_signature='', out_signature='s')
    def GetProtocol(self):
        """
        Get the protocol this connection is using.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection', in_signature='', out_signature='u')
    def GetSelfHandle(self):
        """
        Returns the value of the SelfHandle property. Change notification
        is via the SelfHandleChanged signal.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection', in_signature='', out_signature='u')
    def GetStatus(self):
        """
        Get the current status as defined in the
        StatusChanged signal.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection', in_signature='uau', out_signature='')
    def HoldHandles(self, Handle_Type, Handles):
        """
        If HasImmortalHandles is true,
          which SHOULD always be the case in this version of telepathy-spec,
          this method does nothing and returns successfully, unless
          the given handle type or any of the given handles is invalid.

        In older connection managers, this method
        notifies the connection manger that your client is holding a copy
        of handles which may not be in use in any existing channel or
        list, and were not obtained by using the
        RequestHandles method. For
        example, a handle observed in an emitted signal, or displayed
        somewhere in the UI that is not associated with a channel. The
        connection manager must not deallocate a handle where any clients
        have used this method to indicate it is in use until the
        ReleaseHandles
        method is called, or the clients disappear from the bus.

        Note that HoldHandles is idempotent - calling it multiple times
          is equivalent to calling it once. If a handle is "referenced" by
          several components which share a D-Bus unique name, the client
          should perform reference counting internally, and only call
          ReleaseHandles when none of the cooperating components need the
          handle any longer.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection', in_signature='uau', out_signature='as')
    def InspectHandles(self, Handle_Type, Handles):
        """
        Return a string representation for a number of handles of a given
        type.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection', in_signature='', out_signature='a(osuu)')
    def ListChannels(self):
        """
        List all the channels which currently exist on this connection.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection', in_signature='uau', out_signature='')
    def ReleaseHandles(self, Handle_Type, Handles):
        """
        If HasImmortalHandles is true,
          which SHOULD always be the case in this version of telepathy-spec,
          this method does nothing and returns successfully, unless
          the given handle type or any of the given handles is invalid.

        In older connection managers, this method
        explicitly notifies the connection manager that your client is no
        longer holding any references to the given handles, and that they
        may be deallocated if they are not held by any other clients or
        referenced by any existing channels. See
        HoldHandles for notes.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection', in_signature='suub', out_signature='o')
    def RequestChannel(self, Type, Handle_Type, Handle, Suppress_Handler):
        """
        Request a channel satisfying the specified type and communicating
          with the contact, room, list etc. indicated by the given
          handle_type and handle. The handle_type and handle may both be
          zero to request the creation of a new, empty channel, which may
          or may not be possible, depending on the protocol and channel
          type.

        On success, the returned channel will always be of the requested
          type (i.e. implement the requested channel-type interface).

        If a new, empty channel is requested, on success the returned
          channel will always be an "anonymous" channel for which the type
          and handle are both zero.

        If a channel to a contact, room etc. is requested, on success, the
          returned channel may either be a new or existing channel to
          the requested entity (i.e. its
          TargetHandleType
          and TargetHandle
          properties are the
          requested handle type and handle), or a newly created "anonymous"
          channel associated with the requested handle in some
          implementation-specific way.

        For example, for a contact handle, the returned channel
          might be "anonymous", but implement the groups interface and have
          the requested contact already present among the members.

        If the request cannot be satisfied, an error is raised and no
          channel is created.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection', in_signature='uas', out_signature='au')
    def RequestHandles(self, Handle_Type, Identifiers):
        """
        Request several handles from the connection manager which represent a
          number of contacts, rooms or server-stored lists on the service.

        If HasImmortalHandles is true,
          which SHOULD always be the case in this version of telepathy-spec,
          the handles remain valid until the connection disconnects.

        The implementation of this method in older connection managers
        must record that these handles are in use by the
        client who invokes this method, and must not deallocate the handles
        until the client disconnects from the bus or calls the
        ReleaseHandles
        method. Where the identifier refers to an entity that already has a
        handle in this connection manager, this handle should be returned
        instead. The handle number 0 must not be returned by the connection
        manager.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection', in_signature='as', out_signature='')
    def AddClientInterest(self, Tokens):
        """
        Register a client's interest in notifications related to one or
          more interfaces.

        Groups of notifications are identified by a token which is either
          a D-Bus interface name, or a string that starts with a D-Bus
          interface name. The meaning of each token is given by that D-Bus
          interface, which MUST define it in its documentation.

        
          Initially, all interests are in entire interface, but allowing
            other strings allows subscription to part of an interface; for
            instance, an interest in ...MailNotification/count could track
            the number of messages without caring about their detailed
            content.
        

        For each token with which this method interacts, the
          Connection tracks an "interest count" (like a reference count) for
          each unique bus name that has called this method. When a client
          calls this method, for each token, the interest count for its
          unique bus name is incremented; when
          RemoveClientInterest is called,
          all interest counts for that unique bus name are decremented.
          If the unique bus name leaves the bus (for instance, if the
          client crashes or exits), all interest counts for that unique bus
          name are set to zero.

        The Connection can then use these reference counts to
          avoid subscribing to protocol-level notifications unless at least
          one client has a non-zero interest count for the relevant
          token.

        
          This method exists to reduce memory and network overhead when
            there is no active subscription.

          One situation where this is useful is Location: on XMPP, location updates are received
            over PEP. If the Connection advertises the
            geoloc+notify capability, it will be sent location
            updates for all contacts. To avoid consuming resources for this,
            the connection should avoid advertising that capability until
            a client has expressed an interest in contacts' locations.

          Another example of a protocol that benefits from this method is
            the Google XMPP Mail Notification extension, which can be used
            to implement MailNotification. In this protocol, the CM
            receives a notification that something has changed, but to get
            more information, the CM must request this information. Knowing
            that nobody is currently interested in this information, the CM
            can avoid generating useless network traffic. Similarly, the CM
            may free the list of unread messages to reduce memory overhead.
        

        If this method is called for an interface that might require
          protocol-level subscription, but the connection cannot set up
          that subscription yet (for instance because the
          Status is not Connected yet), the
          Connection MUST remember the client's interest, and attempt to
          subscribe to the appropriate protocol feature when this becomes
          possible.

        Clients MAY ignore any errors raised by this method; it is intended
          to be called with the reply ignored.

        
          The only reason it could fail is if it's unimplemented, in which
            case the only thing the client can usefully do is to proceed as if
            it had succeeded.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection', in_signature='as', out_signature='')
    def RemoveClientInterest(self, Tokens):
        """
        Release an interest registered using
          AddClientInterest. See that
          method's documentation for details.

        Clients MAY ignore any errors raised by this method; it is intended
          to be called with the reply ignored.

        
          The only reasons it could fail are if it's unimplemented, or if
            the client's reference-counting is wrong and it has tried to
            remove a client interest that it did not add. In both cases,
            there's nothing the client could do about it.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection', signature='u')
    def SelfHandleChanged(self, Self_Handle):
        """
        Emitted whenever the SelfHandle property
        changes. If the connection
        is not yet in the CONNECTED state, this signal is not guaranteed
        to be emitted.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection', signature='osuub')
    def NewChannel(self, Object_Path, Channel_Type, Handle_Type, Handle, Suppress_Handler):
        """
        Emitted when a new Channel object is created, either through user
        request or incoming information from the service.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection', signature='sa{sv}')
    def ConnectionError(self, Error, Details):
        """
        Emitted when an error occurs that renders this connection unusable.
        

        Whenever this signal is emitted, it MUST immediately be followed by
          a StatusChanged signal with status
          Connection_Status_Disconnected and an appropriate reason
          code.

        Connection managers SHOULD emit this signal on disconnection, but
          need not do so. Clients MUST support connection managers that emit
          StatusChanged(Disconnected, ...) without first emitting
          ConnectionError.

        
          This signal provides additional information about the reason
            for disconnection. The reason for connection is always
            straightforward - it was requested - so it does not need further
            explanation. However, on errors, it can be useful to provide
            additional information.

          The Connection_Status_Reason is not given
            here, since it will be signalled in
            StatusChanged. A reasonable client
            implementation would be to store the information given by this
            signal until StatusChanged is received, at which point the
            information given by this signal can be used to supplement the
            StatusChanged signal.
        
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection', signature='uu')
    def StatusChanged(self, Status, Reason):
        """
        Emitted when the status of the connection changes.  All states and
        reasons have numerical values, as defined in ConnectionStatus
        and ConnectionStatusReason.
      
        """
        pass
  