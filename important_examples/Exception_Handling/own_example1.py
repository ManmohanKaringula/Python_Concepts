class password_is_not_more_than_10_characters(Exception):
    print("Hello")
    pass
class password_did_not_match(Exception):
    pass

while True:
    try:
        n=input("Enter the password: ")
        if len(n)<10:
            raise password_is_not_more_than_10_characters()
        while True:
            m=input("Enter the password again for conformation: ")
            if n!=m:
                raise password_did_not_match()
            else:
                False

    except password_did_not_match:
        print("The password did not match please try again")
                
    except password_is_not_more_than_10_characters:
        print("Please make sure that password is more than 10 characters")
        
    else:
        print("PASSWORD CONFIRMED")
        break


    

       