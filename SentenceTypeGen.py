import random,re
from random import randint
from textblob import TextBlob

#user says 'milk' is subject, first NN in sentence
#have list of order of tags in function ['nn','in']
#find one with 'NN' and replace with 'milk' (2d arrays...?)

global sentencelist
sentencelist = []

def one(bigdict):
    if bigdict['prp'] == []:
        print("'prp' has lots of value!")
    else:
        sentencelist.append(random.choice(bigdict['prp']))
    if bigdict['vbd'] == []:
        print("key 'vbd' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['vbd']))
    if bigdict['dt'] == []:
        print("'dt' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['dt']))
    if bigdict['jj'] == []:
        print("this 'jj' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['jj']))
    if bigdict['nn'] == []:
        print("this 'nn' key has no value!")
    else:
        sentencelist.append(random.choice(bigdict['nn']))
def two(bigdict):
    if bigdict['vbd'] == []:
        print("key 'vbd' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['vbd']))
    if bigdict['dt'] == []:
        print("this 'dt' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['dt']))
    if bigdict['jj'] == []:
        print("this 'jj' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['jj']))
    if bigdict['nn'] == []:
        print("this 'nn' key has no value!")
    else:
        sentencelist.append(random.choice(bigdict['nn']))

def three(bigdict):
    if bigdict['prp'] == []:
        print("key 'prp' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['prp']))
    if bigdict['vbd'] == []:
        print("'vbd' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['vbd']))
    if bigdict['dt'] == []:
        print("'dt' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['dt']))
    if bigdict['jj'] == []:
        print("'jj' key has no value!")
    else:
        sentencelist.append(random.choice(bigdict['jj']))
    if bigdict['nn'] == []:
        print("'nn' key has no value!")
    else:
        sentencelist.append(random.choice(bigdict['nn']))
    if bigdict['in'] == []:
        print("'in' key has no value!")
    else:
        sentencelist.append(random.choice(bigdict['in']))
    if bigdict['prp$'] == []:
        print("'prp$' key has no value!")
    else:
        sentencelist.append(random.choice(bigdict['prp$']))
    if bigdict['nn'] == []:
        print("'nn' key has no value!")
    else:
        sentencelist.append(random.choice(bigdict['nn']))
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
    if bigdict['in'] == []:
        print("'in' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['in']))
    if bigdict['dt'] == []:
        print("'dt' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['dt']))
    if bigdict['nns'] == []:
        print("'nns' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['nns']))
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

    if bigdict['jj'] == []:
        print("'jj' key hole has no value!")
    else:
        sentencelist.append(random.choice(bigdict['jj']))
    if bigdict['jjs'] == []:
        print("'jjs' key has no value!")
    else:
        sentencelist.append(random.choice(bigdict['jjs']))
    if bigdict['in'] == []:
        print("'in' key has no value!")
    else:
        sentencelist.append(random.choice(bigdict['in']))
    if bigdict['prp'] == []:
        print("'prp' key has no value!")
    else:
        sentencelist.append(random.choice(bigdict['prp']))
    if bigdict[c] == []:
        print("this",c,"key has no value!")
    else:
        sentencelist.append(random.choice(bigdict[c]))
    if bigdict['jj'] == []:
        print("jj key has no value!")
    else:
        sentencelist.append(random.choice(bigdict['jj']))

def five(bigdict):
    if bigdict['nn'] == []:
        print("key 'nn' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['nn']))
    if bigdict['vbz'] == []:
        print("key 'vbz' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['vbz']))
    if bigdict['rb'] == []:
        print("key 'rb' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['rb']))
    if bigdict['jj'] == []:
        print("key 'jj' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['jj']))
    if bigdict['in'] == []:
        print("key 'in' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['in']))
    if bigdict['prp'] == []:
        print("key 'prp' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['prp']))

def six(bigdict):
    if bigdict['prp$'] == []:
        print("key 'prp$' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['prp$']))
    if bigdict['nn'] == []:
        print("key 'nn' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['nn']))
    if bigdict['vbz'] == []:
        print("key 'vbz' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['vbz']))
    if bigdict['jj'] == []:
        print("key 'jj' has no value!")
    else:
        sentencelist.append(random.choice(bigdict['jj']))
    #print(sentencelist)

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
