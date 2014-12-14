# telepathy-python - Base classes defining the interfaces of the Telepathy framework
#
# Copyright (C) 2005, 2006 Collabora Limited
# Copyright (C) 2005, 2006 Nokia Corporation
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import dbus
import dbus.service

from telepathy.constants import (CONNECTION_HANDLE_TYPE_NONE,
                                 CHANNEL_TEXT_MESSAGE_TYPE_NORMAL,
                                 HANDLE_TYPE_NONE)

from telepathy.errors import InvalidArgument, NotImplemented

from telepathy.interfaces import (CHANNEL_INTERFACE,
                                  CHANNEL_INTERFACE_CONFERENCE,
                                  CHANNEL_INTERFACE_DTMF,
                                  CHANNEL_INTERFACE_GROUP,
                                  CHANNEL_INTERFACE_HOLD,
                                  CHANNEL_INTERFACE_PASSWORD,
                                  CHANNEL_TYPE_CONTACT_LIST,
                                  CHANNEL_TYPE_FILE_TRANSFER,
                                  CHANNEL_TYPE_ROOM_LIST,
                                  CHANNEL_TYPE_STREAMED_MEDIA,
                                  CHANNEL_TYPE_TEXT,
                                  MEDIA_SESSION_HANDLER,
                                  MEDIA_STREAM_HANDLER)

from telepathy._generated.Channel import Channel as _Channel

from telepathy.server.properties import DBusProperties

from telepathy.server.handle import NoneHandle

class Channel(_Channel, DBusProperties):

    def __init__(self, connection, manager, props, object_path=None):
        """
        Initialise the base channel object.

        Parameters:
        connection - the parent Connection object
        props - initial channel properties
        """
        self._conn = connection
        self._chan_manager = manager

        object_path = self._conn.get_channel_path(object_path)
        _Channel.__init__(self, self._conn._name, object_path)

        self._type = props[CHANNEL_INTERFACE + '.ChannelType']
        self._requested = props[CHANNEL_INTERFACE + '.Requested']

        tht = props.get(CHANNEL_INTERFACE + '.TargetHandleType', HANDLE_TYPE_NONE)

        if tht == HANDLE_TYPE_NONE:
            self._handle = NoneHandle()
        else:
            self._handle = self._conn.handle(
                props[CHANNEL_INTERFACE + '.TargetHandleType'],
                props[CHANNEL_INTERFACE + '.TargetHandle'])

        self._interfaces = set()

        DBusProperties.__init__(self)
        self._implement_property_get(CHANNEL_INTERFACE,
            {'ChannelType': lambda: dbus.String(self.GetChannelType()),
             'Interfaces': lambda: dbus.Array(self.GetInterfaces(), signature='s'),
             'TargetHandle': lambda: dbus.UInt32(self._handle.get_id()),
             'TargetHandleType': lambda: dbus.UInt32(self._handle.get_type()),
             'TargetID': lambda: dbus.String(self._handle.get_name()),
             'Requested': lambda: self._requested})

        self._add_immutable_properties({
            'ChannelType': CHANNEL_INTERFACE,
            'TargetHandle': CHANNEL_INTERFACE,
            'Interfaces': CHANNEL_INTERFACE,
            'TargetHandleType': CHANNEL_INTERFACE,
            'TargetID': CHANNEL_INTERFACE,
            'Requested': CHANNEL_INTERFACE
            })

    def _add_immutables(self, props):
        #backward compatibility
        self._add_immutable_properties(props)

    @dbus.service.method(CHANNEL_INTERFACE, in_signature='', out_signature='')
    def Close(self):
        self.Closed()

        # Do all these separately in case one works but another doesn't.
        try:
            self._chan_manager.remove_channel(self)
        except:
            pass

        try:
            self._conn.remove_channel(self)
        except:
            pass

        try:
            self.remove_from_connection()
        except:
            pass

    @dbus.service.method(CHANNEL_INTERFACE, in_signature='', out_signature='s')
    def GetChannelType(self):
        """ Returns the interface name for the type of this channel. """
        return self._type

    @dbus.service.method(CHANNEL_INTERFACE, in_signature='', out_signature='uu')
    def GetHandle(self):
        """ Returns the handle type and number if this channel represents a
        communication with a particular contact, room or server-stored list, or
        zero if it is transient and defined only by its contents. """
        return (self._handle.get_type(), self._handle.get_id())

    @dbus.service.method(CHANNEL_INTERFACE, in_signature='', out_signature='as')
    def GetInterfaces(self):
        """
        Get the optional interfaces implemented by the channel.

        Returns:
        an array of the D-Bus interface names
        """
        return self._interfaces

