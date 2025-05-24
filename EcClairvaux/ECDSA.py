from EcClairvaux import EllipticCurveFields as ecf

class ECDSA:
    
    class DSASignature:

        def __init__(self, c, d):
            self.c = c
            self.d = d

    @staticmethod
    def generatePublicKey(privateKey, generator, ec):
        return ecf.multPoint(generator, privateKey, ec)
    