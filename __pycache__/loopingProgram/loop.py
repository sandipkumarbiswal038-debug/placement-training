"""
looping
__________

#wap display hi msg 5 times
print("hi")
print("hi")
print("hi")
print("hi")
print("hi")
 
some statement repeated continously then choose loop concept 

there are 2 types of loop 
(1)while 
(2)for in
every loop there 3 section

(1)initialization / start value
(2)condition / stop value
(2)updateable / step value // inc/dec section

syntax of while loop
______________________

initialization 
while condition:
	.......
	.....
	updateable
"""
n=10
answer=2
while n>0:
	answer=answer+n
	n=n+1
print(answer)