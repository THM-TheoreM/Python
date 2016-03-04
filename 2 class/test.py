class Parent:   #define parentclass
	
	parentAttr=100
	
	def __init__(self):
		print 1
	
	def a(self):
		print 2
		
	def b(self,attr):
		Parent.parentAttr=attr
		
	def c(self):
		print Parent.parentAttr
		
class Child(Parent):   #define subclass
	
	def __init__(self):
		print 3
		
	def d(self):
		print 4
		
child=Child()
child.a()
child.b(200)
child.c()
child.d()