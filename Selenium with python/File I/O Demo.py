# File Handling
file = open('sample.txt', 'r')
print(file.read())
file.close()
l = [87, 778, 87]
for items in l:
    file.write(str(items))
file.close()
