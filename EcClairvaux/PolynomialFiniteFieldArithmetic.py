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
