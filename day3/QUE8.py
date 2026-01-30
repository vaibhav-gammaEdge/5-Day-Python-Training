import random
import string

def password():
    low = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    sp = "~`!@#$%^&*"
    
    
    l = random.sample(low, 4)
    u = random.sample(upper, 4)
    s = random.sample(sp, 4)
    d = random.sample(digit, 4)
    
    total_list = l + u + s + d
    # print(low)
    # print(sp)
    
    random.shuffle(total_list)
    
    
    final_password = "".join(total_list)
    
    print(final_password)

password()
