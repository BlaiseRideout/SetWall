#!/usr/bin/env python3

import os

class Settings:
	#SUBREDDITS = ["wallpapers", "wallpaper"]
	BOARDS = ["wg"]
	DIRECTORY = "/media/home/images/wallpapers/randwalls"
	MAXTRIES = 12
	WALLMANAGER = "feh"

	WIDTH = 1366
	HEIGHT = 768

	@classmethod
	def load(self):
		self.DIRECTORY = os.path.normpath(self.DIRECTORY)

		if not hasattr(self, "WIDTH"):
			self.WIDTH = 1920

		if not hasattr(self, "HEIGHT"):
			self.HEIGHT = 1080

		if hasattr(self, "SUBREDDIT") and not hasattr(self, "PAGE"):
			self.PAGE = "hot"

		if not hasattr(self, "MAXPAGES"):
			self.MAXPAGES = 20

		if not hasattr(self, "MAXTRIES"):
			self.MAXTRIES = 20
