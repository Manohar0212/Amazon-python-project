n=int(input("No of rows"))

for i in range(n):
    for j in range(i+1):
     print(end='  ')
    for j in range(i,n):
        # print('*',end=' ')
        if(i%2==0):
            print('1',end=' ')
        else:
            print('3',end=' ')
    print()
