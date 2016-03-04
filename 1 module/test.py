class Employee:

	empCount=0
	
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
		Employee.empCount+=1
		
	def displayCount(self):
		print 'Total Employee: %d' % Employee.empCount
		
	def displayEmployee(self):
		print "Name: ", self.name, ", Salary: ", self.salary
		

emp1=Employee('Zara',2000)
emp1.displayCount()
emp1.displayEmployee()
print getattr(emp1,'empCount')
print getattr(emp1,'name')
print getattr(emp1,'salary')
print '\n'

emp2=Employee('Manni',5000)
emp2.displayCount()
emp2.displayEmployee()
print getattr(emp2,'empCount')
print getattr(emp2,'name')
print getattr(emp2,'salary')
print '\n'

print Employee.empCount
print emp1.empCount
print emp2.empCount
print '\n'

emp1.age=7
print getattr(emp1,'age')
emp1.age=8
print getattr(emp1,'age')
del emp1.age
print '\n'

print "Employee.__name__: ", Employee.__name__