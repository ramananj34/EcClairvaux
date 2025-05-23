#Made with the help of ChatGPT

import sys
import os
from random import randint
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from EcClairvaux import EllipticCurveFields as ecf
from EcClairvaux import ECMQV as mqv

#Test 1: 

#Public Info: brainpoolP256r1
curve = ecf.CurveField(0x7d5a0975fc2c3057eef67530417affe7fb8055c126dc5c6ce94a4b44f330b5d9, 0x26dc5c6ce94a4b44f330b5d9bbd77cbf958416295cf7e1ce6bccdc18ff8c07b6, 0xa9fb57dba1eea9bc3e660a909d838d726e3bf623d52620282013481d1f6e5377)
generator = ecf.Point(0x8bd2aeb9cb7e57cb2c4b482ffc81b7afb9de27e1e3bd23c23a4453bd9ace3262, 0x547ef835c3dac4fd97f8461a14611dc9c27745132ded8e545c1d54c72f046997)
curve.declareCofactor(0x1)
generator.declareOrder(0xa9fb57dba1eea9bc3e660a909d838d718c397aa3b561a6f7901e0e82974856a7)

bstart = time.time()

aStaticPrivateKey = randint(0, curve.p-1)
bStaticPrivateKey = randint(0, curve.p-1)
aStaticPublicKey = mqv.generatePublicKey(aStaticPrivateKey, generator, curve)
bStaticPublicKey = mqv.generatePublicKey(bStaticPrivateKey, generator, curve)
aEphemeralPrivateKey, aEphemeralPublicKey = mqv.getEphemeralKeyPair(generator, curve)
bEphemeralPrivateKey, bEphemeralPublicKey = mqv.getEphemeralKeyPair(generator, curve)

assert mqv.computeSharedKey(aStaticPrivateKey, aEphemeralPrivateKey, aEphemeralPublicKey, bStaticPublicKey, bEphemeralPublicKey, generator, curve) == mqv.computeSharedKey(bStaticPrivateKey, bEphemeralPrivateKey, bEphemeralPublicKey, aStaticPublicKey, aEphemeralPublicKey, generator, curve)

bend = time.time()

#-----------------------------

#Test 2: 

#Public Info: secp256r1
curve = ecf.CurveField(0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc, 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b, 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff)
generator = ecf.Point(0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
curve.declareCofactor(0x1)
generator.declareOrder(0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551)

sstart = time.time()

aStaticPrivateKey = randint(0, curve.p-1)
bStaticPrivateKey = randint(0, curve.p-1)
aStaticPublicKey = mqv.generatePublicKey(aStaticPrivateKey, generator, curve)
bStaticPublicKey = mqv.generatePublicKey(bStaticPrivateKey, generator, curve)
aEphemeralPrivateKey, aEphemeralPublicKey = mqv.getEphemeralKeyPair(generator, curve)
bEphemeralPrivateKey, bEphemeralPublicKey = mqv.getEphemeralKeyPair(generator, curve)

assert mqv.computeSharedKey(aStaticPrivateKey, aEphemeralPrivateKey, aEphemeralPublicKey, bStaticPublicKey, bEphemeralPublicKey, generator, curve) == mqv.computeSharedKey(bStaticPrivateKey, bEphemeralPrivateKey, bEphemeralPublicKey, aStaticPublicKey, aEphemeralPublicKey, generator, curve)

send = time.time()

print("brainpoolP256r1 time for exchange: " + str(bend-bstart))
print("secp256r1 time for exchange: " + str(send-sstart))
