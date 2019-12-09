# getLyric.py
# Ezra Zinberg

# takes track name as cmd line argument. searches songdata-all-fields.csv for all
# instances of tracks with that track name and prints lyrics for each hit.
# prints number of hits
# usage: $ python getLyric.py "Baby"


import csv
import operator
import sys

def main():

    track = sys.argv[1]
    print('Track name: ' + track + "\n")
        
    hits = 0

    # realpython.com
    with open('songdata-all-fields.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # print(row[1])
            if row[1] == track:
                print("******************************\n" + "Found!\n\"" 
                    + row[1] + "\" by " 
                    + row[0] + ":\n******************************\n")
                print(row[3])
                hits += 1


    print("\n\n" + str(hits) + " match/es found for track name \"" + track + '"')



main()