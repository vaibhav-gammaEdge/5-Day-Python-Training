
s1 = "listen"
s2 = "silent"

l = list(s2)
for ch in s1:
    if ch in l:
        l.remove(ch)
    else:
        print("No")
        break
else:
    print("Yes")