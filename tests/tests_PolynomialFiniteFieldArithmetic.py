import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from EcClairvaux import PolynomialFiniteFieldArithmetic as pffa

#Polynomail Addition
assert pffa.modAdd(pffa.Poly([3, 7, 96, 37]), pffa.Poly([124, 83, 14]), 127) == pffa.Poly([0, 90, 110, 37])

#Polynomial Negation
assert pffa.modNegate(pffa.Poly([1,0,1]), 127) == pffa.Poly([126, 0, 126])

#Polynomail Subtraction
pffa.modSub(pffa.Poly([3, 7, 96, 37]), pffa.Poly([3, 7, 96, 37]), 127) == pffa.Poly([])

#Random Polynomial
print(pffa.randPoly(3, 127))