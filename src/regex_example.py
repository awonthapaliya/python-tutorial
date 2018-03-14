'''
Created on Mar 9, 2018

@author: awon
'''

import re

line = "Fusemachines has a lot of amazing pEopLe."

search_result = re.match(r'(.*)people(.*)', line, re.MULTILINE | re.IGNORECASE)

if search_result:
    print "search.group() : ", search_result.group()
    print "search.group(1) : ", search_result.group(1)
    print "search.group(2) : ", search_result.group(2)
else:
    print "Nothing found!!"

