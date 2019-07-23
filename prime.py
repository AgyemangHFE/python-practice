
n=int(input('type a number:'))
for i in range(2,n+1):

  isprime  = True
  for m in range(2,i):
    if i%m ==0:
        isprime = False
        break

  if isprime:
      print(i)

