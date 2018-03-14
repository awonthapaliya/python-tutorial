'''
Created on Mar 9, 2018

@author: awon
'''

# creating a class by keyoword "class"


class Employee:
# doc is defined as follows
   'Common base class for all employees'
   empCount = 0

# "__init__(self)" is the contructor for class
#  classs members can be initialized here
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name, ", Salary: ", self.salary
      
      
emp1 = Employee("Amit", 20000000)

emp1.displayCount()

emp2 = Employee("Alohan", 20000)

emp1.displayCount()

emp1.displayEmployee()
emp2.displayEmployee()

emp1.name = "Awon"
emp1.displayEmployee()
 
# "del" keyword can be used to delete object element
# del emp2.name

emp2.displayEmployee()

# built in function that prints doc defined after class
print Employee.__doc__

# built in function that checks if object has the element
print hasattr(emp1, "age")

# built in function that gets the value of the element
print getattr(emp1, "salary")