from telepathy._generated.Channel_Type_Contact_List \
        import ChannelTypeContactList as _ChannelTypeContactListIface

class ChannelTypeContactList(Channel, _ChannelTypeContactListIface):
    __doc__ = _ChannelTypeContactListIface.__doc__

    def __init__(self, connection, manager, props, object_path=None):
        """
        Initialise the channel.

        Parameters:
        connection - the parent Telepathy Connection object
        """
        Channel.__init__(self, connection, manager, props,
            object_path=object_path)

    def Close(self):
        raise NotImplemented("Contact lists can't be closed")


from telepathy._generated.Channel_Type_File_Transfer \
        import ChannelTypeFileTransfer as _ChannelTypeFileTransferIface

class ChannelTypeFileTransfer(Channel, _ChannelTypeFileTransferIface):
    __doc__ = _ChannelTypeFileTransferIface.__doc__

    def __init__(self, connection, manager, props, object_path=None):
        """
        Initialise the channel.

        Parameters:
        connection - the parent Telepathy Connection object
        """
        Channel.__init__(self, connection, manager, props,
            object_path=object_path)


from telepathy._generated.Channel_Interface_SASL_Authentication \
        import ChannelInterfaceSASLAuthentication

from telepathy._generated.Channel_Type_Server_Authentication \
        import ChannelTypeServerAuthentication as _ChannelTypeServerAuthenticationIface

class ChannelTypeServerAuthentication(Channel, _ChannelTypeServerAuthenticationIface):
    __doc__ = _ChannelTypeServerAuthenticationIface.__doc__

    def __init__(self, connection, manager, props, object_path=None):
        """
        Initialise the channel.

        Parameters:
        connection - the parent Telepathy Connection object
        """
        Channel.__init__(self, connection, manager, props,
            object_path=object_path)


from telepathy._generated.Channel_Type_Streamed_Media \
        import ChannelTypeStreamedMedia as _ChannelTypeStreamedMediaIface

class ChannelTypeStreamedMedia(Channel, _ChannelTypeStreamedMediaIface):
    __doc__ = _ChannelTypeStreamedMediaIface.__doc__

    def __init__(self, connection, manager, props, object_path=None):
        """
        Initialise the channel.

        Parameters:
        connection - the parent Telepathy Connection object
        """
        Channel.__init__(self, connection, manager, props,
            object_path=object_path)


from telepathy._generated.Channel_Type_Room_List \
        import ChannelTypeRoomList as _ChannelTypeRoomListIface

class ChannelTypeRoomList(Channel, _ChannelTypeRoomListIface):
    __doc__ = _ChannelTypeRoomListIface.__doc__

    def __init__(self, connection, manager, props, object_path=None):
        """
        Initialise the channel.

        Parameters:
        connection - the parent Telepathy Connection object
        """
        Channel.__init__(self, connection, manager, props,
            object_path=object_path)
        self._listing_rooms = False
        self._rooms = {}

        self._add_immutable_properties({'Server': CHANNEL_TYPE_ROOM_LIST})

    @dbus.service.method(CHANNEL_TYPE_ROOM_LIST, in_signature='', out_signature='b')
    def GetListingRooms(self):
        return self._listing_rooms

    @dbus.service.signal(CHANNEL_TYPE_ROOM_LIST, signature='b')
    def ListingRooms(self, listing):
        self._listing_rooms = listing


from telepathy._generated.Channel_Type_Text \
        import ChannelTypeText as _ChannelTypeTextIface

