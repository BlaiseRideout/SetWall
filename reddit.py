#!/usr/bin/env python3

import urllib.request, json, re, os, random, copy

from config import Settings
from setters import fromstr

exts = ['.png', '.jpg', '.jpeg']

def setReddit():
	hdr = {'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0"}
	baseurl = "http://reddit.com/r/" + Settings.SUBREDDIT + "/" + Settings.PAGE + ".json"

	after = None

	set = False

	while not set:
		url = baseurl
		if after != None:
			url += "?after=" + after
		req = urllib.request.Request(url, headers=hdr)
		page = json.loads(urllib.request.urlopen(req).read().decode('utf8'))

		if page['kind'] == "Listing":
			posts = copy.copy(page['data']['children'])
			random.shuffle(posts)
			for post in posts:
				dims = re.search(r'(?P<width>[0-9]+) ?x ?(?P<height>[0-9]+)', post['data']['title'])
				if dims == None:
					continue
				width = int(dims.group('width'))
				height = int(dims.group('height'))
				ext = os.path.splitext(post['data']['url'])[1]
				if ext.lower() in exts:
					fname = post['data']['id'] + ext
					path = Settings.DIRECTORY + "/" + fname 
					f = open(path, "wb+")
					f.write(urllib.request.urlopen(post['data']['url']).read())
					set = fromstr(Settings.WALLMANAGER)(path, width, height)

					if set:
						print("Set: " + fname + ": " + str(width) + "x" + str(height))

						break
			if not set:
				if len(posts) <= 0:
					return False
				after = page['data']['children'][-1]['data']['name']
		else:
			return False

	return True
