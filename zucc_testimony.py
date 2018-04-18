import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Changing Directory
import os
os.chdir(r"C:\Users\Satyam\Desktop\Programs\Datasets\zuckerberg_testimony")

#reading file
testimony = pd.read_csv('mark.csv')

#Name of each Individual
Names_of_people = (testimony.Person.unique())

#Number of people in Conference
Number_of_people = len(Names_of_people)

#Total Statements By each Individual
counts_of_statements = testimony.Person.value_counts()

#Bar graph Of Statements spoken vs Individual
plt.bar(range(len(counts_of_statements.index)),np.array(counts_of_statements))
ax = plt.subplot()
ax.grid()
ax.set_xticks(range(len(counts_of_statements.index)))
ax.set_xticklabels(counts_of_statements.index,rotation=90)
plt.ylabel("Number of statements spoken during the testimony")
plt.subplots_adjust(bottom=0.2)
#plt.show()  #Uncomment for bar graph


#Number of words spoken by each person
statements = [None]*Number_of_people
networds = [0]*Number_of_people
for i in range(len(Names_of_people)):
	statements[i] = np.array(testimony.Text.loc[(testimony.Person == Names_of_people[i])])
	for j in range(len(statements[i])):
		words = len(statements[i][j])
		networds[i] += words
		
		
#Plotting graph of words spoken in the testimony
plt.close('all')
plt.bar(range(len(networds)),networds)
ax = plt.subplot()
ax.grid()
ax.set_xticks(range(len(networds)))
ax.set_xticklabels(Names_of_people,rotation=90)
plt.ylabel("Number of words spoken during the testimony")
plt.subplots_adjust(bottom=0.2)
#plt.show() ###Uncomment for bar graph
