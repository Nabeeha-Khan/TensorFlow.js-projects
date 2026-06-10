from yt_dlp import YoutubeDL

#Not working in office, test at home
url = "https://www.youtube.com/watch?v=C37R_Ix8-qs"

ydl = YoutubeDL()
ydl.extract_info(url, download=False)