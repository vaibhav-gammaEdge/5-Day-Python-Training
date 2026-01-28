s = "Gammaedge"
freq = {}
freq2={}

for c in s:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

for c in s:
    freq2[c]=freq2.get(c,0)+1

print(freq)
print(freq2)