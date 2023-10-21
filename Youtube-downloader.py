from pytube import YouTube as yt

def download_video(link,directory):
    ytobj = yt(link)
    print("To see all strem options press 1 \n to see stram option only in mp4 format press 2 \n for ONLY audio options press 3\n for ONLY video options press 4")
    command = int(input())
    if command == 1:
        print("Bellow are the all stream option to download (it may take few seconds )\n")
        print(ytobj.streams.filter())
    elif command == 2:
        print("Bellow are the stream option in mp4 format to download (it may take few seconds )\n")
        print(ytobj.streams.filter(file_extension = 'mp4'))
    elif command == 3:
        print("Bellow are the stream option in only audio format to download (it may take few seconds )\n")
        print(ytobj.streams.filter(only_audio=True))
    elif command == 4:
        print("Bellow are the stream option in only video format to download (it may take few seconds )\n")
        print(ytobj.streams.filter(only_video =True))
    print("\nEnter the itag of the stream you want to download\n")
    itag = int(input())
    try:
        stream = ytobj.streams.get_by_itag(itag)
        print("Downloading..... (will take a while )")
        stream.download(directory)
        print("Video downloaded succesfully!! \check the directory")
   
    except:
        print("ERROR!!! itag could be wrong ")
    
print("Hello welcome to YT download Python program\n ")
print("Past the directory you want to save the video without any extra cherecter or spaces\n ")
save_dir = input()
print("Past the YT video link below without any extra cherecter or spaces\n ")
link = input()


download_video(link,save_dir)


