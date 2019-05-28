from play import play
from totext import get_text
from data import data
import sys

def get_video_list(kata):
	video = {}
	print(kata)
	for j in data.keys():
		for i in data[j]:
			video[(" %s "%kata.lower()).find(" %s "%i)] = j
	key = list(video.keys())
	key.sort()
	videoList = [video[i] for i in key if i>=0]
	print(videoList)
	return videoList

def main(): 
	kata = get_text()
	if not kata:
		return kata
	else:
		videoList = get_video_list(kata)
		play(videoList)
		return kata


if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == "loop":
			while(1):
				if(main() == "Tutup aplikasi"):
					break
		if sys.argv[1] == "-m":
			play(get_video_list(" ".join(sys.argv[2:])))
		else:
			main()
	else:
		main()	