# conclusions.py
# Ezra Zinberg
# calculates the average of each sentiment metric for all artists!
# reads from artists-with-sentiment.csv

import csv

def main():
    # averages = [avgPosAvg,   avgNegAvg,   avgObjAvg,
    #             totalPosAvg, totalNegAvg, totalObjAvg,
    #             earlyPosAvg, earlyNegAvg, earlyObjAvg,
    #             latePosAvg,  lateNegAvg,  lateObjAvg]
    averages = [0,0,0,
                0,0,0,
                0,0,0,
                0,0,0]

    avgPosVal = 0
    avgNegVal = 0
    avgObjVal = 0
    totalPosVal = 0
    totalNegVal = 0
    totalObjVal = 0
    
    rows = 0

    # realpython.com
    # new read csv
    with open('artists-with-sentiment-2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            rows += 1
            
            if rows == 1:
                continue

            artist = row[0]
            print(artist)
            avg = row[1].strip('][').split(', ')
            total = row[2].strip('][').split(', ')
            early = row[3].strip('][').split(', ')
            late = row[4].strip('][').split(', ')

            for i in range(len(avg)):
                currentVal = float(avg[i])

                if i == 0 and currentVal > avgPosVal:
                    avgPosVal = currentVal
                    avgPosChamp = artist
                if i == 1 and currentVal > avgNegVal:
                    avgNegVal = currentVal
                    avgNegChamp = artist
                if i == 2 and currentVal > avgObjVal:
                    avgObjVal = currentVal
                    avgObjChamp = artist
                
                averages[i] += currentVal
            
            for i in range(len(total)):
                currentVal = float(total[i])

                if i == 0 and currentVal > totalPosVal:
                    totalPosVal = currentVal
                    totalPosChamp = artist
                if i == 1 and currentVal > totalNegVal:
                    totalNegVal = currentVal
                    totalNegChamp = artist
                if i == 2 and currentVal > totalObjVal:
                    totalObjVal = currentVal
                    totalObjChamp = artist
                
                averages[i + 3] += currentVal
            
            for i in range(len(early)):
                currentVal = float(early[i])
                averages[i + 6] += currentVal
            
            for i in range(len(late)):
                currentVal = float(late[i])
                averages[i + 9] += currentVal
            
    rows -= 1
    for i in range(len(averages)):
        averages[i] = str(averages[i] / rows)
    
    print("Averages over all " + str(rows) + " artists:")
    print()
    print("Average, positive:      " + averages[0])
    print("Average, negative:      "+ averages[1])
    print("Average, objective:     "+ averages[2])
    print("Delta-Total, positive:  "+ averages[3])
    print("Delta-Total, negative:  "+ averages[4])
    print("Delta-Total, objective: "+ averages[5])
    print("Delta-Early, positive:  "+ averages[6])
    print("Delta-Early, negative:  "+ averages[7])
    print("Delta-Early, objective: "+ averages[8])
    print("Delta-Late, positive:   "+ averages[9])
    print("Delta-Late, negative:   "+ averages[10])
    print("Delta-Late, objective:  "+ averages[11])
    print()
    print("Greatest average positive:      " + avgPosChamp)
    print("Greatest average negative:      " + avgNegChamp)
    print("Greatest average objective:     " + avgObjChamp)
    print("Greatest delta-total positive:  " + totalPosChamp)
    print("Greatest delta-total negative:  " + totalNegChamp)
    print("Greatest delta-total objective: " + totalObjChamp)

main()