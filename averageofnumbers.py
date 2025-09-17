count=0
total=0
while count<10:
    num=int(input(f"Enter the number{count+1}:"))
    total=total+num
    count=count+1
avg=total/10
print("average of 10 numbers is:",avg)
