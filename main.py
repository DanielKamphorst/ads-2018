from scipy import stats

# TO-DO: pre-processing
t = 6 * 3600 # time starts at 6:00 AM

# start simulation by adding first tram's departure to queue
event_queue = {}

# main loop
while len(event_queue) != 0:
    next_time = min(event_queue.keys())
    next_event = event_queue.pop(next_time)
    # TO-DO: process event
    break
