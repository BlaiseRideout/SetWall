#!/usr/bin/env python3

import urllib.request, json, os, random, copy

from config import Settings
from setters import fromstr

exts = ['.png', '.jpg']

def set4chan():
	hdr = { 'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0" }

	boardslist = json.loads(urllib.request.urlopen(urllib.request.Request("http://api.4chan.org/boards.json", headers=hdr)).read().decode('utf8'))['boards']
	numpages = 0
	boards = []
	for board in boardslist:
		if hasattr(Settings, "BOARD"):
			if board['board'] == Settings.BOARD or board['title'] == Settings.BOARD:
				boards.append(board)
				continue
		if hasattr(Settings, "BOARDS"):
			if board['board'] in Settings.BOARDS or board['title'] in Settings.BOARDS:
				boards.append(board)
				continue


	if len(boards) == 0:
		boards.append({'board': "w", 'pages': 11})

	set = False

	random.shuffle(boards)

	for board in boards:
		pages = list(range(0, board['pages']))
		random.shuffle(pages)

		for page in pages:
			req = urllib.request.Request("http://api.4chan.org/" + board['board'] + "/" + str(page) + ".json", headers=hdr)
			page = json.loads(urllib.request.urlopen(req).read().decode('utf8'))

			threads = copy.copy(page['threads'])
			random.shuffle(threads)

			for thread in threads:
				posts = copy.copy(thread['posts'])
				random.shuffle(posts)

				for post in posts:
					if 'sticky' in post or not ('w' in post and 'h' in post and 'ext' in post and 'tim' in post):
						break
					width = post['w']
					height = post['h']
					ext = post['ext']
					if ext in exts:
						fname = str(post['tim']) + ext
						path = Settings.DIRECTORY + "/" + fname
						f = open(path, "wb+")
						f.write(urllib.request.urlopen("http://images.4chan.org/" + board['board'] + "/src/" + fname).read())
						set = fromstr(Settings.WALLMANAGER)(path, width, height)

						if set:
							print("Set: " + fname + " from /" + board['board'] + "/" + str(thread['posts'][0]['no'])  + ": " + str(width) + "x" + str(height))
							break

				if set:
					break

			if set:
				break

		if set:
			break

	return True


