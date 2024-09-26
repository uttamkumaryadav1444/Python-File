
a=int(input("Enter the number :"))
if(99<a>100):
    print("Three Digits number")
else:
    print("Not Entered Three Digit Number")


#Q2---- 
n=int(input("Enter the number :"))
if(n>0):
    print("Positive Number")
elif(n < 0):
    print("negative Number")
else:
    print("zero Number")


#Q3---
print("Enter the three value a,b and c")
a,b,c=int(input()),int(input()),int(input())
d=b**2-4*a*c
if(d>0):
    print("Real and disting Roots")
elif(d<0):
    print("Imaginary Roots")
else:
    print("Real and Equal Roots")

 #Q4----
year=int(input("Enter the Year :"))
if(year%100):
    if(year%4): 
        print("Not a Leap Year")
    else:
        print("Leap Year")      
else:
    if(year%4):
        print("Not a Leap Year")
    else:
        print("Leap Year") 

#Q5----
print("Enter the Three numbers")
a,b,c=int(input()),int(input()),int(input())
if(a>=b and a>=c):
    print(a)
elif(b>c):
    print(b)
else:
    print(c)

