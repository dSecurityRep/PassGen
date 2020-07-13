import os.path

#geting info

nick = str(input("Enter mickname: "))
date = str(input("Enter year of birth: "))

#generating passwords

v1 = nick + date
v2 = date + nick

v3 = nick + "x123"

v4 = nick + "z123"

#creating brutt base

passwords = [v1, v2, v3, v4]

for p in passwords:
	print(p)