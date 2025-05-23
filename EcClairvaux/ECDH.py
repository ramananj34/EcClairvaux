from EcClairvaux import EllipticCurveFields as ecf

class ECDH:

    @staticmethod
    def generatePublicKey(privateKey, generator, ec):
        return ecf.multPoint(generator, privateKey, ec)

    @staticmethod
    def computeSharedKey(privateKey, publicKey, ec):
        return ecf.multPoint(publicKey, privateKey, ec).x