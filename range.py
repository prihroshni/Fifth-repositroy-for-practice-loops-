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







