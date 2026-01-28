
C=float(input("Enter temperature in celsius:"))

def CtoF(C):

    F= (1.8 * C) + 32
    print(f"Fahrenheit:{F}")
    return F

def FtoC(F):
    
    C=((F-32)*5)/9
    print(f"Celsius:{C}")


FtoC(CtoF(C))