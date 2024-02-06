
def GCD(a, b):
    while (b!=0):
        remainder = a%b
        a=b
        b= remainder
    return a

print(f"{GCD(35, 10)}")




