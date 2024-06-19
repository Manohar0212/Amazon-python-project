# name="John"
# age = 47
# height = 1.75
# Is_student = False
# #
# print(f"Name: {name}, Age: {age}, Height: {height}, is_student= {Is_student}")
# name=input("Enter your name:  ")
# print(f"Hello Welcome, {name}!")
# num=int(input("Enter number:  "))
# if num>0:
#     print("Positive number")
# elif num<0:
#     print("Negative number")
# else:
#     print("zero")

# for loop
# for i in range(6):
#     print(i)
# While looop
# count=0
# while count<10:
#     print(count,end=" ")
#     count+=3
#
# Functions
# def cube(x):
#  return x ** 2
# result=cube(6)
# print(f"cube of 6 :{result}")

# Dictionaries
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "Wonderland"
# }
#
# print("Person Information:", person)
# print("Age:", person["age"])
#
# # File Handling
# with open("example.txt", "w") as file:
#     file.write("Hello, File!")
#
# with open("example.txt", "r") as file:
#     content = file.read()
# print("File Content:", content)

# # Strings and String Manipulation
# sentence = "Python is fun!"
# print(sentence)
# #
# # # String Operations
# uppercase_sentence = sentence.upper()
# word_list = sentence.split()
# print("Uppercase Sentence:", uppercase_sentence)
# print("Word List:", word_list)
#
# # Lists and Iteration
# numbers = [1, 2, 3, 4, 5]
#
# for num in numbers:
#     print(num)
#
# # List Operations
# squared_numbers = [num ** 2 for num in numbers]
# print("Squared Numbers:", squared_numbers)

# class A:
#  count = 0
#  def__init__(self):
#     A.count += 1
#     print('Class A is called')


# a1 = A()
# a2 = A()
# print(A.count)
#
# @pytest.fixture(scope='function', autouse=True)
# def myfixture(self):
#     print("")