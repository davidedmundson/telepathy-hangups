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

from telepathy.errors import NotImplemented
from telepathy.interfaces import (CONN_MGR_INTERFACE)
from telepathy.server.properties import DBusProperties

from telepathy._generated.Connection_Manager \
        import ConnectionManager as _ConnectionManager

class ConnectionManager(_ConnectionManager, DBusProperties):
    def __init__(self, name):
        """
        Initialise the connection manager.
        """
        bus_name = 'org.freedesktop.Telepathy.ConnectionManager.%s' % name
        object_path = '/org/freedesktop/Telepathy/ConnectionManager/%s' % name
        _ConnectionManager.__init__(self,
                                    dbus.service.BusName(bus_name, dbus.Bus(), do_not_queue=True),
                                    object_path)

        self._interfaces = set()
        self._connections = set()
        self._protos = {} # proto name => Connection constructor
        self._protocols = {} # proto name => Protocol object

        DBusProperties.__init__(self)
        self._implement_property_get(CONN_MGR_INTERFACE, {
                'Interfaces': lambda: dbus.Array(self._interfaces, signature='s'),
                'Protocols': lambda: dbus.Dictionary(self._protocol_properties,
                                                     signature='sa{sv}')
                })

    def connected(self, conn):
        """
        Add a connection to the list of connections, emit the appropriate
        signal.
        """
        self._connections.add(conn)
        self.NewConnection(conn._name.get_name(), conn._object_path, conn._proto)

    def disconnected(self, conn):
        """
        Remove a connection from the list of connections.
        """
        self._connections.remove(conn)
        if hasattr(conn, 'remove_from_connection'):
            # requires dbus-python >= 0.81.1
            conn.remove_from_connection()
        del conn

        return False # when called in an idle callback

    def check_proto(self, proto):
        if proto not in self._protos:
            raise NotImplemented('unknown protocol %s' % proto)

    def check_protocol(self, proto):
        if proto not in self._protocols:
            raise NotImplemented('no protocol object for %s' % proto)

    @dbus.service.method(CONN_MGR_INTERFACE, in_signature='s', out_signature='a(susv)')
    def GetParameters(self, proto):
        "Returns the mandatory and optional parameters for the given proto."
        self.check_proto(proto)
        self.check_protocol(proto)

        return self._protocols[proto].parameters

    @dbus.service.method(CONN_MGR_INTERFACE, in_signature='', out_signature='as')
    def ListProtocols(self):
        return list(self._protos.keys())

    def RequestConnection(self, proto, parameters):
        self.check_proto(proto)

        conn = self._protos[proto](self, parameters)
        self.connected(conn)
        return (conn._name.get_name(), conn._object_path)

    def _implement_protocol(self, name, protocol_class):
        protocol = protocol_class(self)
        self._protocols[name] = protocol
        self._protos[name] = protocol.create_connection

    @property
    def _protocol_properties(self):
        properties = {}
        for name, protocol in list(self._protocols.items()):
            properties[name] = protocol.get_immutable_properties()
        return properties
