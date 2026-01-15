import cv2
import time
import threading

class VideoRecorder:
    def __init__(self, output_path, fps = 20.0, frame_size = (640,480)):
        self.output_path = output_path
        self.fps = fps
        self.recording = False
        self.thread = None
    
    def start (self):
        self.recording = True
        self.thread = threading.Thread(target=self._record_video)
        self.thread.start()

    def stop(self):
        self.recording = False
        self.thread.join()
    
    def record(self):
        cap = cv2.VideoCapture(0)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        out = cv2.VideoWriter(self.output_path, fourcc, 
                              self.fps, (width, height))
        
        while self.recording:
            ret, frame = cap.read()
            if ret:
                out.write(frame)
            time.sleep(1 / self.fps)
        
        cap.release()
        out.release()