import random,re
from random import randint
from textblob import TextBlob

#user says 'milk' is subject, first NN in sentence
#have list of order of tags in function ['nn','in']
#find one with 'NN' and replace with 'milk' (2d arrays...?)

global sentencelist
sentencelist = []

def one(bigdict):
    list1 = ['prp','vbd','dt','jj','nn']
    for x in list1:
        if bigdict[x] == []:
            print(x," has lots of value!")
        else:
            sentencelist.append(random.choice(bigdict[x]))

def two(bigdict):
    list1 = ['vbd','dt','jj','nn']
    for x in list1:
        if bigdict[x] == []:
            print(x," has no value!")
        else:
            sentencelist.append(random.choice(bigdict[x]))

def three(bigdict):
    list1 = ['prp','vbd','dt','jj','nn','in','prp$','nn']
    for x in list1:
        if bigdict[x] == []:
            print(x," key has no value!")
        else:
            sentencelist.append(random.choice(bigdict[x]))
    z = randint(1,2)
    if z == 1:
        if bigdict['vbd'] == []:
            print("'vbd' key has no value!")
        else:
            sentencelist.append(random.choice(bigdict['vbd']))
    elif z == 2:
        if bigdict['vbp'] == []:
            print("'vbd' key has no value!")
        else:
            sentencelist.append(random.choice(bigdict['vbp']))

def four(bigdict):
    list1 = ['in','dt','nns']
    for x in list1:
        if bigdict[x] == []:
            print(x," has no value!")
        else:
            sentencelist.append(random.choice(bigdict['in']))
    z = randint(1,2)
    a = 0
    if z == 1:
        if bigdict['vbd'] == []:
            print("'vbd' key has no value!")
        else:
            sentencelist.append(random.choice(bigdict['vbd']))
    elif z == 2:
        if bigdict['vbp'] == []:
            print("'vbd' key has no value!")
    b = a+z
    if b == 1:
        c = 'vbd'
    else:
        c = 'vbp'
    list2 = ['jj','jjs','in','prp',c,'jj']
    for x in list2:
        if bigdict[x] == []:
            print(x," key hole has no value!")
        else:
            sentencelist.append(random.choice(bigdict[x]))

def five(bigdict):
    list1 = ['nn','vbz','rb','jj','in','prp']
    for x in list1:
        if bigdict[x] == []:
            print("key '",x,"' has no value!")
        else:
            sentencelist.append(random.choice(bigdict[x]))

def six(bigdict):
    list1 = ['prp$','nn','vbz','jj']
    for x in list1:
        if bigdict[x] == []:
            print(x," has no value!")
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
