from play import play
from totext import get_text
from data import data
import sys

def main(): 
	kata = get_text()
	print(kata)
	if not kata:
		return kata
	video = {}
	for j in data.keys():
		for i in data[j]:
			video[(" %s "%kata.lower()).find(" %s "%i)] = j
	key = list(video.keys())
	key.sort()
	videoList = [video[i] for i in key if i>=0]
	print(videoList)
	play(videoList)
	return kata


if __name__ == '__main__':
	if len(sys.argv) > 1 and sys.argv[1] == "loop":
		while(1):
			if(main() == "Tutup aplikasi"):
				break
	else:
		main()	