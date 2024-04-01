import rstr
from xeger import Xeger
# x = Xeger(limit = 20)
# for i in range(0, 5):
#     print(x.xeger(r'P(Q|R|S)T(UV|W|X)*Z+'))    

for i in range(0, 5):
    print(rstr.xeger(r'P(Q|R|S)T(UV|W|X)*Z+', limit=20))   
