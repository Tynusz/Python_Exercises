import _datetime #with this you can know what year it is
index = int(input("How many times?:"))
name = []
age = []
year100 = []
for i in range(0,index):
    #append all names,ages and years
    name.append(input("You'r name:"))
    age.append(int(input("You'r age:")))
    YEAR = _datetime.date.today().year #this will find out what year it is
    year100.append((YEAR-age[i])+100) #this will calculate year for every name
#this for statement will print all names with years
for i in range(0,index):
    print(name[i],"You will turn 100 years old in",year100[i])
