import random,re
from random import randint
from textblob import TextBlob

def get_lower(x):
    lowercase = x.lower()
    print(lowercase)

def Japanese(grammar_str):
    languageblob = TextBlob(grammar_str)
    japanese = languageblob.translate(from_lang='en',to='ja')
    print(japanese)
def Korean(grammar_str):
    languageblob = TextBlob(grammar_str)
    korean = languageblob.translate(from_lang='en',to='ko')
    print(korean)
def French(grammar_str):
    languageblob = TextBlob(grammar_str)
    french = languageblob.translate(from_lang='en',to='fr')
    x = french
    get_lower(x)
def Spanish(grammar_str):
    languageblob = TextBlob(grammar_str)
    spanish = languageblob.translate(from_lang='en',to='es')
    x = spanish
    get_lower(x)
def German(grammar_str):
    languageblob = TextBlob(grammar_str)
    german = languageblob.translate(from_lang='en',to='de')
    x = german
    get_lower(x)
def Italian(grammar_str):
    languageblob = TextBlob(grammar_str)
    italian = languageblob.translate(from_lang='en',to='it')
    x = italian
    get_lower(x)
def Finnish(grammar_str):
    languageblob = TextBlob(grammar_str)
    finnish = languageblob.translate(from_lang='en',to='fi')
    x = finnish
    get_lower(x)
def Hebrew(grammar_str):
    languageblob = TextBlob(grammar_str)
    hebrew = languageblob.translate(from_lang='en',to='iw')
    print(hebrew)

def CorrectLang(u,grammar_str):
    if u == 'ja':
        Japanese(grammar_str)
    elif u == 'ko':
        Korean(grammar_str)
    elif u == 'fr':
        French(grammar_str)
    elif u == 'es':
        Spanish(grammar_str)
    elif u == 'de':
        German(grammar_str)
    elif u == 'it':
        Italian(grammar_str)
    elif u == 'fi':
        Finnish(grammar_str)
    else:
        Hebrew(grammar_str)
        
def pick_lang(grammar_str):
    picklanguage = randint(1,8)
    if picklanguage == 1:
        Japanese(grammar_str)
    elif picklanguage == 2:
        Korean(grammar_str)
    elif picklanguage == 3:
        French(grammar_str)
    elif picklanguage == 4:
        Spanish(grammar_str)
    elif picklanguage == 5:
        German(grammar_str)
    elif picklanguage == 6:
        Italian(grammar_str)
    elif picklanguage == 7:
        Finnish(grammar_str)
    else:
        Hebrew(grammar_str)
