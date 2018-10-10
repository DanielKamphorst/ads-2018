from scipy import stats

class Tram:
    def __init__(self, schedule,
                location=0, direction=0, passengers=0):
        self.schedule = schedule
        self.location = location
        self.direction = direction
        self.passengers = passengers

    def event_arrival(self, stations, clock, turnaround_time):
        self.location = self.location + (1 if self.direction == 0 else -1)

        if self.location == 0 or self.location == 8:
            self.direction = (self.direction + 1) % 2 # turn train around
            return clock + turnaround_time

        expected_dwell = 12.5 # + .22 * p_in + .13 * p_out
        departure_time = clock + int(stats.gamma.rvs(2, scale=expected_dwell / 2))
        while departure_time < .8 * expected_dwell:
            departure_time = clock + int(stats.gamma.rvs(2, scale=expected_dwell / 2))
        return departure_time

    def event_departure(self, stations, clock):
        if self.direction == 0:
            next_station = self.location + 1
            expected_time = stations[next_station].in_time
            arrival_time = clock + int(stats.norm.rvs(loc=expected_time, scale=expected_time / 10))
        else:
            next_station = self.location - 1
            expected_time = stations[next_station].out_time
            arrival_time = clock + int(stats.norm.rvs(loc=expected_time, scale=expected_time / 10))
        return arrival_time
