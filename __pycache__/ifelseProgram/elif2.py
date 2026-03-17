#wap take a number from keyboard check no is sd dd td od +ve number
print("enter a number")
no=int(input())
if no<0:
	no=-no
if no>=0 and no<=9:
    print("no is single digit ")
elif no>=10 and no<=99:
    print("no is double digit ")
elif no>=100 and no<=999:
    print("no is triple digit ")
else:
    print("no is Other Digit ")
"""
enter a number
23
no is double digit number
"""