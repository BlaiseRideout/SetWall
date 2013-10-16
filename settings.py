#!/usr/bin/env python3

import os

class Settings:
	@classmethod
	def load(self):
		try:
			import config
		except:
			try:
				with open('config_default.py'):
					import shutil
					print("Using default config file")
					shutil.copyfile('config_default.py', 'config.py')
					import config
			except:
				print("Couldn't open default config file, falling back to defaults")
				config = None


		if not hasattr(config, "DIRECTORY"):
			self.DIRECTORY = "/tmp"
		else:
			self.DIRECTORY = config.DIRECTORY

		self.DIRECTORY = os.path.normpath(os.path.expanduser(self.DIRECTORY))

		if not hasattr(config, "WIDTH"):
			self.WIDTH = 1920
		else:
			self.WIDTH = config.WIDTH

		if not hasattr(config, "HEIGHT"):
			self.HEIGHT = 1080
		else:
			self.HEIGHT = config.HEIGHT

		if (hasattr(config, "SUBREDDIT") or hasattr(config, "SUBREDDITS")) and not hasattr(config, "PAGE"):
			self.PAGE = "hot"
		elif hasattr(config, "PAGE"):
			self.PAGE = config.PAGE

		if not hasattr(config, "MAXPAGES"):
			self.MAXPAGES = 20
		else:
			self.MAXPAGES = config.MAXPAGES

		if not hasattr(config, "MAXTRIES"):
			self.MAXTRIES = 20
		else:
			self.MAXTRIES = config.MAXTRIES

		if not hasattr(config, "WALLMANAGER"):
			self.WALLMANAGER = "gsettings"
		else:
			self.WALLMANAGER = config.WALLMANAGER

		if not (hasattr(config, "SUBREDDIT") or hasattr(config, "SUBREDDITS") or hasattr(config, "BOARD") or hasattr(config, "BOARDS")):
			self.BOARDS=["/wg/", "/w/"]
			self.SUBREDDITS=["wallpapers", "wallpaper"]
		else:
			if hasattr(config, "SUBREDDIT"):
				self.SUBREDDIT = config.SUBREDDIT
			if hasattr(config, "SUBREDDITS"):
				self.SUBREDDITS = config.SUBREDDITS
			if hasattr(config, "BOARDS"):
				self.BOARDS = config.BOARDS
			if hasattr(config, "BOARD"):
				self.BOARD = config.BOARD

