# Finding Sin with Teylor
n,x=input().split()
n=int(n)
x=float(x)

def factorial(n):
    '''
    findig factorial N
    N!
    '''
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))
    
def sinus(n):
    ''' Calcalate Sin(x) with N sentenses of tylor'''
    List=[]
    def inner(x):
        nonlocal List
        x= (x*(3.14))/180
        for i in range (0,n):
            power=(2*i)+1
            sign=(-1)**i
            Sentenses=((sign*(x**power))/ factorial(power))
            List.append(Sentenses)
                       
        return sum(List)
        
    return inner

sin_x=sinus(n)
print(round(sin_x(x),6))                      
