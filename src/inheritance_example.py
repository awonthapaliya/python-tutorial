'''
Created on Mar 9, 2018

@author: awon
'''


class Parent:
    'Parent class' 
    parent_attribute = 100
    
    __attr1 = 10
    
    def __init__(self):
        print "Parent constructor called"
    
    def parentMethod(self):
        print "Parent method called..."
        
    def setAttribute(self, attribute):
        Parent.parent_attribute = attribute
        
    def getAttribute(self):
        print "Parent attribute :", Parent.parent_attribute
        
    def myMethod (self):
        print "Parent my Method called..."


#Child can inherit parent by
class Child(Parent):
    
    def __init__(self):
        print "Child constructor called"
    
    def childMethod(self):
        print "Child method called..."
        
    def myMethod(self):
        print "Child my Method called.."
        
    
c = Child()
c.childMethod()
# calling parent method by child object
c.parentMethod()
# getting parent attribute 
c.getAttribute()  

# change attribute value     
c.setAttribute(20000)

# checking a
c.getAttribute()

c.myMethod()
