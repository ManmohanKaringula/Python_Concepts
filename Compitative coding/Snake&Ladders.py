import random
chart=[
        [ ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""] ],
        [ ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""] ],
        [ ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""] ],
        [ ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""] ],
        [ ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""], ["","","",""] ],

]

n=int(input("Enter the number of players: "))
if n<=4:
    players=["player1", "player2", "player3", "player4"]

else:
    print("Maximum number of players exceeded sorry! maximum number of players allowed are only 4")

Max_Pos=(4,7)

def intialize(chart, players, n):
    for i in range(n):
        chart[0][0][i]=players[i]

intialize(chart, players, n)

for i in range(0,5):
    for j in range(0,8):
        print(chart[i][j], end=" ")
    print("\n")


print(chart[0][0][1])            
    





