#wap check no is +ve or -ve if provide zero no output
print("enter a number")
no=int(input())
if no==0:
	print("zero")
else:
	if no>0:
		print("+ve")
	else:
		print("-ve")
"""
syntax:
if c1:
	if c2:
		true part
	else:
		false part
else:
	false part

#wap check no is +ve or -ve if provide zero output zero
print("enter a number ")
no=int(input())
if n0!=0:
	if n0>0:
		print("+ve")
	else:
		print("-ve")
else:
	print("zero")

syntax3:
if c1:
	c1 block execute
else:
	if c2:

syntax4:
if c1:
	if c2:
		c2 true block
	else:
		c2 false block
else:
	if c3:
		c3 true block
	else:
		c3 false block



"""
#wap take 3 no from keyboard display biggest number
print("enter three nos")
no1=int(input())
no2=int(input())
no3=int(input())
if no1>=no2:
	if no1>=no3:
		print("first no is bigger",no1)
	else:
		print("third no is bigger",no3)
else:
	if no2>=no3:
		print("second no is bigger",no2)
	else:
		print("third no is bigger",no3)

"""
enter three nos
2
3
4
third no is bigger 4
"""