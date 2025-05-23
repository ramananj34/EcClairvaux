#Tests written with the help of chatGPT

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from EcClairvaux import ModularArithmetic as modari

#Add
assert modari.modAdd(5, 3, 7) == 1  # (5 + 3) % 7 = 1
assert modari.modAdd(-5, 3, 7) == 5  # (-5 + 3) % 7 = 5
assert modari.modAdd(0, 5, 7) == 5  # (0 + 5) % 7 = 5
assert modari.modAdd(5, 0, 7) == 5  # (5 + 0) % 7 = 5
assert modari.modAdd(10, 15, 100) == 25  # (10 + 15) % 100 = 25
assert modari.modAdd(999999999, 888888888, 1000000000) == 888888887  # (999999999 + 888888888) % 1000000000 = 888888887
assert modari.modAdd(10, 5, 6) == 3  # (10 + 5) % 6 = 3
assert modari.modAdd(-5, -8, 12) == 11  # (-5 + -8) % 12 = 11
print("(1/12) Addition Tests Passed")

#Subtract
assert modari.modSub(5, 3, 7) == 2  # (5 - 3) % 7 = 2
assert modari.modSub(3, 5, 7) == 5  # (3 - 5) % 7 = 5
assert modari.modSub(0, 5, 7) == 2  # (0 - 5) % 7 = 2
assert modari.modSub(5, 0, 7) == 5  # (5 - 0) % 7 = 5
assert modari.modSub(10, 15, 100) == 95  # (10 - 15) % 100 = 95
assert modari.modSub(999999999, 888888888, 1000000000) == 111111111  # (999999999 - 888888888) % 1000000000 = 111111111
assert modari.modSub(10, 5, 6) == 5  # (10 - 5) % 6 = 5
assert modari.modSub(-5, -8, 12) == 3  # (-5 - -8) % 12 = 3
assert modari.modSub(-5, 3, 7) == 6  # (-5 - 3) % 7 = 6
assert modari.modSub(3, 10, 6) == 5  # (3 - 10) % 6 = 5
print("(2/12) Subtraction Tests Passed")

#Multiply
assert modari.modMult(5, 3, 7) == 1  # (5 * 3) % 7 = 15 % 7 = 1
assert modari.modMult(-5, 3, 7) == 6  # (-5 * 3) % 7 = -15 % 7 = 6
assert modari.modMult(5, -3, 7) == 6  # (5 * -3) % 7 = -15 % 7 = 6
assert modari.modMult(0, 5, 7) == 0  # (0 * 5) % 7 = 0
assert modari.modMult(5, 0, 7) == 0  # (5 * 0) % 7 = 0
assert modari.modMult(10, 15, 100) == 50  # (10 * 15) % 100 = 150 % 100 = 50
assert modari.modMult(999999999, 888888888, 1000000000) == 111111112  # (999999999 * 888888888) % 1000000000 = 111111112
assert modari.modMult(10, 5, 6) == 2  # (10 * 5) % 6 = 50 % 6 = 2
assert modari.modMult(-5, -8, 12) == 4  # (-5 * -8) % 12 = 40 % 12 = 4
assert modari.modMult(-5, 3, 7) == 6  # (-5 * 3) % 7 = -15 % 7 = 6
assert modari.modMult(123456789, 987654321, 1000000000) == 112635269  # (123456789 * 987654321) % 1000000000 = 112635269
print("(3/12) Multiplication Tests Passed")

#Negate
assert modari.modNegate(5, 7) == 2  # -5 % 7 = 2 (since 5 + 2 = 7)
assert modari.modNegate(0, 7) == 0  # -0 % 7 = 0
assert modari.modNegate(-5, 7) == 5  # -(-5) % 7 = 5 (since -5 + 5 = 0)
assert modari.modNegate(10, 12) == 2  # -10 % 12 = 2 (since 10 + 2 = 12)
assert modari.modNegate(999999999, 1000000000) == 1  # -(999999999) % 1000000000 = 1
assert modari.modNegate(10, 6) == 2  # -10 % 6 = 2 (since 10 + 2 = 12, 12 % 6 = 0)
assert modari.modNegate(-3, 7) == 3  # 3 mod 7 = 3
assert modari.modNegate(5, 1) == 0  # -5 % 1 = 0 (anything modulo 1 is 0)
assert modari.modNegate(-13, 12) == 1  # 13 mod 12 = 1
print("(4/12) Negation Tests Passed")

