m=int(input('enter lower num'))
n=int(input('enter upper num'))
for i in range(m,n,1):
    if i > 0:
        for p in range(2,i):
            if i%p==0:
                break
        else:
            print(i)