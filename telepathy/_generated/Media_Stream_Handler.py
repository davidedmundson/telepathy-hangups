# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright (C) 2005-2008 Collabora Limited 
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


class MediaStreamHandler(dbus.service.Object):
    """\
    Handles signalling the information pertaining to a specific media stream.
    A client should provide information to this handler as and when it is
    available.
    """

    @dbus.service.method('org.freedesktop.Telepathy.Media.StreamHandler', in_signature='u', out_signature='')
    def CodecChoice(self, Codec_ID):
        """
        Inform the connection manager of codec used to receive data.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Media.StreamHandler', in_signature='us', out_signature='')
    def Error(self, Error_Code, Message):
        """
        Inform the connection manager that an error occured in this stream. The
        connection manager should emit the StreamError signal for the stream on
        the relevant channel, and remove the stream from the session.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Media.StreamHandler', in_signature='', out_signature='')
    def NativeCandidatesPrepared(self):
        """
        Informs the connection manager that all possible native candisates
        have been discovered for the moment.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Media.StreamHandler', in_signature='ss', out_signature='')
    def NewActiveCandidatePair(self, Native_Candidate_ID, Remote_Candidate_ID):
        """
        Informs the connection manager that a valid candidate pair
        has been discovered and streaming is in progress.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Media.StreamHandler', in_signature='s(usuussduss)s(usuussduss)', out_signature='')
    def NewActiveTransportPair(self, Native_Candidate_ID, Native_Transport, Remote_Candidate_ID, Remote_Transport):
        """
        Informs the connection manager that a valid transport pair
          has been discovered and streaming is in progress. Component
          id MUST be the same for both transports and the pair is
          only valid for that component.

        
          The connection manager might need to send the details of
            the active transport pair (e.g. c and o parameters of SDP
            body need to contain address of selected native RTP transport
            as stipulated by RFC 5245). However, the candidate ID might
            not be enough to determine these info if the transport was
            found after NativeCandidatesPrepared
            has been called (e.g. peer reflexive ICE candidate). 
        

        This method must be called before
          NewActiveCandidatePair.

        
          This way, connection managers supporting this method can
            safely ignore subsequent
            NewActiveCandidatePair call.
        

        Connection managers SHOULD NOT implement this method unless
          they need to inform the peer about selected transports. As a
          result, streaming implementations MUST NOT treat errors raised
          by this method as fatal.

        
          Usually, connection managers only need to do one answer/offer
            round-trip. However, some protocols give the possibility to
            to send an updated offer (e.g. ICE defines such mechanism to
            avoid some race conditions and to properly set the state of
            gateway devices).
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Media.StreamHandler', in_signature='sa(usuussduss)', out_signature='')
    def NewNativeCandidate(self, Candidate_ID, Transports):
        """
        Inform this MediaStreamHandler that a new native transport candidate
        has been ascertained.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Media.StreamHandler', in_signature='a(usuuua{ss})', out_signature='')
    def Ready(self, Codecs):
        """
        Inform the connection manager that a client is ready to handle
        this StreamHandler. Also provide it with info about all supported
        codecs.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Media.StreamHandler', in_signature='a(usuuua{ss})', out_signature='')
    def SetLocalCodecs(self, Codecs):
        """
        Used to provide codecs after Ready(), so the media client can go
          ready for an incoming call and exchange candidates/codecs before
          knowing what local codecs are available.

        This is useful for gatewaying calls between two connection managers.
          Given an incoming call, you need to call
          Ready to get the remote codecs before
          you can use them as the "local" codecs to place the outgoing call,
          and hence receive the outgoing call's remote codecs to use as the
          incoming call's "local" codecs.

        In this situation, you would pass an empty list of codecs to the
          incoming call's Ready method, then later call SetLocalCodecs on the
          incoming call in order to respond to the offer.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Media.StreamHandler', in_signature='u', out_signature='')
    def StreamState(self, State):
        """
        Informs the connection manager of the stream's current state, as
        as specified in Channel.Type.StreamedMedia::ListStreams.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Media.StreamHandler', in_signature='a(usuuua{ss})', out_signature='')
    def SupportedCodecs(self, Codecs):
        """
        Inform the connection manager of the supported codecs for this session.
        This is called after the connection manager has emitted SetRemoteCodecs
        to notify what codecs are supported by the peer, and will thus be an
        intersection of all locally supported codecs (passed to Ready)
        and those supported by the peer.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Media.StreamHandler', in_signature='a(usuuua{ss})', out_signature='')
    def CodecsUpdated(self, Codecs):
        """
        Inform the connection manager that the parameters of the supported
        codecs for this session have changed. The connection manager should
        send the new parameters to the remote contact.

        
          This is required for H.264 and Theora, for example.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Media.StreamHandler', in_signature='b', out_signature='')
    def HoldState(self, Held):
        """
        Notify the connection manager that the stream's hold state has
        been changed successfully in response to SetStreamHeld.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Media.StreamHandler', in_signature='', out_signature='')
    def UnholdFailure(self):
        """
        Notify the connection manager that an attempt to reacquire the
        necessary hardware or software resources to unhold the stream,
        in response to SetStreamHeld, has failed.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Media.StreamHandler', signature='sa(usuussduss)')
    def AddRemoteCandidate(self, Candidate_ID, Transports):
        """
        Signal emitted when the connection manager wishes to inform the
        client of a new remote candidate.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Media.StreamHandler', signature='')
    def Close(self):
        """
        Signal emitted when the connection manager wishes the stream to be
        closed.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Media.StreamHandler', signature='s')
    def RemoveRemoteCandidate(self, Candidate_ID):
        """
        Signal emitted when the connection manager wishes to inform the
        client that the remote end has removed a previously usable
        candidate.

        
          It seemed like a good idea at the time, but wasn't.
        
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Media.StreamHandler', signature='ss')
    def SetActiveCandidatePair(self, Native_Candidate_ID, Remote_Candidate_ID):
        """
        Emitted by the connection manager to inform the client that a
        valid candidate pair has been discovered by the remote end
        and streaming is in progress.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Media.StreamHandler', signature='a(sa(usuussduss))')
    def SetRemoteCandidateList(self, Remote_Candidates):
        """
        Signal emitted when the connection manager wishes to inform the
        client of all the available remote candidates at once.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Media.StreamHandler', signature='a(usuuua{ss})')
    def SetRemoteCodecs(self, Codecs):
        """
        Signal emitted when the connection manager wishes to inform the
        client of the codecs supported by the remote end.
	If these codecs are compatible with the remote codecs, then the client
        must call SupportedCodecs,
        otherwise call Error.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Media.StreamHandler', signature='b')
    def SetStreamPlaying(self, Playing):
        """
        If emitted with argument TRUE, this means that the connection manager
        wishes to set the stream playing; this means that the streaming
        implementation should expect to receive data. If emitted with argument
        FALSE this signal is basically meaningless and should be ignored.

        
          We're very sorry.
        
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Media.StreamHandler', signature='b')
    def SetStreamSending(self, Sending):
        """
        Signal emitted when the connection manager wishes to set whether or not
        the stream sends to the remote end.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Media.StreamHandler', signature='y')
    def StartTelephonyEvent(self, Event):
        """
        Request that a telephony event (as defined by RFC 4733) is transmitted
        over this stream until StopTelephonyEvent is called.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Media.StreamHandler', signature='yu')
    def StartNamedTelephonyEvent(self, Event, Codec_ID):
        """
        Request that a telephony event (as defined by RFC 4733) is transmitted
        over this stream until StopTelephonyEvent is called. This differs from
        StartTelephonyEvent in that you force the event to be transmitted
	as a RFC 4733 named event, not as sound. You can also force a specific
	Codec ID.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Media.StreamHandler', signature='y')
    def StartSoundTelephonyEvent(self, Event):
        """
        Request that a telephony event (as defined by RFC 4733) is transmitted
        over this stream until StopTelephonyEvent is called. This differs from
        StartTelephonyEvent in that you force the event to be transmitted
	as sound instead of as a named event.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Media.StreamHandler', signature='')
    def StopTelephonyEvent(self):
        """
        Request that any ongoing telephony events (as defined by RFC 4733)
        being transmitted over this stream are stopped.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Media.StreamHandler', signature='b')
    def SetStreamHeld(self, Held):
        """
        Emitted when the connection manager wishes to place the stream on
          hold (so the streaming client should free hardware or software
          resources) or take the stream off hold (so the streaming client
          should reacquire the necessary resources).

        When placing a channel's streams on hold, the connection manager
          SHOULD notify the remote contact that this will be done (if
          appropriate in the protocol) before it emits this signal.

        
          It is assumed that relinquishing a resource will not fail.
            If it does, the call is probably doomed anyway.
        

        When unholding a channel's streams, the connection manager
          SHOULD emit this signal and wait for success to be indicated
          via HoldState before it notifies the remote contact that the
          channel has been taken off hold.

        
          This means that if a resource is unavailable, the remote
            contact will never even be told that we tried to acquire it.
        
      
        """
        pass
  