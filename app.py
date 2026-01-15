from flask import Flask, jsonify
from video_recording import capture_video
import os

app = Flask(__name__)

Base_dir = "data/session_001/Q1"

os.makedirs(Base_dir, exist_ok=True)