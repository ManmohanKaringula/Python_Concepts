# We can handle the command line arguments using the getopt methods
import getopt
import sys
args=sys.argv[1:]

try:
    opts, argu=getopt.getopt(args, "u:p:", ["username=", "password="])
    print(opts,argu)

    if len(opts)!=2:
        print("The required parameters are not given")
except getopt.GetoptError:
    print("One or more options are not recognized in the correct order")




