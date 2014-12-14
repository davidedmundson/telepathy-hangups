# -*- coding: utf-8 -*-
    
"""Exception classes, generated from the Telepathy spec

Copyright © 2005-2010 Collabora Limited
Copyright © 2005-2009 Nokia Corporation


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
  
    The D-Bus errors used in Telepathy all start with
      org.freedesktop.Telepathy.Error.. They are used in
      D-Bus messages of type ERROR, and also as plain strings annotated with
      the DBus_Error_Name type.

    In principle, any method can raise any error (this is a general fact
      of IPC). For instance, generic D-Bus errors starting with
      org.freedesktop.DBus.Error. will occur in some
      situations.

    Telepathy methods can also raise implementation-specific errors to
      indicate specialized failure conditions. For better interoperability,
      if a suitable Telepathy error exists, it should be preferred.

    The namespace org.freedesktop.Telepathy.Qt4.Error.
      is reserved for use by the D-Bus client implementation in telepathy-qt4,
      which uses it to represent certain error situations that did not involve
      a D-Bus ERROR message. These errors are defined and documented as part of
      telepathy-qt4's C++ API, and should not be used on D-Bus.
  
"""

from dbus import DBusException

__all__ = (
"NetworkError",
"NotImplemented",
"InvalidArgument",
"NotAvailable",
"PermissionDenied",
"Disconnected",
"InvalidHandle",
"ChannelBanned",
"ChannelFull",
"ChannelInviteOnly",
"NotYours",
"Cancelled",
"AuthenticationFailed",
"EncryptionNotAvailable",
"EncryptionError",
"CertNotProvided",
"CertUntrusted",
"CertExpired",
"CertNotActivated",
"CertFingerprintMismatch",
"CertHostnameMismatch",
"CertSelfSigned",
"CertRevoked",
"CertInsecure",
"CertInvalid",
"CertLimitExceeded",
"NotCapable",
"Offline",
"ChannelKicked",
"Busy",
"NoAnswer",
"DoesNotExist",
"Terminated",
"ConnectionRefused",
"ConnectionFailed",
"ConnectionLost",
"AlreadyConnected",
"ConnectionReplaced",
"RegistrationExists",
"ServiceBusy",
"ResourceUnavailable",
"WouldBreakAnonymity",
"NotYet",
"Rejected",
"PickedUpElsewhere",
"ServiceConfused",
"Confused",
)


class NetworkError(DBusException):
    """\
    Raised when there is an error reading from or writing to the network.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.NetworkError'
  
class NotImplemented(DBusException):
    """\
    Raised when the requested method, channel, etc is not available on this connection.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.NotImplemented'
  
class InvalidArgument(DBusException):
    """\
    Raised when one of the provided arguments is invalid.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.InvalidArgument'
  
class NotAvailable(DBusException):
    """\
    Raised when the requested functionality is temporarily unavailable.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.NotAvailable'
  
class PermissionDenied(DBusException):
    """\
    The user is not permitted to perform the requested operation.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.PermissionDenied'
  
class Disconnected(DBusException):
    """\
      The connection is not currently connected and cannot be used.
      This error may also be raised when operations are performed on a
      Connection for which
      StatusChanged
      has signalled status Disconnected for reason None.

      
        The second usage corresponds to None in the
        Connection_Status_Reason enum; if a better reason
        is available, the corresponding error should be used instead.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Disconnected'
  
class InvalidHandle(DBusException):
    """\
    The handle specified is unknown on this channel or connection.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.InvalidHandle'
  
class ChannelBanned(DBusException):
    """\
    You are banned from the channel.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Channel.Banned'
  
class ChannelFull(DBusException):
    """\
    The channel is full.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Channel.Full'
  
class ChannelInviteOnly(DBusException):
    """\
    The requested channel is invite-only.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Channel.InviteOnly'
  
