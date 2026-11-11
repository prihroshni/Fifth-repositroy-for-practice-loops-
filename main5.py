#Search for a number x in this tuple using loop:


input = int(input("write a no", ))
list = [1,4,9,16,25,36,49,64,81,100]

i = 0
while i < len(list):
    if list[i] == input:
        print("i found", input , "at" , i )
    i += 1
