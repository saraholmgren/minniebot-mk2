import sys,random,re,nltk
import SentenceTypeGen
#import ReplyGen
from SentenceTypeGen import *
#from ReplyGen import *
from textblob import TextBlob
from random import randint

global words
words = []
bigdict = {'cc':[],'cd':[],'dt':[],'ex':[],'fw':[],'in':[],'jj':[],'jjr':[],'jjs':[],'ls':[],'md':[],'nn':[],'nns':[],'nnp':[],'nnps':[],'pdt':[],'pos':[],'prp':[],'prp$':[],'rb':[],'rbr':[],'rbs':[],'rp':[],'sym':[],'to':[],'uh':[],'vb':[],'vbd':[],'vbg':[],'vbn':[],'vbp':[],'vbz':[],'wdt':[],'wp':[],'wp$':[],'wrb':[]}

def ReadIn():
    global file
    try:
        file = open('newwords.txt','r+')
        filestr = file.read().split(" ")
        for x in filestr:
            words.append(x)
        print('read file newwords.txt -- WORDS --')
        file.close()
    except BaseException as error:
        print(error)
ReadIn()

def PosTagger():
    for x in words:
        sort = TextBlob(x).tags[0]
        word_tag = sort[1]
        bigdict[sort[1].lower()].append(sort[0])
PosTagger()

def get_sentence():
    y = randint(1,6)
    SentenceTypeGen.pick_type(y,bigdict)
get_sentence()

def grammar(sentencelist):
    randpunc = randint(1,3)
    if randpunc == 1:
        d = '.'
        sentence_str = ' '.join(sentencelist)
        grammar_str = "".join((sentence_str,d))
        print(grammar_str)
    elif randpunc == 2:
        f = '!'
        sentence_str = ' '.join(sentencelist)
        grammar_str = "".join((sentence_str,f))
        print(grammar_str)
    else:
        g = '?'
        sentence_str = ' '.join(sentencelist)
        grammar_str = "".join((sentence_str,g))
        print(grammar_str)       
grammar(sentencelist)

def answer(question):
    low = question.lower()
    question = re.sub('[^\w]', ' ',  low).split() #list
    #print(question)
    #ReplyGen.writeout(words,question)
    def writeout(words,question):
            r = ''
            file = open('newwords.txt','r+')
            file.truncate()
            words.extend(question)
            r = ' '.join(words)
            file.write(r)
            file.close()
    writeout(words,question)

##for word,tag in TextBlob("x").tags:
##    print(word,",",tag)