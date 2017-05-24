import re
from re import sub
import time
import cookielib
from cookielib import CookieJar
import urllib2
from urllib2 import urlopen
import difflib

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

keyWord = 'samsung'

def getTweet():
    oldTweet = []
    newTweet = []
    simArray = [.5,.5,.5,.5,.5]
    while 1 < 2:
        try:
            sourceCode = opener.open('https://twitter.com/search/realtime?q=' + keyWord + '&src=hash').read()
            splitSource = re.findall(r'<p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">(.*?)</p>', sourceCode)

            for item in splitSource:
                print '-----------------------------------------'
                aTweet = re.sub(r'<.*?>', '', item)
                print aTweet
                newTweet.append(aTweet)
                print '-----------------------------------------'
                print ''
                
            comparison = difflib.SequenceMatcher(None, newTweet, oldTweet)
            sim = comparison.ratio()
            print '############'
            print sim
            simArray.append(sim)
            simArray.remove(simArray[0])
            waitMultiplier = reduce(lambda x, y: x+y, simArray)/len(simArray)

            oldTweet = [None]
            for eachItem in newTweet:
                oldTweet.append(eachItem)

            newTweet = [None]
            time.sleep(waitMultiplier*45)
        


        
        except Exception, e:
            print str(e)
            print 'Error in the main'
            return ''




getTweet()
