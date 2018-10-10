from scipy import stats

from tram import Tram
from station import Station

def event_handler(name, obj):
    if name == "departure":
        time = obj.event_departure(stations, clock)
        event_queue[time] = ("arrival", obj)
    elif name == "arrival":
        time = obj.event_arrival(stations, clock, turnaround_time)
        event_queue[time] = ("departure", obj)


# TO-DO: pre-processing
stations = {
    0: Station("P+R De Uithof", -1, 113),
    1: Station("WKZ", 110, 78),
    2: Station("UMC", 78, 86),
    3: Station("Heidelberglaan", 82, 60),
    4: Station("Padualaan", 60, 101),
    5: Station("Kromme Rijn", 100, 59),
    6: Station("Galgenwaard", 59, 243),
    7: Station("Vaartsche Rijn", 243, 134),
    8: Station("Centraal Station", 135, -1)
}
clock = 6 * 3600 # time starts at 6:00 AM
turnaround_time = 3 * 60 # min 3 minutes

# start simulation by adding first tram's departure to queue
event_queue = {}
event_queue[clock] = ("departure", Tram(None)) # test single empty tram

# main loop
while len(event_queue) != 0:
    clock = min(event_queue.keys())
    next_event, next_obj = event_queue.pop(clock)
    # TO-DO: process event
    event_handler(next_event, next_obj)

    # test single round-trip
    print(clock, next_event, stations[next_obj.location].name)
    if clock > 6 * 3600 and next_obj.location == 0:
        break
