name=(input("enter your name:"))

age=int(input("Enter your age:"))


def format(name,age):
    return f"name:{name}\t age:{age}"

print(format(name,age))