class ChannelTypeText(Channel, _ChannelTypeTextIface):
    __doc__ = _ChannelTypeTextIface.__doc__

    def __init__(self, connection, manager, props, object_path=None):
        """
        Initialise the channel.

        Parameters:
        connection - the parent Telepathy Connection object
        """
        Channel.__init__(self, connection, manager, props,
            object_path=object_path)

        self._pending_messages = {}
        self._message_types = [CHANNEL_TEXT_MESSAGE_TYPE_NORMAL]

    @dbus.service.method(CHANNEL_TYPE_TEXT, in_signature='', out_signature='au')
    def GetMessageTypes(self):
        """
        Return an array indicating which types of message may be sent on this
        channel.

        Returns:
        an array of integer message types as defined above
        """
        return self._message_types

    @dbus.service.method(CHANNEL_TYPE_TEXT, in_signature='au', out_signature='')
    def AcknowledgePendingMessages(self, ids):
        """
        Inform the channel that you have handled messages by displaying them to
        the user (or equivalent), so they can be removed from the pending queue.

        Parameters:
        ids - the message to acknowledge

        Possible Errors:
        InvalidArgument (a given message ID was not found, no action taken)
        """
        for id in ids:
            if id not in self._pending_messages:
                raise InvalidArgument("the given message ID was not found")

        for id in ids:
            del self._pending_messages[id]

    @dbus.service.method(CHANNEL_TYPE_TEXT, in_signature='b', out_signature='a(uuuuus)')
    def ListPendingMessages(self, clear):
        """
        List the messages currently in the pending queue, and optionally
        remove then all.

        Parameters:
        clear - a boolean indicating whether the queue should be cleared

        Returns:
        an array of structs containing:
            a numeric identifier
            a unix timestamp indicating when the message was received
            an integer handle of the contact who sent the message
            an integer of the message type
            a bitwise OR of the message flags
            a string of the text of the message
        """
        messages = []
        for id in list(self._pending_messages.keys()):
            (timestamp, sender, type, flags, text) = self._pending_messages[id]
            message = (id, timestamp, sender, type, flags, text)
            messages.append(message)
            if clear:
                del self._pending_messages[id]
        messages.sort(cmp=lambda x,y:cmp(x[1], y[1]))
        return messages

    @dbus.service.signal(CHANNEL_TYPE_TEXT, signature='uuuuus')
    def Received(self, id, timestamp, sender, type, flags, text):
        if id in self._pending_messages:
            raise ValueError("You can't receive the same message twice.")
        else:
            self._pending_messages[id] = (timestamp, sender, type, flags, text)


from telepathy._generated.Channel_Interface_Chat_State \
        import ChannelInterfaceChatState

from telepathy._generated.Channel_Interface_Conference \
        import ChannelInterfaceConference as _ChannelInterfaceConference

class ChannelInterfaceConference(_ChannelInterfaceConference):

    def __init__(self):
        _ChannelInterfaceConference.__init__(self)

        self._conference_channels = set()
        self._conference_initial_channels = set()
        self._conference_initial_invitees = set()
        self._conference_invitation_message = ""
        self._conference_original_channels = {}

        # D-Bus properties for conference interface
        self._implement_property_get(CHANNEL_INTERFACE_CONFERENCE, {
            'Channels':
                lambda: dbus.Array(self._conference_channels, signature='o'),
            'InitialChannels':
                lambda: dbus.Array(self._conference_initial_channels,
                                   signature='o'),
            'InitialInviteeHandles':
                lambda: dbus.Array(
                    [h.get_id() for h in self._conference_initial_invitees],
                    signature='u'),
            'InitialInviteeIDs':
                lambda: dbus.Array(
                    [h.get_name() for h in self._conference_initial_invitees],
                    signature='s'),
            'InvitationMessage':
                lambda: dbus.String(self._conference_invitation_message),
            'OriginalChannels':
                lambda: dbus.Dictionary(self._conference_original_channels,
                                        signature='uo')
            })

        # Immutable conference properties
        self._add_immutable_properties({
                'InitialChannels': CHANNEL_INTERFACE_CONFERENCE,
                'InitialInviteeIDs': CHANNEL_INTERFACE_CONFERENCE,
                'InitialInviteeHandles': CHANNEL_INTERFACE_CONFERENCE,
                'InvitationMessage': CHANNEL_INTERFACE_CONFERENCE
                })

