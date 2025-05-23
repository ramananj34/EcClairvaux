from EcClairvaux import EllipticCurveFields as ecf
from EcClairvaux import NumericalFiniteFieldArithmetic as nffa
from random import randint
from math import ceil, log2

class ECMQV:
    
    @staticmethod
    def getEphemeralKeyPair(generator, ec):
        emphemeralPrivate = randint(0, ec.p-1)
        ephemeralPublic = ECMQV.generatePublicKey(emphemeralPrivate, generator, ec)
        return emphemeralPrivate, ephemeralPublic
    
    @staticmethod
    def generatePublicKey(privateKey, generator, ec):
        return ecf.multPoint(generator, privateKey, ec)
    
    @staticmethod
    def avf(x, generator):
        #Associate Value Function
        return (x%(pow(2, ceil((log2(generator.order))/2)))) + (pow(2, ceil((log2(generator.order))/2)))
    
    @staticmethod
    def computeSharedKey(aStaticPrivateKey, aEphemeralPrivateKey, aEphemeralPublicKey, bStaticPublicKey, bEphemeralPublicKey, generator, curve):
        sig = aEphemeralPrivateKey + ECMQV.avf(aEphemeralPublicKey.x, generator)*aStaticPrivateKey
        pt = ecf.addPoints(bEphemeralPublicKey, ecf.multPoint(bStaticPublicKey, ECMQV.avf(bEphemeralPublicKey.x, generator), curve), curve)
        sspt = ecf.multPoint(pt, sig, curve)
        if (curve.cofactor > 1):
            sspt = ecf.multPoint(sspt, curve.cofactor, curve)
        return sspt.x