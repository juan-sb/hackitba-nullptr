import pytube
import hashlib
import os


def hashVideo(url):
    yt = pytube.YouTube(url)
    video = yt.streams.first()
    video.download()

    file = str(video.title).replace("|","") + ".3gpp" # Location of the file (can be set a different way)
    BLOCK_SIZE = 65536 # The size of each read from the file

    file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f: # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file

    os.system("rm " + "'" + str(video.title).replace("|","") + "'" + ".3gpp")
    return file_hash.hexdigest() # Get the hexadecimal digest of the hash

if hashVideo("https://www.youtube.com/watch?v=ItFi_08B4wc") == hashVideo("https://youtu.be/QMDf5MSE0LQ"):
    print("they are the same video")
else:
    print("they are not the same video")