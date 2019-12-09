# getYears.py
# calls musicbrainz api to get release years for songs in songdata.csv

import musicbrainzngs
import pprint
import sys
import time

# takes string trackname and string artist and returns year of oldest recording for song
def get(trackname, artist):

    # set up user agent and authentication for api calls
    musicbrainzngs.set_useragent("getYears", 1, contact=None)
    musicbrainzngs.auth("ezinberg", "ezinberg")


    dic = musicbrainzngs.search_recordings(trackname)

    recs = dic["recording-list"]

    oldestDate = "9999-01-01"

    for i in range(len(recs)):
        if recs[i]["artist-credit-phrase"] == artist:
            oldestDate = "9999-01-01"

            if recs[i].get("release-list") != None:
                if "date" in recs[i]["release-list"][0]:
                    dateFound = True
                    date = recs[i]["release-list"][0]["date"]
                    if date < oldestDate:
                        oldestDate = date

    return oldestDate
