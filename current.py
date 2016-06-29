import sys,random,re,nltk
from SentenceTypeGen import *
import SentenceTypeGen
from textblob import TextBlob
from random import randint

words = []
bigdict = {'cc':[],'cd':[],'dt':[],'ex':[],'fw':[],'in':[],'jj':[],'jjr':[],'jjs':[],'ls':[],'md':[],'nn':[],'nns':[],'nnp':[],'nnps':[],'pdt':[],'pos':[],'prp':[],'prp$':[],'rb':[],'rbr':[],'rbs':[],'rp':[],'sym':[],'to':[],'uh':[],'vb':[],'vbd':[],'vbg':[],'vbn':[],'vbp':[],'vbz':[],'wdt':[],'wp':[],'wp$':[],'wrb':[]}

def ReadIn():
    global file
    try:
        file = open('allwords.txt','r+')
        filestr = file.read().split(" ")
        for x in filestr:
            words.append(x)
        print('read file allwords.txt -- WORDS --')
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
    d = '.'
    sentence_str = ' '.join(sentencelist)
    grammar_str = "".join((sentence_str,d))
    print(grammar_str)
grammar(sentencelist)

##for word,tag in TextBlob("x").tags:
##    print(word,",",tag)
