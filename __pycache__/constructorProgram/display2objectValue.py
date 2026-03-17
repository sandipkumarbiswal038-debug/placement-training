class Demo:
	def __init__(self):
		self.x=int(input())
		self.y=int(input())  #instance variable
print("enter object1 2 values")
ob=Demo()
print("enter object2 2 values")
ob1=Demo()
print("display first object value")
print(ob.x,ob.y)
print("display second object values")
print(ob1.x,ob1.y)

"""
enter object1 2 values
2
2
enter object2 2 values
2
2
display first object value
2 2
display second object values
2 2
"""
