import subprocess
import os

def extract_audio(video_path, audio_path):
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    cmd = [
        'ffmpeg',
        '-i',
        video_path,
        '-y',
        '-vn',
        '-acodec',
        'pcm_s16le',
        '-ar', '16000',
        '-ac', '1',
        audio_path
    ]

    subprocess.run(cmd, check=True)