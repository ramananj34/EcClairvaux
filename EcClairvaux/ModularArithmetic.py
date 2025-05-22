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
    def euclidianAlgorithm(a, b):
        if (a < 0 or b < 0):
            raise ValueError("Error, the Euclidian Algorithm requires two POSOTIVE integers")
        #Find the greatest common divisor of a and b
        if (a < b):
            temp = a
            a = b
            b = temp
        if (b == 0):
            return a
        return ModularArithmetic.euclidianAlgorithm(b, a%b)

    @staticmethod
    def extendedEuclidianAlgorithm(a, b):
        if (a < 0 or b < 0):
            raise ValueError("Error, the Euclidian Algorithm requires two POSOTIVE integers")
        #Solves the equation ax+by=gcd(a,b), gaurenteed by Bezout's identity
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