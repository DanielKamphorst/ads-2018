from config import *

class Station:
    def __init__(
            self, name, average_driving_time, plat_1_busy=False,
            plat_2_busy=False):
        self.name = name
        self.average_driving_time = average_driving_time
        self.plat_1_busy = plat_1_busy
        self.plat_2_busy = plat_2_busy

    def dwell():
        pass
