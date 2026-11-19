#Range (start , stop, step)

#printing range
print(range(5))


#applying loops in sequences 
seq = range(5)

for i in seq:
    print(i) 

# range (start, stop, step)
for i in range(5):  #giving stop condition ---  range(stop)
    print(i)
 
for i in range(0,5):    #giving stop condition -- range(start, stop)
    print(i)

for i in range(0,10,2):      #range( start , stop, step)  -- output = 0,2,4,6,8
    print(i)


for i in range(1,100, 2):  #print odd 
    print(i)

for i in range(0,100,2): #print even
    print(i)



#printing numbers from 1-100
for i in range(101):
    print(i)


#print numbers from 100-1
for i in range(100 , 0, -1): 
    print(i)


#printing multiplication of input x 

input= int(input("write a number ,"  ))

x = input
for i in range(x , 20, x): 
    print(i)



