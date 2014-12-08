#!/bin/python
import hangups
import asyncio #maybe want to use gobject event loop? depends on python+dbus
from os.path import expanduser


user_list = None
conversation_list = None
client = None

def _on_connect(initial_data):
    print ("connected")
    user_list = hangups.UserList(
            client, initial_data.self_entity, initial_data.entities,
            initial_data.conversation_participants
        )

    conversation_list = hangups.ConversationList(
        client, initial_data.conversation_states, user_list,
        initial_data.sync_timestamp)

    conversation_list.on_event.add_observer(on_conversation_list_event)

    for x in user_list._user_dict:
        print (user_list._user_dict[x].full_name)
        print (user_list._user_dict[x].emails)

    for conv in conversation_list.get_all():
        print ("active conv", conv.name)
        conv.on_event.add_observer(on_conversation_event)

def on_conversation_list_event(self, conv_event):
    if isinstance(conv_event, hangups.ChatMessageEvent):
        print ("new conversation ")

def on_conversation_event(self, conv_event):
    print "conversation event"

cookies = hangups.auth.get_auth_stdin(expanduser("~/hangups_auth_tmp"))
client = hangups.Client(cookies)
client.on_connect.add_observer(_on_connect)

print ("about to start main loop")
client.connect()
loop = asyncio.get_event_loop()
loop.run_until_complete(client.connect())