#Euclidian Algorithm
assert modari.euclidianAlgorithm(56, 98) == 14  # GCD of 56 and 98 is 14
assert modari.euclidianAlgorithm(48, 18) == 6   # GCD of 48 and 18 is 6
assert modari.euclidianAlgorithm(7, 1) == 1  # GCD of 7 and 1 is 1
assert modari.euclidianAlgorithm(1, 999999) == 1  # GCD of 1 and any number is 1
assert modari.euclidianAlgorithm(0, 10) == 10  # GCD of 0 and 10 is 10
assert modari.euclidianAlgorithm(10, 0) == 10  # GCD of 10 and 0 is 10
assert modari.euclidianAlgorithm(20, 20) == 20  # GCD of 20 and 20 is 20
assert modari.euclidianAlgorithm(35, 64) == 1  # GCD of 35 and 64 is 1 (they are coprime)
assert modari.euclidianAlgorithm(123456789, 987654321) == 9  # GCD of 123456789 and 987654321 is 9
assert modari.euclidianAlgorithm(17, 19) == 1  # GCD of two primes is always 1
assert modari.euclidianAlgorithm(0, 0) == 0  # GCD of 0 and 0 is 0
print("(5/12) Euclidian Algorithm Tests Passed")

#Extended Euclidian Algorithm
x, y = modari.extendedEuclidianAlgorithm(3, 11)
assert 3 * x + 11 * y == 1  # Check if the equation 3x + 11y = 1 holds
x, y = modari.extendedEuclidianAlgorithm(11, 3)
assert 11 * x + 3 * y == 1  # Check if the equation 3x + 11y = 1 holds
x, y = modari.extendedEuclidianAlgorithm(56, 98)
assert 56 * x + 98 * y == 14  # Check if the equation 56x + 98y = 14 holds
x, y = modari.extendedEuclidianAlgorithm(0, 10)
assert 0 * x + 10 * y == 10  # Check if the equation 0x + 10y = 10 holds
x, y = modari.extendedEuclidianAlgorithm(20, 20)
assert 20 * x + 20 * y == 20  # Check if the equation 20x + 20y = 20 holds
x, y = modari.extendedEuclidianAlgorithm(35, 64)
assert 35 * x + 64 * y == 1  # Check if the equation 35x + 64y = 1 holds
x, y = modari.extendedEuclidianAlgorithm(123456789, 987654321)
assert 123456789 * x + 987654321 * y == 9  # Check if the equation holds
x, y = modari.extendedEuclidianAlgorithm(17, 19)
assert 17 * x + 19 * y == 1  # Check if the equation 17x + 19y = 1 holds
x, y = modari.extendedEuclidianAlgorithm(0, 1)
assert 0 * x + 1 * y == 1  # Check if the equation 0x + 1y = 1 holds
print("(6/12) Extended Euclidian Algorithm Tests Passed")

#Inverse
assert modari.modInverse(3, 11) == 4
assert modari.modInverse(10, 17) == 12
assert modari.modInverse(7, 19) == 11
assert modari.modInverse(2, 5) == 3
assert modari.modInverse(123456789, 1000000007) == 18633540
assert modari.modInverse(2, 4) is None
assert modari.modInverse(6, 9) is None
assert modari.modInverse(0, 5) is None
assert modari.modInverse(1, 7) == 1  # 1 * 1 = 1 ≡ 1 (mod 7)
assert modari.modInverse(1, 123456789) == 1  # 1 * 1 = 1 ≡ 1 (mod 123456789)
assert modari.modInverse(7, 7) is None  # gcd(7, 7) = 7, no inverse exists
print("(7/12) Inverse Tests Passed")

