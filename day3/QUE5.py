dummy=[1,2,3,4,5]


def add(a):
    return a+10
ans=list(filter(lambda x:x%2==0 ,list(map(add,dummy))))
print(ans)