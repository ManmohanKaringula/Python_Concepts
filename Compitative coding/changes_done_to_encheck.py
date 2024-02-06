from string import punctuation

RefID=input("Enter the Reference ID: ")
if len(RefID)==12:
        if RefID.isnumeric()==True or RefID.isalpha()==True:
            print("The given Reference ID is not alphanumeric")
        else:
            special_characters=list(punctuation)
            a=""
            x=len(RefID)
            for i in range(0,x):
                if RefID[i]==special_characters:
                    ind=special_characters.index(RefID[i])
                    if ind==31:
                        ind=0
                        a+=special_characters[ind]
                    else:
                        a+=special_characters[ind+1]         
                else:
                    y=ord(RefID[i])
                    z=y+1
                    a+=chr(z)
            print(f'The encrypted Reference ID is : {a}')


else:
    print("The entered Reference ID is not 12 digits")









