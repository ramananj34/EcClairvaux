import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from EcClairvaux import PolynomialFiniteFieldArithmetic as pffa

poly = pffa.Poly([0, 0, 0])
print(poly)