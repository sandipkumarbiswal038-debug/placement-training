class Demo:
	def __init__(self,x,y): #parameter constructor
		self.x=x
		self.y=y #instance variable
print("enter two values")
ob=Demo(int(input()),int(input()))
print("display two object values")
print(ob.x,ob.y)

"""
enter two values
2
3
display two object values
2 3
"""