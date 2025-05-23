from random import randint

class NumericalFiniteFieldArithmetic: 

    @staticmethod
    def modAdd(a, b, n):
        #Calculate a+b (modn)
        return (a+b)%n

    @staticmethod
    def modSub(a, b, n):
        #Calculate a-b (modn)
        return (a-b)%n

    @staticmethod
    def modMult(a, b, n):
        #Calculate a*b (modn)
        return (a*b)%n

    @staticmethod
    def modNegate(a, n):
        #Calculate -a (modn)
        return (-a)%n
    
    @staticmethod
    #Calculate a^e (modn)
    def modPow(a, e, n):
        if (e < 0):
            return NumericalFiniteFieldArithmetic.modInverse(NumericalFiniteFieldArithmetic.modPow(a, -1*e, n), n)
        elif (e == 0):
            return 1
        else:
            if e % 2 == 1:
                return (a * ((NumericalFiniteFieldArithmetic.modPow(a, e // 2, n) ** 2) % n)) % n
            else:
                return (NumericalFiniteFieldArithmetic.modPow(a, e // 2, n) ** 2) % n

    @staticmethod
    #Find the greatest common divisor of a and b
    def euclidianAlgorithm(a, b):
        if (a < 0 or b < 0):
            raise ValueError("Error, the Euclidian Algorithm requires two POSOTIVE integers")
        if (a < b):
            temp = a
            a = b
            b = temp
        if (b == 0):
            return a
        return NumericalFiniteFieldArithmetic.euclidianAlgorithm(b, a%b)

    @staticmethod
    def extendedEuclidianAlgorithm(a, b):
        #Solves the equation ax+by=gcd(a,b), gaurenteed by Bezout's identity
        if (a < 0 or b < 0):
            raise ValueError("Error, the Euclidian Algorithm requires two POSOTIVE integers")
        if a == 0:
            return 0, 1
        x, y = NumericalFiniteFieldArithmetic.extendedEuclidianAlgorithm(b % a, a)
        return y - (b // a) * x, x

    @staticmethod
    def modInverse(a, n):
        #Calculate the inverse of a mod n using the Extended Euclidian Algorithm
        if (NumericalFiniteFieldArithmetic.euclidianAlgorithm(a,n) != 1):
            return None
        else:
            x, y = NumericalFiniteFieldArithmetic.extendedEuclidianAlgorithm(a,n)
            return x%n

    @staticmethod
    def modDiv(a, b, n):
        #Calculate a/b (modn)
        if (NumericalFiniteFieldArithmetic.modInverse(b, n) == None):
            return None
        else:
            return (a * NumericalFiniteFieldArithmetic.modInverse(b, n))%n
        
    @staticmethod
    def randModVal(n):
        #Returns a random value in the cannonical residue class
        return randint(0, n-1)
    
    @staticmethod
    def legendreSymbol(a, n):
        #Returns 0 if n|a, 1 if a is a quad-residue, -1 if a is a nonresidue
        expontent = (n - 1) // 2
        temp = pow(a, expontent, n)
        if temp > 1:
            return temp-n
        else:
            return temp
    
    @staticmethod
    #Calculates the square root of a mod n where a congruent to 1 mod 4, as Fermats Little Theorem does not apply
    def tonelliShankAlgorithm(a, mod):
        q = mod-1
        e = 0
        while (q%2 == 0):
            e+=1
            q//=2
        randnonres = NumericalFiniteFieldArithmetic.randModVal(mod)
        while (NumericalFiniteFieldArithmetic.legendreSymbol(randnonres, mod) != -1):
            randnonres = NumericalFiniteFieldArithmetic.randModVal(mod)
        y = NumericalFiniteFieldArithmetic.modPow(randnonres, q, mod)
        r = e
        x = NumericalFiniteFieldArithmetic.modPow(a, (q-1)//2, mod)
        b = NumericalFiniteFieldArithmetic.modMult(a, pow(x, 2), mod)
        x = NumericalFiniteFieldArithmetic.modMult(a, x, mod)
        while (b != 1):
            m = 1
            while True:
                if (1 == NumericalFiniteFieldArithmetic.modPow(b, pow(2, m), mod)):
                    break
                m+=1
            if (r == m):
                print("Something went wrong, I am not sure what, but it is a problem")
            t = NumericalFiniteFieldArithmetic.modPow(y, pow(2, r-m-1), mod)
            y = NumericalFiniteFieldArithmetic.modPow(t, 2, mod)
            r = m
            x = NumericalFiniteFieldArithmetic.modMult(x, t, mod)
            b = NumericalFiniteFieldArithmetic.modMult(b, y, mod)
        return x

    @staticmethod
    def modSqrt(a, mod):
        #Calculates the square root of a mod n
        if (NumericalFiniteFieldArithmetic.legendreSymbol(a, mod) != 1):
            return None
        elif (mod % 4 == 3): #Use Fermat's Little Theorem Directly
            e = (mod+1)/4
            return NumericalFiniteFieldArithmetic.modPow(a, e, mod)
        else: #Use Tonelli and Shanks Algorithm
            return NumericalFiniteFieldArithmetic.tonelliShankAlgorithm(a, mod)