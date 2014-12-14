# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2009-2010 Collabora Ltd.
Copyright © 2009 Nokia Corporation

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


class ConnectionInterfaceContactList(dbus.service.Interface):
    """\
      An interface for connections that have any concept of a list of
        known contacts (roster, buddy list, friends list etc.)

      
        On many protocols, there's a server-side roster (as in XMPP),
          or a set of server-side lists that can be combined to form a
          roster (as in MSN).

        In some protocols (like link-local XMPP), while there might not be
          any server or roster, it's possible to list "nearby" contacts.

        In Telepathy 0.20 and older, we represented contact lists as a
          collection of ContactList channels. This is remarkably difficult to
          work with in practice - every client that cares about contact lists
          has to take the union of some hard-to-define set of these
          channels - and conflicts with the idea that channels that cannot
          be dispatched to a handler should be closed.
      

      The list of contacts is not exposed as a D-Bus property; it can be
        fetched using GetContactListAttributes.
      

      
        In some protocols, such as XMPP, the contact list may not be
          available immediately. The
          GetContactListAttributes method
          will fail until the contact list is available.
          Using a method also allows extra attributes to be retrieved at
          the same time.
      
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.ContactList')

    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactList', in_signature='asb', out_signature='a{ua{sv}}')
    def GetContactListAttributes(self, Interfaces, Hold):
        """
        Return some contact attributes for a list of contacts
          associated with the user. This list MUST include at least:

        
          all contacts whose subscribe
            attribute is not No
          all contacts whose publish
            attribute is not No
        

        but MAY contain other contacts.

        
          For instance, on XMPP, all contacts on the roster would appear
            here even if they have subscription="none", unless there's
            reason to believe the user does not want to see them (such as
            having been blocked).
        

        This list does not need to contain every visible contact: for
          instance, contacts seen in XMPP or IRC chatrooms SHOULD NOT appear
          here. Blocked contacts SHOULD NOT appear here, unless they still
          have a non-No subscribe or
          publish attribute
          for some reason.

        
          It's reasonable to assume that blocked contacts should not be
            visible to the user unless they specifically go looking for them,
            at least in protocols like XMPP where blocking a contact
            suppresses presence.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactList', in_signature='aus', out_signature='')
    def RequestSubscription(self, Contacts, Message):
        """
        Request that the given contacts allow the local user to
          subscribe to their presence, i.e. that their subscribe attribute
          becomes Yes.

        Connection managers SHOULD NOT attempt to enforce a
          mutual-subscription policy (i.e. when this method is called, they
          should not automatically allow the contacts to see the local user's
          presence). User interfaces that require mutual subscription
          MAY call AuthorizePublication
          at the same time as this method.

        
          Whether to enforce mutual subscription is a matter of policy,
            so it is left to the user interface and/or the server.
        

        Before calling this method on a connection where GetAliasFlags returns the User_Set flag,
          user interfaces SHOULD obtain, from the user, an alias to
          identify the contact in future, and store it using SetAliases.

        The user MAY be
          prompted using the contact's current self-assigned nickname, or
          something derived from the contact's (presumably self-assigned)
          identifier, as a default, but these names chosen by the contact
          SHOULD NOT be used without user approval.

        
          This is a generalization of
            XEP-0165 "Best Practices to Discourage JID Mimicking")
            to protocols other than XMPP. A reasonable user interface for
            this, as used in many XMPP clients, is to have a text entry
            for the alias adjacent to the text entry for the identifier
            to add.
        

        For contacts with subscribe=Yes, this method has no effect.
          It MUST return successfully if all contacts are in this state.

        For contacts with subscribe=Ask, this method SHOULD send a new
          request, with the given message, if allowed by the underlying
          protocol.

        For contacts with subscribe=No or subscribe=Rejected, this method
          SHOULD request that the contact allows the local user to subscribe
          to their presence; in general, this will change their publish
          attribute to Ask (although it could change directly to Yes in some
          situations).

        Any state changes that immediately result from this request MUST
          be signalled via ContactsChanged
          before this method returns.

        
          This makes it easy for user interfaces to see what practical
            effect this method had.
        

        If the remote contact accepts the request, their subscribe
          attribute will later change from Ask to Yes.

        If the remote contact explicitly rejects the request (in protocols
          that allow this), their subscribe attribute will later change from
          Ask to Rejected.

        If the subscription request is cancelled by the local user, the
          contact's subscribe attribute will change from Ask to No.

        This method SHOULD NOT be called until the
          ContactListState changes to Success.
          If the ContactListState changes to
          Failure, this method SHOULD raise the same error as
          GetContactListAttributes.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactList', in_signature='au', out_signature='')
    def AuthorizePublication(self, Contacts):
        """
        For each of the given contacts, request that the local user's
          presence is sent to that contact, i.e. that their publish attribute
          becomes Yes.

        Connection managers SHOULD NOT attempt to enforce a
          mutual-subscription policy (i.e. when this method is called, they
          should not automatically request that the contacts allow the user to
          subscribe to their presence). User interfaces that require mutual
          subscription MAY call
          RequestSubscription at the same time
          as this method.

        
          Whether to enforce mutual subscription is a matter of policy,
            so it is left to the user interface and/or the server.
        

        For contacts with publish=Yes, this method has no effect; it
          MUST return successfully if all contacts given have this state.

        For contacts with publish=Ask, this method accepts the
          contact's request to see the local user's presence, changing
          their publish attribute from Ask to Yes.

        For contacts with publish=No, if the protocol allows it, this
          method allows the contacts to see the local user's presence even
          though they have not requested it, changing their publish attribute
          from No to Yes. Otherwise, it merely records the fact that
          presence publication to those contacts is allowed; if any of
          those contacts ask to receive the local user's presence
          later in the lifetime of the connection, the connection SHOULD
          immediately allow them to do so, changing their publish
          attribute directly from No to Yes.

        
          This makes it easy to implement the common UI policy that if
            the user attempts to subscribe to a contact's presence, requests
            for reciprocal subscription are automatically approved.
        

        Any state changes that immediately result from this request MUST
          be signalled via ContactsChanged
          before this method returns.

        
          This makes it easy for user interfaces to see what practical
            effect this method had.
        

        This method SHOULD NOT be called until the
          ContactListState changes to Success.
          If the ContactListState changes to
          Failure, this method SHOULD raise the same error as
          GetContactListAttributes.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactList', in_signature='au', out_signature='')
    def RemoveContacts(self, Contacts):
        """
        Remove the given contacts from the contact list entirely. It is
          protocol-dependent whether this works, and under which
          circumstances.

        If possible, this method SHOULD set the contacts' subscribe and
          publish attributes to No, remove any stored aliases for those
          contacts, and remove the contacts from the result of
          GetContactListAttributes.

        This method SHOULD succeed even if it was not possible to carry out
          the request entirely or for all contacts (for instance, if there is an
          outstanding request to subscribe to the contact's presence, and it's
          not possible to cancel such requests). However, all signals that
          immediately result from this method call MUST be emitted before it
          returns, so that clients can interpret the result.

        
          User interfaces removing a contact from the contact list are
            unlikely to want spurious failure notifications resulting from
            limitations of a particular protocol. However, emitting the
            signals first means that if a client does want to check exactly
            what happened, it can wait for the method to return (while
            applying change-notification signals to its local cache of the
            contact list's state), then consult its local cache of the
            contact list's state to see whether the contact is still there.
        

        This method SHOULD NOT be called until the
          ContactListState changes to Success.
          If the ContactListState changes to
          Failure, this method SHOULD raise the same error as
          GetContactListAttributes.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactList', in_signature='au', out_signature='')
    def Unsubscribe(self, Contacts):
        """
        Attempt to set the given contacts' subscribe attribute to No,
          i.e. stop receiving their presence.

        For contacts with subscribe=Ask, this attempts to cancel
          an earlier request to subscribe to the contact's presence; for
          contacts with subscribe=Yes, this attempts to
          unsubscribe from the contact's presence.

        As with RemoveContacts, this method
          SHOULD succeed even if it was not possible to carry out the request
          entirely or for all contacts; however, all signals that
          immediately result from this method call MUST be emitted before it
          returns.

        This method SHOULD NOT be called until the
          ContactListState changes to Success.
          If the ContactListState changes to
          Failure, this method SHOULD raise the same error as
          GetContactListAttributes.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactList', in_signature='au', out_signature='')
    def Unpublish(self, Contacts):
        """
        Attempt to set the given contacts' publish attribute to No,
          i.e. stop sending presence to them.

        For contacts with publish=Ask, this method explicitly rejects the
          contact's request to subscribe to the user's presence; for
          contacts with publish=Yes, this method attempts to prevent the
          user's presence from being received by the contact.

        As with RemoveContacts, this method
          SHOULD succeed even if it was not possible to carry out the request
          entirely or for all contacts; however, all signals that
          immediately result from this method call MUST be emitted before it
          returns.

        This method SHOULD NOT be called until the
          ContactListState changes to Success.
          If the ContactListState changes to
          Failure, this method SHOULD raise the same error as
          GetContactListAttributes.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.ContactList', signature='u')
    def ContactListStateChanged(self, Contact_List_State):
        """
        Emitted when ContactListState
        changes.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.ContactList', signature='a{u(uus)}au')
    def ContactsChanged(self, Changes, Removals):
        """
        Emitted when the contact list becomes available, when contacts'
          basic stored properties change, when new contacts are added to the
          list that would be returned by
          GetContactListAttributes,
          or when contacts are removed from that list.

        
          This provides change notification for that list, and for
            contacts' subscribe,
            publish and
            publish-request attributes.
        

        Connection managers SHOULD also emit this signal when a contact
          requests that the user's presence is published to them, even if
          that contact's publish attribute is already
          Ask and the publish-request has not changed.

        
          If the same contact sends 10 identical requests, 10 identical
            signals should be emitted.
        
      
        """
        pass
  