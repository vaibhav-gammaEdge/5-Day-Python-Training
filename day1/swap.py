a=int(input("Enter first no:"))
b=int(input("Enter second no:"))

def swap1(a,b):
    a,b=b,a
    print(f"a:{a},b:{b},")


def swap2(a,b):

    a=a+b
    b=a-b
    a=a-b

    print(f"a:{a},b:{b},")

def swap3(a,b):

    a=a*b
    b=a//b
    a=a//b

    print(f"a:{a},b:{b},")



swap1(a,b)
print("/n")
swap2(a,b)
print("/n")
swap3(a,b)

