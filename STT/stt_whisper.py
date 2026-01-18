from faster_whisper import WhisperModel
from audio_extraction import extract_audio
model = WhisperModel('base', device='cpu', compute_type= 'int8')

def transcribe_audio(file_path):
    audio_file = extract_audio(file_path, beam_size=5)
    segments, info = model.transcribe(audio_file,beam_size=5)
    text = ''.join(segment.text for segment in segments)
    return text
