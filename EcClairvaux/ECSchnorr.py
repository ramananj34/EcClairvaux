from EcClairvaux import EllipticCurveFields as ecf

class ECSchnorr:
    
    @staticmethod
    def generatePublicKey(privateKey, generator, ec):
        return ecf.multPoint(generator, privateKey, ec)