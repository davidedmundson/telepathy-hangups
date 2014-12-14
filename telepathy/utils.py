# telepathy-python - Base classes defining the interfaces of the Telepathy framework
#
# Copyright (C) 2008 Collabora Limited
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

import os
import sys

def debug_divert_messages(filename):
    """debug_divert_messages:
    @filename: A file to which to divert stdout and stderr or None to do
    nothing.

    Open the given file for writing and duplicate its file descriptor to
    be used for stdout and stderr. This has the effect of closing the previous
    stdout and stderr, and sending all messages that would have gone there
    to the given file instead.

    By default the file is truncated and hence overwritten each time the
    process is executed.
    If the filename is prefixed with '+' then the file is not truncated and
    output is added at the end of the file.
    Passing None to this function is guaranteed to have no effect. This is
    so you can call it with the recommended usage
    debug_divert_messages (os.getenv('MYAPP_LOGFILE'))
    and it won't do anything if the environment variable is not set."""

    if filename is None:
        return

    try:
        if filename.startswith('+'):
            logfile = open(filename[1:], 'a')
        else:
            logfile = open(filename, 'w')
    except IOError as e:
        print("Can't open logfile '%s' : '%s'" % (filename, e))
        return

    sys.stdout = logfile
    sys.stderr = logfile
