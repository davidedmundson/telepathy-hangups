# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2009 Collabora Limited
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
      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
      02110-1301, USA.
  
"""

import dbus.service


class ChannelInterfaceConference(dbus.service.Interface):
    """\
      An interface for multi-user conference channels that can "continue
        from" one or more individual channels. This could be used to invite
        other contacts to an existing 1-1 text conversation, combine two phone
        calls into one conference call, and so on, with roughly the same API in
        each case.

      
        This interface addresses freedesktop.org bug
            #24906 (GSM-compatible conference calls) and bug
            #24939 (upgrading calls and chats to multi-user).
          See those bugs for more rationale and use cases.
      

      Existing channels are upgraded by requesting a new channel of the same
        ChannelType,
        listing the channels to be merged into the new conference in the
        InitialChannels property of the request.
        If InitialInviteeHandles and
        InitialInviteeIDs are
        Allowed_Properties in RequestableChannelClasses,
        ad-hoc conferences to a set of contacts may be created by requesting a
        channel, specifying
        InitialInviteeHandles and/or
        InitialInviteeIDs to be the contacts in
        question. A request may specify these alongside
        InitialChannels, to simultaneously
        upgrade a channel to a conference and invite others to join it.

      Channels with this interface MAY also implement MergeableConference.DRAFT
        to support merging more 1-1 channels into an ongoing conference.
        Similarly, 1-1 channels MAY implement Splittable.DRAFT to
        support being broken out of a Conference channel.

      The Group interface on Conference channels MAY use
          channel-specific handles for participants; clients SHOULD support
          both Conferences that have channel-specific handles, and those that
          do not.

      
        In the GSM case, the Conference's Group interface MAY have
          channel-specific handles, to represent the fact that the same
          phone number may be in a conference twice (for instance, it could be
          the number of a corporate switchboard).

        In the XMPP case, the Conference's Group interface SHOULD have
          channel-specific handles, to reflect the fact that the participants
          have MUC-specific identities, and the user might also be able to see
          their global identities, or not.

        In most other cases, including MSN and link-local XMPP, the
          Conference's Group interface SHOULD NOT have channel-specific
          handles, since users' identities are always visible.
      

      Connection managers implementing channels with this interface
        MUST NOT allow the object paths of channels that could be merged
        into a Conference to be re-used, unless the channel re-using the
        object path is equivalent to the channel that previously used it.

      
        If you upgrade some channels into a conference, and then close
          the original channels, InitialChannels
          (which is immutable) will contain paths to channels which no longer
          exist. This implies that you should not re-use channel object paths,
          unless future incarnations of the path are equivalent.

        For instance, on protocols where you can only have
          zero or one 1-1 text channels with Emily at one time, it would
          be OK to re-use the same object path for every 1-1 text channel
          with Emily; but on protocols where this is not true, it would
          be misleading.
      

      Examples of usage

      A pair of 1-1 GSM calls C1 and C2 can be merged
        into a single conference call by calling:

      
        CreateChannel({
            ...ChannelType: ...Call,
            ...InitialChannels: [C1, C2]
          })
      

      which returns a new channel Cn implementing the conference
        interface. (As a quirk of GSM, both 1-1 will cease to function normally
        until they are Split
        from the conference, or the conference ends.)

      An XMPP 1-1 conversation C3 (with
        chris@example.com, say) can be continued in a newly created
        multi-user chatroom by calling:

      
        CreateChannel({
            ...ChannelType: ...Text,
            ...InitialChannels: [C3]
          })
      

      Or, to invite emily@example.net to join the newly-created MUC
        at the same time:

      
        CreateChannel({
            ...ChannelType: ...Text,
            ...InitialChannels: [C3],
            ...InitialInviteeIDs: ['emily@example.net']
          })
      

      To continue C3 in a particular multi-user
        chatroom (rather than the implementation inventing a unique name for
        the room), call:

      
        EnsureChannel({
            ...ChannelType: ...Text,
            ...TargetHandleType: ...Room,
            ...TargetID: 'telepathy@conf.example.com',
            ...InitialChannels: [C3]
          })
      

      Note the use of EnsureChannel — if a channel for
        telepathy@conf.example.com is already open, this SHOULD be
        equivalent to inviting chris@example.com to the existing
        channel.

      In the above cases, the text channel C3 SHOULD remain open
        and fully functional (until explicitly closed by a client); new
        incoming 1-1 messages from chris@example.com SHOULD appear in
        C3, and messages sent using C3 MUST be relayed
        only to chris@example.com.

      
        If there is an open 1-1 text channel with a contact, in every
          other situation new messages will appear in that channel. Given
          that the old channel remains open — which is the least surprising
          behaviour, and eases us towards a beautiful world where channels
          never close themselves — it stands to reason that it should be
          where new messages from Chris should appear. On MSN, creating a
          conference from C3 should migrate the underlying
          switchboard from C3 to the new channel; this is an
          implementation detail, and should not affect the representation on
          D-Bus. With a suitable change of terminology, Skype has the same
          behaviour.

        If the current handler of that channel doesn't want this to happen
          (maybe it transformed the existing tab into the group chat window,
          and so there'd be no UI element still around to show new messages),
          then it should just Close the
          old 1-1 channel; it'll respawn if necessary.
      

      Either of the XMPP cases could work for Call channels, to
        upgrade from 1-1 Jingle to multi-user Jingle. Any of the XMPP cases
        could in principle work for link-local XMPP (XEP-0174).

      XMPP and MSN do not natively have a concept of merging two or more
        channels C1, C2... into one channel, Cn. However, the GSM-style
        merging API can be supported on XMPP and MSN, as an API short-cut
        for upgrading C1 into a conference Cn (which invites the
        TargetHandle of C1 into Cn), then immediately inviting the
        TargetHandle of C2, the TargetHandle of C3, etc. into Cn as well.

      Sample RequestableChannelClasses

      A GSM connection might advertise the following channel class for
        conference calls:

      
        
( Fixed = {
    ...ChannelType:
      ...StreamedMedia
  },
  Allowed = [ InitialChannels,
              InitialAudio
            ]
)
        
      

      This indicates support for starting audio-only conference calls by
        merging two or more existing channels (since
        InitialInviteeHandles and
        InitialInviteeIDs are not allowed).

      An XMPP connection might advertise the following classes for ad-hoc
        multi-user text chats:

      
        
( Fixed = {
    ...ChannelType:
      ...Text
  },
  Allowed = [ InitialChannels,
              InitialInviteeHandles,
              InitialInviteeIDs,
              InvitationMessage
            ]
),
( Fixed = {
    ...ChannelType:
      ...Text,
    ...TargetHandleType:
      Room
  },
  Allowed = [ TargetHandle,
              TargetID,
              InitialChannels,
              InitialInviteeHandles,
              InitialInviteeIDs,
              InvitationMessage
            ]
)
        
      

      The first class indicates support for starting ad-hoc (nameless) chat
        rooms, upgraded from existing 1-1 channels and/or inviting new
        contacts, along with a message to be sent along with the invitations.
        The second indicates support for upgrading to a particular named chat
        room.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Channel.Interface.Conference')

    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.Conference', signature='oua{sv}')
    def ChannelMerged(self, Channel, Channel_Specific_Handle, Properties):
        """
        Emitted when a new channel is added to the value of
          Channels.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.Conference', signature='oa{sv}')
    def ChannelRemoved(self, Channel, Details):
        """
        Emitted when a channel is removed from the value of
          Channels, either because it closed
          or because it was split using the Splittable.DRAFT.Split method.

        If a channel is removed because it was closed, Closed should be emitted
          before this signal.
      
        """
        pass
  