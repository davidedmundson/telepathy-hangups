# telepathy-python - Base classes defining the interfaces of the Telepathy framework
#
# Copyright (C) 2005, 2006, 2008 Collabora Limited
# Copyright (C) 2005, 2006 Nokia Corporation
# Copyright (C) 2008 Olivier Le Thanh Duong <olivier@lethanh.be>
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

from telepathy.interfaces import PROPERTIES_INTERFACE
import telepathy.errors

from telepathy._generated.Properties_Interface import PropertiesInterface

class DBusProperties(dbus.service.Interface):
    def __init__(self):
        if not getattr(self, '_interfaces', None):
            self._interfaces = set()

        self._interfaces.add(dbus.PROPERTIES_IFACE)

        if not getattr(self, '_immutable_properties', None):
            self._immutable_properties = dict()

        if not getattr(self, '_prop_getters', None):
            self._prop_getters = {}
            self._prop_setters = {}

    def _implement_property_get(self, iface, dict):
        self._prop_getters.setdefault(iface, {}).update(dict)

    def _implement_property_set(self, iface, dict):
        self._prop_setters.setdefault(iface, {}).update(dict)

    def _add_immutable_properties(self, props):
        self._immutable_properties.update(props)

    def get_immutable_properties(self):
        props = dict()
        for prop, iface in list(self._immutable_properties.items()):
            props[iface + '.' + prop] = self._prop_getters[iface][prop]()
        return props

    @dbus.service.method(dbus_interface=dbus.PROPERTIES_IFACE, in_signature='ss', out_signature='v')
    def Get(self, interface_name, property_name):
        if interface_name in self._prop_getters \
            and property_name in self._prop_getters[interface_name]:
                return self._prop_getters[interface_name][property_name]()
        else:
            raise telepathy.errors.InvalidArgument()

    @dbus.service.method(dbus_interface=dbus.PROPERTIES_IFACE, in_signature='ssv', out_signature='')
    def Set(self, interface_name, property_name, value):
        if interface_name in self._prop_setters \
            and property_name in self._prop_setters[interface_name]:
                self._prop_setters[interface_name][property_name](value)
        else:
            raise telepathy.errors.PermissionDenied()

    @dbus.service.method(dbus_interface=dbus.PROPERTIES_IFACE, in_signature='s', out_signature='a{sv}')
    def GetAll(self, interface_name):
        if interface_name in self._prop_getters:
            r = {}
            for k, v in list(self._prop_getters[interface_name].items()):
                r[k] = v()
            return r
        else:
            raise telepathy.errors.InvalidArgument()
