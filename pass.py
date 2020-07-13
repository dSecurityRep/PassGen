import os.path

#geting info

nick = str(input("Enter nickname: "))
date = str(input("Enter year of birth: "))
name = str(input("Enter name [or - ]: "))

#generating passwords

x = "x123"
z = "z123"

d = (date[2:4])

v1 = nick + date
v2 = date + nick

v3 = nick + x
v4 = nick + z

if name == "-":
	v5 = ""
	v6 = ""

else:
	v5 = name + x
	v6 = name + z

v7 = name + "." + nick
v8 = nick + "." + name

v9 = nick + "4ka"
v10 = nick + "4ik"

v11 = name + "4ka"
v12 = name + "4ik"

v13 = name + "." + nick + "4ka"
v14 = nick + "." + name + "4ka"

v15 = name + "." + nick + "4ik"
v16 = nick + "." + nick + "4ik"

v17 = name + d
v18 = nick + d

v19 = v7 + d
v20 = v8 + d

#creating brutt base

save = open('brut.txt', 'w', encoding = "utf- 8")
save.write(nick + '\n')
save.write(name + '\n')
save.write(v1 + '\n')
save.write(v2 + '\n')
save.write(v3 + '\n')
save.write(v4 + '\n')
save.write(v5 + '\n')
save.write(v6 + '\n')
save.write(v7 + '\n')
save.write(v8 + '\n')
save.write(v9 + '\n')
save.write(v10 + '\n')
save.write(v11 + '\n')
save.write(v12 + '\n')
save.write(v13 + '\n')
save.write(v14 + '\n')
save.write(v15 + '\n')
save.write(v16 + '\n')
save.write(v17 + '\n')
save.write(v18 + '\n')
save.write(v19 + '\n')
save.write(v20 + '\n')
