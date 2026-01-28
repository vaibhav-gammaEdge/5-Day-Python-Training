ans=input("String:")


def P1(ans):

    check=ans[::-1]

    if(check==ans):
        print("YES this is Palindrome")
    else:
        print("Not")

def P2(ans):
    i,j=0,len(ans)-1

    for k in range(j//2):
        if(ans[i]!=ans[j]):
            print("NOT A PALINDROME")
            break
    
        i=i+1
        j=j-1
    

P1(ans.lower())
P2(ans.lower())