class NotYours(DBusException):
    """\
      The requested channel or other resource already exists, and another
        user interface in this session is responsible for it.

      User interfaces SHOULD handle this error unobtrusively, since it
        indicates that some other user interface is already processing the
        channel.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.NotYours'
  
class Cancelled(DBusException):
    """\
      Raised by an ongoing request if it is cancelled by user request before
      it has completed, or when operations are performed on an object which
      the user has asked to close (for instance, a Connection where the user
      has called Disconnect, or a Channel where the user has called Close).

      
        The second form can be used to correspond to the Requested member in
        the Connection_Status_Reason enum, or to
        to represent the situation where disconnecting a Connection,
        closing a Channel, etc. has been requested by the user but this
        request has not yet been acted on, for instance because the
        service will only act on the request when it has finished processing
        an event queue.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Cancelled'
  
class AuthenticationFailed(DBusException):
    """\
      Raised when authentication with a service was unsuccessful.
      
        This corresponds to Authentication_Failed in the
        Connection_Status_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.AuthenticationFailed'
  
class EncryptionNotAvailable(DBusException):
    """\
      Raised if a user request insisted that encryption should be used,
      but encryption was not actually available.

      
        This corresponds to part of Encryption_Error in the
        Connection_Status_Reason enum. It's been separated
        into a distinct error here because the two concepts that were part
        of EncryptionError seem to be things that could reasonably appear
        differently in the UI.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.EncryptionNotAvailable'
  
class EncryptionError(DBusException):
    """\
      Raised if encryption appears to be available, but could not actually be
      used (for instance if SSL/TLS negotiation fails).
      
        This corresponds to part of Encryption_Error in the
        Connection_Status_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.EncryptionError'
  
class CertNotProvided(DBusException):
    """\
      Raised if the server did not provide a SSL/TLS certificate. This error
      MUST NOT be used to represent the absence of a client certificate
      provided by the Telepathy connection manager.
      
        This corresponds to Cert_Not_Provided in the
        Connection_Status_Reason enum. That error
        explicitly applied only to server SSL certificates, so this one
        is similarly limited; having the CM present a client certificate
        is a possible future feature, but it should have its own error
        handling.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Cert.NotProvided'
  
class CertUntrusted(DBusException):
    """\
      Raised if the server provided a SSL/TLS certificate signed by an
      untrusted certifying authority. This error SHOULD NOT be used to
      represent a self-signed certificate: see the Self Signed error for that.
      
        This corresponds to Cert_Untrusted in the
        Connection_Status_Reason enum and to Untrusted in the
        TLS_Certificate_Reject_Reason enum, with a clarification
        to avoid ambiguity.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Cert.Untrusted'
  
class CertExpired(DBusException):
    """\
      Raised if the server provided an expired SSL/TLS certificate.
      
        This corresponds to Cert_Expired in the
        Connection_Status_Reason enum and to Expired in
        the TLS_Certificate_Reject_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Cert.Expired'
  
class CertNotActivated(DBusException):
    """\
      Raised if the server provided an SSL/TLS certificate that will become
      valid at some point in the future.
      
        This corresponds to Cert_Not_Activated in the
        Connection_Status_Reason enum and to
        Not_Activated in the TLS_Certificate_Reject_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Cert.NotActivated'
  
class CertFingerprintMismatch(DBusException):
    """\
      Raised if the server provided an SSL/TLS certificate that did not have
      the expected fingerprint.
      
        This corresponds to Cert_Fingerprint_Mismatch in the
        Connection_Status_Reason enum and to
        Fingerprint_Mismatch in the TLS_Certificate_Reject_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Cert.FingerprintMismatch'
  
