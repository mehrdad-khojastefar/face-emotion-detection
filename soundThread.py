import threading
import playsound

class PlayThread(threading.Thread):
    def __init__(self) -> None:
        threading.Thread.__init__(self,daemon=True)
        self.file_path = ""

    def run(self):
        playsound.playsound(self.file_path)

class ThreadManager():
    def __init__(self):
        self.thread = PlayThread()

    def runThread(self,file):
        if not self.thread.is_alive():
            self.thread = PlayThread()
            self.thread.file_path = file
            self.thread.run()
        



