# All numbers should be natural numbers
# every number should have two factors

# d={'a':3,'b':3,'c':1} print duplicate values not in a dictionary
# dict1={'a':3,'b':3,'c':1}
# dict2={}
# # print(dict1.duplicate())
# for key,value in dict1.items():
#  if value not in dict2.values():
#             dict2[key]=value
# print(dict2)
#
# # dictA={'a':3,'b':3,'c':1} print duplicate values in a dictionary
# # dictA = {'Sun': 5, 'Mon': 3, 'Tue': 5, 'Wed': 4}
# dictA={'a':3,'b':3,'c':1}
# print("Given Dictionary :", dictA)
# dictB = {}
# for key, value in dictA.items():
#    dictB.setdefault(value, set()).add(key)
# res = filter(lambda x: len(x) >1, dictB.values())
# Result+
# print("New Dictionary:",list(res))




# l=[2,3,5,7,8,9,21,2,3,27] print prime numbers in a list

# l = [2, 3, 5, 7, 8, 9, 21, 2, 3, 27]
# prime=[]
# # c=0
# for i in l:
#     c=0
#     for j in range (1,i):
#          if  i%j == 0:
#             c = c +1
#     if c == 1:
#         prime.append(i)
# print("prime numbers",prime)

# print duplicate numbers in a list
# l=[1,4,4,4,5,6,7,4,3,3,9]
# u=[]
# for num in l:
#       if num not in u:
#        u.append(num)
# print(u)


# How to remove consecutive duplicates from a list

# l=[1,4,4,4,5,6,7,4,3,3,9]
# l+=[" "]
# w=[]
# for i in range(1,len(l)):
#      # print(i)
#      if l[i] != l[i-1]:
#         # print(i)
#         w.append(l[i-1])
# print(w)
#







# l=[1,4,4,4,5,6,7,4,3,2,5,8,9,10]
# l+=" "
# w=[]
# for i in range(1,len(l)):
#     if l[i]!=l[i-1]:
#      w.append(l[i-1])
# print(w)



string="jsfgsjfhiieufjfsgfsjdffg"
dict={}
for i in string:
    if i in dict:
        continue
    else:
        dict[i]=string.count(i)
print(dict)

# context manager

# class file:
#     def__init__(self,name:str):
#         self.name=name
#     def__enter__(self):
#        print(f'opening{self.name}...')
#        return self
#     def__exit__(self.exc_type,exc_value,exc_tb):
#         print(f,Closing{self.name}....)
# if__name__=='__main__':
#    with File('main.py') as file:
#        print(file.name)
#    print('Done!')