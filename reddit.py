#!/usr/bin/env python3

import urllib.request, json, re, os, random, copy

from settings import Settings
from setters import fromstr

import util

exts = ['.png', '.jpg', '.jpeg']

def setReddit():
	hdr = {'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0"}

	set = False

	subreddits = []

	if hasattr(Settings, "SUBREDDITS"):
		subreddits += Settings.SUBREDDITS

	if hasattr(Settings, "SUBREDDIT") and not Settings.SUBREDDIT in subreddits:
		subreddits.append(Settings.SUBREDDIT)

	random.shuffle(subreddits)

	for subreddit in subreddits:
		baseurl = "http://reddit.com/r/" + subreddit + "/" + Settings.PAGE + ".json"

		after = None
		page = 0

		while not set:
			url = baseurl
			if after != None:
				url += "?after=" + after
			req = urllib.request.Request(url, headers=hdr)
			pagedata = json.loads(urllib.request.urlopen(req).read().decode('utf8'))

			if pagedata['kind'] == "Listing":
				posts = copy.copy(pagedata['data']['children'])
				random.shuffle(posts)
				for post in posts:
					dims = re.search(r'(?P<width>[0-9]+) ?x ?(?P<height>[0-9]+)', post['data']['title'])
					if dims == None:
						continue
					width = int(dims.group('width'))
					height = int(dims.group('height'))
					ext = os.path.splitext(post['data']['url'])[1]
					if ext.lower() in exts and width >= Settings.WIDTH and height >= Settings.HEIGHT:
						fname = post['data']['id'] + ext
						path = util.wget(post['data']['url'], Settings.DIRECTORY)
						set = fromstr(Settings.WALLMANAGER)(path, width, height)

						if set:
							print("Set: " + fname + ": " + str(width) + "x" + str(height) + " from /r/" + subreddit)
							break

				if not set:
					if len(posts) <= 0 or page > Settings.MAXPAGES:
						break
					page += 1
					after = pagedata['data']['children'][-1]['data']['name']
			else:
				break
		if set:
			break
	return set
