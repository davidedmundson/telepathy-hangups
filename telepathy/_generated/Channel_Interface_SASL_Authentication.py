# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright © 2010 Collabora Limited 

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


class ChannelInterfaceSASLAuthentication(dbus.service.Interface):
    """\
      A channel interface for SASL authentication,
        as defined by
        RFC 4422.
        When this interface appears on a ServerAuthentication
        channel, it represents authentication with the server. In future,
        it could also be used to authenticate with secondary services,
        or even to authenticate end-to-end connections with contacts. As a result,
        this interface does not REQUIRE ServerAuthentication to allow for a potential future
        Channel.Type.PeerAuthentication interface.

      In any protocol that requires a password, the connection manager can
        use this channel to let a user interface carry out a simple SASL-like
        handshake with it, as a way to get the user's credentials
        interactively. This can be used to connect to protocols that may
        require a password, without requiring that the password is saved in
        the Account.Parameters.

      In some protocols, such as XMPP, authentication with the server
        is also carried out using SASL. In these protocols, a channel with this
        interface can provide a simple 1:1 mapping of the SASL negotiations
        taking place in the protocol, allowing more advanced clients to
        perform authentication via SASL mechanisms not known to the
        connection manager.

      
        By providing SASL directly when the protocol supports it, we can
          use mechanisms like Kerberos or Google's X-GOOGLE-TOKEN
          without specific support in the connection manager.
      

      For channels managed by a
        ChannelDispatcher,
        only the channel's Handler may call the
        methods on this interface. Other clients MAY observe the
        authentication process by watching its signals and properties.

      
        There can only be one Handler, which is a good fit for SASL's
          1-1 conversation between a client and a server.
      
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Channel.Interface.SASLAuthentication')

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.SASLAuthentication', in_signature='s', out_signature='')
    def StartMechanism(self, Mechanism):
        """
        Start an authentication try using Mechanism, without
          sending initial data (an "initial response" as defined in RFC
          4422).

        
          This method is appropriate for mechanisms where the client
            cannot send anything until it receives a challenge from the
            server, such as
            DIGEST-MD5
            in "initial authentication" mode.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.SASLAuthentication', in_signature='say', out_signature='')
    def StartMechanismWithData(self, Mechanism, Initial_Data):
        """
        Start an authentication try using Mechanism, and send
          Initial_Data as the "initial response" defined in
          RFC 4422
            §3.3.

        
          This method is appropriate for mechanisms where the client may
            send data first, such as PLAIN, or must send data
            first, such as
            DIGEST-MD5
            in "subsequent authentication" mode.

          Having two methods allows any mechanism where it makes a difference
            to distinguish between the absence of an initial response
            (StartMechanism) and a zero-byte
            initial response (StartMechanismWithData, with Initial_Data
            empty).
        

        If the HasInitialData
          property is false, this indicates that the underlying protocol
          does not make it possible to send initial data. In such protocols,
          this method may only be used for the X-TELEPATHY-
          pseudo-mechanisms (such as X-TELEPATHY-PASSWORD),
          and will fail if used with an ordinary SASL mechanism.

        
          For instance, the IRC SASL extension implemented in Charybdis and
            Atheme does not support initial data - the first message in the
            exchange only carries the mechanism. This is significant if using
            DIGEST-MD5,
            which cannot be used in the faster "subsequent authentication"
            mode on a protocol not supporting initial data.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.SASLAuthentication', in_signature='ay', out_signature='')
    def Respond(self, Response_Data):
        """
        Send a response to the the last challenge received via
          NewChallenge.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.SASLAuthentication', in_signature='', out_signature='')
    def AcceptSASL(self):
        """
        If the channel's status is SASL_Status_Server_Succeeded,
          this method confirms successful authentication and advances
          the status of the channel to SASL_Status_Succeeded.

        If the channel's status is SASL_Status_In_Progress, calling this
          method indicates that the last
          NewChallenge signal was in fact
          additional data sent after a successful SASL negotiation, and
          declares that from the client's point of view, authentication
          was successful. This advances the state of the channel to
          SASL_Status_Client_Accepted.

        In mechanisms where the server authenticates itself to the client,
          calling this method indicates that the client considers this to have
          been successful. In the case of ServerAuthentication
          channels, this means that the connection manager MAY continue to
          connect, and MAY advance the Connection.Status to Connected.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.SASLAuthentication', in_signature='us', out_signature='')
    def AbortSASL(self, Reason, Debug_Message):
        """
        Abort the current authentication try.

        If the current status is SASL_Status_Server_Failed or
          SASL_Status_Client_Failed, this method returns successfully, but has
          no further effect. If the current status is SASL_Status_Succeeded
          or SASL_Status_Client_Accepted then NotAvailable is raised.
          Otherwise, it changes the channel's state to
          SASL_Status_Client_Failed, with an appropriate error name and
          reason code.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.SASLAuthentication', signature='usa{sv}')
    def SASLStatusChanged(self, Status, Reason, Details):
        """
        Emitted when the status of the channel changes.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.SASLAuthentication', signature='ay')
    def NewChallenge(self, Challenge_Data):
        """
        Emitted when a new challenge is received from the server, or when
          a message indicating successful authentication and containing
          additional data is received from the server.

        When the channel's handler is ready to proceed, it should respond
          to the challenge by calling Respond,
          or respond to the additional data by calling
          AcceptSASL. Alternatively, it may call
          AbortSASL to abort authentication.
      
        """
        pass
  