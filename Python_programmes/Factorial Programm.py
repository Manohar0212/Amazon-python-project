# import math
# def factorial(n):
#     return(math.factorial(n))
# n=9
# print("Factorial of", n, "is",factorial(n))


# def factorial(n):
#     return 1 if (n==0 or n==1) else  n*factorial(n-1)
# n=6
# print("factorial of", n, "is", factorial(n))
























def factorial(n):
    return 1 if(n==0 or n==1) else n*factorial(n-1)
n = 9
print("Factorial of", n, "is", factorial(n))
