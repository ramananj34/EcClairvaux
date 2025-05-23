#Made with the help of ChatGPT

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from EcClairvaux import EllipticCurveFields as ecf

#Point and Curve Class and Prints
p = ecf.Point(1, 2)
assert str(p) == "(1,2)"
e = ecf.CurveField(-4, 7, 97)
assert str(e) == "y^2 = x^3 + -4x + 7 Over Field 97"
print("(1/) Point/Curve Declaration and toString Tests Passed")

#Point and Curve Equals
assert ecf.Point(1,2) == ecf.Point(1,2)
assert ecf.Point(0,0) != ecf.Point(0,1)
assert ecf.CurveField(5, 5, 97) == ecf.CurveField(5,5, 97)
assert ecf.CurveField(4, 5, 97) != ecf.CurveField(5,5, 101)
print("(2/) Point and Curve Equality Tests Passed")

#Negate Point
p = ecf.Point(13, 6)
assert str(ecf.negatePoint(p)) == "(13,-6)"
p = ecf.Point(1, -4)
assert str(ecf.negatePoint(p)) == "(1,4)"
print("(3/) Point Negation Tests Passed")

#Point at infinity
assert str(ecf.POINT_AT_INFINITY) == "(0,0)"
print("(4/) Point at Infinity Tests Passed")

#Point Addition
assert ecf.addPoints(ecf.Point(10, 17), ecf.Point(90, 28), ecf.CurveField(6,5,97)) == ecf.Point(82, 41)
assert ecf.addPoints(ecf.Point(16, 13), ecf.Point(3, 1), ecf.CurveField(2,2,17)) == ecf.Point(7, 11)
assert ecf.addPoints(ecf.Point(10, 17), ecf.Point(0, 0), ecf.CurveField(6, 5, 97)) == ecf.Point(10, 17)
assert ecf.addPoints(ecf.Point(0, 0), ecf.Point(90, 28), ecf.CurveField(6, 5, 97)) == ecf.Point(90, 28)
assert ecf.addPoints(ecf.Point(10, 17), ecf.Point(10, 17), ecf.CurveField(6, 5, 97)) == ecf.Point(61, 9)
assert ecf.addPoints(ecf.Point(16, 13), ecf.Point(16, 13), ecf.CurveField(2, 2, 17)) == ecf.Point(0, 11)
assert ecf.addPoints(ecf.Point(3, 1), ecf.Point(3, 1), ecf.CurveField(2, 2, 17)) == ecf.Point(13, 7)
assert ecf.addPoints(ecf.Point(3, 1), ecf.Point(3, 16), ecf.CurveField(2, 2, 17)) == ecf.Point(0, 0)
assert ecf.addPoints(ecf.Point(0, 0), ecf.Point(0, 0), ecf.CurveField(2, 2, 17)) == ecf.Point(0, 0)
assert ecf.addPoints(ecf.Point(4, 6), ecf.Point(7, 10), ecf.CurveField(2, 3, 13)) == ecf.Point(11, 2)
assert ecf.addPoints(ecf.Point(1, 1), ecf.Point(3, 7), ecf.CurveField(0, 0, 11)) == ecf.Point(5, 9)
assert ecf.addPoints(ecf.Point(4, 11), ecf.Point(10, 7), ecf.CurveField(1, 1, 13)) == ecf.Point(11, 11)
print("(5/) Point addition Tests Passed")

#Point Multiplication
assert ecf.multPoint(ecf.Point(3, 6), 2, ecf.CurveField(2, 3, 97)) == ecf.Point(80,10)
assert ecf.multPoint(ecf.Point(3, 6), 1, ecf.CurveField(2, 3, 97)) == ecf.Point(3, 6)
assert ecf.multPoint(ecf.Point(3, 6), 0, ecf.CurveField(2, 3, 97)) == ecf.Point(0, 0)
assert ecf.multPoint(ecf.Point(80, 10), 1, ecf.CurveField(2, 3, 97)) == ecf.Point(80, 10)
assert ecf.multPoint(ecf.Point(80, 10), 2, ecf.CurveField(2, 3, 97)) == ecf.Point(3, 91)
assert ecf.multPoint(ecf.Point(3, 6), 3, ecf.CurveField(2, 3, 97)) == ecf.Point(80, 87)
assert ecf.multPoint(ecf.Point(3, 6), 20, ecf.CurveField(2, 3, 97)) == ecf.POINT_AT_INFINITY
assert ecf.multPoint(ecf.Point(3, 6), 2, ecf.CurveField(2, 3, 97)) == ecf.addPoints(ecf.Point(3, 6), ecf.Point(3, 6), ecf.CurveField(2, 3, 97))
assert ecf.multPoint(ecf.Point(0, 0), 10, ecf.CurveField(2, 3, 97)) == ecf.Point(0, 0)
assert ecf.multPoint(ecf.Point(16, 34), 15, ecf.CurveField(5, 7, 1009)) == ecf.Point(112, 490)
assert ecf.multPoint(ecf.Point(3, 6), 6, ecf.CurveField(2, 3, 97)) == ecf.Point(3, 6)


print("All Tests Passed!")