from telepathy._generated.Channel_Interface_DTMF import ChannelInterfaceDTMF


from telepathy._generated.Channel_Interface_Group \
        import ChannelInterfaceGroup as _ChannelInterfaceGroup

class ChannelInterfaceGroup(_ChannelInterfaceGroup):

    def __init__(self):
        _ChannelInterfaceGroup.__init__(self)

        self._implement_property_get(CHANNEL_INTERFACE_GROUP,
            {'GroupFlags': lambda: dbus.UInt32(self.GetGroupFlags()),
             'Members': lambda: dbus.Array(self.GetMembers(), signature='u'),
             'RemotePendingMembers': lambda: dbus.Array(self.GetRemotePendingMembers(), signature='u'),
             'SelfHandle': lambda: dbus.UInt32(self.GetSelfHandle())})

        self._group_flags = 0
        self._members = set()
        self._local_pending = set()
        self._remote_pending = set()

    @dbus.service.method(CHANNEL_INTERFACE_GROUP, in_signature='', out_signature='u')
    def GetGroupFlags(self):
        return self._group_flags

    @dbus.service.signal(CHANNEL_INTERFACE_GROUP, signature='uu')
    def GroupFlagsChanged(self, added, removed):
        self._group_flags |= added
        self._group_flags &= ~removed

    @dbus.service.method(CHANNEL_INTERFACE_GROUP, in_signature='', out_signature='au')
    def GetMembers(self):
        return self._members

    @dbus.service.method(CHANNEL_INTERFACE_GROUP, in_signature='', out_signature='u')
    def GetSelfHandle(self):
        self_handle = self._conn.GetSelfHandle()
        if (self_handle in self._members or
            self_handle in self._local_pending or
            self_handle in self._remote_pending):
            return self_handle
        else:
            return 0

    @dbus.service.method(CHANNEL_INTERFACE_GROUP, in_signature='', out_signature='au')
    def GetLocalPendingMembers(self):
        return self._local_pending

    @dbus.service.method(CHANNEL_INTERFACE_GROUP, in_signature='', out_signature='au')
    def GetRemotePendingMembers(self):
        return self._remote_pending

    @dbus.service.method(CHANNEL_INTERFACE_GROUP, in_signature='', out_signature='auauau')
    def GetAllMembers(self):
        return (self._members, self._local_pending, self._remote_pending)

    @dbus.service.signal(CHANNEL_INTERFACE_GROUP, signature='sauauauauuu')
    def MembersChanged(self, message, added, removed, local_pending, remote_pending, actor, reason):

        self._members.update(added)
        self._members.difference_update(removed)

        self._local_pending.update(local_pending)
        self._local_pending.difference_update(added)
        self._local_pending.difference_update(removed)

        self._remote_pending.update(remote_pending)
        self._remote_pending.difference_update(added)
        self._remote_pending.difference_update(removed)


from telepathy._generated.Channel_Interface_Hold import ChannelInterfaceHold


# ChannelInterfaceMediaSignalling is in telepathy.server.media


from telepathy._generated.Channel_Interface_Password \
        import ChannelInterfacePassword as _ChannelInterfacePassword

class ChannelInterfacePassword(_ChannelInterfacePassword):
    def __init__(self):
        _ChannelInterfacePassword.__init__(self)
        self._password_flags = 0
        self._password = ''

    @dbus.service.method(CHANNEL_INTERFACE_PASSWORD, in_signature='', out_signature='u')
    def GetPasswordFlags(self):
        return self._password_flags

    @dbus.service.signal(CHANNEL_INTERFACE_PASSWORD, signature='uu')
    def PasswordFlagsChanged(self, added, removed):
        self._password_flags |= added
        self._password_flags &= ~removed


from telepathy._generated.Channel_Interface_Call_State import ChannelInterfaceCallState
