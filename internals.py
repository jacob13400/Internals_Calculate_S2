import camelot
import pandas as pd
import operator
# For getting DE marks
print("Your roll number is being read ........",end="")
tables = camelot.read_pdf('S2BE.pdf', pages='1,2')

table = tables[0].df
name = table[1].tolist()
markBE = table[5].tolist()

table = tables[1].df
name += table[1].tolist()
markBE += table[5].tolist()

#Remove unwanted elements
name.remove('')
name.remove('')
name.remove('Name')
markBE.remove('')
markBE.remove('Total')
del markBE[0]

# For getting CS marks
tables = camelot.read_pdf('S2CS.pdf', pages='1,2')

table = tables[0].df
markCS = table[6].tolist()

table = tables[1].df
markCS += table[6].tolist()
print("Done")
print("Your marks are being calculated..........",end="")
#Remove unwanted elements
markCS.remove('Total \n(50)')
markCS.remove('Total \n(50)')
del markCS[65]

# For getting DE marks
tables = camelot.read_pdf('S2DE.pdf', pages='1,2,3,4,5,6,7,8,9,10,11')
markDE=[]
for i in tables:
    table = i.df
    #print(table)
    markDE += table[2].tolist()

#Remove unwanted elements
markDE.remove('Internal\nMark\nRegulatio\nn /50')

# For getting DE marks
tables = camelot.read_pdf('S2EG.pdf', pages='1,2,3')
markEG=[]
for i in tables:
    table = i.df
    #print(table)
    markEG += table[2].tolist()

#Remove unwanted elements
markEG.remove('')
markEG.remove('')
markEG.remove('Final')
print("Done")

#print((name))
#print(len(markEG))

print("\n\nProvide me with your Roll No :")
roll=int(input())

print("\nYour name and details are provided.\nAs this is a prototype, this might have errors. Contact me for any corrections.\nAlso Chem PDF was not in a readable format, so that was not available.\n")
if(roll<=0 or roll >=66):
    print("Go check your roll number please")
print("Name                 : "+name[roll-1])
print("Computer Science     :"+markCS[roll-1])
print("Diffrential Equation :"+markDE[roll-1])
print("Basics of Electronics:"+markBE[roll-1])
print("Engineering Graphics :"+markEG[roll-1])