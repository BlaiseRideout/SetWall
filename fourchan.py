#!/usr/bin/env python3

import urllib.request, json, os, random, copy

from settings import Settings
from setters import fromstr

import util

exts = ['.png', '.jpg', '.jpeg']

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
				op = thread['posts'][0]
				if 'sticky' in op:
					break
				req = urllib.request.Request("http://api.4chan.org/" + board['board'] + "/res/" + str(op['no']) + ".json", headers=hdr)
				posts = json.loads(urllib.request.urlopen(req).read().decode('utf8'))['posts']
				random.shuffle(posts)

				for post in posts:
					if not ('w' in post and 'h' in post and 'ext' in post and 'tim' in post):
						break
					width = int(post['w'])
					height = int(post['h'])
					ext = post['ext']
					if ext.lower() in exts and width >= Settings.WIDTH and height >= Settings.HEIGHT:
						fname = str(post['tim']) + ext
						path = util.wget("http://images.4chan.org/" + board['board'] + "/src/" + fname, Settings.DIRECTORY)
						set = fromstr(Settings.WALLMANAGER)(path, width, height)

						if set:
							print("Set: " + fname + " from /" + board['board'] + "/" + str(op['no'])  + ": " + str(width) + "x" + str(height))
							break

				if set:
					break

			if set:
				break

		if set:
			break

	return True


