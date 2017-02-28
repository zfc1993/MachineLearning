#coding=utf-8

# 2016-11-22

from numpy import *

# load data from file 
def loadDataSet(fileName):
	dataMat = []
	fr = open(fileName)
	for line in fr.readlines():
		curLine = line.strip().split('\t')
		fltLine = map(float,curLine)
		dataMat.append(fltLine)
	return dataMat
		
# compute distance in E 

'''def distEclud(vecA, vecB):
	return sqrt(sum(pow(vecA - vecB, 2)))
'''
	
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))	
	
# initialize centroids 这块循环不是很明白咋个回事

def randCent(dataSet, k):
	n = shape(dataSet)[1]
	centroids = mat(zeros((k,n)))
	for j in range(n):
		minJ = min(dataSet[:,j])
		rangeJ = float(max(array(dataSet)[:,j])- minJ)
		centroids[:, j] = minJ + rangeJ * random.rand(k,1)
	return centroids
	
# k-means
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
	m = shape(dataSet)[0]
	# 存放距离每个样本点最近的聚类中心的序号（以下标表示）
	clusterAssment = mat(zeros((m,2)))
	centroids = randCent(dataSet, k)
	# 控制迭代次数 当所有样本点所属的聚类中心不再变化时clusterChanged为False
	clusterChanged = True
	while clusterChanged:
		clusterChanged = False
		# 为每个样本点计算最近聚类中心
		for i in range(m):
			# inf:正无穷
			minDist = inf
			minIndex = -1
			for j in range(k):
				dist = distEclud(centroids[j, :],dataSet[i, :])
				if dist < minDist:
					minDist = dist
					minIndex = j
			if clusterAssment[i,0] !=  minIndex:
				clusterChanged = True
			clusterAssment[i,:] = minIndex, minDist**2
		print centroids
		# recalculate centroids
		for cent in range(k):
			# get all the points in this cluster 
			ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
			# assign centroid to mean 
			centroids[cent, :] = mean(ptsInClust, axis = 0)
	return centroids, clusterAssment
	
# plot data matplotlib显示图像 。。。。。。
def show(dataSet, k, centroids, clusterAssment):
     from matplotlib import pyplot as plt  
     numSamples, dim = dataSet.shape  
     mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']  
     for i in xrange(numSamples):  
         markIndex = int(clusterAssment[i, 0])  
         plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])  
     mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']  
     for i in range(k):  
         plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)  
     plt.show()
       

# test funcion
def main():
	dataMat = mat(loadDataSet('testSet.txt'))
	myCentroids, clusterAssing = kMeans(dataMat, 4)
	print myCentroids
	show(dataMat, 4, myCentroids, clusterAssing)
	
if __name__ == '__main__':
	main() 