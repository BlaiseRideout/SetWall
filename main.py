#!/usr/bin/env python3

import random, time

from settings import Settings

def main():
	Settings.load()

	setters = []

	if hasattr(Settings, "SUBREDDIT") or hasattr(Settings, "SUBREDDITS"):
		from reddit import setReddit
		setters.append(setReddit)

	if hasattr(Settings, "BOARD") or hasattr(Settings, "BOARDS"):
		from fourchan import set4chan
		setters.append(set4chan)

	if len(setters) > 0:
		random.shuffle(setters)

		tried = 0

		set = False
		while not set and tried < Settings.MAXTRIES:
			excepted = False
			for setter in setters:
				try:
					set = setter()
					if set:
						break
				except Exception as e:
					excepted = True
					print("Failed to retrieve wallpaper: " + str(e))
					tried += 1
					if tried < Settings.MAXTRIES:
						print("Trying again in 5 seconds...")
						time.sleep(5)
						break
			if not set and not excepted:
				print("Failed to retrieve wallpaper. Please check your configuration.")
				break

if __name__ == "__main__":
	main()