#!/usr/bin/env python3

import random, time

from config import Settings

def main():
	Settings.load()

	setters = []

	if hasattr(Settings, "SUBREDDIT"):
		from reddit import setReddit
		setters.append(setReddit)

	if hasattr(Settings, "BOARD") or hasattr(Settings, "BOARDS"):
		from fourchan import set4chan
		setters.append(set4chan)

	if len(setters) > 0:
		random.shuffle(setters)

		set = False
		while not set:
			excepted = False
			for setter in setters:
				try:
					set = setter()
					if set:
						break
				except Exception as e:
					excepted = True
					print("Failed to retrieve wallpaper: " + str(e) + "\nTrying again in 5 seconds...")
					time.sleep(5)
					continue
			if not set and not excepted:
				print("Failed to retrieve wallpaper. Please check your configuration.")
				break

if __name__ == "__main__":
	main()