
s=input("Enter a string: ")

l=[]

for i in s:
    if i=='(' or i=='{'or i=='[' :
        l.append(i)
    elif i==')' and l[-1]=='(':
        l.pop()
    elif i==']' and l[-1]=='[':
        l.pop()
    elif i=='}' and l[-1]=='{':
        l.pop()
    else:
        break

if not l:
    print(True)
else:
    
    print(False)