import rstr
from xeger import Xeger

#Code that generates string of a given regex using xeger 
#with limit
x = Xeger(limit = 20)
for _ in range(5):
    print(x.xeger(r'P(Q|R|S)T(UV|W|X)*Z+'))    

#without limit
for _ in range(5):
    print(rstr.xeger(r'1(0|1)*2(3|4){5}36'))
