data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos1 = data.find('@')
atpos2 = data.find(" ")
atpos3 = data[atpos1 + 1 : atpos2]


print(atpos1, atpos2, atpos3)