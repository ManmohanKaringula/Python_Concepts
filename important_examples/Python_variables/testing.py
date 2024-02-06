
chart=[[ [], ["apple"], [], [], [], [], [], [] ],
       [ [], [], [], [], [], [], [], [] ],
       [ [], [], [], [], [], [], [], [] ],
       [ [], [], [], [], [], [], [], [] ],
       [ [], [], [], [], [], [], [], [] ]
]

chart1=[[["", "", ""]],
        [["", "", ""]],
        [["", "", ""]],
        [["", "", ""]],
        [["", "", ""]],
        [["", "", ""]],

]

chart[0][0].append("player1")
chart[0][0].append("player2")

for i in range(5):
    for j in range(7):
        
        print(chart[i][j],",", end=" ")
    print("\n")

for i in range(5):
    for j in range(8):
        for q in range(3):
            if chart[i][j][q]=="player1":
                print("The string apple is present at index: " ,str(i), str(j), str(q))


