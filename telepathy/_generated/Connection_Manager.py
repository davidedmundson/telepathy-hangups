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


class ConnectionManager(dbus.service.Object):
    """\
    A D-Bus service which allows connections to be created. The manager
      processes are intended to be started by D-Bus service activation.

    For service discovery, each Telepathy connection manager must have
      a connection manager name (see
      Connection_Manager_Name for syntax).

    The connection manager must then provide a well-known bus name of
      org.freedesktop.Telepathy.ConnectionManager.cmname
      where cmname is its connection manager name. If it makes sense
      to start the connection manager using D-Bus service activation, it
      must register that well-known name for service activation by installing
      a .service file.

    Clients can list the running connection managers by calling the
      ListNames method on the D-Bus daemon's org.freedesktop.DBus interface
      and looking for names matching the above pattern; they can list the
      activatable connection managers by calling ListActivatableNames, and
      they should usually combine the two lists to get a complete list of
      running or activatable connection managers.

    When the connection manager is running, it must have an object
      implementing the ConnectionManager interface at the object path
      /org/freedesktop/Telepathy/ConnectionManager/cmname.
    

    Connection managers' capabilities can be determined dynamically by
      calling their ListProtocols method, then
      for each protocol of interest, calling
      GetParameters to discover the required and
      optional parameters.
      However, since it is inefficient to activate all possible connection
      managers on the system just to find out what they can do, there
      is a standard mechanism to store static information about CMs in
      ".manager files".

    To look up a connection manager's supported protocols, clients
      should search the data directories specified by
      the
        freedesktop.org XDG Base Directory Specification ($XDG_DATA_HOME,
      defaulting to $HOME/.local/share if unset, followed by
      colon-separated paths from $XDG_DATA_DIRS, defaulting to
      /usr/local/share:/usr/share if unset) for the first file named
      telepathy/managers/cmname.manager that can be
      read without error. This file has the same syntax as a
      freedesktop.org Desktop Entry file.

    Clients must still support connection managers for which no
      .manager file can be found, which they can do by activating
      the connection manager and calling its methods; the
      .manager file is merely an optimization. Connection managers
      whose list of protocols can change at any time (for instance, via
      a plugin architecture) should not install a .manager
      file.

    The .manager file SHOULD have a group headed
      [ConnectionManager], containing a key
      Interfaces representing
      Interfaces as a sequence of strings
      each followed by a semicolon (the "localestrings" type from the Desktop
      Entry Specification).

    The [ConnectionManager] group SHOULD NOT contain keys
      ObjectPath or BusName. If it does, they MUST
      be ignored.

    
      The object path and bus name are derivable from the connection
        manager's name, which is part of the filename, so these keys are
        redundant. They were required in very old versions of Telepathy.
    

    For each protocol name proto that would be returned by
      ListProtocols, the .manager file contains a group
      headed [Protocol proto]. For each parameter
      p that would be returned by GetParameters(proto), the
      .manager file contains a key param-p with a value
      consisting of a D-Bus signature (a single complete type), optionally
      followed by a space and a space-separated list of flags. The supported
      flags are:

    
      required, corresponding to
        Conn_Mgr_Param_Flag_Required
      register, corresponding
        to Conn_Mgr_Param_Flag_Register
      secret, corresponding
        to Conn_Mgr_Param_Flag_Secret
      dbus-property, corresponding
        to Conn_Mgr_Param_Flag_DBus_Property
    

    The group may also contain a key default-p
      whose value is a string form of the default value for the parameter.
      If this key exists, it sets the default, and also sets the flag
      Conn_Mgr_Param_Flag_Has_Default. The default value is formatted
      according to the D-Bus signature as follows:

    
      s (string)
        The UTF-8 string, with the standard backslash escape
          sequences supported by the Desktop Entry Specification
          (the "localestring" type from the Desktop Entry Specification)
      o (object path)
        The object path as an ASCII string
      b (boolean)
        "true" (case-insensitively) or "1" means True, "false"
          (case-insensitively) or "0" means False; when writing a file,
          "true" and "false" SHOULD be used
      y, q, u, t (8-, 16-, 32-, 64-bit unsigned integer)
        ASCII decimal integer
      n, i, x (16-, 32-, 64-bit signed integer)
        ASCII decimal integer, optionally prefixed with "-"
      d (double-precision floating point)
        ASCII decimal number
      as (array of string)
        A sequence of UTF-8 strings each followed by a semicolon, with
          any semicolons they contain escaped with a backslash
          (the "localestrings" type from the Desktop Entry Specification)
    

    Currently, no other D-Bus signatures are allowed to have default values,
      but clients parsing the .manager file MUST ignore defaults
      that they cannot parse, and treat them as if the
      default-p key was not present at all.

    It is not required that a connection manager be able to support multiple
    protocols, or even multiple connections. When a connection is made, a
    service name where the connection object can be found is returned. A
    manager which can only make one connection may then remove itself from its
    well-known bus name, causing a new connection manager to be activated when
    somebody attempts to make a new connection.
    """

    @dbus.service.method('org.freedesktop.Telepathy.ConnectionManager', in_signature='s', out_signature='a(susv)')
    def GetParameters(self, Protocol):
        """
        Get a list of the parameters which must or may be provided to the
        RequestConnection method when connecting
        to the given protocol,
        or registering (the boolean "register" parameter is available,
        and set to true).
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.ConnectionManager', in_signature='', out_signature='as')
    def ListProtocols(self):
        """
        Get a list of protocol identifiers that are implemented by this
        connection manager.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.ConnectionManager', in_signature='sa{sv}', out_signature='so')
    def RequestConnection(self, Protocol, Parameters):
        """
        Request a
          Connection
          object representing a given account on a given
          protocol with the given parameters. The method returns the bus name
          and the object path where the new Connection object can be found,
          which should have the status of Connection_Status_Disconnected, to
          allow signal handlers to be attached before connecting is started
          with the
          Connect
          method.

        The parameters which must and may be provided in the parameters
        dictionary can be discovered with the
        GetParameters method. These
        parameters, their types, and their default values may be cached
        in files so that all available connection managers do not need to be
        started to discover which protocols are available.

        To request values for these parameters from the user, a client must
        have prior knowledge of the meaning of the parameter names, so the
        well-known names and types defined by the
        Connection_Parameter_Name type should be used where
        appropriate.

        Connection manager authors SHOULD avoid introducing parameters
          whose default values would not be serializable in a
          .manager file.

        
          The same serialization format is used in Mission Control
            to store accounts.
        

        Every successful RequestConnection call will cause the emission of a
        NewConnection signal for the same newly
        created connection. The
        requester can use the returned object path and service name
        independently of the emission of that signal. In that case this signal
        emission is most useful for, e.g. other processes that are monitoring
        the creation of new connections.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.ConnectionManager', signature='sos')
    def NewConnection(self, Bus_Name, Object_Path, Protocol):
        """
        Emitted when a new Connection object
        is created.
      
        """
        pass
  