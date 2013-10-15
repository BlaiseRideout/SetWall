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

def fromstr(s):
	if s == "feh":
		return Feh
	else:
		return Feh