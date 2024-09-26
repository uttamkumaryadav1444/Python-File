#Q1--
n="hello world"
for i in n:
    print(i,'_',ord(i))
#Q2--
n=input("Enter the number")  
for e in n:
    if e in "aeiouAEIOU":
        print(e,end='')

#Q3--
s1=input("Enter the number") 
count=0
for e in s1:
    if e=='':
        count+=1
#Q4--
print("total space is:",count) 
s1=int(input("Enter the number")) 
for digit in "0123456789":
    if digit in str(n):
        print(digit,end='')


#Q5--
n=int(input("Enter the number"))
count=0
for e in str(n):
    count+=1
print("Total digit",count)