x=int(input('enter a number'))

for i in range(1,2*x,2):
    for j in range(0,(2*x-i)//2):
        print(' ',end="")
    for j in range(0,i):
        print('*',end="")
    print()