#!/usr/bin/python3
#-*- coding: utf-8 -*-

import joblib
import csv
from numpy import *
from trainData import toFloat

def loadTestData():
    l=[]
    with open('test.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l.remove(l[0])
    data = array(l)
    return toFloat(data);

def saveResult(result,csvName):
    with open(csvName,'w',newline='') as myFile:
        myWriter = csv.writer(myFile)
        for i in result:
            tmp=[]
            tmp.append(int(i))
            myWriter.writerow(tmp)

def testData():
    testData = loadTestData()

    clf=joblib.load('svmClf.pkl')
    resultSVM = clf.predict(testData)
    clf=joblib.load('knnClf.pkl')
    resultKNN = clf.predict(testData)
    clf=joblib.load('treeClf.pkl')
    resultTree= clf.predict(testData)
    clf=joblib.load('LRClf.pkl')
    resultLR  = clf.predict(testData)
    

    result = []
    result.append(resultKNN)
    result.append(resultSVM)
    result.append(resultTree)
    result.append(resultLR)

#    vote=[]
#    result=[]
#    n = len(resultSVM)
#    for i in range(n):
#        vote.append(resultLR[i])
#        vote.append(resultSVM[i])
#        vote.append(resultKNN[i])
#        vote.append(resultNB[i])
#        vote.append(resultTree[i])
#        result.append(max(vote, key=vote.count))
#        vote.clear()
        

#    saveResult(resultLR,'resultLR.csv')
#    saveResult(resultSVM,'resultSVM.csv')
#    saveResult(resultKNN,'resultKNN.csv')
    
    saveResult(result[3],'result.csv')

    answer=[]
    with open('answer.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            answer.append(line)


    l = len(result[0])
    for j in range(4):
        i = 0
        match=0
        while i < l:
            if int(answer[i][0])==int(result[j][i]):
                match+=1
            i+=1
        print("Done!")
        print(match,"/",l)
        print(1.0*match/l)


if __name__=='__main__':
    testData()
