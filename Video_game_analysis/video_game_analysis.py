"""
This project aims to create various KPI for the video game industry based on a data set from Kaggle
As the data set contains more than 16K games, the first part of the project consists in explaining the data :
there are many games for many console and for a large period of time.
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import csv


videoGameData = []
with open("vgsales.csv") as vgsales:
	reader = csv.reader(vgsales, delimiter =',')
	for row in reader:
		videoGameData.append(row)

videoGameDf = pd.read_csv("vgsales.csv",na_values = ["nan"])

"""
----------------------------------------------List of games per platform---------------------------------------
"""

listPlatform=[]
for platform in videoGameDf['Platform']:
	if platform not in listPlatform:
		listPlatform.append(platform)
listPlatformDf = pd.DataFrame(sorted(listPlatform))

listVideogamesPlatform=[]
nbGamesPlatform = []
nbSalesPlatform=[] #used further, but created here
for item in listPlatform:
	listVideogamesPlatform.append([])
	nbGamesPlatform.append(0)
	nbSalesPlatform.append(0)

for row in videoGameData[1:]:
	listVideogamesPlatform[listPlatform.index(row[2])].append(row[1])

for index,item in enumerate(listVideogamesPlatform):
	nbGamesPlatform[index]+=len(item)

nbGamesPlatformDf = pd.DataFrame({'Platform' :listPlatform,'Nb Games' : nbGamesPlatform})
nbGamesPlatformDf = nbGamesPlatformDf.sort_values('Nb Games', ascending=False)

plt.figure(1)
plt.bar('Platform','Nb Games',data=nbGamesPlatformDf)
plt.xlabel('Name of the Platform')
plt.ylabel('Number of games in the data set')
plt.title('Number of games per platform', size=20)

"""
------------------------------------------Average number of sales per game by platform------------------------------
"""

for game in videoGameData[1:]:
	nbSalesPlatform[listPlatform.index(game[2])] += float(game[-1])

avgSalesPlatform = []
for index,sales in enumerate(nbSalesPlatform):
	nbSalesPlatform[index]=round(nbSalesPlatform[index],2)
	avgSalesPlatform.append(sales/nbGamesPlatform[index])
	avgSalesPlatform[index] = round(avgSalesPlatform[index],3)

avgSalesPlatformDf = pd.DataFrame({'Platform':listPlatform,'Average Sales':avgSalesPlatform})
avgSalesPlatformDf = avgSalesPlatformDf.sort_values('Average Sales',ascending=False)

plt.figure(2)
plt.bar('Platform','Average Sales',data=avgSalesPlatformDf)
plt.title('Average Sales per Platform', size=20)

"""
--------------------------------------Average number of sales per year---------------------------------
"""

listOfYears=[]
for years in videoGameDf['Year']:
	try:
		year=round(int(years))
	except:
		year = -1
	if year not in listOfYears:
		listOfYears.append(year)

listOfYears=sorted(listOfYears)

nbGamesYear=[0]*len(listOfYears)


for game in videoGameData[1:]:
	try:
		nbGamesYear[listOfYears.index(int(game[3]))]+=1
	except:
		nbGamesYear[0]+=1

nbGamesYearDf = pd.DataFrame({'Years':listOfYears[1:],'Number of Games':nbGamesYear[1:]})
nbGamesYearDf = nbGamesYearDf.sort_values('Number of Games',ascending=False)

plt.figure(3)
plt.bar('Years','Number of Games', data=nbGamesYearDf)
plt.title('Number of games in the data set per year',size=20)

print(nbGamesYear[0])
"""
----------------------------------------------Analysis of the genre-------------------------------------------
"""

listOfGenre=[]
for genre in videoGameDf['Genre']:
	if genre not in listOfGenre:
		listOfGenre.append(genre)


nbSalesGenre=[0]*len(listOfGenre)
nbGamesGenre=[0]*len(listOfGenre)

for game in videoGameData[1:]:
		nbSalesGenre[listOfGenre.index(game[4])] += float(game[-1])
		nbGamesGenre[listOfGenre.index(game[4])] += 1

avgSalesGenre = [0]*len(listOfGenre)
for i in range(len(listOfGenre)):
	avgSalesGenre[i] = round(nbSalesGenre[i]/nbGamesGenre[i],2)

avgSalesGenreDf = pd.DataFrame({'Genre' :listOfGenre,'Average Sales' : avgSalesGenre})
avgSalesGenreDf = avgSalesGenreDf.sort_values('Average Sales', ascending=False)

plt.figure(4)
plt.bar('Genre','Average Sales',data=avgSalesGenreDf)
plt.title('Average number of sales per genre',size=20)
