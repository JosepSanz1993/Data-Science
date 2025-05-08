import threading
import time
from vpython import sphere, vector, color, label, rate

class Cron3D:
    def __init__(self, init, interval=1.0):
        self.initial_time = init
        self.interval = interval
        self._stop = False
        self.thread = threading.Thread(target=self._update_loop)

        self.ball = sphere(pos=vector(init, 0, 0), radius=0.5, color=color.green)
        self.tag = label(pos=vector(init, 1, 0), text='', height=20, box=False)

    def start(self):
        self.thread.start()

    def _update_loop(self):
        steps = int(self.initial_time / self.interval)
        for i in range(steps + 1):
            if self._stop:
                break
            time.sleep(self.interval) 
            remaining = self.initial_time - i * self.interval
            self.ball.pos.x = remaining
            self.tag.text = f"Remaining time: {remaining:.1f} s"
            self.tag.pos = vector(remaining, 1, 0)

        if not self._stop:
            self.tag.text = "Time over"
            self.ball.color = color.red

    def stop(self):
        self._stop = True

    def join(self):
        self.thread.join()