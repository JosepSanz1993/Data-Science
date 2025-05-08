import threading
import time
from vpython import sphere,vector, color, label,rate

class Cron3D(threading.Thread):
    def init__(self, init,interval):
        super().__init__()
        self.initial_time = init
        self.interval = interval
        self._stop = False

    def run(self):
        ball = sphere(pos=vector(self.initial_time), radius=0.5, color=color.green)
        tag = label(pos=vector(self.initial_time,1,0),text='',height=20,box=False)

        step = int(self.temps_inicial / self.interval)
        for i in range(step + 1):
            if self._deturat:
                break
            rate(1 / self.interval)
            temps_rest = self.temps_inicial - i * self.interval
            ball.pos.x = temps_rest
            tag.text = f"Remaining time: {temps_rest:.1f} s"
            tag.pos = vector(temps_rest, 1, 0)

        if not self._deturat:
            tag.text = "Time over"
            ball.color = color.red

    def aturar(self):
        self._deturat = True