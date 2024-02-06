# This is a samplecipher function which takes two parameters and, one a string and two a nember. Every single character's 
# ASCII value in the string is reduced by K (K value) and then the corresponding alphabet for the ASCII value is 
# printed 
def sampleCipher(Encrypted,k):
    a=""
    x=len(Encrypted)
    for i in range(0,x):
        y=ord(Encrypted[i])
        z=y-k
        if z<65:
            p=65-z
            q=91-p
            a+=chr(q)
        else:
            a+=chr(z)

    return a

if __name__=="__main__":
    Encrypted= input("Enter a string in capital letters: ")
    k=int(input("Enter the number: "))
    ans=sampleCipher(Encrypted, k)
    print(ans)