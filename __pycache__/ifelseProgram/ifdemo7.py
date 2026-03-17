"""
Wap take emp salary from keyboard if Sal>=5000 da=30% hra=20% 
if sal<5000 da=20% hra=10% then display basic salary da hra and totalsal
"""

print("enter basic salary")
sal=float(input())
da,hra=0,0
# if sal>=5000:
# 	da=sal*0.3
# 	hra=sal*0.2
# else:
# 	da=sal*0.2
# 	hra=sal*0.1
da=sal*0.3 if sal>=5000 else sal*0.2
hra=sal*0.2 if sal>=5000 else sal*0.1 
totalsalary=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",totalsalary)


"""enter basic salary
2000
basic sal= 2000.0
da= 400.0
hra= 200.0
total salary= 2600.0"""