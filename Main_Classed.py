from logging import error
from pytube import YouTube

class App:
    

    def __init__(self):
        print("init has run...")
        # Get the link from the user
        link = input("Enter Link: ")
        # Create a youtube object from the link 
        yt = YouTube(link)

        # Filter streams for progressive video
        # Progressive has Audio & Vidoe in a single file
        available_streams = yt.streams.filter(progressive=True)

        # Print the streams for the user to see 
        for stream in available_streams:
            print(stream, "\n")


        # Downlaod the video
        def download(self):
            location = input("Optional: Enter a directory to save to: ")
            name = input("Optional: Change File name: ")
            yt.streams.get_highest_resolution().download(output_path=location, filename=name)
            print("Attempting to download the file...")
         
        try:
            # Download the video with highest resolution
            download()
        
        except error as e:
            message = f"Something went wrong {e}"
            print(message)

        print("File Downloaded Successfully!")


        

def main():
    t = App()



if __name__ == "__main__":
    main()


    



