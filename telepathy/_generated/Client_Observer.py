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


class ClientObserver(dbus.service.Object):
    """\
      Observers monitor the creation of new channels. This
        functionality can be used for things like message logging.
        All observers are notified simultaneously.

      Observers SHOULD NOT modify the state of a channel except
        via user interaction.

      
        We want Observer UIs for file transfer channels (a progress
          bar for the transfer) to be able to have a Cancel button.
      

      Observers MUST NOT carry out actions that exactly one process
        must take responsibility for (e.g. acknowledging Text
        messages, or carrying out the actual transfer in a file transfer
        channel).

      
        Since arbitrarily many observers can be activated for
          each channel, it would not make sense for observers to do things
          that can only be done by one process (acknowledging
          Text
          messages, carrying out streaming for
          StreamedMedia
          channels, doing the actual data transfer for file transfers,
          setting up the out-of-band connection for Tubes). The
          Handler
          is responsible for such tasks.

        Handlers MAY, of course, delegate responsibility for these
          tasks to other processes (including those run as observers),
          but this MUST be done explicitly via a request from the Handler
          to the Observer.
      

      Whenever a collection of new channels is signalled, the channel
        dispatcher will notify all running or activatable observers whose
        ObserverChannelFilter property
        (possibly as cached in the .client file) indicates that they are
        interested in some of the channels.

      Observers are activated for all channels in which they have
        registered an interest - incoming, outgoing or automatically created -
        although of course the ObserverChannelFilter property can be set
        to filter on the
        Requested
        property.

      Because it might take time for an observer to become ready (for
        instance, a Text logger needs to wait until pending messages have been
        downloaded), the channel dispatcher must wait (up to some timeout) for
        all observers to return from
        ObserveChannels before letting anything
        destructive happen. Destructive things (e.g. acknowledging messages)
        are defined to be done by handlers, therefore HandleWith and Claim
        aren't allowed to succeed until all observers are ready.
    """

    @dbus.service.method('org.freedesktop.Telepathy.Client.Observer', in_signature='ooa(oa{sv})oaoa{sv}', out_signature='')
    def ObserveChannels(self, Account, Connection, Channels, Dispatch_Operation, Requests_Satisfied, Observer_Info):
        """
        Called by the channel dispatcher when channels in which the
          observer has registered an interest are announced in a NewChannels
          signal.

        If the same NewChannels signal announces some channels that match
          the filter, and some that do not, then only a subset of the channels
          (those that do match the filter) are passed to this method.

        If the channel dispatcher will split up the channels from a single
          NewChannels signal and dispatch them separately (for instance
          because no installed Handler can handle all of them), it will call
          ObserveChannels several times.

        The observer MUST NOT return from this method call until it is ready
          for a handler for the channel to run (which may change the channel's
          state).

        
          The channel dispatcher must wait for observers to start up,
            to avoid the following race: text channel logger (observer) gets
            ObserveChannels, text channel handler gets
            HandleChannels
            channel handler starts up faster and acknowledges messages,
            logger never sees those messages.
        

        The channel dispatcher SHOULD NOT change its behaviour based on
          whether this method succeeds or fails: there are no defined D-Bus
          errors for this method, and if it fails, this only indicates that
          an Observer is somehow broken.

        
          The expected error response in the channel dispatcher is to
            log a warning, and otherwise continue as though this method
            had succeeded.
        
      
        """
        raise NotImplementedError
  