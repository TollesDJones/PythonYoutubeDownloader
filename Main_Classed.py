from logging import error
from pytube import YouTube

class App:
    
    # Get the link from the user
    link = input("Enter Link: ")
    # Create a youtube object from the link 
    yt = YouTube(link)

    # Filter streams for progressive video
    # Progressive has Audio & Vidoe in a single file
    available_streams = yt.streams.filter(progressive=True)

    # Print message to show available streams 
    print(15*"-","Here are all availabl streams/ qualities: ", 15*"-")

    # Print the streams for the user to see 
    for stream in available_streams:
        print(stream, "\n")
        
    # Decoration 
    print(20*"-", "\n")


    def __init__(self):
    # Downlaod the video
        print("Attempting to download the file...")
        location = "./downloaded_videos"
        name = input("Optional: Change File name: ")
        self.yt.streams.get_highest_resolution().download(output_path=location, filename=(name + ".mp4"))
        print("File Downloaded Successfully!")
        

    
        
    
     

        

# Test Video 
# https://www.youtube.com/watch?v=Fyhuwmz_3PM
        

def main():
    t = App()
    
    
    


if __name__ == "__main__":
    main()


    


