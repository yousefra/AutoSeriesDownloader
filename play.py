import os
import sys

def playDefaultPlayer(path, episode):
    print('Playing ' + str(episode) + '...')
    playEpisode = '""' + path + '""'
    os.system(playEpisode)

currentEpisode = int(open('D:/One Piece/current.txt', 'r').read())
change = True

if len(sys.argv) > 1:
    if sys.argv[1] == 'current':
        if len(sys.argv) > 2 and sys.argv[2] == 'play':
            pass
        else:
            print("Current eposide:", currentEpisode)
            exit()
    elif sys.argv[1] == 'next':
        currentEpisode = currentEpisode + 1
    elif sys.argv[1] == 'prev':
        currentEpisode = currentEpisode - 1
    else:
        change = False
        currentEpisode = int(sys.argv[1])
        if len(sys.argv) > 2 and sys.argv[2] == 'true':
            change = True

episode = 'D:\One Piece\One-Piece-' + str(currentEpisode) + '.mp4'
filer = 'D:\One Piece\One-Piece-' + str(currentEpisode) + ' [Filler].mp4'

if os.path.isfile(episode):
    playDefaultPlayer(episode, currentEpisode)
elif os.path.isfile(filer):
    choice = input('Episode ' + str(currentEpisode) + ' is a filler do you want to play it (Y/N) ')
    if choice == 'Y' or choice == 'y':
        playDefaultPlayer(filer, currentEpisode)
else:
    choice = input('Episode does not exist!\nDownload episode (Y/N) ')
    if choice == 'Y' or choice == 'y':
        os.system('powershell opdownload one ' + str(currentEpisode))

if change:
    file = open('D:/One Piece/current.txt', 'w')
    file.write(str(currentEpisode))
