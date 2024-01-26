#python prg to check leap year
a = 0
b = 1
n = int(input("enter d no in sequence"))
print(a,b,end="")
while(n-2):
    c=a+b
    a,b = b,c
    print(c,end="")
    n=n-1