from play import play
from totext import get_text
from data import data

kata = get_text()
print(kata)
video = []
for i in kata.split(" "):
	for j in data.keys():
		if i.lower() in data[j]:
			video.append(j)

print(video)
play(video)