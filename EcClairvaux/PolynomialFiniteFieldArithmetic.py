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

    @staticmethod
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
    def modPolyMult(p1, p2, pn):
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
        return PolynomialFiniteFieldArithmetic.Poly(PolynomialFiniteFieldArithmetic.untrail0s(result))
    
    @staticmethod
    def modNumMult(a, b, p):
        res = [0] * (len(a.cx) + len(b.cx) - 1)
        for i in range(len(a.cx)):
            for j in range(len(b.cx)):
                res[i + j] = (res[i + j] + a.cx[i] * b.cx[j]) % p
        return PolynomialFiniteFieldArithmetic.Poly(PolynomialFiniteFieldArithmetic.untrail0s(res))
    
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
                result = PolynomialFiniteFieldArithmetic.modPolyMult(result, base, primePoly)
            base = PolynomialFiniteFieldArithmetic.modPolyMult(base, base, primePoly)
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
        return PolynomialFiniteFieldArithmetic.Poly(PolynomialFiniteFieldArithmetic.untrail0s(quot)), PolynomialFiniteFieldArithmetic.Poly(PolynomialFiniteFieldArithmetic.untrail0s(num))
    
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
            greater = PolynomialFiniteFieldArithmetic.Poly(lesser.cx.copy())
            lesser = PolynomialFiniteFieldArithmetic.Poly(r.cx.copy())
        return PolynomialFiniteFieldArithmetic.normalizePoly(PolynomialFiniteFieldArithmetic.Poly(greater.cx.copy()), n)

    @staticmethod
    def extendedEuclidianAlgorithm(p1, p2, p):
        if p1.degree() >= p2.degree():
            greater = p1.cx.copy()
            lesser = p2.cx.copy()
            flag = False
        else:
            lesser = p1.cx.copy()
            greater = p2.cx.copy()
            flag = True
        s0, s1 = [1], [0]
        t0, t1 = [0], [1]
        while lesser != [0]:
            q, r = PolynomialFiniteFieldArithmetic.modNumDiv(PolynomialFiniteFieldArithmetic.Poly(greater), PolynomialFiniteFieldArithmetic.Poly(lesser), p)
            greater, lesser = lesser, r.cx
            s0, s1 = s1, PolynomialFiniteFieldArithmetic.modSub(PolynomialFiniteFieldArithmetic.Poly(s0), PolynomialFiniteFieldArithmetic.modNumMult(q, PolynomialFiniteFieldArithmetic.Poly(s1), p), p).cx
            t0, t1 = t1, PolynomialFiniteFieldArithmetic.modSub(PolynomialFiniteFieldArithmetic.Poly(t0), PolynomialFiniteFieldArithmetic.modNumMult(q, PolynomialFiniteFieldArithmetic.Poly(t1), p), p).cx
        if (greater[-1] != 1):
            inverse = nffa.modInverse(greater[-1], p)
            t0 = PolynomialFiniteFieldArithmetic.Poly([nffa.modMult(inverse, c, p) for c in t0])
            s0 = PolynomialFiniteFieldArithmetic.Poly([nffa.modMult(inverse, c, p) for c in s0])
        else: 
            t0 = PolynomialFiniteFieldArithmetic.Poly(t0)
            s0 = PolynomialFiniteFieldArithmetic.Poly(s0)
        if flag:
            return t0, s0
        else:
            return s0, t0
        
    @staticmethod
    def modInverse(p, primePoly):
        if (PolynomialFiniteFieldArithmetic.euclidianAlgorithm(p, primePoly, primePoly.p) != PolynomialFiniteFieldArithmetic.Poly([1])):
            return None
        x, _ = PolynomialFiniteFieldArithmetic.extendedEuclidianAlgorithm(p, primePoly, primePoly.p)
        return x

    @staticmethod
    def modPolyDiv(p, q, primePoly):
        invq = PolynomialFiniteFieldArithmetic.modInverse(q, primePoly)
        if (invq is None):
            raise ValueError("Can not divide by 0")
        return PolynomialFiniteFieldArithmetic.modPolyMult(p, invq, primePoly)
    
    @staticmethod
    def getContent(p):
        #Returns the gcd of all the coefficients of a polynomail
        gcd = p.cx[-1]
        i = p.degree()-1
        while gcd != 1 and i >= 0:
            gcd = nffa.euclidianAlgorithm(gcd, p.cx[i])
            i-=1
        return gcd

    @staticmethod
    def modPseudoDivide(p, q, n):
        if p.degree() < q.degree():
            return PolynomialFiniteFieldArithmetic.Poly([0]), PolynomialFiniteFieldArithmetic.Poly(p.cx)
        denom = PolynomialFiniteFieldArithmetic.Poly([a for a in q.cx])
        Q = PolynomialFiniteFieldArithmetic.Poly([0])
        R = PolynomialFiniteFieldArithmetic.Poly([a for a in p.cx])
        e = p.degree() - q.degree() + 1
        d = q.cx[q.degree()]
        while R.degree() >= denom.degree():
            S = PolynomialFiniteFieldArithmetic.Poly([0] * (R.degree() - denom.degree()+1))
            S.cx[S.degree()] = R.cx[R.degree()]
            for i in range(0, Q.degree()+1):
                Q.cx[i] = nffa.modMult(Q.cx[i], d, n)
            Q = PolynomialFiniteFieldArithmetic.modAdd(Q, S, n)
            for i in range(0, R.degree()+1):
                R.cx[i] = nffa.modMult(R.cx[i], d, n)
            k = S.degree()
            T = PolynomialFiniteFieldArithmetic.Poly([0]*(S.degree() + denom.degree()+1))
            for i in range(0, denom.degree()+1):
                T.cx[i+k]=nffa.modMult(denom.cx[i], S.cx[k], n)
            R = PolynomialFiniteFieldArithmetic.modSub(R, T, n)
            e-=1
        if e >= 1:
            d = nffa.modPow(d, e, n)
            for i in range(0, Q.degree()+1):
                Q.cx[i] = nffa.modMult(Q.cx[i], d, n)
            for i in range(0, R.degree()+1):
                R.cx[i] = nffa.modMult(R.cx[i], d, n)
        return PolynomialFiniteFieldArithmetic.Poly(PolynomialFiniteFieldArithmetic.untrail0s(Q.cx)), PolynomialFiniteFieldArithmetic.Poly(PolynomialFiniteFieldArithmetic.untrail0s(R.cx))
    
    @staticmethod
    def resultant(A, B, n):
        if (A.degree() == 0 and A.cx[0] == 0) or (B.degree() == 0 and B.cx[0] == 0):
            return 0
        contA = PolynomialFiniteFieldArithmetic.getContent(A)
        contB = PolynomialFiniteFieldArithmetic.getContent(B)
        if contA != 1:
            Aa = PolynomialFiniteFieldArithmetic.Poly([nffa.modDiv(c, contA, n) for c in A.cx])
            ta = nffa.modPow(a, B.degree(), n)
        else:
            Aa = PolynomialFiniteFieldArithmetic.Poly(A.cx[:])
            ta = 1
        if b != 1:
            Bb = PolynomialFiniteFieldArithmetic.Poly([nffa.modDiv(c, contB, n) for c in B.cx])
            tb = nffa.modPow(b, A.degree(), n)
        else:
            Bb = PolynomialFiniteFieldArithmetic.Poly(B.cx[:])
            tb = 1
        g = 1
        h = 1
        s = 1
        if Aa.degree() < Bb.degree():
            Aa, Bb = Bb, Aa
        while Bb.degree() > 0:
            delta = Aa.degree() - Bb.degree()
            if Aa.degree() % 2 == 1 and Bb.degree() % 2 == 1:
                s = -s
            _, R = PolynomialFiniteFieldArithmetic.modPseudoDivide(Aa, Bb, n)
            Aa = Bb
            a = nffa.modPow(h, delta, n)
            b = nffa.modMult(a, g, n)
            Bb = PolynomialFiniteFieldArithmetic.Poly([nffa.modDiv(c, b, n) for c in R.cx])
            g = Aa.cx[Aa.degree()]
            i = nffa.modSub(1, delta, n)
            a = nffa.modPow(h, i, n)
            b = nffa.modPow(g, delta, n)
            h = nffa.modMult(a, b, n)
        i = nffa.modSub(1, Aa.degree(), n)
        a = nffa.modPow(h, i, n)
        b = nffa.modPow(Bb.cx[0], Aa.degree(), n)
        h = nffa.modMult(a, b, n)
        result = nffa.modMult(h, ta, n)
        result = nffa.modMult(result, tb, n)
        if s < 0:
            result = nffa.modNegate(result, n)
        return result

    @staticmethod
    def quadResidue():
        pass

    @staticmethod
    def modSqrt():
        pass