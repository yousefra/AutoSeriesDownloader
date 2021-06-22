import requests
import os
import sys
from bs4 import BeautifulSoup

def downloadEpisode(url, i):
    file_name = 'One-Piece-' + str(i) + '.mp4'

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        downloadArea = soup.find('div', {'id': 'DownloadArea'})
        downloadURL = downloadArea.find('a', {'class': 'DownloadURL'})['href']

        os.system('idman /q /n /d "' + downloadURL + '" /p "D:/One Piece" /f "' + file_name + '"')
        print("[SUCCESS]", file_name, "downloaded!")
    except:
        print("[ERROR] Could not download", file_name)

if len(sys.argv) > 1:
    if sys.argv[1] == 'many':
        fromEp = sys.argv[2]
        toEp = sys.argv[3]
        print('Downloading episodes from ' + fromEp + '-' + toEp)
    elif sys.argv[1] == 'one':
        fromEp = sys.argv[2]
        toEp = int(fromEp) + 1
        print('Downloading episode ' + fromEp)

for i in range(int(fromEp), int(toEp)):
    url = 'http://mycima.me/%D9%85%D8%B4%D8%A7%D9%87%D8%AF%D8%A9-%D8%A7%D9%86%D9%85%D9%8A-one-piece-%D8%AD%D9%84%D9%82%D8%A9-' + str(i) + '/'
    downloadEpisode(url, i)
