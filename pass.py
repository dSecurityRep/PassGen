import os.path

#geting info

nick = str(input("Enter nickname: "))
date = str(input("Enter year of birth: "))
name = str(input("Enter name [or -]: "))
surname = str(input("Enter surname [or -]: "))

pet = str(input("Enter pet\'s name [or -]: "))

girl = str(input("Enter girlfriend or wife name [or -]: "))
girlnick = str(input("Enter girlfriend or wife nicname [or -]: "))

boy = str(input("Enter boyfriend or hustband name [or -]"))
boynick = str(input("Enter boyfriend or hustband nickname [or -]"))

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

v21 = name + nick
v22 = nick + name

if pet == "-":
	v23 = ""

	v24 = ""
	v25 = ""

	v26 = ""
	v27 = ""

else:
	v23 = pet

	v24 = pet + x
	v25 = pet + z

	v26 = pet + "4ik"
	v27 = pet + "4ka"

if girl == "-":
	v28 = ""
	v29 = ""
	v30 =  ""

	v31 = ""

	v32 = ""
	v33 = ""

	v34 = ""
	v35 = ""
	v36 = ""

	v37 = ""
	v38 = ""

	v39 = ""
	v40 = ""

else:
	v28 = girl
	v29 = girlnick
	v30 = girl + girlnick

	v31 = girlnick + girl

	v32 = girl + "." + girlnick
	v33 = girlnick + "." + girl

	v34 = girl + "4ka"
	v35 = girlnick + "4ka"
	v36 = girlnick + "4ik"

	v37 = girl + x
	v38 = girl + z

	v39 = girlnick + x
	v40 = girlnick + z

if boy == "-":
	v41 = ""
	v42 = ""
	v43 = ""
	v44 = ""
	v45 = ""
	v46 = ""
	v47 = ""
	v48 = ""
	v49 = ""
	v50 = ""
	v51 = ""
	v52 = ""
	v53 = ""

else:
	v41 = boy
	v42 = boynick
	v43 = boy + boynick

	v44 = boynick + boy

	v45 = boy + "." + boynick
	v46 = girlnick + "." + girl

	v47 = boy + "4ik"
	v48 = boynick + "4ka"
	v49 = boynick + "4ik"

	v50 = boy + x
	v51 = boy + z

	v52 = boynick + x
	v53 = boynick + z

if surname == "-":
	v54 = ""
	v55 = ""

else:
	v54 = surname + date
	v55 = date + surname

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
save.write(v21 + '\n')
save.write(v22 + '\n')
save.write(v23 + '\n')
save.write(v24 + '\n')
save.write(v25 + '\n')
save.write(v26 + '\n')
save.write(v27 + '\n')
save.write(v28 + '\n')
save.write(v29 + '\n')
save.write(v30 + '\n')
save.write(v31 + '\n')
save.write(v32 + '\n')
save.write(v33 + '\n')
save.write(v34 + '\n')
save.write(v35 + '\n')
save.write(v36 + '\n')
save.write(v37 + '\n')
save.write(v38 + '\n')
save.write(v39 + '\n')
save.write(v40 + '\n')
save.write(v41 + '\n')
save.write(v42 + '\n')
save.write(v43 + '\n')
save.write(v44 + '\n')
save.write(v45 + '\n')
save.write(v46 + '\n')
save.write(v47 + '\n')
save.write(v48 + '\n')
save.write(v49 + '\n')
save.write(v50 + '\n')
save.write(v51 + '\n')
save.write(v52 + '\n')
save.write(v53 + '\n')
save.write(v54 + '\n')
save.write(v55 + '\n')

save.close()