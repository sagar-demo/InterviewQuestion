num=15
flag=0
if num<2:
    flag=1
elif num==2:
    flag=0
else:
    for i in range(3,int(pow(num,0.5)+1),2):
        if num%i==0:
            flag=1
            break
if flag==1:
    print("Not prime number")
else:
    print("Prime number")