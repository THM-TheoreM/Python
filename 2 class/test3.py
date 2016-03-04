class Vector:
	
	def __init__(self,a,b):
		self.a=a
		self.b=b

	def __str__(self):   #basic method overload
		return 'Vector (%d, %d)' % (self.a,self.b)
   
	def __add__(self,other):   #operator overload
		return Vector(self.a+other.a,self.b+other.b)

v1=Vector(2,10)
v2=Vector(5,-2)
print str(v1)
print v1 + v2