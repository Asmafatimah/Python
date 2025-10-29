f=open("msg.txt","w")
f.write("hi,there")
f.close()

f=open('msg.txt','r')
print(f.read())
