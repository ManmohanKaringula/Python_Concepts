# Syntax:
                     # class parentclass_name():
                     # <statement-1>
                     # <statement-2>

                     # class childclass_name(parentclass_name):
                     # <statement-1>
                     # <statement-2>

# importing a module to use the class present in the module to inherit the classes present in the module
import module_for_importing_class
""" We can also use the "from module_for_importing_class import *" """
class chip_1st_gen(module_for_importing_class.processors):
    Architecture_name="ARM"
    power="150V, 3.2Amp"

class chip_2nd_gen(chip_1st_gen):
    Memory="220MB"
    # overriding: The variable with same name are present in both of the classes(child, parent)
    # but we can rewite the variables for both the classes this is known as overriding. In this case we have overridden 
    # the variables but we can do this with methods too which is known as method overriding.
    power="220V, 4.5Amp"

x=chip_2nd_gen
print(x.type)
print(x.Architecture_name)
print(x.Memory)
print(x.power)
print(module_for_importing_class.sniper)