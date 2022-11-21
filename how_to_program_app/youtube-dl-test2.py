import subprocess

def extractVideoDataPlaylist(url):
    # youtube-dl --flat-playlist --get-duration # --get-id
    # youtube-dl --get-duration
    args = ["youtube-dl", "--get-duration", "--get-id", "--get-title", url]
    p = subprocess.run(args, check=True, capture_output=True)
    return p.stdout.decode().strip("\n").strip(" ")

url = "https://www.youtube.com/watch?v=L1ung0wil9Y"
ll = extractVideoDataPlaylist(url)
print(ll)

