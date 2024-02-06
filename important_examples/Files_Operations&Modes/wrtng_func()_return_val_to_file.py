import sys
def html_tag(msg1):

    def wrap(msg2):
        print(f"<{msg1}> {msg2} <{msg1}>")

    return wrap

printA= html_tag("h1")
printA("This is a text")

original_sys=sys.stdout # emptying the stout object so that it can point to a file 
with open("important_examples/Files_Operations&Modes/super.html", 'w+') as f:
    sys.stdout=f # now the sys.stdout points to f "important_examples/Python_functions/super.html" which is file
    printA("This is manmohan")
    sys.stdout=original_sys # refering to original value again 

# in the above program the python print() function points to sys.stdout object hence the output is printed onto the 
# console, but we wanted to print the function return value to file the function html_tag above returns another function
# wrap which has print() function which prints onto the console hence we redirected onto the file so the output is 
# printed to the file.
