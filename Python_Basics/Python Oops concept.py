# classes & Objects
# class Manohar:
#     print("manohar is calling")
#     d=12
#     def display(self):
#         a=10
#         b=45
#         print(a,b)
# obj=Manohar()
# obj.display()
# print(obj.d)

# class Mobile:
#     def __init__(self,brand, price, battery):
#         self.brand=brand
#         self.price=price
#         self.battery=battery
#     def display(self):
#         print("Brand:",self.brand)
#         print("Price:",self.price)
#         print("Battery:",self.battery)
#         print("---------------------")
# for i in range(2):
#
#   obj = Mobile("Samsung", "20000", "5000mah")
#   obj.display()
#   obj2 = Mobile("Apple", "30000", "5000mah")
#   obj2.display()
#
# Inheritance
# Single level Inheritance
# class Parent:
#     def fun(self):
#         print("parent class")
# class Child(Parent):
#     def fun1(self):
#         print("child class")
#
# obj=Child()
# obj.fun1()
# obj.fun()

# Multilevel Inhertance
# class Parent:
#     def fun1(self):
#         print("Parent class")
# class Child(Parent):
#     def fun2(self):
#         print("Child class")
# class Grand_Child(Child):
#     def fun3(self):
#         print("Grand child class")
# Obj=Grand_Child()
# Obj.fun1()
# Obj.fun2()
# Obj.fun3()

# Hirarchial Inheritance
# class Parent:
#     def fun1(self):
#         print("Parent class")
# class Child1(Parent):
#     def fun2(self):
#         print("Child1 class")
# class Child2(Parent):
#     def fun3(self):
#         print(" child2 class")
# Obj=Child2()
# Obj.fun1()
# # Obj.fun2()
# Obj.fun3()

# Multiple Inheritance
# class Father:
#     def func1(self):
#      print("Father class")
# class Mother:
#     def func2(self):
#       print("Mother class")
# class Child(Father,Mother):
#     def func3(self):
#         print("Child class")
# Obj=Child()
# Obj.func1()
# Obj.func2()
# Obj.func3()

# super
# class A:
#     def __init__(self):
#      print("This is init classA")
#     def func1(self):
#        print("This is calss A")
# class B(A):
#     def __init__(self):
#         print("This is init class B")
#         super().__init__()
#     def func2(self):
#         print("This is class B")
# obj=B()
# # obj.func1()
# # obj.func2()

# Polymorphisam:
# Compile time
# a)Method Overloading: Same class and same method but different parameters
# Run time or  dynamic
# b)Methos Overriding: Different classes but same method and different parameters.
# This polymorphisam came from inheritance concept

# Method Overloading: same class and same method but different parameters
# class A:
#     def sum(self,a,b):
#         return a+b
#     def sum(self,a,b,c=1):
#         return a+b+c
# obj=A()
# print(obj.sum(2,3))

# Method Overriding: Different classes and same method but different parameters
# class A:
#     def sum(self):
#         print("calling method1")
# class B(A):
#     def sum(self):
#         print("calling method2")
#         super().sum()
#
# obj=B()
# obj.sum()
#
#
# Encapsulation:
# Wrapping of methods and variables in a single unit is called Encapsulation acheived through inheritance.
class demo:
   def __init__(self,a,b):
       self.__a=a
       self._b=b
class demo1(demo):
    def display(self):
      print(self._b)
obj=demo1(3,5)
obj.display( )



