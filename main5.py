#Search for a number x in this tuple using loop:
list = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

user = int(input("write a number: " ))
#prints = (list.index(user))
#print(prints)

i = 0
while i <len(list):
    if(list[i] == user):
        print("i found it ", user)
    i += 1 
