#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
从train.csv中读取数据训练，
训练并保存训练模型
'''

from numpy import *
import csv
import joblib

def toFloat(arr):
    arr = mat(arr)
    m,n = shape(arr)
    for i in range(m):
        for j in range(n):  
            arr = arr.astype(float64)
    return arr



def loadTrainData():
    l=[]
    with open('train.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l.remove(l[0])
    l=array(l)
    label=l[:,0]
    data = l[:,1:]
    return toFloat(data),toFloat(label);

from sklearn.neighbors import KNeighborsClassifier
def knnClassify(trainData, trainLabel):
    clf = KNeighborsClassifier()
    clf.fit(trainData, ravel(trainLabel))        # ravel转换成行向量
    return clf
from sklearn import svm
def svmClassify(trainData, trainLabel):
    clf = svm.SVC(gamma='scale')
    clf.fit(trainData, ravel(trainLabel))        # ravel转换成行向量
    return clf
from sklearn import tree
def treeClassify(trainData, trainLabel):
    clf = tree.DecisionTreeClassifier()
    clf.fit(trainData, ravel(trainLabel))        # ravel转换成行向量
    return clf
from sklearn.linear_model import LogisticRegression
def LRClassify(trainData, trainLabel):
    clf = LogisticRegression(solver='newton-cg', multi_class='auto')
    clf.fit(trainData, ravel(trainLabel))
    return clf
from sklearn.naive_bayes import GaussianNB
def NBClassify(trainData, trainLabel):
    clf = GaussianNB()
    clf.fit(trainData, ravel(trainLabel))
    return clf


def main():
    trainData, trainLabel = loadTrainData()
    print('Data Ready')
    clf = knnClassify(trainData,trainLabel)
    joblib.dump(clf, 'knnClf.pkl')
    clf = svmClassify(trainData, trainLabel)
    joblib.dump(clf, 'svmClf.pkl')
    clf= treeClassify(trainData, trainLabel)
    joblib.dump(clf, 'treeClf.pkl')
    clf= LRClassify(trainData, trainLabel)
    joblib.dump(clf, 'LRClf.pkl')
   # clf= NBClassify(trainData, trainLabel)
    #joblib.dump(clf, 'NBClf.pkl')

    print('Training Over')


if __name__ == '__main__':
    main()
