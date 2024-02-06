# This code is to give intro to the threads....

import time

start=time.time()

def do_something():
    print("Going to sleep")
    time.sleep(4)
    print("Done sleeping!")

do_something()
do_something()

print(f"The method completed in {round(time.time()-start)} seconds")