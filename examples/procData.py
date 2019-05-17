#!/usr/bin/python3
#-*- coding: utf-8 -*-
import csv
import random

def procData():
    l=[]
    avg=[]
    with open('tmpData.csv') as file:
        lines = csv.reader(file)
        nl = 1
        for line in lines:
            if nl==1:
                nl=0
            else:
                sm=0
                for i in range(1,31):
                    sm+=float(line[i])
                sm/=30
                sm *= 0.05
                avg.append(sm)
            l.append(line) #l[i]的噪声为avg[i-1]
        
        title = l[0]
        l.remove(l[0])#l[i]的噪声为avg[i]

        for j in range(0,len(l)):
            for i in range(1,31):
                l[j][i] = float(l[j][i])+random.uniform(-avg[j],avg[j])
        with open('data.csv','w',newline='')as myFile:
            myWriter = csv.writer(myFile)
            myWriter.writerow(title)
            for x in l:
                myWriter.writerow(x)

if __name__=='__main__':
    procData()
