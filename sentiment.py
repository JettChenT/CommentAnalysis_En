import nltk
import math
from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def getsent(text, analyzer):
    try:
        score = analyzer.polarity_scores(text)
        return score
    except:
        return "error"


def average(list):
    return sum(list) / len(list)


def analysis(clist):
    # core algorithm, the exciting part
    # improve over time
    print(clist)
    slist = []
    for s in clist:
        sen = getsent(s, analyzer)
        if sen != "error":
            slist.append(sen)
    for i in range(len(slist)):
        slist[i] = round(slist[i], 1)
    print(slist)
    retlist = []
    for n in range(-10, 11):
        retlist.append(slist.count(n / 10))
    return retlist
