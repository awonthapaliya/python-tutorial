'''
Created on Mar 14, 2018

@author: awon
'''


def check_exist1(a):
    if(a == 'a'):
        return 1;
    else:
        return 0
    

def check_exist2(a):
    if(a == 'a'):
        return True
    else:
        return None


if(check_exist1('a')):
    print "A1 present"
     
if(check_exist2('b')):
    print "A2 present"
    
if(check_exist1('b')):
    print "A3 present"

if(check_exist2('a')):
    print "A4 present"
