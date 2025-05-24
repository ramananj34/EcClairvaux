from EcClairvaux import NumericalFiniteFieldArithmetic as nffa

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


    def modNegate(p, n):
        return PolynomialFiniteFieldArithmetic.Poly([nffa.modNegate(p.cx[i], n) for i in range(len(p.cx))])

    def modSub(p1, p2, n):
        return PolynomialFiniteFieldArithmetic.modAdd(p1, PolynomialFiniteFieldArithmetic.modNegate(p2, n), n)
    
    def randPoly(maxDegree, n):
        return PolynomialFiniteFieldArithmetic.Poly([nffa.randModVal(n) for i in range(maxDegree + 1)])

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
    
    def normalizePoly(p, n): #Untested
        if (p.cx[-1] == 1):
            return p
        else:
            inverse = nffa.modInverse(p.cx[-1], n)
            return PolynomialFiniteFieldArithmetic.Poly([nffa.modMult(inverse, c, n) for c in p.cx])


