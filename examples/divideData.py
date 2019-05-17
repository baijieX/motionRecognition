#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
读取data.csv中内容,
随机选出20%输出到test.csv，
80%输出到train.csv,
测试正确结果输出到answer.txt
'''
import random
import csv
def divideData():
    lTrain=[]
    lTest=[]
    answer=[]
    with open("data.csv") as file:
        lines = csv.reader(file)
        for line in lines:
            lTrain.append(line)
 #   numData = len(lTrain)-1
 #   numTrain = int(numData*0.8)
 #   numTest = numData-numTrain
    numTrain= 1000
    numTest = 400
    numData = numTrain+numTest
    lTrain = lTrain[0:numData+1]
    t = [];#t中存放y用于测试的数据行数
    cnt = 0;
    while cnt<numTest:
        x = random.randint(1,numData)
        if x not in t:
            t.append(x)
            cnt+=1
    #到这里已经写完t数组;
    lTest.append(lTrain[0][1:])
    t.sort(reverse=True);
    for i in t:
        lTest.append(lTrain[i][1:])
        answer.append(lTrain[i][0])
        del lTrain[i]

    with open('answer.csv','w',newline='') as myFile:
        myWriter = csv.writer(myFile)
        for i in answer:
            myWriter.writerow(i)
    print('answer.csv Ready')

    with open('test.csv','w',newline='') as myFile:
        myWriter = csv.writer(myFile)
        for i in lTest:
            myWriter.writerow(i)

    print('test.csv Ready')

    with open('train.csv','w',newline='') as myFile:
        myWriter = csv.writer(myFile)
        for i in lTrain:
            myWriter.writerow(i)
    
    print('train.csv Ready')

    return answer;
if __name__=='__main__':
    divideData()
