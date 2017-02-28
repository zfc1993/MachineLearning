# coding=utf-8
'''
name: LinearRegression with normal equation
date: 2017.02.21
author: Vincent

'''

from numpy import *

def loadDataSet(fileName):
	numFeat = len(open(fileName).readline().split('\t')) - 1 # the num of features
	dataMat = []; labelMat = []
	fr = open(fileName)
	for line in fr.readlines():
		lineArr = []
		curLine = line.strip().split('\t')
		for i in range(numFeat):
			lineArr.append(float(curLine[i]))
		dataMat.append(lineArr)
		labelMat.append(float(curLine[-1]))
	return dataMat, labelMat

def standRegres(xArr, yArr):
	xMat = mat(xArr); yMat = mat(yArr).T
	xTx = xMat.T*xMat
	if linalg.det(xTx) == 0.0:
		print ("This matrix is singular, cannot do inverse!")
		return 
	ws = xTx.I * xMat.T * yMat
	return ws 

if __name__ == '__main__':
	dataMat,labelMat = loadDataSet("ex0.txt")
	ws = standRegres(dataMat,labelMat)
	for i in ws:
		print(i)
	
	
	