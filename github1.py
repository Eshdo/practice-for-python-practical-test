c=0
Max=0
Min=0
num=int(input("Enter Number= "))
while num!=0:
    if num<10000:
        if num>Max:
            Max=num
        else:
            if num<Min:
                Min=num
            else:
                c=c+1
            c=c+1
        num=int(input("Enter Number= "))
print("Maximum value=",Max,"Minimum value= ",Min)
