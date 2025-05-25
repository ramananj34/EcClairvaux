import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from EcClairvaux import PolynomialFiniteFieldArithmetic as pffa

#Polynomail Addition
assert pffa.modAdd(pffa.Poly([3, 7, 96, 37]), pffa.Poly([124, 83, 14]), 127) == pffa.Poly([0, 90, 110, 37])

#Polynomial Negation
assert pffa.modNegate(pffa.Poly([1,0,1]), 127) == pffa.Poly([126, 0, 126])

#Polynomail Subtraction
assert pffa.modSub(pffa.Poly([3, 7, 96, 37]), pffa.Poly([3, 7, 96, 37]), 127) == pffa.Poly([])

#Random Polynomial
#print(pffa.randPoly(3, 127))

#MultTableDeclaration
primePoly = pffa.Poly([5, 3, 1, 2, 1])
primePoly.declareMultTable(7)
#primePoly.printMultTable()

primePoly = pffa.Poly([19, 0, 1, 0, 1])
primePoly.declareMultTable(131)
#primePoly.printMultTable()

#Polynomial Multiplication
pa = pffa.Poly([-6, 0, 0, 5])
pb = pffa.Poly([-1, 2])
pc = pffa.Poly([-6, 5])
primePoly = primePoly = pffa.Poly([5, 3, 1, 2, 1])
primePoly.declareMultTable(4219)
mult = pffa.modMult(pa, pb, primePoly)
assert str(mult) == "4194x^3 + 4209x^2 + 4177x^1 + 4175x^0"
mult = pffa.modMult(pc, pb, primePoly)
assert str(mult) == "10x^2 + 4202x^1 + 6x^0"

#Polynomial Normalization
p = pffa.Poly([4, 2, 1, 5])
assert str(pffa.normalizePoly(p, 7)) == "1x^3 + 3x^2 + 6x^1 + 5x^0"

#Polynomial Powers:
primePoly = pffa.Poly([3, 1, 1])
primePoly.declareMultTable(43)
power = 25
poweredPoly = pffa.Poly([3, 11])
assert str(pffa.modPower(poweredPoly, power, primePoly)) == "3x^1 + 26x^0"
primePoly = pffa.Poly([3, 1, 1])
primePoly.declareMultTable(43)
power = 1848
poweredPoly = pffa.Poly([3, 11])
assert str(pffa.modPower(poweredPoly, power, primePoly)) == "1x^0" #Expected from Fermats Little Theorem

#Polynomial Divison mod n
pa = pffa.Poly([1, 3, 2, 1])
pb = pffa.Poly([6, 1, 0, 5])
mod = 7
q, rem = pffa.modNumDiv(pa, pb, mod)
assert f"{q} and {rem}" == "3x^0 and 2x^2 + 4x^0"
pa = pffa.Poly([6, 19, 0, 14, 0, 0, 0, 13])
pb = pffa.Poly([17, 0, -1, 0, 0, 1])
mod = 43
q, rem = pffa.modNumDiv(pa, pb, mod)
assert f"{q} and {rem}" == "13x^2 and 13x^4 + 14x^3 + 37x^2 + 19x^1 + 6x^0"
pa = pffa.Poly([6, 19, 0, 14, 0, 0, 0, 13])
pb = pffa.Poly([6, 19, 0, 14, 0, 0, 0, 13])
mod = 43
q, rem = pffa.modNumDiv(pa, pb, mod)
assert f"{q} and {rem}" == "1x^0 and Empty Polynomial"
pa = pffa.Poly([0, 5])
pb = pffa.Poly([5])
q, rem = pffa.modNumDiv(pa, pb, mod)
assert f"{q} and {rem}" == "1x^1 and Empty Polynomial"
pa = pffa.Poly([5])
pb = pffa.Poly([5])
q, rem = pffa.modNumDiv(pa, pb, mod)
assert f"{q} and {rem}" == "1x^0 and Empty Polynomial"

#euclidian Algorithm
a = pffa.Poly([12, 4, 13, 1])
b = pffa.Poly([11, 16, 2, 22, 1])
#print(pffa.euclidianAlgorithm(a, b, 23))
a = pffa.Poly([6, 7, 1])
b = pffa.Poly([-6, -5, 1])
#print(pffa.euclidianAlgorithm(a, b, 23))
a = pffa.Poly([6, 7, 1])
b = pffa.Poly([6, 7, 1])
#print(pffa.euclidianAlgorithm(a, b, 23))
a = pffa.Poly([-2, -1, 1, 0, -2, 1])
b = pffa.Poly([-2, -1, -1, 1])
#print(pffa.euclidianAlgorithm(a, b, 23))
a = pffa.Poly([-2, -1, 1, 0, -2, 5])
b = pffa.Poly([-2, -1, -1, 1])
#print(pffa.euclidianAlgorithm(a, b, 23))