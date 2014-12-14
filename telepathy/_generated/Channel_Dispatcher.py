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
      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
      USA.
  
"""

import dbus.service


class ChannelDispatcher(dbus.service.Object):
    """\
      The channel dispatcher is responsible for responding to new
        channels and launching client processes to handle them. It also
        provides functionality for client processes to request that new
        channels are created.

      If a channel dispatcher is running, it is responsible for dispatching
        new channels on all
        Connections
        created by the
        AccountManager.
        Connections not created by the AccountManager are outside the scope
        of the channel dispatcher.

      
        Connections created by standalone Telepathy clients
          that do not intend to interact with the channel dispatcher
          should be ignored - otherwise, the channel dispatcher would try
          to launch handlers for channels that the standalone client
          was already handling internally.
      

      The current channel dispatcher is defined to be the process that
        owns the well-known bus name
        org.freedesktop.Telepathy.ChannelDispatcher on
        the session bus. This process MUST export an object with this
        interface at the object path
        /org/freedesktop/Telepathy/ChannelDispatcher.

      Until a mechanism exists for making a reasonable automatic choice
        of ChannelDispatcher implementation, implementations SHOULD NOT
        register as an activatable service for the ChannelDispatcher's
        well-known bus name. Instead, it is RECOMMENDED that some component
        of the user's session will select and activate a particular
        implementation, and that other Telepathy-enabled programs
        can detect whether channel request/dispatch functionality is available
        by checking whether the ChannelDispatcher's well-known name is in use
        at runtime.

      There are three categories of client process defined by this
        specification:

      
        Observer
        Observers monitor the creation of new channels. This
            functionality can be used for things like message logging.
            All observers are notified simultaneously.

        Approver
        
          Approvers notify the user that new channels have been created,
            and also select which channel handler will be used for the channel,
            either by asking the user or by choosing the most appropriate
            channel handler.
        

        Handler
        
          Each new channel or set of channels is passed to exactly one
            handler as its final destination. A typical channel handler is a
            user interface process handling channels of a particular type.
        
      
    """

    @dbus.service.method('org.freedesktop.Telepathy.ChannelDispatcher', in_signature='oa{sv}xs', out_signature='o')
    def CreateChannel(self, Account, Requested_Properties, User_Action_Time, Preferred_Handler):
        """
        Equivalent to calling
          CreateChannelWithHints with an empty
          Hints parameter.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.ChannelDispatcher', in_signature='oa{sv}xs', out_signature='o')
    def EnsureChannel(self, Account, Requested_Properties, User_Action_Time, Preferred_Handler):
        """
        Equivalent to calling
          EnsureChannelWithHints with an empty
          Hints parameter.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.ChannelDispatcher', in_signature='oa{sv}xsa{sv}', out_signature='o')
    def CreateChannelWithHints(self, Account, Requested_Properties, User_Action_Time, Preferred_Handler, Hints):
        """
        Start a request to create a channel. This initially just creates a
          ChannelRequest
          object, which can be used to continue the request and track its
          success or failure.

        
          The request can take a long time - in the worst case, the
            channel dispatcher has to ask the account manager to put the
            account online, the account manager has to ask the operating
            system to obtain an Internet connection, and the operating
            system has to ask the user whether to activate an Internet
            connection using an on-demand mechanism like dialup.

          This means that using a single D-Bus method call and response
            to represent the whole request will tend to lead to that call
            timing out, which is not the behaviour we want.
        

        If this method is called for an Account that is disabled, invalid
          or otherwise unusable, no error is signalled until
          ChannelRequest.Proceed
          is called, at which point
          ChannelRequest.Failed
          is emitted with an appropriate error.

        
          This means there's only one code path for errors, apart from
            InvalidArgument for "that request makes no sense".

          It also means that the request will proceed if the account is
            enabled after calling CreateChannel, but before calling
            Proceed.
        
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.ChannelDispatcher', in_signature='oa{sv}xsa{sv}', out_signature='o')
    def EnsureChannelWithHints(self, Account, Requested_Properties, User_Action_Time, Preferred_Handler, Hints):
        """
        Start a request to ensure that a channel exists, creating it if
          necessary.  This initially just creates a ChannelRequest
          object, which can be used to continue the request and track its
          success or failure.

        If this method is called for an Account that is disabled, invalid
          or otherwise unusable, no error is signalled until
          ChannelRequest.Proceed
          is called, at which point
          ChannelRequest.Failed
          is emitted with an appropriate error.

        
          The rationale is as for CreateChannelWithHints.
        
      
        """
        raise NotImplementedError
  