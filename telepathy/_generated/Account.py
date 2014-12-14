# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2008-2009 Collabora Ltd.
Copyright © 2008-2009 Nokia Corporation

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


class Account(dbus.service.Object):
    """\
      An Account object encapsulates the necessary details to make a
        Telepathy connection.

      Accounts are uniquely identified by object path. The object path
        of an Account MUST take the form
        /org/freedesktop/Telepathy/Account/cm/proto/acct, where:

      
        cm is the same Connection_Manager_Name
          that appears in the connection manager's well-known bus name and
          object path
        proto is the Protocol name as seen in
          ConnectionManager.ListProtocols,
          but with "-" replaced with "_"
          (i.e. the same as in the object-path of a Connection)
        acct is an arbitrary string of ASCII letters, digits
          and underscores, starting with a letter or underscore, which
          uniquely identifies this account
        Clients SHOULD parse the object path to discover the
          connection manager and protocol
        Clients MUST NOT attempt to parse acct
        Clients MUST NOT assume that acct matches
          the connection-specific part of a Connection's object-path and
          bus name
        The account manager SHOULD choose acct such that if
          an account is deleted, its object path will be re-used if and only
          if the new account is in some sense "the same"
          (incorporating the 'account' parameter in some way is
          recommended)
      

      
        This API avoids specifying the "profiles" used in Mission Control
          4.x or the "presets" that have been proposed to replace them. An
          optional interface will be provided for AM implementations
          that want to provide presets.

        There is deliberately no functionality here for opening channels;
          we intend to provide that in the channel dispatcher.

        Other missing features which would be better in their own
          interfaces:

        
          dynamic parameter-providing (aka provisioning)
          saved server capabilities
          account conditions
          account grouping
        
      

    """

    @dbus.service.method('org.freedesktop.Telepathy.Account', in_signature='', out_signature='')
    def Remove(self):
        """Delete the account.
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Account', in_signature='a{sv}as', out_signature='as')
    def UpdateParameters(self, Set, Unset):
        """
        Change the value of the Parameters
          property.

        If any of the changed parameters'
          Conn_Mgr_Param_Flags include
          DBus_Property, the change will be applied immediately to
          the
          corresponding D-Bus Property on the active
          Connection, if there is one. Changes to
          other parameters will not take effect until the next time the account
          is disconnected and reconnected.

        
          In general, reconnecting is a destructive operation that shouldn't
            happen as a side-effect. In particular, migration tools that
            twiddle the settings of all accounts shouldn't cause an automatic
            disconnect and reconnect.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Account', in_signature='', out_signature='')
    def Reconnect(self):
        """
        Re-connect this account. If the account is currently disconnected
          and the requested presence is offline, or if the account
          is not Enabled or not
          Valid, this does nothing.

        If the account is disconnected and the requested presence is not
          offline, this forces an attempt to connect with the requested
          presence immediately.

        If the account is connecting or connected, this is equivalent to
          remembering the current value of
          RequestedPresence, setting its value
          to (OFFLINE, "offline", ""), waiting for the change to take effect,
          then setting its value to the value that was previously
          remembered.

        
          Clients desiring "instant apply" semantics for CM parameters MAY
            call this method to achieve that.
        

        In particular, if the account's
          Connection is in the Connecting
          state, calling this method causes the attempt to connect to be
          aborted and re-tried.

        
          This is necessary to ensure that the new parameters are
            picked up.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Account', signature='')
    def Removed(self):
        """
        This account has been removed.

        
          This is redundant with AccountRemoved,
          but it's still worth having,
          to avoid having to bind to AccountManager.AccountRemoved to tell
          you whether your Account is valid — ideally, an account-editing UI
          should only care about a single Account.
        
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Account', signature='a{sv}')
    def AccountPropertyChanged(self, Properties):
        """
        The values of one or more properties on this interface (that do not
        specify that this signal does not apply to them) may have changed.
        This does not cover properties of other interfaces, which must
        provide their own change notification if appropriate.
      
        """
        pass
  