"""logical or short circuit operator
_________________________________
or
and 
not
 		 or
op1	 	op2		result
true	true	true
true	false	true
false	true	true
false	false	false

if first operand is true second operand not checking
if first operand is false second operand must checking
any non zero value true
5 	-7
zero value false

5 	or 	7 		5	in  c    1
print(5 or 7) 	o/p: 5

"""
a=10
b=20
print(a>5 or b<12)
print(a<5 or b<12)
print(a<5 or b>12)

print(a>5 and b<12)
print(a<5 and b<12)
print(a<5 and b>12)
print(a>5 and b>12)

print(not 0)
print(not 5)

""""
			and




			not
op 		result
true	false
false	true


"""
a=5
b=7
c=3
a=a+b+c 
c=a*3
b=a//4
print(a,b,c)
a=b>c 
c=5 or b
b=c>3 and b<7
print(a,b,c)
