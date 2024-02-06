
# In Tabulation method the output of every function is stored and used the next time the output is needed.
# In this way with tabulation method dynamic programming.
# Note: In Tabultion the problem is solved from bottom-up. 
# dp[x+1]= dp[x]*(x+1)

# Program:

dp=[]
dp.insert(0,1)
n=int(input("Enter the number to find the factorial: "))
for i in range(1,n+1):
    dp.insert(i,dp[i-1]*i)
print(dp)



