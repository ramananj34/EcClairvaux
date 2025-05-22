import sys
import os

# Add the project root directory to sys.path
print(sys.path)
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from EcClairvaux import ModularArithmetic

print(ModularArithmetic.euclidianAlgorithm(5, 15))