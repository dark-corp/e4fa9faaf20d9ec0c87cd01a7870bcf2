import os
import sys
os.system("pip install pytube")
os.system("pip3 install pytube")
os.system("clear")
import pytube
x = input("Insira a URL aqui: ")
def downloadYouTube(videourl, path):
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
        yt.download(path)
    downloadYouTube(x, '/')
    print("Pronto!")
