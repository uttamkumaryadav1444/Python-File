i=0
while i<=3:
    print("Enetr the an even number")
    num=int(input())
    if num%2==0:
        print("you win")
        break
    i+=1
    if i==4:
        print("game over")  