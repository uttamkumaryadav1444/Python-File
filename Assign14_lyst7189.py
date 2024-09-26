"""
#Q1
num=int(input("Enter A Number :- "))
match 1000>num>99:
    case True:
        print("Three Digit")
    case False:
        print("Not Three Digit")
#Q2
num=int(input("Enter A Number :- "))
match num:
    case num if(num>0):
        print("POSITIVE")
    case num if(num<0):
        print("NEGATIVE")
    case _:
        print("ZERO")
#Q3
print("1. Odd Even")
print("2. Positive and Non Positive")
print("3. Simple Interest")
print("4. Roots of Quadratic Equation")
choice=int(input("Enter your choice"))
match choice:
    case 1:
        num=int(input("Enter a number"))
        print("Odd" if num%2 else "Even")
    case 2:
        num=int(input("Enter a number"))
        print("Positive" if num>0 else "Non Positive")
    case 3:
        print("Enter principal, rate and time")
        p,r,t=float(input()),float(input()),float(input())
        si=p*r*t/100
        print("Simple Interest is",si)
    case 4:
        print("Enter values of a,b and c of a quadratic equation")
        a,b,c=int(input()),int(input()),int(input())
        r1=(-b+(b**2-4*a*c)**0.5)/2*a
        r2=(-b-(b**2-4*a*c)**0.5)/2*a
        print("Roots are",r1,"and",r2)

      
#Q4
data=eval(input("Enter a data"))
match data:
    case data if type(data)==int:
        print("Monday")
    case data if type(data)==float:
        print("Tuesday")
    case data if type(data)==complex:
        print("Wednesday")
    case data if type(data)==bool:
        print("Thursday")
    """
#Q5
s1=input("Enter a string :")

match s1:
    case s1 if s1 in "mysirg":
        print("One")
    case s1 if s1 in "education":
        print("Two")
    case s1 if s1 in "services":
        print("Three")