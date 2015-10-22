str='asdfsD1df'

def l2u(str):
	ret=''
	for c in str:
		ret += chr(ord(c)&(0xff^0x20)) if c.isalpha() else c;
	return ret

def u2l(str):
	ret=''
	for c in str:
		ret += chr(ord(c)|0x20) if c.isalpha() else c;
	return ret

print (l2u(str))
print (u2l(str))
