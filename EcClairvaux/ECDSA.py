from EcClairvaux import EllipticCurveFields as ecf
from EcClairvaux import NumericalFiniteFieldArithmetic as nffa
import hashlib

class ECDSA:
    
    class DSASignature:

        def __init__(self, s1, s2):
            self.s1 = s1
            self.s2 = s2

        def __str__(self):
            return "S1: " + str(self.s1) + " S2: " + str(self.s2)

    @staticmethod
    def generatePublicKey(privateKey, generator, ec):
        return ecf.multPoint(generator, privateKey, ec)
    
    @staticmethod
    def signDoc(message, secretKey, generator, curve):
        hash = int.from_bytes(hashlib.sha256((message).encode('utf-8')).digest(), byteorder='big') % generator.order
        randVal = nffa.randModVal(generator.order)
        randPoint = ecf.multPoint(generator, randVal, curve)
        xOnRand = randPoint.x % generator.order
        d = nffa.modDiv(nffa.modAdd(hash, nffa.modMult(xOnRand, secretKey, generator.order), generator.order), randVal, generator.order)
        return ECDSA.DSASignature(xOnRand, d)
    
    @staticmethod
    def validateDoc(message, publicKey, signature, generator, ec):
        hash = int.from_bytes(hashlib.sha256((message).encode('utf-8')).digest(), byteorder='big') % generator.order
        h = nffa.modInverse(signature.s2, generator.order)
        h1 = nffa.modMult(hash, h, generator.order)
        h2 = nffa.modMult(signature.s1, h, generator.order)
        pt = ecf.addPoints(ecf.multPoint(generator, h1, ec), ecf.multPoint(publicKey, h2, ec), ec)
        return pt.x == signature.s1

    