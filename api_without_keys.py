import time,random,sys,current
from current import *
from tumblpy import Tumblpy

t = Tumblpy('w','x','y','z')

def makerandomthought():
    print("getting random thought...")
    post_text = current.randomthought()
    print(type(post_text))

    t.post("blog/"+['minnie-bot']+"/post",params={'type':'text',
                                                  'tags':'random thought',
                                                  'body':str(post_text)
                                                  })
makerandomthought()
