from EcClairvaux import NumericalFiniteFieldArithmetic as nffa
import time

class PolynomialFiniteFieldArithmetic: 
    
    class Poly:
        
        def __init__(self, coefArr):
            self.cx = [i for i in coefArr]

        def __str__(self):
            e = len(self.cx)-1
            str = ""
            flag = False
            for i in self.cx[::-1]:
                if i!= 0:
                    if not flag:
                        str+=(f"{i}x^{e}")
                        flag = not flag
                    else:
                        str+=(f" + {i}x^{e}")
                e-=1
            if (str == ""):
                return "Empty Polynomial"
            else:
                return str
            
        def __eq__(self, other):
            if len(self.cx) != len(other.cx):
                return False
            for i in range(0, len(self.cx)):
                if self.cx[i] != other.cx[i]:
                    return False
            return True

        def degree(self):
            return len(self.cx)-1
        
        def declareMultTable(self, p):
            self.p = p
            cols = self.degree()
            rows = 2*self.degree()
            self.multTable = [[0 for _ in range(cols)] for _ in range(rows)]
            for i in range(cols):
                self.multTable[i][i] = 1
                self.multTable[cols][i] = -1*self.cx[i]
            for i in range(cols+1, rows):
                for j in range(1, cols):
                    temp = nffa.modMult(self.multTable[cols][j], self.multTable[i-1][cols-1], p)
                    self.multTable[i][j] = nffa.modAdd(temp, self.multTable[i-1][j-1], p)
                temp = nffa.modMult(self.multTable[cols][0], self.multTable[i-1][cols-1], p)
                self.multTable[i][0] = temp

        def printMultTable(self):
            for i in range(len(self.multTable)):
                for j in range(len(self.multTable[i])):
                    print(str(self.multTable[i][-j-1]) + "   ", end="")
                print()

    def untrail0s(arr):
        newArr = [x for x in arr]
        while newArr and newArr[-1] == 0:
            newArr.pop()
        if newArr == []:
            newArr = [0]
        return newArr

    @staticmethod  
    def modAdd(p1, p2, n):
        size = max(p1.degree(), p2.degree()) + 1
        newPolyDegrees = [0 for i in range(size)]
        for i in range(size):
            if (not i > p1.degree()):
                newPolyDegrees[i] = nffa.modAdd(newPolyDegrees[i], p1.cx[i], n)
            if (not i > p2.degree()):
                newPolyDegrees[i] = nffa.modAdd(newPolyDegrees[i], p2.cx[i], n)
        while (len(newPolyDegrees)>0 and newPolyDegrees[-1] == 0):
            newPolyDegrees = newPolyDegrees[:-1]
        return PolynomialFiniteFieldArithmetic.Poly(newPolyDegrees)

    @staticmethod
    def modNegate(p, n):
        return PolynomialFiniteFieldArithmetic.Poly([nffa.modNegate(p.cx[i], n) for i in range(len(p.cx))])

    @staticmethod
    def modSub(p1, p2, n):
        return PolynomialFiniteFieldArithmetic.modAdd(p1, PolynomialFiniteFieldArithmetic.modNegate(p2, n), n)
    
    @staticmethod
    def randPoly(maxDegree, n):
        return PolynomialFiniteFieldArithmetic.Poly([nffa.randModVal(n) for i in range(maxDegree + 1)])

    @staticmethod
    def modMult(p1, p2, pn):
        newPolyDegrees = [0 for _ in range(p1.degree() + p2.degree()+1)]
        for i in range(len(newPolyDegrees)):
            for j in range(i+1):
                newPolyDegrees[i] = nffa.modAdd(newPolyDegrees[i], nffa.modMult((p1.cx[j] if j <= p1.degree() else 0), (p2.cx[i-j] if i-j <= p2.degree() else 0), pn.p), pn.p)
        if (p1.degree() + p2.degree() < pn.degree()):
            result = newPolyDegrees
        else:
            result = [newPolyDegrees[i] for i in range(pn.degree())]
            for i in range(pn.degree(), len(newPolyDegrees)):
                for j in range(pn.degree()):
                    result[j] = nffa.modAdd(result[j], nffa.modMult(newPolyDegrees[i], pn.multTable[i][j], pn.p), pn.p)
        while(result[-1] == 0):
            result = result[:-1]
        return PolynomialFiniteFieldArithmetic.Poly(result)
    
    @staticmethod
    def normalizePoly(p, n):
        if (p.cx[-1] == 1):
            return p
        else:
            inverse = nffa.modInverse(p.cx[-1], n)
            return PolynomialFiniteFieldArithmetic.Poly([nffa.modMult(inverse, c, n) for c in p.cx])
        
    @staticmethod
    def modPower(poly, k, primePoly):
        bits = bin(k)[2:][::-1]
        result = PolynomialFiniteFieldArithmetic.Poly([1])
        base = PolynomialFiniteFieldArithmetic.Poly(poly.cx)
        for bit in bits:
            if bit == "1":
                result = PolynomialFiniteFieldArithmetic.modMult(result, base, primePoly)
            base = PolynomialFiniteFieldArithmetic.modMult(base, base, primePoly)
        return result

    @staticmethod
    def modNumDiv(di, do, n):
        num = PolynomialFiniteFieldArithmetic.untrail0s(di.cx)
        den = PolynomialFiniteFieldArithmetic.untrail0s(do.cx)
        if len(num) < len(den):
            return PolynomialFiniteFieldArithmetic.Poly([0]), PolynomialFiniteFieldArithmetic.Poly(num)
        shiftlen = len(num) - len(den)
        den = [0] * shiftlen + den
        quot = []
        for _ in range(shiftlen + 1):
            mult = nffa.modDiv(num[-1], den[-1], n)
            quot.insert(0, mult)
            if mult:
                d = [nffa.modMult(mult, u, n) for u in den]
                num = [nffa.modSub(u, v, n) for u, v in zip(num, d)]
            num.pop()
            den.pop(0)
        num = [x % n for x in num if x != 0 or any(num[num.index(x)+1:])]
        quot = [x % n for x in quot]
        num = PolynomialFiniteFieldArithmetic.untrail0s(num)
        quot = PolynomialFiniteFieldArithmetic.untrail0s(quot)
        return PolynomialFiniteFieldArithmetic.Poly(quot), PolynomialFiniteFieldArithmetic.Poly(num)
    
    @staticmethod
    def euclidianAlgorithm(p1, p2, n):
        if all(c == 0 for c in p1.cx):
            return PolynomialFiniteFieldArithmetic.Poly(p2.cx.copy())
        elif all(c == 0 for c in p2.cx):
            return PolynomialFiniteFieldArithmetic.Poly(p1.cx.copy())
        if p1.degree() >= p2.degree():
            greater = PolynomialFiniteFieldArithmetic.Poly(p1.cx.copy())
            lesser = PolynomialFiniteFieldArithmetic.Poly(p2.cx.copy())
        else:
            lesser = PolynomialFiniteFieldArithmetic.Poly(p1.cx.copy())
            greater = PolynomialFiniteFieldArithmetic.Poly(p2.cx.copy())
        while not all(c == 0 for c in lesser.cx):
            q, r = PolynomialFiniteFieldArithmetic.modNumDiv(greater, lesser, n)
            print(f"Div {greater} by {lesser}: {q} and {r}")
            greater = PolynomialFiniteFieldArithmetic.Poly(lesser.cx.copy())
            lesser = PolynomialFiniteFieldArithmetic.Poly(r.cx.copy())
            time.sleep(1)
        return PolynomialFiniteFieldArithmetic.Poly(greater.cx.copy())

    @staticmethod
    def extendedEuclidianAlgorithm():
        pass

    @staticmethod
    def modInverse():
        pass

    @staticmethod
    def modPolyDiv():
        pass