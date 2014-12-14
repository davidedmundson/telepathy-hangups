# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""
    Copyright © 2008-2009 Collabora Limited
  

    This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Library General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
  
"""

import dbus.service


class ChannelTypeFileTransfer(dbus.service.Interface):
    """\
      A channel type for transferring files. The
      transmission of data between contacts is achieved by reading from
      or writing to a socket. The type of the socket (local Unix, IPv4,
      etc.) is decided on when the file transfer is offered or accepted.

      A socket approach is used to make the transfer less dependent on both
      client and connection manager knowing the same protocols. As an example,
      when browsing an SMB share in a file manager, one selects "Send file"
      and chooses a contact. Instead of passing a URL which would then require
      the connection manager to connect to the SMB share itself, the client
      passes a stream from which the connection manager reads, requiring no
      further connection to the share. It also allows connection managers to
      be more restricted in their access to the system, allowing tighter
      security policies with eg SELinux, or more flexible deployments which
      cross user or system boundaries.

      The Telepathy client should connect to the socket or address that
      the connection manager has set up and provided back to the clients
      through the two methods.

      In order to send a file, one should request a FileTransfer
      channel for a contact, including at least the mandatory properties
      (Filename,
      Size and ContentType).
      Then, one should
      call ProvideFile to configure the socket that
      will be used to transfer the file.

      In order to receive an incoming file transfer, one should call
      AcceptFile and then wait until the state
      changes to Open. When the receiver wants to resume a transfer, the Offset
      argument should be should be set to a non-zero value when calling
      AcceptFile.

    Once the offset has been negotiated, the
      InitialOffsetDefined signal
      is emitted and the InitialOffset property
      is defined. The InitialOffsetDefined
      signal is emitted before channel becomes Open.
      The receiver MUST check the value of
      InitialOffset for a difference in offset
      from the requested value in AcceptFile.

      When the state changes to Open, Clients can start the transfer of the
      file using the offset previously announced.
      

      If something goes wrong with the transfer,
      Channel.Close
      should be called on the channel.

      The File channel type may be requested for handles of type
      HANDLE_TYPE_CONTACT. If the channel is requested for any other
      handle type then the behaviour is undefined.

      Connection managers SHOULD NOT advertise support for file transfer to
        other contacts unless it has been indicated by a call to
        UpdateCapabilities.
      
      
        People would send us files, and it would always fail. That would be silly.
      
    """

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.FileTransfer', in_signature='uuvt', out_signature='v')
    def AcceptFile(self, Address_Type, Access_Control, Access_Control_Param, Offset):
        """
        Accept a file transfer that's in the Pending state. The file
        transfer's state becomes Accepted after this method is called.
        At this point the client can connect to the socket. CM MUST emit
        InitialOffsetDefined and change
        the state to Open before writing to the socket.
        Then InitialOffset should be respected in case
        its value differs from the offset that was specified as an argument
        to AcceptFile.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.FileTransfer', in_signature='uuv', out_signature='v')
    def ProvideFile(self, Address_Type, Access_Control, Access_Control_Param):
        """
        Provide the file for an outgoing file transfer which has been offered.
        Opens a socket that the client can use to provide a file to the connection manager.
        The channel MUST have been requested, and will change state
        to Open when this method is called if its state was Accepted.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.FileTransfer', signature='uu')
    def FileTransferStateChanged(self, State, Reason):
        """
        Emitted when the state of a file transfer changes.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.FileTransfer', signature='t')
    def TransferredBytesChanged(self, Count):
        """
        Emitted when the number of transferred bytes changes. This will not be
        signalled with every single byte change. Instead, the most frequent
        this signal will be emitted is once a second. This should be
        sufficient, and the TransferredBytes
        property SHOULD NOT be polled.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.FileTransfer', signature='t')
    def InitialOffsetDefined(self, InitialOffset):
        """
        Emitted when the value of the InitialOffset
        property has been negotiated. This signal MUST be emitted before the channel
        becomes Open and clients have to use this offset when transferring the
        file.
      
        """
        pass
  