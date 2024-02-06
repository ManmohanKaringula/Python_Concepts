import math
      
def calculate_dist(a,b):
    ans=math.dist((0,0), (a,b))
    print(f'the calculated distance is {ans}')

initx=0; inity=0
while True:
    x= input()
    x=x.split()
    if x==[]:
        break
    else:
        
        if x[0]=='UP':
            inity+=int(x[1])
        elif x[0]=='DOWN':
            inity-=int(x[1])
        elif x[0]=='RIGHT':
            initx+=int(x[1])
        elif x[0]=='LEFT':
            initx-=int(x[1])
print(f"the calculated distance is: {math.dist((0,0), (initx, inity))} at position ({initx}, {inity})"  )





