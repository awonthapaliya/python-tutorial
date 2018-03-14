'''
Created on Mar 9, 2018

@author: awon
'''


class Employee:
   'Common base class for all employees'
   empCount = 0

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

#del emp2.name


emp2.displayEmployee()


print Employee.__doc__

print hasattr(emp1, "age")

print getattr(emp1, "salary")