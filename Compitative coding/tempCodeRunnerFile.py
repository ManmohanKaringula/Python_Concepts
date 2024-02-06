lst=[]
ro1= Robot()
while True:
    x= input().split()
    x.split()
    if x=='':
        break
    else:
        ro1.robotActions(x[0], int(x[1]))
ro1.calculatedist()