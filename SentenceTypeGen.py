import random,re
from random import randint
from textblob import TextBlob

#user says 'milk' is subject, first NN in sentence
#have list of order of tags in function ['nn','in']
#find one with 'NN' and replace with 'milk' (2d arrays...?)

global sentencelist
sentencelist = []

def one(bigdict):
    onelist = ['prp','vbd','dt','jj','nn']
    for x in onelist:
        if bigdict[x] == []:
            print("key '",x,"' has no value!")
        else:
            sentencelist.append(random.choice(bigdict[x]))
def two(bigdict):
    twolist = ['vbd','dt','jj','nn']
    for x in twolist:
        if bigdict[x] == []:
            print("key '",x,"' has no value!")
        else:
            sentencelist.append(random.choice(bigdict[x]))

def three(bigdict):
    z = randint(1,2)
    if z == 1:
        y = 'vbd'
    else:
        y = 'vbp'
    threelist = ['prp',y,'dt','jj','nn','in','prp$','nn',y]
    for x in threelist:
        if bigdict[x] == []:
            print("key '",x,"' has no value!")
        else:
            sentencelist.append(random.choice(bigdict[x]))
    
def four(bigdict):
    z = randint(1,2)
    if z == 1:
        c = 'vbd'
    elif z == 2:
        c = 'vbp'
    fourlist = ['in','dt','nns',c,'jj','jjs','in','prp',c,'jj']
    for x in fourlist:
        if bigdict[x] == []:
            print("key '",x,"' has no value!")
        else:
            sentencelist.append(random.choice(bigdict[x]))
    
def five(bigdict):
    fivelist = ['nn','vbz','rb','jj','in','prp']
    for x in fivelist:
        if bigdict[x] == []:
            print("key '",x,"' has no value!")
        else:
            sentencelist.append(random.choice(bigdict[x]))

def six(bigdict):
    sixlist = ['prp$','nn','vbz','jj']
    for x in sixlist:
        if bigdict[x] == []:
            print("key '",x,"' has no value!")
        else:
            sentencelist.append(random.choice(bigdict[x]))

def pick_type(y,bigdict):
    if y == 1:
        one(bigdict)
    elif y == 2:
        two(bigdict)
    elif y == 3:
        three(bigdict)
    elif y == 4:
        four(bigdict)
    elif y == 5:
        five(bigdict)
    elif y == 6:
        six(bigdict)
