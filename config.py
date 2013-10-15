#!/usr/bin/env python3

import os

class Settings:
	SUBREDDIT = "wallpaper"
	BOARDS = ["wg", "w"]
	DIRECTORY = "/media/home/images/wallpapers/randwalls"
	WALLMANAGER = "gsettings"

	WIDTH = 1366
	HEIGHT = 768

	@classmethod
	def load(self):
		self.DIRECTORY = os.path.normpath(os.path.expanduser(self.DIRECTORY))

		if not hasattr(self, "WIDTH"):
			self.WIDTH = 1920

		if not hasattr(self, "HEIGHT"):
			self.HEIGHT = 1080

		if hasattr(self, "SUBREDDIT") and not hasattr(self, "PAGE"):
			self.PAGE = "hot"
