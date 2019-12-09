# getSentiment.py
# Ezra Zinberg


from nltk.corpus import sentiwordnet as swn
from nltk import word_tokenize
from nltk.corpus import stopwords
import sys

# sortedSent array holds [date, trackname, [pos, neg, obj]], sorted by date
sortedSent = [[]]

#  takes lyric string. returns [avgpossent, avgnegsent, avgobjsent]
def average(lyric):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(lyric)
    lowercase = []
    for word in word_tokens:
        lowercase.append(word.lower())
    filtered_lyric = [w for w in lowercase if not w in stop_words]

    posSum = 0
    negSum = 0
    objSum = 0
    wordcount = 0

    for s in filtered_lyric:        
        syns = list(swn.senti_synsets(s))
        # print(syns)
        if (len(syns) > 0):
            word = syns[0]
            posSum += word.pos_score()
            negSum += word.neg_score()
            objSum += word.obj_score()
            wordcount += 1

    avgPos = posSum/wordcount
    avgNeg = negSum/wordcount
    avgObj = objSum/wordcount

    return [avgPos, avgNeg, avgObj]


# def main():
#     # lyric = ("Just gonna stand there and watch me burn  But that's alright, because I like the way it hurts  Just gonna stand there and hear me cry  But that's alright, because I love the way you lie  I love the way you lie  I can't tell you what it really is  I can only tell you what it feels like  And right now there's a steel knife, in my windpipe  I can't breathe, but I still fight, while I can fight  As long as the wrong feels right, it's like I'm in flight  ")
#     # print(average(lyric))

# main()