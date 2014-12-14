This is a telepathy connection manager for hangups, a reverse engineering of Google Hangouts

This allows hangouts to be used natively with KTp or Empathy.

Although the XMPP gateway exists, this could close at any moment and does not allow us access to attachments or group chats. Both of these /should/ be available via hangups

It is **not** ready for usage.

==Requirements==

Python 3.4
hangups (https://github.com/tdryer/hangups/)
python-dbus

==Running==

Run generate_login.py
This will prompt you for a user name and password and cache the auth result.

start cm_demo.py

Create an account using your favourite Telepathy client (KTp or empathy)  (or mc-tool add)
Set yourself to online

you should see a contact list

starting a chat will open a window, but sending/receiving messages is not implemeneted yet


==Developing==

I would love help developing.

Personally I find it is easiest to run bustle a dbus-monitor whilst running the examples in telepathy-qt.

More info can be found in tasks.