#Made with the help of ChatGPT

import sys
import os
from random import randint
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from EcClairvaux import EllipticCurveFields as ecf
from EcClairvaux import ECMQV as mqv

#Public Info: brainpoolP256r1
curve = ecf.CurveField(0x7d5a0975fc2c3057eef67530417affe7fb8055c126dc5c6ce94a4b44f330b5d9, 0x26dc5c6ce94a4b44f330b5d9bbd77cbf958416295cf7e1ce6bccdc18ff8c07b6, 0xa9fb57dba1eea9bc3e660a909d838d726e3bf623d52620282013481d1f6e5377)
generator = ecf.Point(0x8bd2aeb9cb7e57cb2c4b482ffc81b7afb9de27e1e3bd23c23a4453bd9ace3262, 0x547ef835c3dac4fd97f8461a14611dc9c27745132ded8e545c1d54c72f046997)
curve.declareCofactor(0x1)
generator.declareOrder(0xa9fb57dba1eea9bc3e660a909d838d718c397aa3b561a6f7901e0e82974856a7)

aStaticPrivateKey = randint(0, curve.p-1)
bStaticPrivateKey = randint(0, curve.p-1)
aStaticPublicKey = mqv.generatePublicKey(aStaticPrivateKey, generator, curve)
bStaticPublicKey = mqv.generatePublicKey(bStaticPrivateKey, generator, curve)
aEphemeralPrivateKey, aEphemeralPublicKey = mqv.getEphemeralKeyPair(generator, curve)
bEphemeralPrivateKey, bEphemeralPublicKey = mqv.getEphemeralKeyPair(generator, curve)

print(mqv.computeSharedKey(aStaticPrivateKey, aEphemeralPrivateKey, aEphemeralPublicKey, bStaticPublicKey, bEphemeralPublicKey, generator, curve))
print(mqv.computeSharedKey(bStaticPrivateKey, bEphemeralPrivateKey, bEphemeralPublicKey, aStaticPublicKey, aEphemeralPublicKey, generator, curve))