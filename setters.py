#!/usr/bin/env python3

from subprocess import call

from config import Settings

def Feh(path, width, height):
	if width > Settings.WIDTH and height > Settings.HEIGHT:
		iasp = int(height * 1.0 / width * 16)
		asp = int(Settings.HEIGHT * 1.0 / Settings.WIDTH * 16)
		if iasp >= asp - 1 and iasp <= asp + 1:
			call(['feh', '--bg-fill', path])
			return True
		else:
			return False
	else:
		return False

def gsettings(path, width, height):
	if width > Settings.WIDTH and height > Settings.HEIGHT:
		iasp = int(height * 1.0 / width * 16)
		asp = int(Settings.HEIGHT * 1.0 / Settings.WIDTH * 16)
		if iasp >= asp - 1 and iasp <= asp + 1:
			from gi.repository import Gio
			Gio.Settings.new('org.gnome.desktop.background').set_string('picture-uri', "file://" + path)
			return True
		else:
			return False
	else:
		return False

def dummy(path, width, height):
	return True

def fromstr(s):
	s = s.lower()
	if s == "feh":
		return Feh
	elif s == "gsettings" or s == "ubuntu" or s == "gnome":
		return gsettings
	elif s == "disable":
		return dummy
	else:
		return Feh