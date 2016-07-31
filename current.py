import sys,random,re,nltk,os,SentenceTypeGen,LanguageHandler
from SentenceTypeGen import *
from LanguageHandler import *
from textblob import TextBlob
from random import randint

global words
words = []
badwords = []
bigdict = {'cc':[],'cd':[],'dt':[],'ex':[],'fw':[],'in':[],'jj':[],'jjr':[],'jjs':[],'ls':[],'md':[],'nn':[],'nns':[],'nnp':[],'nnps':[],'pdt':[],'pos':[],'prp':[],'prp$':[],'rb':[],'rbr':[],'rbs':[],'rp':[],'sym':[],'to':[],'uh':[],'vb':[],'vbd':[],'vbg':[],'vbn':[],'vbp':[],'vbz':[],'wdt':[],'wp':[],'wp$':[],'wrb':[]}

def ReadIn():
    global file,words,badwords
    try:
        file = open('newwords.txt','r+')
        filestr = file.read().split(" ")
        for x in filestr:
            words.append(x)
        print('read file')
        file.close()
    except BaseException as e:
        print(e)
    try:
        file = open('badwords.txt','r+')
        filestr = file.read().split(" ") 
        for x in filestr:
            badwords.append(x)
        print('read file')
        file.close()
    except BaseException as e:
        print(e)
ReadIn()

def BadWords(questions):
    for x in badwords:
        if x in questions:
            print(x,"is a blocked word.")
            questions.remove(x)
        else:
            pass

def randomthought():
    def PosTagger(words): 
        for x in words:
            sort = TextBlob(x).tags[0]
            word_tag = sort[1]
            bigdict[sort[1].lower()].append(sort[0])
    PosTagger(words)

    def get_sentence():
        y = randint(1,6)
        SentenceTypeGen.pick_type(y,bigdict)
    get_sentence()

    def grammar(sentencelist):
        randlang = randint(1,10)
        randpunc = randint(1,3)
        if randpunc == 1:
            d = '.'
            sentence_str = ' '.join(sentencelist)
            grammar_str = "".join((sentence_str,d))
            try:
                IsAnswer
            except NameError: # if it runs through randomthought()
                if randlang == 10:
                    LanguageHandler.pick_lang(grammar_str)
                else:
                    print(grammar_str)
            else: # if runs through answer()
                if u != 'en':
                    LanguageHandler.CorrectLang(u,grammar_str)
                else:
                    print(grammar_str)
            while len(sentencelist) > 0:
                sentencelist.pop()
        elif randpunc == 2:
            f = '?'
            sentence_str = ' '.join(sentencelist)
            grammar_str = "".join((sentence_str,f))
            try:
                IsAnswer
            except NameError: 
                if randlang == 10:
                    LanguageHandler.pick_lang(grammar_str)
                else:
                    print(grammar_str)
            else: 
                if u != 'en':
                    LanguageHandler.CorrectLang(u,grammar_str)
                else:
                    print(grammar_str)
            while len(sentencelist) > 0:
                sentencelist.pop()
        else:
            h = '!'
            sentence_str = ' '.join(sentencelist)
            grammar_str = "".join((sentence_str,h))
            try:
                IsAnswer
            except NameError:
                if randlang == 10:
                    LanguageHandler.pick_lang(grammar_str)
                else:
                    print(grammar_str)
            else:
                if u != 'en':
                    LanguageHandler.CorrectLang(u,grammar_str)
                else:
                    print(grammar_str)
            while len(sentencelist) > 0:
                sentencelist.pop()
    grammar(sentencelist)


def answer(question):
    global IsAnswer,detected,u
    IsAnswer = True
    DetectLang = TextBlob(question)
    detected = DetectLang.detect_language()
    if detected == 'en':
        print("language detected: en")
        u = 'en'
        print(len(words),"len(words)")
        low = question.lower()
        questions = re.sub('[^\w]',' ',low).split() #list
        BadWords(questions)
        print(questions)
        def writeout(words,question,IsAnswer):
            r = []
            if len(words) > 3000:
                a1 = len(questions)
                for x in range(0,a1):
                    words.remove(random.choice(words))
                print(len(words),"len(words)")
            else:
                pass
            os.remove('newwords.txt')
            file = open('newwords.txt','w')
            words.extend(questions)
            r.extend(words)
            s = ' '.join(r)
            file.write(s)
        writeout(words,question,IsAnswer)
        randomthought()
    else:
        u = detected
        print("language detected:",u)
        randomthought()
        
##for word,tag in TextBlob("x").tags:
##    print(word,",",tag)
