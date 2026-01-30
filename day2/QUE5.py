import sys
L=[1,3,54,67,543]
s=None
max=sys.float_info.min


for i in L:
    if max<i:
        s=max
        max=i
        
print(s)