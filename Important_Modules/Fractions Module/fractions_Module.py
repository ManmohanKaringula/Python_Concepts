import fractions

x=fractions.Fraction(5,2) # Syntax: fractions.Fraction(n1, n2) n1=numerator, n2= denominator
print(x)

d=2.5
c=d.as_integer_ratio() # the .as_integer_ratio() gives the output as numerator/denominator;
print(c)
#OR
e=fractions.Fraction.from_float(d)
print(e)