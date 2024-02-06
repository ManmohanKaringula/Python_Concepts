def html():
    print("This is a html file")
    def css():
        print("This is a css file")
    # Inorder to use css() function we should call the css function or use the css function in return statement

    # calling the css function 
    css() 
    return css()
x=html()
print(x)