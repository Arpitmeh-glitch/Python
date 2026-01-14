count=0
for i in range (0,100):
    if(i%5==0)&(i%7==0):
        print(i)
        count+=1
print ("count: ",count)