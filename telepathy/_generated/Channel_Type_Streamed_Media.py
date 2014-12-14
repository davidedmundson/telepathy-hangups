# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright © 2005-2009 Collabora Limited 
 Copyright © 2005-2009 Nokia Corporation 
 Copyright © 2006 INdT 

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


class ChannelTypeStreamedMedia(dbus.service.Interface):
    """\
      A channel that can send and receive streamed media such as audio or
        video.  Provides a number of methods for listing and requesting new
        streams, and signals to indicate when streams have been added, removed
        and changed status. The state of the call (ringing remotely, ringing
        locally, answered, missed, etc.) are represented using the properties
        and signals of the Group interface.

      In general this should be used in conjunction with the MediaSignalling
        interface to exchange connection candidates and codec choices with
        whichever component is responsible for the streams. However, in certain
        applications where no candidate exchange is necessary (eg the streams
        are handled by specialised hardware which is controlled directly by the
        connection manager), the signalling interface can be omitted and this
        channel type used simply to control the streams.

      Outgoing calls

      To make an audio-only call to a contact foo@example.com,
        clients should call:

      
        
CreateChannel({
  ChannelType: StreamedMedia,
  TargetHandleType: Contact,
  TargetID: 'foo@example.com',
  InitialAudio: True,
)

      As always, TargetHandle
        may be used in place of TargetID if the contact's handle is already
        known. To make an audio-and-video call, the client should also specify
        InitialVideo.  The connection manager
        SHOULD return a channel whose immutable properties contain the local
        user as the InitiatorHandle,
        the remote contact as the TargetHandle,
        Requested = True
        (indicating that the call is outgoing); the Group interface should
        initially have the local user in Members and the remote
        contact in RemotePendingMembers, to
        indicate that we are awaiting their response.

      The contact answering the call is represented by the CM signalling
        MembersChanged,
        moving the remote contact to Members, with the remote contact as the
        Actor and Reason None. The contact
        rejecting the call is represented by both contacts being removed from
        the group, with the remote contact as the Actor and
        Reason set appropriately. The local user may hang up at any
        time by calling
        RemoveMembersWithReason
        to remove themself, with an appropriate reason; the CM SHOULD relay the
        reason to the remote contact, and emit MembersChanged removing both
        contacts from the group with the self handle as the Actor.

      (In the past, several other patterns have been used to place outgoing
        calls; see
        'Requesting StreamedMedia Channels' on the Telepathy wiki
        for the details.)

      Incoming calls

      Incoming calls' immutable properties should contain TargetHandleType
        = Contact, both TargetHandle and
        InitiatorHandle
        set to the remote contact, Requested = False
        (indicating that this is an incoming call), and appropriate values of
        InitialAudio and
        InitialVideo; the Group interface should
        initially have the local user in LocalPendingMembers
        and the remote contact in Members,
        indicating that the contact is awaiting our response.

      To accept the call, use AddMembers
        to move the local user to the group's members. To reject the call, use
        RemoveMembersWithReason
        to remove the local member from the group, with an appropriate reason.
        If the remote user ends the call before it is answered, this is
        represented by MembersChanged
        removing both parties from the group with the remote contact as the
        Actor, and Reason set appropriately.

      Note that the call may end with the self handle as the
        Actor without the user having chosen to reject the call, as
        indicated by the nature of the Reason. Specifically, some
        local component may time out the call (indicating this with reason
        No_Answer; for example, the CM may have forwarded the call
        to another number, as configured using Forwarding.DRAFT),
        or something may have gone wrong with the call
        (indicated by reason Error). Such calls SHOULD be
        considered missed, just as if the remote contact had hung up before the
        local user answered the call.

      
        This is a bit awkward, but these are the best ways we can represent
          these situations. It's important to document which calls should be
          considered missed, to ensure that the user can be notified.
      

      When the local user accepts an incoming call, the connection manager
        SHOULD change the direction of any streams with pending local send
        to be sending, without altering whether those streams are
        receiving.

      
        This matches existing practice, and means that a client
          can answer incoming calls and get an unmuted microphone/activated
          webcam without having to take additional action to accept the
          stream directions.

        It does, however, introduce a race condition: a client believing
          that it is accepting an audio-only call by calling AddMembers
          can inadvertantly accept an audio + video call (and hence activate
          sending from a webcam without the user's permission) if a video
          stream is added just before AddMembers is processed. This race
          should be removed when this specification is revised.
      

    During a call

    If ImmutableStreams is
      False, new streams may be requested using
      RequestStreams (to add video to an
      audio-only call, for instance), and existing streams may be removed using
      RemoveStreams (for example, to downgrade
      an audio-video call to audio-only). The call may be ended by calling
      RemoveMembers
      or RemoveMembersWithReason; the call ending is signalled by the CM emitting MembersChanged,
      removing both parties from the group.

    Handler filters

    For historical reasons, handlers must specify more than one filter if
      they want to correctly advertise support for audio and/or video calls. If
      they can handle channels using the MediaSignalling
      interface, they should also advertise various
      Handler_Capability_Tokens to indicate which codecs and
      transports they support. See InitialAudio
      and MediaSignalling/video/h264
      for the gory details. In summary:

    
      To advertise support for streamed media in general, include the
        following filter in HandlerChannelFilter:
      
{ '...Channel.ChannelType': '...Channel.Type.StreamedMedia' ,
  '...Channel.TargetHandleType': Contact,
}

      To advertise support for audio calls, also include the following
        filter:
      
{ '...Channel.ChannelType': '...Channel.Type.StreamedMedia' ,
  '...Channel.TargetHandleType': Contact,
  '...Channel.Type.StreamedMedia.InitialAudio': True,
}

      To advertise support for video calls, also include the following
        filter:
      
{ '...Channel.ChannelType': '...Channel.Type.StreamedMedia' ,
  '...Channel.TargetHandleType': Contact,
  '...Channel.Type.StreamedMedia.InitialVideo': True,
}

      If you use telepathy-farsight, and have H.264 support, you probably
        want these Capabilities:
      
[ "org.freedesktop.Telepathy.Channel.Interface.MediaSignalling/ice-udp",
  "org.freedesktop.Telepathy.Channel.Interface.MediaSignalling/gtalk-p2p",
  "org.freedesktop.Telepathy.Channel.Interface.MediaSignalling/video/h264",
]
    
    """

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.StreamedMedia', in_signature='', out_signature='a(uuuuuu)')
    def ListStreams(self):
        """
        Returns an array of structs representing the streams currently active
        within this channel. Each stream is identified by an unsigned integer
        which is unique for each stream within the channel.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.StreamedMedia', in_signature='au', out_signature='')
    def RemoveStreams(self, Streams):
        """
        Request that the given streams are removed. If all streams are
          removed, the channel MAY close.

        Clients SHOULD NOT attempt to terminate calls by removing all the
          streams; instead, clients SHOULD terminate calls by removing the
          Group.SelfHandle
          from the channel, using either
          RemoveMembers
          or
          RemoveMembersWithReason.
          
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.StreamedMedia', in_signature='uu', out_signature='')
    def RequestStreamDirection(self, Stream_ID, Stream_Direction):
        """
        Request a change in the direction of an existing stream. In particular,
        this might be useful to stop sending media of a particular type,
        or inform the peer that you are no longer using media that is being
        sent to you.

        Depending on the protocol, streams which are no longer sending in
        either direction should be removed and a
        StreamRemoved signal emitted.
        Some direction changes can be enforced locally (for example,
        BIDIRECTIONAL -> RECEIVE can be achieved by merely stopping sending),
        others may not be possible on some protocols, and some need agreement
        from the remote end. In this case, the MEDIA_STREAM_PENDING_REMOTE_SEND
        flag will be set in the
        StreamDirectionChanged signal, and the
        signal
        emitted again without the flag to indicate the resulting direction when
        the remote end has accepted or rejected the change.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.StreamedMedia', in_signature='uau', out_signature='a(uuuuuu)')
    def RequestStreams(self, Contact_Handle, Types):
        """
        Request that streams be established to exchange the given types of
        media with the given member. In general this will try and establish a
        bidirectional stream, but on some protocols it may not be possible to
        indicate to the peer that you would like to receive media, so a
        send-only stream will be created initially. In the cases where the
        stream requires remote agreement (eg you wish to receive media from
        them), the StreamDirectionChanged signal
        will be emitted with the
        MEDIA_STREAM_PENDING_REMOTE_SEND flag set, and the signal emitted again
        with the flag cleared when the remote end has replied.

        If streams of the requested types already exist, calling this
          method results in the creation of additional streams. Accordingly,
          clients wishing to have exactly one audio stream or exactly one
          video stream SHOULD check for the current streams using
          ListStreams before calling this
          method.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.StreamedMedia', signature='uuu')
    def StreamAdded(self, Stream_ID, Contact_Handle, Stream_Type):
        """
        Emitted when a new stream has been added to this channel.
          Clients SHOULD assume that the stream's
          Media_Stream_State is initially Disconnected.

        If a connection manager needs to represent the addition of a stream
          whose state is already Connecting or Connected, it MUST do this
          by emitting StreamAdded, closely followed by
          StreamStateChanged indicating a
          change to the appropriate state.

        
          Historically, it was not clear from the StreamAdded signal what
            the state of the stream was. telepathy-spec 0.17.22
            clarified this.
        

        Similarly, clients SHOULD assume that the initial
          Media_Stream_Direction of a newly added stream
          is Receive, and that the initial
          Media_Stream_Pending_Send is
          Pending_Local_Send.

        If a connection manager needs to represent the addition of a stream
          whose direction or pending-send differs from those initial values,
          it MUST do so by emitting StreamAdded, closely followed by
          StreamDirectionChanged indicating a
          change to the appropriate direction and pending-send state.

        
          StreamAdded doesn't itself indicate the stream's direction; this
            is unfortunate, but is preserved for compatibility.

          This is the appropriate direction for streams added by a remote
            contact on existing connection managers, and does not violate
            user privacy by automatically sending audio or video (audio streams
            start off muted, video streams start off not sending). For
            streams added by the local user using the client receiving the
            signal, the true direction can also be determined from the return
            value of the RequestStreams
            method.

          Existing clients typically operate by maintaining a separate
            idea of the directions that they would like the streams to have,
            and enforcing these intended directions by calling
            RequestStreamDirection whenever
            needed.
        
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.StreamedMedia', signature='uuu')
    def StreamDirectionChanged(self, Stream_ID, Stream_Direction, Pending_Flags):
        """
        Emitted when the direction or pending flags of a stream are
          changed.

        If the MEDIA_STREAM_PENDING_LOCAL_SEND flag is set, the remote user
          has requested that we begin sending on this stream.
          RequestStreamDirection
          should be called to indicate whether or not this change is
          acceptable.

        
          This allows for a MSN-style user interface, "Fred has asked you
            to enable your webcam. (Accept | Reject)", if desired.
        
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.StreamedMedia', signature='uus')
    def StreamError(self, Stream_ID, Error_Code, Message):
        """
        Emitted when a stream encounters an error.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.StreamedMedia', signature='u')
    def StreamRemoved(self, Stream_ID):
        """
        Emitted when a stream has been removed from this channel.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.StreamedMedia', signature='uu')
    def StreamStateChanged(self, Stream_ID, Stream_State):
        """
        Emitted when a member's stream's state changes.
      
        """
        pass
  