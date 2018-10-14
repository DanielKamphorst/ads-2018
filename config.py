from station import Station

# TO-DO: pre-processing
stations = {
    0: Station("P+R De Uithof", (-1, 113)),
    1: Station("WKZ", (110, 78)),
    2: Station("UMC", (78, 86)),
    3: Station("Heidelberglaan", (82, 60)),
    4: Station("Padualaan", (60, 101)),
    5: Station("Kromme Rijn", (100, 59)),
    6: Station("Galgenwaard", (59, 243)),
    7: Station("Vaartsche Rijn", (243, 134)),
    8: Station("Centraal Station", (135, -1))
}
clock = 6 * 3600 # time starts at 6:00 AM
turnaround_time = 3 * 60 # min 3 minutes
