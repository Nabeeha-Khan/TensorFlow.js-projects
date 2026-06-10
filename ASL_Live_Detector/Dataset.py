import json
#forgot that yt doesn't work on office netwerk :)
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
import tempfile
import os
import cv2
import mediapipe as mp
import numpy as np
from tqdm import tqdm
import pandas as pd

#Open json file containing training dataset
with open('MS-ASL/MSASL_train.json', 'r') as file:
    items = json.load(file)

#Create tensors for each item in dataset
for item in items:
    #Accessing yt url in json file
    url = item["url"]
    #Download video temporarily by creating a temporary directory
    with tempfile.TemporaryDirectory() as tempdirname:
        ydl_opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "merge_output_format": "mp4",
            "outtmpl": f"{tempdirname}/%(id)s.%(ext)s",
            "noplaylist": True,
            "verbose": True,
        }
        ydl = YoutubeDL(ydl_opts)
        try:
            meta = ydl.extract_info(
            url,
            download=True,
            )
        except DownloadError as e:
            raise e
        


