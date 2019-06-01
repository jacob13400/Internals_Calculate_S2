import camelot
import pandas as pd
import operator
import pickle

name=[]
markBE=[]
markCS=[]
markEG=[]
markDE=[]

with open('name.data', 'rb') as filehandle:  
    # read the data as binary data stream
    name = pickle.load(filehandle)

with open('markBE.data', 'rb') as filehandle:  
    # read the data as binary data stream
    markBE = pickle.load(filehandle)

with open('markCS.data', 'rb') as filehandle:  
    # read the data as binary data stream
    markCS = pickle.load(filehandle)

with open('markDE.data', 'rb') as filehandle:  
    # read the data as binary data stream
    markDE = pickle.load(filehandle)

with open('markEG.data', 'rb') as filehandle:  
    # read the data as binary data stream
    markEG = pickle.load(filehandle)


print("\n\nProvide me with your Roll No :")
roll=int(input())

print("\nYour name and details are provided.\nAs this is a prototype, this might have errors. Contact me for any corrections.\nAlso Chem PDF was not in a readable format, so that was not available.\n")
if(roll<=0 or roll >=66):
    print("Go check your roll number please")
else:
    print("Name                 : "+name[roll-1])
    print("Computer Science     :"+markCS[roll-1])
    print("Diffrential Equation :"+markDE[roll-1])
    print("Basics of Electronics:"+markBE[roll-1])
    print("Engineering Graphics :"+markEG[roll-1])