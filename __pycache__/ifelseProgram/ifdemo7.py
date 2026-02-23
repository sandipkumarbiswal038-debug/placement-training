"""
Wap take emp salary from keyboard if Sal>=5000
"""

print("enter basic salary")
sal=float(input())
da,hra=0,0
if sal>=5000:
	da=sal*0.3
	hra=sal*0.2
totalsalary=sal+da+hra
print("basic sal=",totalsalary)
print("da=",totalsalary)
print("hra=",totalsalary)
print("total salary=",totalsalary)
