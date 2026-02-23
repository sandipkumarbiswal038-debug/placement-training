ch='A'
print(ch)
print(ord(ch))

ch=80
print(ch)
print(chr(ch))

ch='A'
print(ch)
ch=chr(ord(ch)+32)
print(ch)

import sys
print("enter a char")
ch=input()
if len(ch)>1:
	print("one char allow")
	sys.exit()
if ch>='A' and ch<='Z':  #if 65<ch<90
	