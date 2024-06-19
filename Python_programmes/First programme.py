
n=int(input("Given number"))
# p=1
for i in range(n):
    p=1
    for j in range(i+1):
        print(p,end=' ')
        p+=1
    print()
