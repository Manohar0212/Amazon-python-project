n=int(input("No of rows"))

for i in range(n):
    for j in range(n-1-i):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=" ")
    print()

