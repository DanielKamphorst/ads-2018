from scipy import stats
from config import *
from tram import Tram
from station import Station

def event_handler(name, obj):
    if name == "departure":
        time = obj.event_departure()
        event_queue[time] = ("arrival", obj)
    elif name == "arrival":
        time = obj.event_arrival()
        event_queue[time] = ("departure", obj)

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
