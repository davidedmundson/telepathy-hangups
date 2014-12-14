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
      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
      02110-1301, USA.
  
"""

import dbus.service


class Client(dbus.service.Object):
    """\
      Telepathy clients use connection managers, the channel dispatcher
        and optionally the account manager to provide useful
        functionality.

      User interface processes are the obvious example of Telepathy
        clients, but they can provide other functionality, such as
        address-book synchronization.

      Every running or activatable process with a well-known
        name of the form org.freedesktop.Telepathy.Client.clientname
        should be probed by the channel dispatcher to discover its
        capabilities. Each client is either an observer, an
        approver, a channel handler, or some combination
        of these.

      
        Activatable services (those with a D-Bus .service
          file) must be supported so that we can run clients
          in response to channel creation.

        Non-activatable services (those that do not register a D-Bus
          .service file for their well-known name, but do
          request it at runtime) must be supported so that we can have
          programs that process channels, but only if they are already
          running - for instance, a full-screen media centre
          application might do this.
      

      The client name, clientname, MUST be a non-empty string of
        ASCII digits, letters, dots and/or underscores, starting with a
        letter, and without sets of two consecutive dots or a dot
        followed by a digit. For non-activatable services, it MAY contain a
        part that is generated per instance at runtime.

      
        If each of a client Foo's instances should be able to manipulate
          channels separately, the instance with unique name
          :1.25 might request a well-known name like
          org.freedesktop.Telepathy.Client.Foo._1._25.

        (Note that well-known bus-name components may not start with a
          digit, so o.f.T.Client.Foo.1.25 would not be acceptable.)
      

      Each Client MUST export an object whose object path may be
        determined by replacing '.' with '/' in the well-known name and
        prepending '/'. This object represents its API as a Telepathy
        client; the channel dispatcher will call its methods and read
        its properties when appropriate.

      As an optimization, activatable clients SHOULD install a file
        $XDG_DATA_DIRS/telepathy/clients/clientname.client
        containing a cached version of its immutable properties,
        so that for most clients, the channel dispatcher can
        just read a file to discover capabilities, instead of
        having to service-activate the client immediately in order to fetch
        its read-only properties. However, the D-Bus API is canonical, and
        the channel dispatcher MUST support clients without such a file.

      Non-activatable clients MAY install a .client file,
        but there's not much point in them doing so.

      The .client files MUST contain UTF-8 text with the same syntax
        as
        Desktop
          Entry files (although the allowed groups, keys and values differ).
        Every .client file MUST contain a group whose name is
        the name of this interface.

      The groups, keys and values in the .client file are
        defined by individual interfaces. Each interface that can usefully
        cache information in the .client file SHOULD correspond
        to a group with the same name.
    """
