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

    def modMult(p1, p2, n):
        pass
