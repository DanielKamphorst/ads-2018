from scipy import stats
from config import *

class Tram:
    def __init__(self, schedule, location=0, direction=0, passenger_count=0):
        self.schedule = schedule
        self.location = location
        self.direction = direction
        self.passenger_count = passenger_count

    def next_station(self):
        if ((self.location == 8 and self.direction == 0)
            or (self.location == 0 and self.direction == 1)):
            self.direction = (self.direction + 1) % 2
        return self.location + (1 if self.direction == 0 else -1)

    def update_location(self):
        self.location = self.next_station()

    def event_arrival(self):
        self.update_location()

        if self.location % 8 == 0:
            return clock + turnaround_time

        expected_dwell = 12.5 # + .22 * p_in + .13 * p_out
        dwell = int(stats.gamma.rvs(2, scale=expected_dwell / 2))
        while dwell < .8 * expected_dwell:
            dwell = int(stats.gamma.rvs(2, scale=expected_dwell / 2))
        return clock + dwell

    def event_departure(self):
        expected_time = \
            stations[self.next_station()].average_driving_time[self.direction]
        arrival_time = (clock
            + int(stats.norm.rvs(loc=expected_time, scale=expected_time / 10)))
        return arrival_time
