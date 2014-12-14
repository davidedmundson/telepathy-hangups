# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright (C) 2005-2008 Collabora Limited
Copyright (C) 2005-2008 Nokia Corporation
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


class ConnectionInterfaceAvatars(dbus.service.Interface):
    """\
      An interface for requesting avatars for contacts on a given connection,
    receiving notification when avatars are changed, and publishing your own
    avatar.

    Avatars are identified by a string, the Avatar_Token,
    which represents a particular avatar. Tokens MUST be chosen by the
    connection manager in such a way that the triple
    (Connection_Manager_Name, Protocol,
    Avatar_Token) uniquely identifies an avatar.
    An empty token means that an avatar has not been set for this contact, and
    a changed token implies the contact's avatar has changed, but the strings
    should otherwise be considered opaque by clients.

    A client should use GetKnownAvatarTokens
    to request the tokens for the
    avatars of all the contacts it is interested in when it connects. The
    avatars can then be requested using
    RequestAvatars for the contacts.  Clients
    should bind to the AvatarUpdated signal and
    request a new copy of
    the avatar when a contacts' avatar token changes. Clients should cache the
    token and data of each contact's avatar between connections, to avoid
    repeatedly retrieving the same avatar.

    To publish an avatar, a client should use
    SetAvatar to provide an image which meets
    the requirements returned by the
    GetAvatarRequirements
    function. On some protocols the avatar is stored on the server, so setting
    the avatar is persistent, but on others it is transferred via a peer to
    peer mechanism, so needs to be set every connection. Hence, on every
    connection, clients should inspect the avatar token of the connection's
    self handle using GetKnownAvatarTokens; if
    the self handle is not in the
    returned map, the client should re-set the avatar. If the self handle's
    avatar token is known, but the avatar has been changed locally since the
    last connection, the client should upload the new avatar; if the avatar has
    not changed locally, then the client should download the avatar from the
    server if its token differs from the that of the local avatar.

    To remove the published avatar on protocols which have persistent avatars,
    a client should use the ClearAvatar method.
    This method can safely be used even if there is no avatar for this
    connection.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Connection.Interface.Avatars')

    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Avatars', in_signature='', out_signature='asqqqqu')
    def GetAvatarRequirements(self):
        """
        Get the required format of avatars on this connection.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Avatars', in_signature='au', out_signature='as')
    def GetAvatarTokens(self, Contacts):
        """
        Get the unique tokens for all of the given contacts' avatars.

        Using this method in new Telepathy clients is deprecated; use
        GetKnownAvatarTokens instead.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Avatars', in_signature='au', out_signature='a{us}')
    def GetKnownAvatarTokens(self, Contacts):
        """
        Get the unique tokens for the given contacts' avatars. These tokens
        can be persisted across connections, and should be used by the client
        to check whether the avatars have been updated.  For handles other than
        the self handle, only tokens that are already known are returned; an
        empty token means the given contact has no avatar.  However, a CM must
        always have the tokens for the self handle if one is set (even if it is
        set to no avatar).  On protocols where the avatar does not persist
        between connections, a CM should omit the self handle from the returned
        map until an avatar is explicitly set or cleared.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Avatars', in_signature='u', out_signature='ays')
    def RequestAvatar(self, Contact):
        """
        Request the avatar for a given contact. Using this method in new
        Telepathy clients is deprecated; use RequestAvatars instead.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Avatars', in_signature='au', out_signature='')
    def RequestAvatars(self, Contacts):
        """
        Request avatars for a number of contacts. The
        AvatarRetrieved signal is emitted for
        each avatar retrieved. If the handles are valid but retrieving an
        avatar fails (for any reason, including the contact not having an
        avatar) the AvatarRetrieved signal is not emitted for that contact.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Avatars', in_signature='ays', out_signature='s')
    def SetAvatar(self, Avatar, MIME_Type):
        """
        Set a new avatar image for this connection. The avatar image must
        respect the requirements obtained by
        GetAvatarRequirements.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Connection.Interface.Avatars', in_signature='', out_signature='')
    def ClearAvatar(self):
        """
        Remove the avatar image for this connection.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.Avatars', signature='us')
    def AvatarUpdated(self, Contact, New_Avatar_Token):
        """
        Emitted when the avatar for a contact has been updated, or first
        discovered on this connection. If the token differs from the token
        associated with the client's cached avatar for this contact, the new
        avatar should be requested with
        RequestAvatars.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Connection.Interface.Avatars', signature='usays')
    def AvatarRetrieved(self, Contact, Token, Avatar, Type):
        """
        Emitted when the avatar for a contact has been retrieved.
      
        """
        pass
  