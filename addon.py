#!/usr/bin/env python
import os
import xbmc
import xbmcaddon
 
__addon__       = xbmcaddon.Addon(id='script.service.lirc_rpi_launcher')
__addonname__   = __addon__.getAddonInfo('name')
__icon__        = __addon__.getAddonInfo('icon')
 
title = "Lirc_RPi Helper"
text = "Remote Initialised"
time = 5000  # ms
 
cmd = 'killall lircd; /usr/sbin/lircd --driver=default --device=/dev/lirc0 --uinput --output=/var/run/lirc/lircd --pidfile=/var/run/lirc/lircd-lirc0.pid /storage/.config/lircd.conf'

os.system(cmd)

xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(title, text, time, __icon__))
