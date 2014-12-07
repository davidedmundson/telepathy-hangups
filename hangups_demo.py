#!/bin/python
import hangups
import asyncio #maybe want to use gobject event loop? depends on python+dbus
from os.path import expanduser

user_list = None
client = None

def _on_connect(initial_data):
    print ("connected")
    user_list = hangups.UserList(
            client, initial_data.self_entity, initial_data.entities,
            initial_data.conversation_participants
        )
    for x in user_list._user_dict:
        print (user_list._user_dict[x].full_name)
        print (user_list._user_dict[x].emails)


cookies = hangups.auth.get_auth_stdin(expanduser("~/hangups_auth_tmp"))
client = hangups.Client(cookies)
client.on_connect.add_observer(_on_connect)

print ("about to start main loop")
client.connect()
loop = asyncio.get_event_loop()
loop.run_until_complete(client.connect())
