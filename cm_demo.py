#!/usr/bin/python

import telepathy
import gobject
import dbus

from dbus.mainloop.glib import DBusGMainLoop

import sys

from tphangups import HangupsConnectionManager

if __name__ == '__main__':

    #this is a collection of black magic.
    dbus.set_default_main_loop(dbus.mainloop.glib.DBusGMainLoop())
    manager = HangupsConnectionManager()
    mainloop = gobject.MainLoop(is_running=True)
    mainloop.run()