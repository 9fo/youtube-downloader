from pytube import YouTube

print("Made by github.com/9fo")

print("""
[1] Download video as mp4
[2] Download video as mp3
[3] Download entire list (videos.txt) (mp4)
[3] Download entire list (videos.txt) (mp3)
""")

a = input()

if a == "1":
    vid = input("Video link: ")
    yt = YouTube(vid)
    yt.filter(progressive=True, file_extension='mp4')
    yt.download()
    print("[!] Video downloaded")
elif a == "2":
    vid = input("Video link: ")
    yt = YouTube(vid)
    yt.filter(progressive=True, file_extension='mp3')
    yt.download()
    print("[!] Video downloaded")
elif a == "3":
    with open('videos.txt', 'r') as f:
        for line in f.readlines():
            yt = YouTube(vid)
            yt.filter(progressive=True, file_extension='mp4')
            yt.download()
    print('[!] All videos have been downloaded')
elif a == "4":
    with open('videos.txt', 'r') as f:
        for line in f.readlines():
            yt = YouTube(vid)
            yt.filter(progressive=True, file_extension='mp3')
            yt.download()
    print('[!] All videos have been downloaded')
