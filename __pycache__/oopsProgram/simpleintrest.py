class SimpleIntrest:
	def __init__(self,p,t,r):
		self.amount=p
		self.interest=t
		self.time=r 
	def show(self):
		print("Enter Principal Amount: ",self.amount)
		print("Enter Rate of Interest: ",self.interest)
		print("Enter Time: ",self.time)
	def sical(self):
		return self.amount*self.interest*self.time/100	
print("enter principle rate and time ")	
#s1=SimpleIntrest(100,23,4)
s1=SimpleIntrest(float(input()),float(input()),float(input()))
s1.show()
print("Simple Interest =",s1.sical())


"""
Enter Principal Amount:  100
Enter Rate of Interest:  23
Enter Time:  4
Simple Interest = 92.0

Enter Principal Amount:  1222.0
Enter Rate of Interest:  22.0
Enter Time:  2.0
Simple Interest = 537.68
"""
