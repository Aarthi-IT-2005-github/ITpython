
#arithmetic
print("ARITHMETIC OPERATOR")
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=a+b
print("the add value",c)
c=a-b
print("the sub value",c)
c=a*b
print("the multiple value",c)
c=a/b
print("the divide value",c)
#comparison
print("COMPARISON OPERATOR")
if(a>b):
    print("a is greater")
elif(a==b):
    print("both are equal")
elif(a>=b):
    print("a is greater or equal to b")
elif(b>=a):
    print("b is greater or equal to a")
    
else:
    print("b is greater")
#logical
print("LOGICAL OPERATOR")
print(a>5 and b>0)
print(a>b or a==b)
print(not(a<10))
#bitwise
print("BIT WISE")
print("this is bitwise and ",a & b)
print("this is bitwise or ",a | b)
print("this is bitwise xor ",a ^ b)
print("complement",~a)
print("left shift",a<<1)
print("right shift",a>>1)
#assignment
print("ASIGNMENT OPERATOR")
d=5
i=10
print("the asignment operator add value",d+i)
#boolean
print("BOOLEAN OPERATOR")
a=True
b=False
print("the boolean value",a and b)
print("the boolean value",a or b)


