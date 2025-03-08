import os
import subprocess


def compress_video(video_path, compression_level=50):
    output_path = os.path.join("output", os.path.basename(video_path))
