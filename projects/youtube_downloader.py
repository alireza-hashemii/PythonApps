from pytube import YouTube

yt = YouTube("https://youtu.be/NaaSpRMBHjg",proxies=None)
print(yt.title())