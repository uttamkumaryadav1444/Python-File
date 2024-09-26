#write a python script to claculate simple intrest
print("calculate the simple intrest ")
p=int(input("Enter the price ="))
r=int(input("Enter the Rate ="))
t=int(input("Enter the time ="))
intrest=p*r*t
print("Simple intrst is =",intrest)
 
#Q2 Write a python script to calculate area of a rectangle
print("Calculate the Area of reactangle")
l=int(input("Enter the length ="))
w=int(input("Enter the Width ="))
Rectangle=l*w
print("Arae of rectangle is =",Rectangle)

# Q3 Write a python script to calculate average of three numbers entered by user
print("Calculate the Average")
num1=int(input("Enter the interger value1 ="))
num2=int(input("Enter the interger value2 ="))
num3=int(input("Enter the interger value3 ="))
#A,B,C=int(input()),int(input()),int(input()),
sum=num1+num2+num3
Average=sum/2
print("Average is =",Average)

# Q4 Write a python script calculate volume of a cuboid
print("Calculate the volume of cuboid")
l=int(input("Enter the length ="))
b=int(input("Enter the breadth ="))
h=int(input("Enter the height ="))
cuboid= l*b*h
print("Volume of cuboid is =",cuboid)

# Q5--
print("Enter a number abd its exponant")
x,y=int(input()),int(input())
print("Result is =",x**y)
