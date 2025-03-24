print("THIS IS NUMERICAL ORDER")
print("this is the increment of order numerical")
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(i)
print("this is the decrement of numerical")
for i in reversed(a):#for i in a [::-1]
    print(i)

searchvalue=int(input("enter your  search value:"))
if searchvalue in a:
    print("found the value",searchvalue)
else:
    print("value not in the list")
