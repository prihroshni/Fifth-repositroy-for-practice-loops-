# printing list as much as it has numbers
nums = [1,2,3,4,5]

for val in nums:
    print(nums)


#can change
nums = [1,2,3,4,5]

for a in nums:
    print(a)


#replce int with strings
nums = ["roshni" , "prih", "abeha",  "ayesha" , "Python"]

for a in nums:
    print(a)


#can add tuple also 
tuple = (1,55,77,4,3,9,99,10099,3333)

for val in tuple:
    print(val)



#want seperate characters
string = "prihroshni"

for char in string:
    print(char) 


#loop ended i want something else to get print also, will use else
list = [1,2,3,4]

for el in list:
    print(el)
else:
    print("end")


#else will not work if i use break statement
list = [1,2,3,4]

for el in list:
    if(el == 3):
        print("found 3")
        break

    print(el)
else:
    print("end") 
    

#printing list via for loops
list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for el in list:
    print(el)


#tracking its numbers index
list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

a = 9
idx = 0
for el in list:
    if(el == a):
        print(" i found" , a , "at" , idx )
    idx += 1

    print(el)


#finding a in list , output = all numbers + a 
list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

a = 9
for el in list:
    if(el == a):
        print(" i found" , a)

    print(el)








