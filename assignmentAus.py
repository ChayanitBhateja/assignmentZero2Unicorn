import pandas
import numpy as np
import matplotlib.pyplot as plt

#loading the csv file first..
df = pandas.read_csv('addresses.csv')
print(30 * '-'+ 'Tooth fairy Records'+ 30 * '-')
print(df)

def statics():
		print('Total number of childern: ', df['First_Name'].count())
		print('Average teeth claimed over the years: ', df['Teeth_lost'].mean())
		print('number of children who havent lost any tooth: ', childrenNullTooth())
		print('Number of children who have lost all of their baby teeth: ', childerNullAll())
		print('Total expenditure this year: ', int(expense()))

def childrenNullTooth():
	# df[df.Teeth_lost == 0].count()
	dfNullTooth = pandas.read_csv('C:/Users/Bateja/Documents/GitHub/PythonTraining/addresses.csv')
	dfNullTooth.sort_values('Teeth_lost', inplace = True)
	filter = dfNullTooth['Teeth_lost'] == 0
	dfNullTooth.where(filter, inplace = True)
	dfNullTooth = dfNullTooth[pandas.notnull(dfNullTooth['First_Name'])] 
	return dfNullTooth['First_Name'].count() 

def childerNullAll():
	dfNullAll = pandas.read_csv('C:/Users/Bateja/Documents/GitHub/PythonTraining/addresses.csv')
	dfNullAll.sort_values('Teeth_lost', inplace = True)
	filter1 = dfNullAll['Teeth_lost'] == 20
	dfNullAll.where(filter1, inplace = True)
	dfNullAll = dfNullAll[pandas.notnull(dfNullAll['First_Name'])]
	return dfNullAll['First_Name'].count()

def expense():
	exp = 0
	dfExpense = pandas.read_csv('C:/Users/Bateja/Documents/GitHub/PythonTraining/addresses.csv')
	cols = [2]
	dfExpense = dfExpense[dfExpense.columns[cols]]
	arr = dfExpense.to_numpy()

	for x in arr:
		if(x == 1):
			exp = exp + 1
		elif(x > 1):
			exp = exp+(0.5 * x)
		
	return exp

def exportChildrenToFile(name):
    dfExport = df
    dfExport.sort_values('Teeth_lost', inplace = True)
    filter = dfExport['Teeth_lost'] == 0
    dfExport.where(filter, inplace = True)
    dfExport.dropna()
    print('writing to csv')
    dfExport.to_csv(name)
    print('done')
    
def claimsGraph():
	dfGraph = pandas.read_csv('C:/Users/Bateja/Documents/GitHub/PythonTraining/addresses.csv')
	print(dfGraph)
	foo = dfGraph.groupby(['State'])
	# print(foo.get_group("jk")["State"].tolist())
	plt.bar(x=foo.get_group("jk")["State"].tolist(),height=foo.get_group("jk")["Teeth_lost"].sum(), align = 'center')
	plt.bar(x=foo.get_group("hj")["State"].tolist(),height=foo.get_group("hj")["Teeth_lost"].sum(), align = 'center')
	plt.bar(x=foo.get_group("uh")["State"].tolist(),height=foo.get_group("uh")["Teeth_lost"].sum(), align = 'center')
	plt.bar(x=foo.get_group("sd")["State"].tolist(),height=foo.get_group("sd")["Teeth_lost"].sum(), align = 'center')
	plt.bar(x=foo.get_group("dfs")["State"].tolist(),height=foo.get_group("dfs")["Teeth_lost"].sum(), align = 'center')
	plt.bar(x=foo.get_group("aha")["State"].tolist(),height=foo.get_group("aha")["Teeth_lost"].sum(), align = 'center')
	plt.title("Tooth Claims per State")
	plt.xticks(dfGraph['State'])
	plt.xlabel("State")
	plt.ylabel("Claims")
	plt.xlim([0,len(dfGraph['State'])])
	plt.show()

def comapareGraph(first, second):
	dfCompare = dfGraph = pandas.read_csv('C:/Users/Bateja/Documents/GitHub/PythonTraining/addresses.csv')
	foo = dfGraph.groupby(['State'])
	plt.bar(x=first,height=foo.get_group(first)["Teeth_lost"].sum(), align = 'center')
	plt.bar(x=second,height=foo.get_group(second)["Teeth_lost"].sum(), align = 'center')
	plt.title("Tooth Claims per State")
	plt.xticks([first, second])
	plt.xlabel("State")
	plt.ylabel("Claims")
	plt.xlim([0,len(dfGraph['State'])])
	plt.show()

ans = 0
while ans <= 5:
	print(30 * '-'+ 'Tooth Fairy Audit'+ 30 * '-')
	print('1. statics')
	print('2. export children who havent lost any tooth')
	print('3. Display number of claims per state')
	print('4. compare 2 states')
	print('5. exit')
	ans = int(input('Enter your Choice[1 - 4]: '))

	if(ans == 1):
		statics()
	elif(ans == 2):
		name = input('Enter the name of new File WITHOUT extension: ')
		exportChildrenToFile(name+'.csv')
	elif(ans == 3):
		claimsGraph()
	elif(ans == 4):
		state1 = input('Enter first State: ')
		state2 = input('Enter first State: ')
		comapareGraph(state1, state2)
	elif(ans == 5):
		break


