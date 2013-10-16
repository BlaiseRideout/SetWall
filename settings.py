#!/usr/bin/env python3

import os

class Settings:
	@classmethod
	def load(self):
		if not os.path.exists('config.py'):
			try:
				with open('config_default.py'):
					import shutil
					print("Using default config file")
					shutil.copyfile('config_default.py', 'config.py')
					import config
			except:
				print("Couldn't open default config file, falling back to defaults")

		if os.path.exists('config.py'):
			import config

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
		else:
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

