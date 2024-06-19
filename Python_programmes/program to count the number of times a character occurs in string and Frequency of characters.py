# str="khdskghrtihthgkdghd:"
# s=str.count('k')
# print(s)

# To count frequency of string
# str="khfdkhkdghretitekgkd"
# c={}
# for i in str:
#     if i in c:
#         c[i]=c[i]+1
#     else:
#          c[i]=1
# print(c)



# Approch 1
list1=['a','b','c']
list2=[1,2,3]
dict1=dict(zip(list1,list2))
print(dict1)

# Approach 2
dict2={list1[i]:list2[i] for i in range (len(list1))}
print(dict2)

# Approach 3
dict3={}
for key in  list1:
  for value in list2:
        dict3[key]=value
        list2.remove(value)
        break
print(dict3)







