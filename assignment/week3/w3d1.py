#q1
a =int(input())
b =int(input())
c =int(input())
if (a>b):
    if (a>c):
        print ("a is biggest")
    else:
        print("c is greatest")
else:
    if (b>c):
        print("b is greatest")
    else:
        print("c is greatest")

#q2
if (b>a and a>c)or(c>a and a>b):
    print ("a is 2nd large ")
elif (a>b and b>c)or(c>b and b>a):
    print("b is 2nd large")
else:
    print("c is 2nd larger") 
#q3
s = int (input())
if (s%3==0 and s%5==0):
    print ("Fizz-buzz")
elif (s%3==0):
    print("fizz")
elif (s%5==0):
    print("buzz")
else:
    print("")