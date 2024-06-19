# len(s):Return the number of items in an object.If object is string it will return count of an object.
x="     ';' ;';';';'; 777;';'  This is Manohar This is Manohar This is Manohar This is Manohar This is Manohar  999 "
# print(len(x))
# str:Converts specified value into string
# y=948764397630
# print(y)
# z=str(y)
# print(z.find("43"))
# print(x.upper())
# print(x.count("Manohar",24,50))
a=x.upper()
print(a.isupper())
print(a.islower())
print(x.split())
print(x.rsplit())
print(x.strip(';79 \''))
print(x.rstrip(';9 \''))
print(x.lstrip(';7  \''))
print(x.replace("Manohar","Naveen",2))
print(x.find("Manohar"))
print(x.index("Manohar"))
