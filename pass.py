import os.path

#geting info

nick = str(input("Enter nickname: "))
date = str(input("Enter year of birth: "))
name = str(input("Enter name [or - ]: "))

#generating passwords

x = "x123"
z = "z123"

v1 = nick + date
v2 = date + nick

v3 = nick + x

v4 = nick + z

if name == "-":
	v5 = ""
	v6 = ""

else:
	pass

	v5 = name + x
	v6 = name + z

#creating brutt base

passwords = [v1, v2, v3, v4, v5, v6]


for p in passwords:
	print(p)