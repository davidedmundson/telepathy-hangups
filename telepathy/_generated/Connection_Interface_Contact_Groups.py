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


class ConnectionInterfaceContactGroups(dbus.service.Interface):
    """\
      An interface for connections in which contacts can be placed in
        user-defined groups.

      The most basic functionality of this interface is to list and monitor
        a contact's set of groups. To do this, use the
        GroupsChanged signal, and the
        groups contact attribute (this should
        usually be done by connecting to the GroupsChanged signal, then
        calling GetContactListAttributes with this interface
        included in the Interfaces argument). Simple user interfaces can
        limit themselves to displaying that information, and ignore the rest
        of this interface: to ensure that this works,
        GroupsChanged is emitted for every
        change, even if that change could be inferred from another signal
        such as GroupsRemoved.

      Looking at contacts' lists of groups is sufficient to present a
        user interface resembling XMPP's data model, in which groups behave
        like tags applied to contacts, and so an empty group cannot exist
        or is not interesting. However, some protocols model groups as
        objects in their own right. User interfaces may either track
        the set of groups via the Groups
        property and the GroupsCreated and
        GroupsRemoved signals, or ignore
        this extra information.

      Similarly, in some protocols it is possible to rename a group as
        a single atomic operation. Simpler user interfaces will
        see the new name being created, the old name being removed, and the
        members moving to the new name, via the signals described above.
        More advanced user interfaces can optionally distinguish between an
        atomic rename and a create/remove pair, and display renamed groups
        differently, by monitoring the
        GroupRenamed signal.

      This interface also provides various methods to manipulate
        user-defined groups, which can be expected to work if
        GroupStorage is not None.

      Depending on the protocol, some methods might be implemented by
        more than one protocol operation; for instance, in a
        "contact-centric" protocol like XMPP,
        SetContactGroups is a single
        protocol operation and SetGroupMembers
        requires a protocol operation per contact, whereas in a more
        "group-centric" protocol it might be the other way around. User
        interfaces SHOULD call whichever method most closely resembles the
        way in which the user's action was represented in the UI, and
        let the connection manager deal with the details.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.ContactGroups')

    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactGroups', in_signature='uas', out_signature='')
    def SetContactGroups(self, Contact, Groups):
        """
        Add the given contact to the given groups (creating new groups
          if necessary), and remove them from all other groups.

        
          This is the easiest and most correct way to implement user
            interfaces that display a single contact with a list of groups,
            resulting in a user expectation that when they apply the changes,
            the contact's set of groups will become exactly what was
            displayed.
        

        If the user is removed from a group of which they were the only
          member, the group MAY be removed automatically.

        
          In protocols like XMPP where groups behave like tags, a group
            with no members has no protocol representation.
        

        Any GroupsCreated,
          GroupsChanged and
          GroupsRemoved signals that result from
          this method call MUST be emitted before the method returns.

        This method SHOULD NOT be called until the
          ContactListState changes to Success.
          If the ContactListState is Failure, this method SHOULD raise the
          same error as
          GetContactListAttributes.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactGroups', in_signature='sau', out_signature='')
    def SetGroupMembers(self, Group, Members):
        """
        Add the given members to the given group (creating it if necessary),
          and remove all other members.

        
          This is the easiest and most correct way to implement user
            interfaces that display a single group with a list of contacts,
            resulting in a user expectation that when they apply the changes,
            the groups's set of members will become exactly what was
            displayed.
        

        If DisjointGroups is true,
          this will also remove each member from their previous group.

        If the user is removed from a group of which they were the only
          member, the group MAY be removed automatically.

        Any GroupsCreated,
          GroupsChanged and
          GroupsRemoved signals that result from
          this method call MUST be emitted before the method returns.

        This method SHOULD NOT be called until the
          ContactListState changes to Success.
          If the ContactListState is Failure, this method SHOULD raise the
          same error as
          GetContactListAttributes.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactGroups', in_signature='sau', out_signature='')
    def AddToGroup(self, Group, Members):
        """
        Add the given members to the given group, creating it if
          necessary.

        If DisjointGroups is true,
          this will also remove each member from their previous group.

        
          This is good for user interfaces in which you can edit groups
            via drag-and-drop.
        

        Any GroupsCreated,
          GroupsChanged and
          GroupsRemoved signals that result from
          this method call MUST be emitted before the method returns.

        This method SHOULD NOT be called until the
          ContactListState changes to Success.
          If the ContactListState is Failure, this method SHOULD raise the
          same error as
          GetContactListAttributes.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactGroups', in_signature='sau', out_signature='')
    def RemoveFromGroup(self, Group, Members):
        """
        Remove the given members from the given group.

        
          This is good for user interfaces in which you can edit groups
            via drag-and-drop.
        

        Any GroupsChanged or
          GroupsRemoved signals that result from
          this method call MUST be emitted before the method returns.

        This method SHOULD NOT be called until the
          ContactListState changes to Success.
          If the ContactListState is Failure, this method SHOULD raise the
          same error as
          GetContactListAttributes.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactGroups', in_signature='s', out_signature='')
    def RemoveGroup(self, Group):
        """
        Remove all members from the given group, then remove the group
          itself. If the group already does not exist, this method SHOULD
          return successfully.

        Any GroupsChanged or
          GroupsRemoved signals that result from
          this method call MUST be emitted before the method returns.

        This method SHOULD NOT be called until the
          ContactListState changes to Success.
          If the ContactListState is Failure, this method SHOULD raise the
          same error as
          GetContactListAttributes.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.ContactGroups', in_signature='ss', out_signature='')
    def RenameGroup(self, Old_Name, New_Name):
        """
        Rename the given group.

        On protocols where groups behave like tags, this is an API
          short-cut for adding all of the group's members to a group with
          the new name, then removing the old group.

        
          Otherwise, clients can't perform this operation atomically, even
            if the connection could.
        

        Any GroupRenamed or
          GroupsRemoved signals that result from
          this method call MUST be emitted before the method returns.

        This method SHOULD NOT be called until the
          ContactListState changes to Success.
          If the ContactListState is Failure, this method SHOULD raise the
          same error as
          GetContactListAttributes.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.ContactGroups', signature='auasas')
    def GroupsChanged(self, Contact, Added, Removed):
        """
        Emitted when contacts' groups change.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.ContactGroups', signature='as')
    def GroupsCreated(self, Names):
        """
        Emitted when new, empty groups are created. This will often be
        followed by GroupsChanged signals that
        add some members.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.ContactGroups', signature='ss')
    def GroupRenamed(self, Old_Name, New_Name):
        """
        Emitted when a group is renamed, in protocols where this can
          be distinguished from group creation, removal and membership
          changes.

        Immediately after this signal is emitted,
          GroupsCreated MUST signal the
          creation of a group with the new name, and
          GroupsRemoved MUST signal the
          removal of a group with the old name.

        
          Emitting these extra signals, in this order, means that clients
            that are interested in the set of groups that exist (but treat a
            rename and a create/remove pair identically) can ignore the
            GroupRenamed signal entirely.
        

        If the group was not empty, immediately after those signals are
          emitted, GroupsChanged MUST signal
          that the members of that group were removed from the old name
          and added to the new name.

        On connection managers where groups behave like tags, renaming a
          group MAY be signalled as a set of
          GroupsCreated,
          GroupsRemoved and
          GroupsChanged signals, instead of
          emitting this signal.

        
          On protocols like XMPP, another resource "renaming a group" is
            indistinguishable from changing contacts' groups individually.
        
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.ContactGroups', signature='as')
    def GroupsRemoved(self, Names):
        """
        Emitted when one or more groups are removed. If they had members at
          the time that they were removed, then immediately after this signal
          is emitted, GroupsChanged MUST signal
          that their members were removed.

        
          Emitting the signals in this order allows for two modes of
            operation. A client interested only in a contact's set of groups
            can ignore GroupsRemoved and rely
            on the GroupsChanged signal that
            will follow; a more elaborate client wishing to distinguish between
            all of a group's members being removed, and the group itself
            being removed, can additionally watch for
            GroupsRemoved and use it to
            disambiguate.
        
      
        """
        pass
  