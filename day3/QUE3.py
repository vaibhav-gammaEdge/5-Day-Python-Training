def average(*a):

    ans=0
    for i in a:
        ans=i+ans

    av=ans//len(a)

    return av



ans=average(1,2,3,4,5,6,7,8,9)

print(f"Average:{ans}")