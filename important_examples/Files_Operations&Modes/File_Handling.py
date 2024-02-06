#The modes to write, read and append the strings into a textfile(.txt) are: 
""" ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.(basically r and r+ are the same)

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.(rewrites the file as new file)

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file. (rewrites the file as new file)

 ``a''   Open for writing.The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar. 

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar """

# Examples:

with open("important_examples/Files_Operations&Modes/output.txt", 'r+') as f:
    f.write("Manmohan Reddy") 
    f.seek(0) #before invoking read() we should set the file pointer to 0 ie. seek(0) so that the file can be read from starting.
    f.read()

with open("important_examples/Files_Operations&Modes/results.txt", 'a+') as p:
    p.write("\n")
    p.write("Son of Manjula Reddy")  
    p.seek(0)  
    p.read()
    

""" WARNING: The file operation modes(r, r+, w, w+, a, a+) take and return string type only, hence we cannot pass any other
types like int,float etc.,  """