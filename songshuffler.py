import os
import random
import eyed3

#put directory where your songs are located
directory = 'C:\\Users\\Some_User\\Desktop\\Songs'

#puts all files in the directory in a list
songlist = os.listdir(directory)

#generate random numbers to pair with song titles
def get_random_nums():
    numlist = []
    for num in range(1, len(songlist)+1):
        numlist.append(num)

    random.shuffle(numlist)
    return numlist

def rename_songs():
    for num, song in zip(random_nums, songlist):
        audio = eyed3.load('C:\\Users\\compa\\Some_User\\Songs\\' + song)
        src = song
        dst = str(num) + '_' + audio.tag.title + '.mp3'

        # rename() function will
        # rename all the files
        os.rename(src, dst)

if __name__ == "__main__":
	random_nums = get_random_nums()
	rename_songs()
