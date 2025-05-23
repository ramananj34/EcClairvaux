from random import randint

class ModularArithmetic: 

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
            return ModularArithmetic.modInverse(ModularArithmetic.modPow(a, -1*e, n), n)
        elif (e == 0):
            return 1
        else:
            if e % 2 == 1:
                return (a * ((ModularArithmetic.modPow(a, e // 2, n) ** 2) % n)) % n
            else:
                return (ModularArithmetic.modPow(a, e // 2, n) ** 2) % n

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
        return ModularArithmetic.euclidianAlgorithm(b, a%b)

    @staticmethod
    def extendedEuclidianAlgorithm(a, b):
        #Solves the equation ax+by=gcd(a,b), gaurenteed by Bezout's identity
        if (a < 0 or b < 0):
            raise ValueError("Error, the Euclidian Algorithm requires two POSOTIVE integers")
        if a == 0:
            return 0, 1
        x, y = ModularArithmetic.extendedEuclidianAlgorithm(b % a, a)
        return y - (b // a) * x, x

    @staticmethod
    def modInverse(a, n):
        #Calculate the inverse of a mod n using the Extended Euclidian Algorithm
        if (ModularArithmetic.euclidianAlgorithm(a,n) != 1):
            return None
        else:
            x, y = ModularArithmetic.extendedEuclidianAlgorithm(a,n)
            return x%n

    @staticmethod
    def modDiv(a, b, n):
        #Calculate a/b (modn)
        if (ModularArithmetic.modInverse(b, n) == None):
            return None
        else:
            return (a * ModularArithmetic.modInverse(b, n))%n
        
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
        randnonres = ModularArithmetic.randModVal(mod)
        while (ModularArithmetic.legendreSymbol(randnonres, mod) != -1):
            randnonres = ModularArithmetic.randModVal(mod)
        y = ModularArithmetic.modPow(randnonres, q, mod)
        r = e
        x = ModularArithmetic.modPow(a, (q-1)//2, mod)
        b = ModularArithmetic.modMult(a, pow(x, 2), mod)
        x = ModularArithmetic.modMult(a, x, mod)
        while (b != 1):
            m = 1
            while True:
                if (1 == ModularArithmetic.modPow(b, pow(2, m), mod)):
                    break
                m+=1
            if (r == m):
                print("Something went wrong, I am not sure what, but it is a problem")
            t = ModularArithmetic.modPow(y, pow(2, r-m-1), mod)
            y = ModularArithmetic.modPow(t, 2, mod)
            r = m
            x = ModularArithmetic.modMult(x, t, mod)
            b = ModularArithmetic.modMult(b, y, mod)
        return x

    @staticmethod
    def modSqrt(a, mod):
        #Calculates the square root of a mod n
        if (ModularArithmetic.legendreSymbol(a, mod) != 1):
            return None
        elif (mod % 4 == 3): #Use Fermat's Little Theorem Directly
            e = (mod+1)/4
            return ModularArithmetic.modPow(a, e, mod)
        else: #Use Tonelli and Shanks Algorithm
            return ModularArithmetic.tonelliShankAlgorithm(a, mod)