# telepathy-python - Base classes defining the interfaces of the Telepathy framework
#
# Copyright (C) 2005,2006,2009,2010 Collabora Limited
# Copyright (C) 2005,2006 Nokia Corporation
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

from telepathy.constants import HANDLE_TYPE_NONE

class Handle(object):
    def __init__(self, id, handle_type, name):
        self._id = id
        self._type = handle_type
        self._name = name

    def get_id(self):
        return self._id

    def __hash__(self):
        return self._id.__hash__()

    def __int__(self):
        return int(self._id)

    def __long__(self):
        return int(self._id)

    def get_type(self):
        return self._type

    def get_name(self):
        return self._name

    def __eq__(self, other):
        return (int(self) == int(other) and self.get_type() == other.get_type())

    def __ne__(self, other):
        return not self.__eq__(other)

    id = property(get_id)
    type = property(get_type)
    name = property(get_name)


class NoneHandle(Handle):
    def __init__(self):
        Handle.__init__(self, 0, HANDLE_TYPE_NONE, '')
