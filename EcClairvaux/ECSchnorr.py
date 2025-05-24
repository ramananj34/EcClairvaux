from EcClairvaux import EllipticCurveFields as ecf
from EcClairvaux import NumericalFiniteFieldArithmetic as nffa
import hashlib

class ECSchnorr:

    class SchnorrSignature:

        def __init__(self, point, s):
            self.point = point
            self.s = s

        def __str__(self):
            return "Point: " + str(self.point) + " S: " + str(self.s)
    
    @staticmethod
    def generatePublicKey(privateKey, generator, ec):
        return ecf.multPoint(generator, privateKey, ec)
    
    @staticmethod 
    def signDoc(message, secretKey, generator, ec):
        randVal = nffa.randModVal(generator.order)
        randPoint = ecf.multPoint(generator, randVal, ec)
        hash = int.from_bytes(hashlib.sha256((str(randPoint.x) + str(randPoint.y) + message).encode('utf-8')).digest(), byteorder='big') % generator.order
        sig = nffa.modSub(randVal, nffa.modMult(secretKey, hash, generator.order), generator.order)
        return ECSchnorr.SchnorrSignature(randPoint, sig)
    
    @staticmethod
    def validateDoc(message, publicKey, signature, generator, ec):
        hash = int.from_bytes(hashlib.sha256((str(signature.point.x) + str(signature.point.y) + message).encode('utf-8')).digest(), byteorder='big') % generator.order
        point = ecf.addPoints(ecf.multPoint(generator, signature.s, ec), ecf.multPoint(publicKey, hash, ec), ec)
        return signature.point == point