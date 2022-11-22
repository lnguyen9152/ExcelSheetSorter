#Lance Nguyen 11/22/2022

#this file is used to gather data from an excel file to output as arrays for any use.
#the .xlsx file must be named TradingPlans.xlsx and placed within the same folder as the program
#The sheet must be named Main, but can be changed on line 19.

#the program will automatically find the file path
#use the template posted to input levels, and this will sort and organize into a matrix.

# -1 is currently being used to signify empty values.

import pandas as pd
import numpy as np
import os

#Initilaize file path (uses same location as program and looks for a file named trading plan .xlsx)
file_path = os.path.abspath(os.path.dirname(__file__)  + '/TradingPlans.xlsx')

#debugging and setup
df=pd.read_excel(file_path,sheet_name='Main')

#appends empty to be -1
df = df.fillna(-1)

#create temp array to store values
temp = []
exit = []
hardstop_be = []
hardstop = []

#arrays
long = []
short = []
longexit = []
shortexit = []

#ranges of interest
r = [None]*4

#final arrays 
long_a = []
short_a = []

#array population
def loadValues():
    global temp, exit, hardstop_be, hardstop
    for i in range(len(df)):                #read row by row from excel file
        entry = df.loc[i, "Entry"]
        exit_a = df.loc[i, "Trail"]
        hardstop_be_a = df.loc[i, "Hardstop-BE"]
        hardstop_a = df.loc[i,"Hardstop"]
        temp.append(int(entry))
        exit.append(int(exit_a))
        hardstop_be.append(int(hardstop_be_a))
        hardstop.append(int(hardstop_a))

#points values to positions
def customArrays():
    global temp, long, short, longexit, shortexit
    longexit = temp[20:25]
    shortexit = temp[25:30]
    long = temp[0:10]
    short = temp[10:20]

def sortLS():
    global short, long, r, exit, hardstop_be, hardstop, temp, longexit, shortexit
    x = 0
    y = 0
    xflag = True
    yflag = True
    aflag = True
    for i in range(11):  
        x = (temp[i])           #long levels
        y = (temp[i+10])        #short levels
        if(x == -1 and xflag):
            r[0] = i
            xflag = False
        if(y == -1 and yflag):
            r[1] = i
            yflag = False
    for i in range(4):
        a = temp[i+20]
        if(a == -1 and aflag):
            r[2] = i
            aflag = False
        longexit = longexit[0:r[2]]

def matchArrays():
    global long, short, exit, hardstop_be, hardstop, long_a, short_a
    long = long[0:r[0]]
    short = short[0:r[1]]
    numLong = r[0]
    numShort = r[1]
    values = []
    for i in range(len(long)): 
        values = [long[i],exit[i],hardstop_be[i],hardstop[i]]
        long_a.append(values)
    for i in range(len(short)): 
        values = [short[i],exit[i+10],hardstop_be[i+10],hardstop[i+10]]
        short_a.append(values)

def sorter(ar):                                             #sort arrays in numerical order
    p = 0
    while(p<len(ar)-1):
        if(ar[p][0]>ar[p+1][0]):
            ar[p],ar[p+1] = ar[p+1],ar[p]
            if(not(p==0)):
                p = p-1
        else:
            p += 1
    return ar
        
def sortervar(ar):                                             #sort arrays in numerical order
    p = 0
    while(p<len(ar)-1):
        if(ar[p]>ar[p+1]):
            ar[p],ar[p+1] = ar[p+1],ar[p]
            if(not(p==0)):
                p = p-1
        else:
            p += 1
    return ar

loadValues()
customArrays()
sortLS()
matchArrays()

#final arrays
long_a = sorter(long_a)
short_a = sorter(short_a)
longexit = sortervar(longexit)
shortexit = sortervar(shortexit)

#testing prints
print("Long Levels")
print(long_a)
print("Short Levels")
print(short_a)
print("Long Exits")
print(longexit)
print("Short Exits")
print(shortexit)