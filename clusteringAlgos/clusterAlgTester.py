from kMeans import *
from numpy import *


print "Clustering Algorithm Testing Class"

kMeansObject = KMeansCluster()
numVecs = random.randint(4, 100)
numDims = random.randint(3, 5)

print "numVecs = " , numVecs, " numDims = ", numDims

# Generate random data in order to test clustering algorithms.
randomData = numpy.zeros( (numVecs, numDims) )
for i in range(numVecs):
    for j in range(numDims):
        randomData[i][j] = random.uniform(.01, 99.99)



kMeansObject.findKMeans(randomData, 2)