#Division
assert modari.modDiv(4, 2, 5) == 2
assert modari.modDiv(3, 4, 11) == 9
assert modari.modDiv(10, 3, 17) == 9
assert modari.modDiv(5, 2, 7) == 6
assert modari.modDiv(0, 5, 7) == 0  # 0 / 5 mod 7 = 0
assert modari.modDiv(123456789, 987654321, 1000000007) == 203935601
assert modari.modDiv(4, 2, 4) is None
assert modari.modDiv(6, 9, 12) is None
assert modari.modDiv(5, 0, 7) is None
assert modari.modDiv(7, 7, 7) is None
assert modari.modDiv(1, 1, 7) == 1
assert modari.modDiv(1, 1, 123456789) == 1
print("(8/12) Divide Tests Passed")

#Random Int in CCRC
for i in range(0,100):
    pick = modari.randModVal(10)
    assert pick >= 0 and pick <= 9
print("(9/12) Random CCRC Tests Passed")

#Legrande Symbols
assert modari.legendreSymbol(1, 5) == 1
assert modari.legendreSymbol(0, 7) == 0
assert modari.legendreSymbol(6, 7) == -1
assert modari.legendreSymbol(2, 5) == -1
assert modari.legendreSymbol(3, 7) == -1 
assert modari.legendreSymbol(9, 11) == 1
assert modari.legendreSymbol(-4, 13) == 1
assert modari.legendreSymbol(200, 97) == 1
assert modari.legendreSymbol(14, 19) == -1
assert modari.legendreSymbol(1, 2) == 1
print("(10/12) Legrande Symbol Tests Passed")

#Power
assert modari.modPow(2, 3, 5) == 3  # 2^3 % 5 = 8 % 5 = 3
assert modari.modPow(5, 0, 7) == 1  # 5^0 % 7 = 1
assert modari.modPow(3, -1, 7) == 5  # 3^(-1) % 7 = 5, because 3 * 5 % 7 = 1
assert modari.modPow(2, 100, 7) == 2  # 2^100 % 7 = 2 
assert modari.modPow(-3, 3, 7) == 1  # (-3)^3 % 7 = -27 % 7 = 6
assert modari.modPow(-3, 4, 7) == 4  # (-3)^4 % 7 = 81 % 7 = 2
assert modari.modPow(10, 3, 7) == 6  # 10^3 % 7 = 1000 % 7 = 6
assert modari.modPow(1, 12345, 7) == 1  # 1^12345 % 7 = 1
assert modari.modPow(0, 5, 7) == 0  # 0^5 % 7 = 0
assert modari.modPow(0, 0, 7) == 1  # 0^0 % 7 = 1
assert modari.modPow(12345, 67890, 1) == 0  # any number mod 1 = 0
assert modari.modPow(5, -3, 13) == 5  # 5^(-3) % 13 = 5
print("(11/12) Power Tests Passed")

#Sqrt
# %3 (FLT)
assert modari.modPow(modari.modSqrt(2, 7), 2, 7) == 2
assert modari.modPow(modari.modSqrt(4, 11), 2, 11) == 4
assert modari.modPow(modari.modSqrt(6, 19), 2, 19) == 6
assert modari.modPow(modari.modSqrt(1, 19), 2, 19) == 1
assert modari.modPow(modari.modSqrt(1, 7), 2, 7) == 1
# %1 (Tonelli/Shank)
assert modari.modPow(modari.modSqrt(4, 5), 2, 5) == 4
assert modari.modPow(modari.modSqrt(9, 13), 2, 13) == 9
assert modari.modPow(modari.modSqrt(1, 5), 2, 5) == 1
assert modari.modPow(modari.modSqrt(4, 17), 2, 17) == 4
assert modari.modPow(modari.modSqrt(8, 17), 2, 17) == 8
assert modari.modPow(modari.modSqrt(3, 13), 2, 13) == 3
print("(12/12) Square Root Tests Passed")
    

print("All Tests Passed!")