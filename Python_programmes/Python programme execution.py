# # 1.Find the frequency of each letter in the given string.
# s='the quick brown fox jumps over the lazy dog.'
# c=s.count('o')
# print(c)

# 2.Write a program in Python to find the largest and second-largest element in an array using Python?
# a = [4, 2, 4, 2, 1, 6, 7, 78, 3, 2, 8, 0, 10]
# def sol(x):
#     x = sorted(x)
#     lar = x[-1]
#     lar2 = x[-2]
#     return lar, lar2
# sol(a)
# print(sol(a))

# 3. Create a Python program that will print the highest sequence of 1s in an array with 0s and 1s?
# a = [1, 1, 1, 0, 1, 1, 1, 1, 1]
# count = 0
# for i in range(0,len(a)):
#     if a[i] == 1:
#         count += 1
#     else:
#         count = 0
# print(count)

# 4. In the given array, write a list comprehension that will print the sum of even numbers.
# sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum(x for x in sample if x%2==0))

# 5. Write a function to output separate lists containing even and odd elements from a given array.
# s = [1, 66, 22, 45, 89, 76, 41, 88, 56, 78, 45]
# # def func(s):
# print([x for x in s if x%2==0])
# print([x for x in s if x%2!=0])
# i = "manu"
# while (i == "manu"):
#  print("Value of i is" + i)

# 8. Write a Python program to print a list of primes in a given range?
# l=[2,3,5,6,7,8,9,10,23,56,89,41,78,64]
# prime=[]
# num=[]
# for num in l:
#     if num%2==0:
#         print(num)
# else:
#     if num not in prime:
#      print(num)


# num=int(input("Given number:"))
# age=15
# if age<=18:
#     print("Voter is not eligible")
# elif age==18:
#     print("Voter is eligible")
# else:
#     if age>18:
#      print("wait for vote")


string = "abcdbcaabdca"
dict={}
for i in string:
    if i in dict:
        continue
    elif i==" ":
        continue
    else:
      dict[i]=string.count(i)
print(dict)


