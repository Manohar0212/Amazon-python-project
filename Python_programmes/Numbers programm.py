# n=int(input("Given number"))
# p=1
# for i in range(n):
#     # p=1
#     for j in range(i+1):
#         print( p,end=' ')
#         p+=1
#     print()









num=int(input("Enter number:"))
n1,n2=0,1
sum=1
if num<=0:
     print("Enter number greater than 0")
else:
      print(sum, end=" ")
      n1 = n2
      n2 = sum
      sum = n1 + n2
