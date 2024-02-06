
def GCD(a, b):
    if a<b:
        a,b=b,a
    remainder = a%b
    if remainder !=0:
        a=b
        b=remainder
        GCD(a,b)
    return b

print(f"{GCD(24, 36)}")
