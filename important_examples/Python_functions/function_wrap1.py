import sys
def html_tag(msg1):

    def wrap(msg2):
        print(f"<{msg1}> {msg2} <{msg1}>")

    return wrap

printA= html_tag("h1")  # This is known as closure where the passed paramater h1 is remembered whenever PrintA() function 
printA("This is a text") # is called.

PrintB=html_tag("h2") 
PrintB("This is another text") 


original_sys=sys.stdout
with open("important_examples/Python_functions/super.html", 'a+') as f:
    sys.stdout=f
    printA("This is manmohan")
    sys.stdout=original_sys