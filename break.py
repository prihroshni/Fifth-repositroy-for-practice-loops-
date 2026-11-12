#simple break code 
i = 0
while i <= 5:
    print(i)
    if (i == 2):
        break
    i += 1
 
#finding number then breaking
nums = [1,2,3,4,5,6,7,8,9,10]
x = 3
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("i found", x , "at", i)
        break
    else:
        print("findingnnnnn")
        i += 1
