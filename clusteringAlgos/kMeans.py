import math
import numpy
import random

class KMeansCluster:

    def findKMeans(self, data, k, numIterations):
        numPoints = len(data)
        numDims = len(data[0])

        means = []
        clusterNumbers = []

        # Generate an initial set of means. TODO: optimize initial guess.
        for vector in range(k):
            mean = []
            for index in range(numDims):
                x = random.uniform( 0.01, 99.99)
                mean.append(x)
                #print "vector = ", vector, "index = " , index, "x = " , x
            means.append(mean)

        print "Finding " , k , " means"


        # calculate new means
        for i in range(numIterations):
            distances = calcDistanceMatrx(data, means)
            clusterNumbers = assignPointsToClusters(distances, means)
            means = calcNewMeans(distances)
            if(i%10 == 0):
                print "Iteration: " , i

        return clusterNumbers



    def calcDistanceMatrix(self, originalPoints, calculatedMeans):
        numPoints = len(originalPoints)
        numDims = len(originalPoints[0])
        numMeans = len(calculatedMeans)

        distances = numpy.zeros( (numPoints, numPoints) )

        #TODO only compute upper triangular and reflect.
        for vector_i in range(numPoints):
            for vector_j in range(numMeans):
                norm = 0
                for index in range(numDims):
                    norm += math.pow( originalPoints[vec_i][index]-calculatedMeans[vec_j][index], 2)
                distances[vector_i][vector_j]= math.sqrt(norm)

        return distance

    def assignPointsToClusters(self, originalPoints, calculatedMeans):


    def calcNewMeans(self, distances, calculatedMeans):

        newMeans = []

        return newMeans;
