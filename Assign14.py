'''
#Q1--
print("Enter three digit number")
num=int(input())
match 1000>num>99:
    case True:
        print("Three Digit")
    case False:
        print("Not a Three Digit ")

#Q 3---
print("Enter the number")
n1=int(input())
match n1:
    case n1 if(n1>0):
        print("Positive")
    case n1 if(n1<0):
        print("Negative")
    case n1:
        print("Zero")

#Q3--
print("1. Odd-Even")
print("2. Positive-negative")
print("3.Simple intrest")
print("4.Finf Roots of Qudratic equation")
choice=int(input("Enter the number"))
match choice:
    case 1:
        num=int(input("Enter the number :"))
        if(num%2):
            print("Odd Number")
        else:
            print("Even number")
    case 2:
        num1=int("Enter the number :")
        if(num1>0):
            print("Positive Number")
        else:
            print("Negative Number")
    case 3:
        print("Entre the Three value")
        p,r,t=int(input()),int(input()),int(input())
        si=(p*r*t)/100
        print("Simple intrest is =",si)
    case 4:
        a,b,c=float(input()),float(input()),float(input())
        r1=(-b+(b**2-4*a*c)**0.5)/2*a
        r2=(-b-(b**2-4*a*c)**0.5)/2*a
        print("Roots is",r1,r2)
'''
#Q4
data=eval(input("Enter the Data\n"))
match data:
    case data if(type(data)==int):
        print("Monday")
    case data if(type(data)==float):
        print("Tuesday")
    case data if(type(data)==complex):
        print("Wednesday")
    case data if(type(data)==bool):
        print("Thrusday")

#Q5--
print("Enter the String")
a=input()
match a:
    case a if a in "mysirg":
        print("ONE")
    case a if a in "education":
        print("TWo")
    case a if a in "services":
        print("Three")


