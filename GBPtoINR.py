#-------------------------------------------------------#
# Webscrapping example :				#
# Queries xe.com and fetches current GBP to INR value   #
#-------------------------------------------------------#

import urllib, re, sys

url = 'http://www.xe.com/currencyconverter/convert/?From=GBP&To=INR'

def Banner(text):
    print "=" * 40
    print text
    print "=" * 40
    sys.stdout.flush()


def GBPtoINR(url):
    sourcecode = urllib.urlopen(url)
    htmltext = sourcecode.read()
    #pattern = re.compile('\'uccResultAmount\'>(.+?)<\/span>')
    pattern = re.compile('<span class=\'uccResultAmount\'>(.+?)</span>')
    CurrentRate = re.findall(pattern, htmltext)
    print "Current Pound to INR rate is", CurrentRate[0]


Banner("Quering internet for exchange rate:")
GBPtoINR(url)

