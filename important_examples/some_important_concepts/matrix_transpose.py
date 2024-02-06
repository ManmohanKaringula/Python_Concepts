
matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    ]

result=[
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def transpose(n=[]):
    
    # iterate through rows
    for i in range(len(n)):
   # iterate through columns
        for j in range(4):
                result[j][i]=n[i][j]

    for r in result:
        print(r)

transpose(matrix)

# another simple and very easy way yo transpose a matrix:
print(list(zip(*matrix)))

# Transpose of matrix using nested comprehension:
transpose=[[row[i] for row in matrix] for i in range(4)]

print(transpose)

# DONE!!!!!! superb :-)