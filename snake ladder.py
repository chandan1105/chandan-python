#program of snake ladder
import random
count=0
while(count<=100):
    n=input("enter r to roll the dice")
    if n=='r':
        a=input(random.randint(1,6))
    count=count+a
    print("random",a)
    print("count",count)
if count==8:
    count==37
    print("ladder")
elif count==11:
    count=2
    print("snake bite come to 2 ")
elif count==13:
    count=34
    print("ladder")
elif count==25:
    count=4
    print("snake bite come to 4")
elif count==40:
    count=68
    print("ladder")
elif count==38:
    count=9
    print("snake is bite come to 9")
elif count==52:
    count=81
    print("ladder")
elif count==65:
    count=46
    print("snake is bite come to 46")
elif count==76:
    count=97
    print("ladder")
elif count==93:
    count=64
    print("snake is bite come to 64")
elif count==89:
    count=70
    print("snake is bite come to 70")
          
            
