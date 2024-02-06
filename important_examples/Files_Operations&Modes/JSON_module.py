# JSON Module is used to convert Python hierarchies into string representation 
# The process of converting the data into string is known is serialization and the process of converting it back into data
# is known as deserialization, the string representation of object can be stored into file or it can be sent to distant server.
import json
x=["Manmohan",22,"Manjula",56]



with open("important_examples/Files_Operations&Modes/JSON_output.txt", "r+") as f:
    json.dump(x,f)
    

    
    
   

   
     