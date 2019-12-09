# buildCsv.py
# Ezra Zinberg
# reads list of artists from stdin. for each artist, calls getArtistSentiment.py.
# writes artist, avgSent, deltaSTotal, deltaSEarly, deltaSLate to artists-with-sentiment.csv
# python buildCsv.py < uniqueArtistList.txt
# open artists-with-sentiment.csv

import csv
import sys
import getArtistSentiment


def main():
    data = [["Artist", "avgSent", "deltaSTotal", "deltaSEarly", "deltaSLate"]] 

    line = sys.stdin.readline().strip()
    while line != "":
        row = [line] 
        metrics = getArtistSentiment.get(line)
        for i in range(len(metrics)):
            row.append(metrics[i])
        
        data.append(row)

        line = sys.stdin.readline().strip()
    
    # trying again, new write csv
    with open('artists-with-sentiment-2.csv', mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(data)
    csv_file.close()

    print(data)
        
    print("success. csv built at \'artists-with-sentiment-2.csv\'")

main()