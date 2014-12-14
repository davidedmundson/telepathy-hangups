# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2005-2009 Collabora Limited
Copyright © 2005-2009 Nokia Corporation
Copyright © 2006 INdT

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


class ChannelInterfaceGroup(dbus.service.Interface):
    """\
      Interface for channels which have multiple members, and where the members
    of the channel can change during its lifetime. Your presence in the channel
    cannot be presumed by the channel's existence (for example, a channel you
    may request membership of but your request may not be granted).

  This interface implements three lists: a list of current members
    (Members), and two lists of local pending
    and remote pending members
    (LocalPendingMembers and
    RemotePendingMembers, respectively).
    Contacts on the remote
    pending list have been invited to the channel, but the remote user has not
    accepted the invitation. Contacts on the local pending list have requested
    membership of the channel, but the local user of the framework must accept
    their request before they may join. A single contact should never appear on
    more than one of the three lists. The lists are empty when the channel is
    created, and the MembersChanged signal
    (and, if the channel's GroupFlags contains
    Members_Changed_Detailed, the
    MembersChangedDetailed signal)
    should be emitted when information
    is retrieved from the server, or changes occur.

  If the MembersChanged or
    MembersChangedDetailed signal indicates
    that the SelfHandle has been removed from
    the channel, and the channel subsequently emits Closed,
    clients SHOULD consider the details given in the MembersChanged or
    MembersChangedDetailed signal to be the reason why the channel closed.

  Addition of members to the channel may be requested by using
    AddMembers. If
    remote acknowledgement is required, use of the AddMembers method will cause
    users to appear on the remote pending list. If no acknowledgement is
    required, AddMembers will add contacts to the member list directly.  If a
    contact is awaiting authorisation on the local pending list, AddMembers
    will grant their membership request.

  Removal of contacts from the channel may be requested by using
    RemoveMembers.  If a contact is awaiting
    authorisation on the local pending
    list, RemoveMembers will refuse their membership request. If a contact is
    on the remote pending list but has not yet accepted the invitation,
    RemoveMembers will rescind the request if possible.

  It should not be presumed that the requester of a channel implementing this
    interface is immediately granted membership, or indeed that they are a
    member at all, unless they appear in the list. They may, for instance,
    be placed into the remote pending list until a connection has been
    established or the request acknowledged remotely.

  If the local user joins a Group channel whose members or other state
    cannot be discovered until the user joins (e.g. many chat room
    implementations), the connection manager should ensure that the channel
    is, as far as possible, in a consistent state before adding the local
    contact to the members set; until this happens, the local contact should
    be in the remote-pending set. For instance, if the connection manager
    queries the server to find out the initial members list for the
    channel, it should leave the local contact in the remote-pending set
    until it has finished receiving the initial members list.
  

  If the protocol provides no reliable way to tell whether the complete
    initial members list has been received yet, the connection manager
    should make a best-effort attempt to wait for the full list
    (in the worst case, waiting for a suitable arbitrary timeout)
    rather than requiring user interfaces to do so on its behalf.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Channel.Interface.Group')

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Group', in_signature='aus', out_signature='')
    def AddMembers(self, Contacts, Message):
        """
        Invite all the given contacts into the channel, or accept requests for
          channel membership for contacts on the pending local list.

        A message may be provided along with the request, which will be sent
        to the server if supported. See the CHANNEL_GROUP_FLAG_MESSAGE_ADD and
        CHANNEL_GROUP_FLAG_MESSAGE_ACCEPT
        GroupFlags to see in which cases this
        message should be provided.

        Attempting to add contacts who are already members is allowed;
          connection managers must silently accept this, without error.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Group', in_signature='', out_signature='auauau')
    def GetAllMembers(self):
        """
        Returns arrays of all current, local and remote pending channel
        members.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Group', in_signature='', out_signature='u')
    def GetGroupFlags(self):
        """
        Returns the value of the GroupFlags property.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Group', in_signature='au', out_signature='au')
    def GetHandleOwners(self, Handles):
        """
        If the CHANNEL_GROUP_FLAG_CHANNEL_SPECIFIC_HANDLES flag is set on
        the channel, then the handles of the group members are specific
        to this channel, and are not meaningful in a connection-wide
        context such as contact lists. This method allows you to find
        the owner of the handle if it can be discovered in this channel,
        or 0 if the owner is not available.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Group', in_signature='', out_signature='au')
    def GetLocalPendingMembers(self):
        """
        Returns the To_Be_Added handle (only) for each structure in the
        LocalPendingMembers property.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Group', in_signature='', out_signature='a(uuus)')
    def GetLocalPendingMembersWithInfo(self):
        """
        Returns the LocalPendingMembers property.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Group', in_signature='', out_signature='au')
    def GetMembers(self):
        """
        Returns the Members property.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Group', in_signature='', out_signature='au')
    def GetRemotePendingMembers(self):
        """
        Returns an array of handles representing contacts who have been
        invited to the channel and are awaiting remote approval.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Group', in_signature='', out_signature='u')
    def GetSelfHandle(self):
        """
        Returns the value of the SelfHandle
        property.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Group', in_signature='aus', out_signature='')
    def RemoveMembers(self, Contacts, Message):
        """
        Requests the removal of contacts from a channel, reject their
          request for channel membership on the pending local list, or
          rescind their invitation on the pending remote list.

        If the SelfHandle is in a Group,
          it can be removed via this method, in order to leave the group
          gracefully. This is the recommended way to leave a chatroom, close
          or reject a StreamedMedia
          call, and so on.

        Accordingly, connection managers SHOULD support
          doing this, regardless of the value of
          GroupFlags.
          If doing so fails with PermissionDenied, this is considered to a bug
          in the connection manager, but clients MUST recover by falling back
          to closing the channel with the Close
          method.

        Removing any contact from the local pending list is always
          allowed. Removing contacts other than the
          SelfHandle from the channel's members
          is allowed if and only if Channel_Group_Flag_Can_Remove is in the
          GroupFlags,
          while removing contacts other than the
          SelfHandle from the remote pending list
          is allowed if and only if Channel_Group_Flag_Can_Rescind is in the
          GroupFlags.

        A message may be provided along with the request, which will be
          sent to the server if supported. See the
          Channel_Group_Flag_Message_Remove,
          Channel_Group_Flag_Message_Depart,
          Channel_Group_Flag_Message_Reject and
          Channel_Group_Flag_Message_Rescind
          GroupFlags to see in which cases this
          message should be provided.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.Group', in_signature='ausu', out_signature='')
    def RemoveMembersWithReason(self, Contacts, Message, Reason):
        """
        As RemoveMembers, but a reason code may
        be provided where
        appropriate. The reason code may be ignored if the underlying
        protocol is unable to represent the given reason.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.Group', signature='a{uu}au')
    def HandleOwnersChanged(self, Added, Removed):
        """
        Emitted whenever the HandleOwners
        property changes.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.Group', signature='u')
    def SelfHandleChanged(self, Self_Handle):
        """
        Emitted whenever the SelfHandle property
        changes.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.Group', signature='uu')
    def GroupFlagsChanged(self, Added, Removed):
        """
        Emitted when the flags as returned by
        GetGroupFlags are changed.
        The user interface should be updated as appropriate.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.Group', signature='sauauauauuu')
    def MembersChanged(self, Message, Added, Removed, Local_Pending, Remote_Pending, Actor, Reason):
        """
        Emitted when contacts join any of the three lists (members, local
          pending or remote pending) or when they leave any of the three lists.
          There may also be a message from the server regarding this change,
          which may be displayed to the user if desired.

        All channel-specific handles that are mentioned in this signal
          MUST be represented in the value of the
          HandleOwners property.
          In practice, this will mean that
          HandleOwnersChanged is
          emitted before emitting a MembersChanged signal in which
          channel-specific handles are added, but that it is emitted
          after emitting a MembersChanged signal in which
          channel-specific handles are removed.

        See StreamedMedia
          for an overview of how group state changes are used to indicate the
          progress of a call.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.Group', signature='auauauaua{sv}')
    def MembersChangedDetailed(self, Added, Removed, Local_Pending, Remote_Pending, Details):
        """
        Emitted when contacts join any of the three lists (members, local
          pending or remote pending) or when they leave any of the three
          lists. This signal provides a superset of the information provided by
          MembersChanged;
          if the channel's GroupFlags
          contains Members_Changed_Detailed, then clients may listen exclusively
          to this signal in preference to that signal.

        All channel-specific handles that are mentioned in this signal
          MUST be represented in the value of the
          HandleOwners property.  In practice,
          this will mean that
          HandleOwnersChanged is emitted
          before emitting a MembersChangedDetailed signal in which
          channel-specific handles are added, but that it is emitted
          after emitting a MembersChangedDetailed signal in which
          channel-specific handles are removed.

        See StreamedMedia
          for an overview of how group state changes are used to indicate the
          progress of a call.
      
        """
        pass
  