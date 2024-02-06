def avg(marks):
    assert len(marks)!=0, "The marks list is empty"  # Syntax: asserr <condition>, <error message>
    return sum(marks)/len(marks)

marks1=[]
marks2=[22,23,45]
print("Average of mark1: ", avg(marks1))
print("Average of mark2: ", avg(marks2)) 
# Note: you will see that once you the assertion error is raised then the program terminates and the code below does not 
# execute.