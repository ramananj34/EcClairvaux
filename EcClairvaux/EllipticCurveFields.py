import NumericalFiniteFieldArithmetic as nffa

class EllipticCurveFields:

    class Point: 
        
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return "(" + str(self.x) + "," + str(self.y) + ")"
        
        def __eq__(self, other):
            return self.x == other.x and self.y == other.y
        
    class CurveField:

        def __init__(self, a4, a6, p):
            self.a4 = a4
            self.a6 = a6
            self.p = p

        def __str__(self):
            return "y^2 = x^3 + " + str(self.a4) + "x + " + str(self.a6) + " Over Field " + str(self.p)
        
        def __eq__(self, other):
            return self.a4 == other.a4 and self.a6 == other.a6 and self.p == other.p
    
    POINT_AT_INFINITY = Point(0,0)
        
    @staticmethod
    def negatePoint(p):
        #Compute -(x,y) = (x,-y)
        return EllipticCurveFields.Point(p.x, -1*p.y)

    @staticmethod
    def calcSlope(p1, p2, ec):
        #Calculates the slope between p1 and p2 on curve ec, avoiding a side-channel attack 
        if (p1 == EllipticCurveFields.POINT_AT_INFINITY or p2 == EllipticCurveFields.POINT_AT_INFINITY):
            raise ValueError("Cant calculate the slope of a Point at Infinity")
        num = nffa.modAdd(nffa.modAdd(nffa.modPow(p1.x, 2, ec.p), nffa.modMult(p1.x, p2.x, ec.p), ec.p), nffa.modAdd(nffa.modPow(p2.x, 2, ec.p), ec.a4, ec.p), ec.p)
        denom = nffa.modAdd(p1.y, p2.y, ec.p)
        if (denom == 0): #If the side channel resistant method doesn't work, i.e we have a 0 in the denominator, we switch to the traditional method
            denom = nffa.modSub(p2.x, p1.x, ec.p)
            if (denom == 0): #If x1=x2, we have a point at infinity
                return None
            num = nffa.modSub(p2.y, p1.y, ec.p)
        return nffa.modDiv(num,denom,ec.p)

    @staticmethod
    def addPoints(p1, p2, ec):
        #Adds two points on an elliptic curve
        if (p1 == EllipticCurveFields.POINT_AT_INFINITY):
            return p2
        elif (p2 == EllipticCurveFields.POINT_AT_INFINITY):
            return p1
        slope = EllipticCurveFields.calcSlope(p1, p2, ec)
        x = nffa.modSub(nffa.modPow(slope, 2, ec.p), nffa.modAdd(p1.x, p2.x, ec.p), ec.p)
        y = nffa.modSub(nffa.modMult(slope, (nffa.modSub(p1.x, x, ec.p)), ec.p), p1.y, ec.p)
        return EllipticCurveFields.point(x, y)

    @staticmethod
    def multPoint():
        pass

    @staticmethod
    def embedData(ec, data):
        pass

    @staticmethod
    def getRandomPoint(ec):
        pass
