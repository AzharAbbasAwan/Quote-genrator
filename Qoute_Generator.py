#!Python3
import sys
import json
import random
data=json.load( open('quotes.json'))

class Quote:
    index=random.randint(1,100)
    def __init__(self,data):
        self.data=data
    def getAuthor(self):
        return self.data[Quote.index]['quoteAuthor']
    def getQuote(self):
        return self.data[Quote.index]['quoteText']

quote=Quote(data)
title="-    "+quote.getAuthor()
message=quote.getQuote()

'''
print("\n"+quote.getAuthor())
print("\n\t'",quote.getQuote(),"'\n")
'''
#
