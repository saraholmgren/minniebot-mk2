import random,re
import current
from textblob import TextBlob

def writeout(words,question):
        r = ''
        file = open('testwords.txt','r+')
        #file.truncate()
        words.extend(question)
        r = ' '.join(words)
        file.write(r)
        file.close()
writeout(words,question)
