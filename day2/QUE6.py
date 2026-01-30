#zip combine iterable

l1=[1,2,3,4,5]
l2=('one','two','thre')
dict={}
for key,value in zip(l1,l2):
    dict[key]=value


print(dict)