class CertHostnameMismatch(DBusException):
    """\
      Raised if the server provided an SSL/TLS certificate that did not match
      its hostname.
      You MAY be able to get more details about the expected and certified
      hostnames by looking up the 'expected-hostname' and 'certificate-hostname'
      keys in the details map that came together with this error.
      
        This corresponds to Cert_Hostname_Mismatch in the
        Connection_Status_Reason enum and to Hostname_Mismatch
        in the TLS_Certificate_Reject_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Cert.HostnameMismatch'
  
class CertSelfSigned(DBusException):
    """\
      Raised if the server provided an SSL/TLS certificate that is self-signed
      and untrusted.
      
        This corresponds to Cert_Self_Signed in the
        Connection_Status_Reason enum and to Self_Signed
        in the TLS_Certificate_Reject_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Cert.SelfSigned'
  
class CertRevoked(DBusException):
    """\
      Raised if the server provided an SSL/TLS certificate that has been
      revoked.
      
        This corresponds to Cert_Revoked in the
        Connection_Status_Reason enum and to Revoked
        in the TLS_Certificate_Reject_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Cert.Revoked'
  
class CertInsecure(DBusException):
    """\
      Raised if the server provided an SSL/TLS certificate that uses an
      insecure cipher algorithm or is cryptographically weak.
      
        This corresponds to Cert_Insecure in the
        Connection_Status_Reason enum and to Insecure
        in the TLS_Certificate_Reject_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Cert.Insecure'
  
class CertInvalid(DBusException):
    """\
      Raised if the server provided an SSL/TLS certificate that is
      unacceptable in some way that does not have a more specific error.
      
        This corresponds to Cert_Other_Error in the
        Connection_Status_Reason enum and to Unknown
        in the TLS_Certificate_Reject_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Cert.Invalid'
  
class CertLimitExceeded(DBusException):
    """\
      Raised if the length in bytes of the server certificate, or the depth of the
      server certificate chain exceeds the limits imposed by the crypto
      library.
      
        This corresponds to Cert_Limit_Exceeded in the
        Connection_Status_Reason enum and to Limit_Exceeded
        in the TLS_Certificate_Reject_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Cert.LimitExceeded'
  
class NotCapable(DBusException):
    """\
    Raised when requested functionality is unavailable due to contact
    not having required capabilities.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.NotCapable'
  
class Offline(DBusException):
    """\
      Raised when requested functionality is unavailable because a contact is
      offline.

      
        This corresponds to Offline in the
        Channel_Group_Change_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Offline'
  
class ChannelKicked(DBusException):
    """\
      Used to represent a user being ejected from a channel by another user,
      for instance being kicked from a chatroom.

      
        This corresponds to Kicked in the
        Channel_Group_Change_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Channel.Kicked'
  
class Busy(DBusException):
    """\
      Used to represent a user being removed from a channel because of a
      "busy" indication. This error SHOULD NOT be used to represent a server
      or other infrastructure being too busy to process a request - for that,
      see ServerBusy.

      
        This corresponds to Busy in the
        Channel_Group_Change_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Busy'
  
class NoAnswer(DBusException):
    """\
      Used to represent a user being removed from a channel because they did
      not respond, e.g. to a StreamedMedia call.

      
        This corresponds to No_Answer in the
        Channel_Group_Change_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.NoAnswer'
  
class DoesNotExist(DBusException):
    """\
      Raised when the requested user does not, in fact, exist.

      
        This corresponds to Invalid_Contact in the
        Channel_Group_Change_Reason enum, but can also be
        used to represent other things not existing (like chatrooms, perhaps).
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.DoesNotExist'
  
class Terminated(DBusException):
    """\
      Raised when a channel is terminated for an unspecified reason. In
      particular, this error SHOULD be used whenever normal termination of
      a 1-1 StreamedMedia call by the remote user is represented as a D-Bus
      error name.

      
        This corresponds to None in the
        Channel_Group_Change_Reason enum.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Terminated'
  
class ConnectionRefused(DBusException):
    """\
      Raised when a connection is refused.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.ConnectionRefused'
  
