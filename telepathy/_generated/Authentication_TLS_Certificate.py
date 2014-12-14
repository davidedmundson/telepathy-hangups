# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2010 Collabora Limited

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


class AuthenticationTLSCertificate(dbus.service.Object):
    """\
      This object represents a TLS certificate.
    """

    @dbus.service.method('org.freedesktop.Telepathy.Authentication.TLSCertificate', in_signature='', out_signature='')
    def Accept(self):
        """
        Accepts this certificate, i.e. marks it as verified.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Authentication.TLSCertificate', in_signature='a(usa{sv})', out_signature='')
    def Reject(self, Rejections):
        """
        Rejects this certificate.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Authentication.TLSCertificate', signature='')
    def Accepted(self):
        """
        The State of this certificate has changed to Accepted.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Authentication.TLSCertificate', signature='a(usa{sv})')
    def Rejected(self, Rejections):
        """
        The State of this certificate has changed to Rejected.
      
        """
        pass
  