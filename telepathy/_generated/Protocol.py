# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2009-2010 Collabora Ltd.

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


class Protocol(dbus.service.Object):
    """\
      An object representing a protocol for which this ConnectionManager
        can create Connections.

      Each Protocol object has the same well-known bus name as its parent
        ConnectionManager. Its object path is formed by taking the
        ConnectionManager's object path and appending '/', followed by the
        Protocol name with any hyphen/minus '-' converted
        to underscores '_'.

      
        This is the same as the representation of protocol names
          in Account object paths, and in Connection object paths and bus
          names. For instance, telepathy-gabble and telepathy-salut would
          implement objects at
          /org/freedesktop/Telepathy/ConnectionManager/gabble/jabber
          and
          /org/freedesktop/Telepathy/ConnectionManager/salut/local_xmpp,
          respectively.
      

      If the ConnectionManager has a .manager file, each
        Protocol's immutable properties must be represented in that file;
        the representation is described as part of the documentation for
        each property. For instance, a very simple ConnectionManager with one
        Protocol might be represented like this:


[ConnectionManager]
Interfaces=

[Protocol example]
Interfaces=
ConnectionInterfaces=org.freedesktop.Telepathy.Connection.Interface.Requests;
param-account=s required
param-password=s required secret
RequestableChannelClasses=text;
VCardField=x-example
EnglishName=Example
Icon=im-example
AuthenticationTypes=org.freedesktop.Telepathy.Channel.Type.ServerTLSConnection;org.freedesktop.Telepathy.Channel.Interface.SASLAuthentication;

[text]
org.freedesktop.Telepathy.Channel.ChannelType s=org.freedesktop.Telepathy.Channel.Type.Text
org.freedesktop.Telepathy.Channel.TargetHandleType u=1
allowed=org.freedesktop.Telepathy.Channel.TargetHandle;org.freedesktop.Telepathy.Channel.TargetID;

    """

    @dbus.service.method('org.freedesktop.Telepathy.Protocol', in_signature='a{sv}', out_signature='s')
    def IdentifyAccount(self, Parameters):
        """
        Return a string which uniquely identifies the account to which the
          given parameters would connect.

        
          For many protocols, this would return the well-known 'account'
            parameter. However, for IRC the returned string would be composed
            from the 'account' (i.e. nickname) and 'server' parameters.
            AccountManager implementations can use this to form the
            account-specific part of an Account's object path.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Protocol', in_signature='s', out_signature='s')
    def NormalizeContact(self, Contact_ID):
        """
        Attempt to normalize the given contact ID. Where possible, this
          SHOULD return the same thing that would be returned by
          InspectHandles(RequestHandles(CONTACT, [Contact_ID])) on a connected
          Connection.

        If full normalization requires network activity or is otherwise
          impossible to do without a Connection,
          this method SHOULD perform a best-effort normalization.

        
          One common example of a best-effort offline normalization
            differing from the ideal normalization is XMPP.

          On XMPP, contacts' JIDs should normally have the resource removed
            during normalization, but for contacts in a MUC (chatroom), the
            resource is an integral part of the JID - so the contact JID
            alice@example.com/Empathy should normalize to alice@example.com,
            but the in-MUC JID wonderland@conference.example.com/Alice should
            normalize to itself.

          While online, the connection manager has enough context to know
            which chatrooms the user is in, and can infer from that whether
            to remove resources, but the best-effort normalization performed
            while offline does not have this context, so the best that can be
            done is to remove the resource from all JIDs.
        

        This method MAY simply raise NotImplemented on some protocols.

        
          In link-local XMPP, you can't talk to someone who isn't present
            on your local network, so normalizing identifiers in advance is
            meaningless.
        
      
        """
        raise NotImplementedError
  