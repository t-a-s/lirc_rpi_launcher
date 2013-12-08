#!/usr/bin/env python
import os
import xbmc
import xbmcaddon
 
__addon__       = xbmcaddon.Addon(id='script.service.lirc_rpi_launcher')
__addonname__   = __addon__.getAddonInfo('name')
__icon__        = __addon__.getAddonInfo('icon')
 
title = "Lirc_RPi Launcher"
text1 = "Initialising"
text2 = "Initialised"
time = 5000  # ms

cmd_mod_rpi = "modprobe lirc_rpi"

cmd_kill_lircd = "killall lircd; sleep 4; killall lircd;" # give modprobe time to finish
 
cmd_lircd = "/usr/sbin/lircd --driver=default --device=/dev/lirc0 --uinput --output=/var/run/lirc/lircd --pidfile=/var/run/lirc/lircd-lirc0.pid /storage/.config/lircd.conf"

xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(title, text1, time, __icon__))

os.system(cmd_mod_rpi)
os.system(cmd_kill_lircd)
os.system(cmd_lircd)

xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(title, text2, time, __icon__))
