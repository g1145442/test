# coding: utf-8
import csv
with open('PrimeMinisters.csv','rU') as aFile:
    reader = csv.reader(aFile)
    for row in reader:
        for colmn in row:
            print colmn,
        print
aFile.close()