a= 50
num=a
b=2

while a>b:
    if(a%b==0):
        a=a/b
        b=b+1
    else:
        b=b+1
        
if num%2==0:
    print b-1 
else:
    print b
