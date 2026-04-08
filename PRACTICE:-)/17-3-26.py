search_name="aditya"
with open("studname.txt","r") as f1:
    found=False
    for i in f1:
        if search_name in f1:
            print("Found")
        else:
            print("not found")
with open("student.txt","r") as f1:
    total=0
    count=0
    for i in f1:
        i= int(i)
        total=total+i
        count=count+1
    avg=total/count
    print(avg)
with open ("student.txt","a") as f1:
    f1.write("avg=",avg)
#structure/complex structure of data
