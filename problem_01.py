a=0
for x in filter(lambda i: i%3==0 or i%5==0,range(1,1000)):
    a+=x
print a   