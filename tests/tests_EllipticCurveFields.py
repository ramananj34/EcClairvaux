#Tests written with the help of chatGPT

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

print("All Tests Passed!")