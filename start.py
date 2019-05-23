from play import play
from totext import get_text
from data import data

kata = get_text()
print(kata)
video = {}
for j in data.keys():
	for i in data[j]:
		video[(" %s "%kata.lower()).find(" %s "%i)] = j
key = list(video.keys())
key.sort()
videoList = [video[i] for i in key if i>=0]
print(videoList)
play(videoList)
