#Q1--
n=int(input("Enter the number"))
for i in range(2,n,2):
    print(i)

#Q2--
n=int(input("Enter the number"))
for i in range(1,n,2):
    print(i)

#Q3--
n=int(input("Enter the number"))
for i in range(n):
    print(i**2)

#Q4--
n=int(input("Enter the number"))
for i in range(1,n+1):
    print(i**3,end='')


#Q5--
a=int(input("Enter the number"))
b=int(input("Enter the number"))
for x in range(a,b):
    for i in range(2,x):
        if x%i==0:
            break
        else:
            print(x,end='')