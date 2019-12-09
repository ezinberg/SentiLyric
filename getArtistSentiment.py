# getArtistSentimment.py
# Ezra Zinberg

# takes an artist name, returns sentiment metrics:
# 1) average sentiment
# 2) deltaS total
# 3) deltaS early
# 4) deltaS late


import csv
import operator
import sys
import getSentiment
from nltk.corpus import sentiwordnet as swn
from nltk import word_tokenize
from nltk.corpus import stopwords
import datetime
from dateutil import parser

# returns [[avgSent], [deltaSTotal], [deltaSEarly], [deltaSLate]] for given artist
def get(artist):
    result = [[], [], [], []]

    print('\nArtist: ' + artist)

    hits = 0
    trackSent = [0, 0, 0]
    avg = [0, 0, 0]

    # realpython.com
    with open('songdata-all-fields.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == artist:
                trackSent = getSentiment.average(row[3])
                for i in range(len(trackSent)):
                    avg[i] += trackSent[i]
                hits += 1

    if hits < 5:
        return []
    
    for i in range(len(trackSent)):
        avg[i] = avg[i] / hits


    result[0] = avg

    r = delta(artist, avg)
    result[1] = r[0]
    result[2] = r[1]
    result[3] = r[2]

    for arr in range(len(result)):
        for elem in range(len(result[arr])):
            result[arr][elem] = round(result[arr][elem], 3)

    print("avg:\t" + str(avg))
    print("deltaTotal:\t" + str(result[1]))
    print("deltaEarly:\t" + str(result[2]))
    print("deltaLate:\t" + str(result[3]))

    return result


def delta(artist, avg):
    deltaTotal = [0, 0, 0]
    trackSent = [0, 0, 0]
    # avg = [0, 0, 0]
    early = [0, 0, 0]
    late = [0, 0, 0]

    earliestDate = parser.parse(str(datetime.MAXYEAR))
    latestDate = parser.parse("1000-01-01")
    
    # iterate through rows and find range of dates for artist's songs
    with open('songdata-all-fields.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == artist:
                if (row[2] == ""): 
                    continue
                releaseDate = parser.parse(row[2])
                if releaseDate > parser.parse("2019-11-23"):
                    continue
                if releaseDate < earliestDate:
                    earliestDate = releaseDate
                if releaseDate > latestDate:
                    latestDate = releaseDate
               
    earlyBound = earliestDate + (latestDate-earliestDate) / 5
    lateBound = latestDate - (latestDate-earliestDate) / 5

    print("early period: " + str(earliestDate) + " thru " + str(earlyBound))
    print("late period: " + str(lateBound) + " thru " + str(latestDate))

    earlyHits = 0
    lateHits = 0


    with open('songdata-all-fields.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == artist:
                if (row[2] == ""): 
                    continue
                releaseDate = parser.parse(row[2])

                if releaseDate < earlyBound:
                    earlyHits += 1
                    trackSent = getSentiment.average(row[3])
                    for i in range(len(trackSent)):
                        early[i] += trackSent[i]

                elif releaseDate > lateBound:
                    lateHits += 1
                    trackSent = getSentiment.average(row[3])
                    for i in range(len(trackSent)):
                        late[i] += trackSent[i]
               
    print("songs in early period: " + str(earlyHits))
    print("songs in late period: " + str(lateHits))

    if earlyHits == 0 or lateHits == 0:
        return [[],[],[]]

    for i in range(len(early)):
        early[i] = early[i] / earlyHits
        late[i] = late[i] / lateHits

        deltaTotal[i] = late[i] - early[i]
        # note: late - early, NOT early-late

    deltaEarly = [0,0,0]
    for i in range(len(early)):
        deltaEarly[i] = avg[i] - early[i]
    
    deltaLate = [0,0,0]
    for i in range(len(late)):
        deltaLate[i] = late[i] - avg[i]

    return [deltaTotal, deltaEarly, deltaLate]
