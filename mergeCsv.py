# buildCsv.py
# Ezra Zinberg

import csv
import sys


def main():
    data = [[]]

    # add artist, track, date to data
    with open('songdata-with-years.csv') as csv_file1: 
        csv_reader = csv.reader(csv_file1, delimiter=',')
        for row in csv_reader:
            data.append([row[0], row[1], row[2]])

    csv_file1.close() 
    print("file 1 closed")    

    # add lyric string to correct row in data
    dataRow = 1
    with open('songdata.csv') as csv_file2: 
        csv_reader = csv.reader(csv_file2, delimiter=',')
        for row in csv_reader:
            if dataRow < len(data):
                if data[dataRow][0] != "" and data[dataRow][1] != "":
                    if row[0] == data[dataRow][0] and row[1] == data[dataRow][1]:
                        data[dataRow].append(row[3])
                        dataRow += 1
    
    print("row hits: " + str(dataRow))
    csv_file2.close()  

    with open('songdata-all-fields-1.csv', mode='w') as all_fields_file:
        writer = csv.writer(all_fields_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerows(data)
    all_fields_file.close()        


main()