# The orderd dictionary are similar to the normal dictionary but they maintain the order in whihc they were inserted...
from collections import OrderedDict, defaultdict

ordd=OrderedDict()
ordd['A']=1
ordd['B']=2
ordd['C']=3
ordd['D']=4
print(ordd)

# there is also defaultdict() which similar to the noraml dictionary but it takes the data type of the
# elements as the first parameter....
dfd=defaultdict(int)
dfd["one"]=1
dfd["two"]=2
print(dfd)
print(dfd['one'])