# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
"""Copyright © 2005-2010 Collabora Limited
Copyright © 2005-2010 Nokia Corporation
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


class ChannelInterfaceDTMF(dbus.service.Interface):
    """\
      An interface that gives a Channel the ability to send DTMF events over
      audio streams which have been established using the StreamedMedia channel
      type. The event codes used are in common with those defined in RFC4733, and are
      listed in the DTMF_Event enumeration.
    """

    def __init__(self):
        self._interfaces.add('org.freedesktop.Telepathy.Channel.Interface.DTMF')

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.DTMF', in_signature='uy', out_signature='')
    def StartTone(self, Stream_ID, Event):
        """
        Start sending a DTMF tone to all eligible streams in the channel.
          Where possible, the tone will continue until
          StopTone is called. On certain protocols,
          it may only be possible to send events with a predetermined length. In
          this case, the implementation MAY emit a fixed-length tone, and the
          StopTone method call SHOULD return NotAvailable.
          
            The client may wish to control the exact duration and timing of the
            tones sent as a result of user's interaction with the dialpad, thus
            starting and stopping the tone sending explicitly.
          

        Tone overlaping or queueing is not supported, so this method can only
          be called if no DTMF tones are already being played.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.DTMF', in_signature='u', out_signature='')
    def StopTone(self, Stream_ID):
        """
        Stop sending any DTMF tones which have been started using the
        StartTone or
        MultipleTones methods.
        If there is no current tone, this method will do nothing.
        If MultipleTones was used, the client should not assume the
        sending has stopped immediately; instead, the client should wait
        for the StoppedTones signal.
        
          On some protocols it might be impossible to cancel queued tones
          immediately.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Interface.DTMF', in_signature='s', out_signature='')
    def MultipleTones(self, Tones):
        """
        Send multiple DTMF events to all eligible streams in the channel.
        Each tone will be played for an implementation-defined number of
        milliseconds (typically 250ms), followed by a gap before the next tone
        is played (typically 100ms). The
        duration and gap are defined by the protocol or connection manager.

        
          In cases where the client knows in advance the tone sequence it
            wants to send, it's easier to use this method than manually start
            and stop each tone in the sequence.

          The tone and gap lengths may need to vary for interoperability,
            according to the protocol and other implementations' ability to
            recognise tones. At the time of writing, GStreamer uses a
            minimum of 250ms tones and 100ms gaps when playing in-band DTMF
            in the normal audio stream, or 70ms tones and 50ms gaps when
            encoding DTMF as audio/telephone-event.
        

        Tone overlaping or queueing is not supported, so this method can only
          be called if no DTMF tones are already being played.
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.DTMF', signature='s')
    def TonesDeferred(self, Tones):
        """
        Emitted when 'w' or 'W', indicating "wait for the user to continue",
          is encountered while playing a DTMF string queued by
          MultipleTones or
          InitialTones. Any queued DTMF events
          after the 'w', which have not yet been played, are placed in the
          DeferredTones property and copied
          into this signal's argument.

        When the channel handler is ready to continue, it MAY pass the
          value of DeferredTones to
          MultipleTones, to resume sending.
          Alternatively, it MAY ignore the deferred tones, or even play
          different tones instead. Any deferred tones are discarded the next
          time a tone is played.

        This signal SHOULD NOT be emitted if there is nothing left to play,
          i.e. if the 'w' was the last character in the DTMF string.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.DTMF', signature='s')
    def SendingTones(self, Tones):
        """
        DTMF tone(s)are being sent to all eligible streams in the channel.
        The signal is provided to indicating the fact that the streams are
        currently being used to send one or more DTMF tones, so any other
        media input is not getting through to the audio stream. It also
        serves as a cue for the
        StopTone method.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Interface.DTMF', signature='b')
    def StoppedTones(self, Cancelled):
        """
        DTMF tones have finished playing on streams in this channel.
      
        """
        pass
  