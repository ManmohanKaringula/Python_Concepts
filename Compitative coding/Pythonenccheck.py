from string import punctuation
def sampleCipher(Encrypted):
    special_characters=list(punctuation)
    a=""
    x=len(Encrypted)
    for i in range(0,x):
        if Encrypted[i]==special_characters:
            ind=special_characters.index(Encrypted[i])
            if ind==31:
                ind=0
                a+=special_characters[ind]
            else:
                a+=special_characters[ind+1]         
        else:
            y=ord(Encrypted[i])
            z=y+1
            a+=chr(z)
    return a

def action(var):
    answer=""
    if len(var)==12:
            answer+=sampleCipher(var)
            print(f'The encrypted Reference ID is : {answer}')

    else:
        print("The entered Reference ID is not 12 digits")
    return answer

RefID=input("Enter the Reference ID: ")
action(RefID)




