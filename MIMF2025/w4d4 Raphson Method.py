#Inputs your initial root guess(x), 

E = 0.001
x = 1 #initial root guess
def func(x): #fuction
    return 2*x**3 + x**2 - 67
def funcprime(x): #derivative
    return 6*x**2 + 2*x
delta = 2 #initializing the difference betw, two root guesses
i = 0 #initializing the iteration count
while delta > E : #defining tolerance
    if i == 0: #first iteration
        Xn = x #xn equals our initial guess
        Xn1 = Xn - (func(Xn)/funcprime(Xn))
        delta = abs(Xn1 - Xn)
        i += 1
    else:
        Xn = Xn1
        Xn1 = Xn - (func(Xn)/funcprime(Xn))
        delta = abs(Xn1 - Xn)
        i += 1

print(Xn1)
print(i)
