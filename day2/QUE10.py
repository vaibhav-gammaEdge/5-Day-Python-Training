Ls = ["manan", "naman", "silent", "listen"]

dic = {}

for word in Ls:
    
    key = "".join(sorted(word))
    
    if key in dic:
        dic[key].append(word)
    else:
        dic[key] = [word]

print(dic)
