from pytube import YouTube

#class Downloader:

link = input("Enter Link: ")
# print("Downloading video...")

yt = YouTube(link)
progressiveStreams = yt.streams.filter()
# print(yt.streams.filter(progressive=True))


# Parse the list of progressive stream
# one per line for human reading
for stream in progressiveStreams:
    print(stream, "\n")


# Automatically sleect the highest quality progressive stream
yt.streams.get_highest_resolution().download()
print("Video Downlad Successful!")


# YouTube(link).streams.first().download()
# print("Video Downlad Successful!")