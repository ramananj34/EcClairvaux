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
    def tonelliShankAlgorithm(a, n):
        pass


    @staticmethod
    def modSqrt(a, n):
        #Calculates the square root of a mod n
        if (ModularArithmetic.legendreSymbol(a, n) != 1):
            return None
        elif (a%4 == 3): #Use Fermat's Little Theorem
            pass
        else: #Use Tonelli and Shanks Algorithm
            pass

