my_list=["Jessy","for","manu","Geeks","Jessy"]
word="Jessy"
n=2
count=0
for i in range(0,len(my_list)):
        if my_list[i]==word:
            count=count+1
        if (count==n):
            del my_list[i]
print("Updated list",my_list)





