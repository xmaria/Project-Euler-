a=0
i=1
j=2

while i<=4000000:
    if(j%2==0):
        a+=j
    j=i+j
    i=j-i
    
print a   