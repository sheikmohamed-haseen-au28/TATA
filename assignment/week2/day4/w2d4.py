#q1
n = int (input())
i = 1
for i in range(n):
    print("hello world")

#q2
j = 1
a = int(input())
for j in range (j ,a+1):
    print(2**j)

#q3
s = int(input())
m = 1
for m in range (m,s+1):
    if m%3==0 and m%5==0 :
        print("fizz,fuzz")
    elif m%3==0 :
        print("fizz")
    elif m%5==0 :
        print("fuzz")
    else:
        print(m) 