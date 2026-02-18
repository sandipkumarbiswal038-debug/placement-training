"""operator is a symbol that operate the operator
+ - *,.....

types of operator:-
1-unary:

-5

2-binary:

a+b

3-ternary:

**	power
*	mult
/	floor division(q)
//	moduls(reminder)

10/3 3.33333(10/3 	c c++ java 3 10.0/3 3.33333)
10//3 	3
10%3  	1
10**3 	1000
5/2 	2.5


display first digit

1245%1000	1
367%100 	3
45%10 		4


display last digit
1245//1000	5
367//100 	7
45//10 		5


precdence:

1 	()
2 	**  -  + (unary)
3 	// /  * % (L to R)
4 	
5
6
7
8
9
10

10*3//4
30//4
7

10//3*4
3*4
12

R to L
______
a=b=5

Assignment operator(=)
_________________________

variable=variable/constant/expression

a=10
b=a
c=a+b



10=a   invalid
10=20  invalid
a+b=30 invalid





"""
a=10
print(id(a))
print(a)
b=10
print(id(b))
print(b)

#assigned to 2 operator
a=10
b=a
print(id(a),id(b))
print(a,b)
a=20
print(id(a),a)
b=10
print(id(b),b)


#swapping 2 number using 3rd variable 
a=10
b=20
print("before swapping a=",a,"b=",b)
t=a 
a=b
b=t
print("after swappinga=",a,"b=",b)

#swapping 2 number without using 3rd variable 
a=10
b=20
print("before swapping a=",a,"b=",b)
a=a+b
b=a-b
a=a-b
print("after swappinga=",a,"b=",b)
#    ^ 	bitwise operator

#swapping 2 number without using 3rd variable 

# a=10
# b=2.5
# c="hi"
a,b,c=10,2.5,"hi"
print(a,b,c)


a=10,2.5,"hi"
print(a)
print(type(a))  #tuple type
print(id(a))


a=10
b=20
a,b=b,a
print(a,b)

# increment(++) and decrement (--) opertator not available
# ________________________________________________________









#relation operator
#_________________

# < > <=  >= == !=  is not in is is not
# <lessthan
# 2<3	true
# 7<4	false
# 10<20<30	false  in c lang  1  java error

# > graterthan
# 5>3  true
# 10>4>2  true
# 10>5>7   false

# 3==3     true
# 3==4	 false


# 2<=3   true
# 4<=3  false

# 4>=3  true


# 2<3==3<4

# 2<3==5<<3    false
# 2<3!=5<7       true

# is not membership operator
print("e" in "hello")
print("x" in "hello")
print("x" not in "hello")
print(10 in[10,20,30,10])
print(40 in[10,20,30,10])
print(40 not in[10,20,30,10])

# identity operator  is is not
a=10
b=10
print(a is b)
print(a is c)
print(a is not c)
print(a==b)

a=[10]
b=[10]
c=[20]
print(a is b)
print(a is c)
print(a is not c)
print(a==b)


