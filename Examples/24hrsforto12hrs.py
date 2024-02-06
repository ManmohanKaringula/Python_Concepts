def gettime(num1):
    num3=num1-12
    return num3

def main():
    print("Enter time in 24 hours format")
    num1=int(input("Enter hours: "))
    num2=int(input("Enter minutes: "))
    if(num1<24 and num2<60):
        if(num1>12):
            output=gettime(num1)
            print(f'{output} : {num2} PM')
        else:
            print(f'{num1} : {num2} AM')

    else:
        print("Invalid time")
main()


    



