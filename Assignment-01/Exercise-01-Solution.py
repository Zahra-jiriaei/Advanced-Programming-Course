#Arc Sinus
# inputs
e,x=input().split()
e=float(e)
x=float(x)

import math
def Arcsinus(e):
    """ our error has to be less than e for calculating Arctag(x)"""
    a=-1*(math.pi) # First part
    b=1*(math.pi) # Last part
    
    def inner(x):
        nonlocal a
        nonlocal b
        
        while True:
            mid =(a+b)/2
            sin_mid=math.sin(mid)
            
            if sin_mid<=x:
                a=mid
                b=b
                if (b-a) <=e:
                    break
            elif sin_mid>x:
                a=a
                b=mid
                if (b-a) <=e:
                    break
        return mid
    return inner

Arcsin_e = Arcsinus(e)
print(round(Arcsin_e(x),4))
