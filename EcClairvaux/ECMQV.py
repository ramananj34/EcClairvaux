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
    def computeSharedKey(staticPrivateKeyA, ephemeralPrivateKeyA, ephemeralPublicKeyA, staticPublicKeyB, ephemeralPublicKeyB, generator, ec):
        impSig = nffa.modAdd(ephemeralPrivateKeyA, nffa.modMult(ECMQV.avf(ephemeralPublicKeyA.x, generator), staticPrivateKeyA, ec.p), ec.p)
        pt = ecf.addPoints(ephemeralPublicKeyB, ecf.multPoint(staticPublicKeyB, ECMQV.avf(ephemeralPublicKeyB.x, generator), ec), ec)
        ss = ecf.multPoint(pt, impSig, ec)
        if (ec.cofactor > 1):
            print(ec.cofactor)
            ss = ecf.multPoint(ss, ec.cofactor, ec)
        return ss.x