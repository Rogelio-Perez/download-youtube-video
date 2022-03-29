from pytube import YouTube


try:
    yt = input("Enter the link of the video: ")
    print('\n')
    yt = YouTube(yt)
    print("Title: ", yt.title)
    print('\n')
    length_video = int(yt.length)
    min, sec = divmod(length_video, 60)
    print("Duration: ", "{}:{}min".format(min, sec))
    print('\n')
    print("Views: ", format(yt.views, ','))
    print('\n')
    print(yt.description)
    print('\n')
    print('Downloading video... ⌛')
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print('\n')
    print('Download complete!🎉')
except:
    print("Error: Invalid link or video not found! ☹️")
    print('\n')
    print('Please introduce a valid link video (https://www.youtube.com/watch?v=...)')
    exit()
