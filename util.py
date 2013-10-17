#!/usr/bin/env python3

import urllib.request, os

def wget(url, path, overwrite = False):
	stream = urllib.request.urlopen(url)

	if os.path.exists(path):
		if os.path.isdir(path):
			path = os.path.normpath(path)
			path += "/" + url.split('/')[-1]
		elif not overwrite and os.path.getsize(path) == stream.info()['Content-Length']:
			return path

	downloaded = 0
	size = int(stream.info()['Content-Length'])

	print("[--------------------]", end="")

	with open(path, 'wb+') as f:
		while True:
			s = "\r["
			s += "=" * int(20 * downloaded / size)
			s += "-" * (20 - int(20 * downloaded / size))
			s += "]"
			s += " " + str(int(downloaded / size * 100)) + "%"
			print(s, end='')
			chunk = stream.read(1024 * 128)
			if not chunk:
				break
			f.write(chunk)
			f.flush()
			downloaded += 1024 * 128

	print("\rSaved file to " + path)

	return path