class ConnectionFailed(DBusException):
    """\
      Raised when a connection can't be established.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.ConnectionFailed'
  
class ConnectionLost(DBusException):
    """\
      Raised when a connection is broken.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.ConnectionLost'
  
class AlreadyConnected(DBusException):
    """\
      Raised when the user attempts to connect to an account but they are
      already connected (perhaps from another client or computer), and the
      protocol or account settings do not allow this.

      
        XMPP can have this behaviour if the user chooses the same resource
        in both clients (it is server-dependent whether the result is
        AlreadyConnected on the new connection, ConnectionReplaced on the
        old connection, or two successful connections).
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.AlreadyConnected'
  
class ConnectionReplaced(DBusException):
    """\
      Raised by an existing connection to an account if it is replaced by
      a new connection (perhaps from another client or computer).

      
        In MSNP, when connecting twice with the same Passport, the new
        connection "wins" and the old one is automatically disconnected.
        XMPP can also have this behaviour if the user chooses the same
        resource in two clients (it is server-dependent whether the result is
        AlreadyConnected on the new connection, ConnectionReplaced on the
        old connection, or two successful connections).
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.ConnectionReplaced'
  
class RegistrationExists(DBusException):
    """\
      Raised during in-band registration if the server indicates that the
      requested account already exists.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.RegistrationExists'
  
class ServiceBusy(DBusException):
    """\
      Raised if a server or some other piece of infrastructure cannot process
      the request, e.g. due to resource limitations. Clients MAY try again
      later.

      
        This is not the same error as Busy, which indicates that a
        user is busy.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.ServiceBusy'
  
class ResourceUnavailable(DBusException):
    """\
      Raised if a request cannot be satisfied because a process local to the
      user has insufficient resources. Clients MAY try again
      later.

      
        For instance, the ChannelDispatcher
        might raise this error for some or all channel requests if it has
        detected that there is not enough free memory.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.ResourceUnavailable'
  
class WouldBreakAnonymity(DBusException):
    """\
      Raised if a request cannot be satisfied without violating an earlier
      request for anonymity, and the earlier request specified that raising
      an error is preferable to disclosing the user's identity (for instance
      via Connection.Interface.Anonymity.AnonymityMandatory or
      Channel.Interface.Anonymity.AnonymityMandatory).
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.WouldBreakAnonymity'
  
class NotYet(DBusException):
    """\
      Raised when the requested functionality is not yet available, but is
      likely to become available after some time has passed.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.NotYet'
  
class Rejected(DBusException):
    """\
      Raised when an incoming or outgoing Call.DRAFT is
      rejected by the the receiver.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Rejected'
  
class PickedUpElsewhere(DBusException):
    """\
      Raised when a call was terminated as a result of the local user
      picking up the call on a different resource.
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.PickedUpElsewhere'
  
class ServiceConfused(DBusException):
    """\
      Raised when a server or other piece of infrastructure indicates an
      internal error, or when a message that makes no sense is received from
      a server or other piece of infrastructure.

      
        For instance, this is appropriate for XMPP's
        internal-server-error, and is also appropriate if
        you receive sufficiently inconsistent information from a server that
        you cannot continue.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.ServiceConfused'
  
class Confused(DBusException):
    """\
      Raised if a server rejects protocol messages from a connection manager
      claiming that they do not make sense, two local processes fail to
      understand each other, or an apparently impossible situation is
      reached.

      
        For instance, this would be an appropriate mapping for XMPP's
        errors bad-format, invalid-xml, etc., which can't happen unless
        the local (or remote) XMPP implementation is faulty. This is
        also analogous to
        Media_Stream_Error_Invalid_CM_Behavior,
        TP_DBUS_ERROR_INCONSISTENT in telepathy-glib, and
        TELEPATHY_QT4_ERROR_INCONSISTENT in telepathy-qt4.
      
    
    """
    _dbus_error_name = 'org.freedesktop.Telepathy.Error.Confused'
  