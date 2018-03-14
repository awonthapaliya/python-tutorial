'''
Created on Mar 7, 2018

@author: awon
'''
def add(a,b):
    return a+b

def add_fixed_value(a):
    y=5
    return y+a

def substract(a,b):
    if a < b:
        return a + b
            
    return a-b


def loop_test():
    i = 0
    for i in range(20):
        print i
   
      



def lower_case(a):
    return a.lower()

def upper_case(a):
    return a.upper()


print substract(3,2)
print loop_test()

print lower_case('AWON')

print upper_case('awon')


print 'this is a text plus a number ' + str(10)

