import re
from re import sub
import time
import http.cookiejar
from http.cookiejar import CookieJar
import urllib.request
from urllib.request import urlopen
import difflib
import functools

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

#Unfortunately this version does not support spaces in the key word
keyWord = 'Samsung'

def getTweet():
    oldTweet = []
    newTweet = []
    simArray = [.5,.5,.5,.5,.5]
    while 1 < 2:
        try:
            sourceCode = opener.open('https://twitter.com/search/realtime?q=' + keyWord + '&src=hash').read()
            splitSource = re.findall(r'<p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">(.*?)</p>', str(sourceCode))
            for item in splitSource:
                print('-----------------------------------------')
                aTweet = re.sub(r'<.*?>', '', item)
                print (aTweet)
                newTweet.append(aTweet)
                print ('-----------------------------------------')
                print ('')

            comparison = difflib.SequenceMatcher(None, newTweet, oldTweet)
            sim = comparison.ratio()
            print ('############')
            print ("Similarity " + str(sim))
            simArray.append(sim)
            simArray.remove(simArray[0])
            waitMultiplier = functools.reduce(lambda x, y: x+y, simArray)/len(simArray)

            oldTweet = [None]
            for eachItem in newTweet:
                oldTweet.append(eachItem)

            newTweet = [None]
            time.sleep(waitMultiplier*45)
        except:
            print("HELP!")



if __name__ == '__main__':
    getTweet()

