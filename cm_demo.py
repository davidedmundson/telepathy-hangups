#!/usr/bin/python

import dbus
import asyncio

from gi.repository import GObject
from dbus.mainloop.glib import DBusGMainLoop
from gbulb import glib_events

from tphangups import HangupsConnectionManager

if __name__ == '__main__':

    #both dbus and asyncio need an event loop
    #having two event loops would be mental
    #this makes them both use the glib event loop via dark and evil black magic
    #don't touch it

    asyncio.set_event_loop_policy(glib_events.GLibEventLoopPolicy())
    dbus.set_default_main_loop(dbus.mainloop.glib.DBusGMainLoop())

    manager = HangupsConnectionManager()

    mainloop = GObject.MainLoop()
    mainloop.run()
    loop = asyncio.get_event_loop()
    loop.run_forever()