class Parent:

	def a(self):
		print 1
		
class Child(Parent):

	def a(self):
		print 2

child=Child()          
child.a()   #override         