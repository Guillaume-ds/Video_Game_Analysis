"""
KPI from the video game sales data set (vgsales.csv)
KPI based on a very diversificated data set
"""

from video_game_analysis import *

"""
-------------------------------------------Geographical approach-------------------------------------------------
"""

# Average number of sales by platform by region
NAPlatformSales = [0]*len(listPlatform)
EUPlatformSales = [0]*len(listPlatform)
JPPlatformSales = [0]*len(listPlatform)
OPlatformSales = [0]*len(listPlatform)
NAPlatformGames = [0]*len(listPlatform)
EUPlatformGames = [0]*len(listPlatform)
JPPlatformGames = [0]*len(listPlatform)
OPlatformGames = [0]*len(listPlatform)


for game in videoGameData[1:]:
	NAPlatformSales[listPlatform.index(game[2])]+=float(game[7])
	NAPlatformGames[listPlatform.index(game[2])]+=1
	EUPlatformSales[listPlatform.index(game[2])]+=float(game[8])
	EUPlatformGames[listPlatform.index(game[2])]+=1
	JPPlatformSales[listPlatform.index(game[2])]+=float(game[9])
	JPPlatformGames[listPlatform.index(game[2])]+=1
	OPlatformSales[listPlatform.index(game[2])]+=float(game[10])
	OPlatformGames[listPlatform.index(game[2])]+=1



avgNAPlatformSales = [0]*len(listPlatform) 
avgEUPlatformSales = [0]*len(listPlatform) 
avgJPPlatformSales = [0]*len(listPlatform) 
avgOPlatformSales = [0]*len(listPlatform) 

for i in range(len(listPlatform)):
	avgNAPlatformSales[i] = NAPlatformSales[i]/NAPlatformGames[i]
	avgEUPlatformSales[i] = EUPlatformSales[i]/EUPlatformGames[i]
	avgJPPlatformSales[i] = JPPlatformSales[i]/JPPlatformGames[i]
	avgOPlatformSales[i] = OPlatformSales[i]/OPlatformGames[i]

avgNAPlatformSales = pd.DataFrame({
	'platforms':listPlatform,
	'avgNAPlatformSales':avgNAPlatformSales,
})
avgNAPlatformSales = avgNAPlatformSales.sort_values('avgNAPlatformSales',ascending=False)

plt.figure(5)
plt.bar('platforms','avgNAPlatformSales',data=avgNAPlatformSales[0:10])
plt.title('Average Sales in North America for the most performing platforms',size=20)

avgEUPlatformSales = pd.DataFrame({
	'platforms':listPlatform,
	'avgEUPlatformSales':avgEUPlatformSales,
})
avgEUPlatformSales = avgEUPlatformSales.sort_values('avgEUPlatformSales',ascending=False)

plt.figure(6)
plt.bar('platforms','avgEUPlatformSales',data=avgEUPlatformSales[0:10])
plt.title('Average Sales in EU for the most performing platforms',size=20)




"""
-------------------------------------Platform Approach---------------------------------------
"""
print(listPlatform)

#let's compute the average sales for the PS3/X360 and the PS4/XOne

listRegion = ['NA','EU','JP','Others']

PS3RegionalSales = [0]*len(listRegion)
PS4RegionalSales = [0]*len(listRegion)
X360RegionalSales = [0]*len(listRegion)
XOneRegionalSales = [0]*len(listRegion)
PS3RegionalGames = [0]*len(listRegion)
PS4RegionalGames = [0]*len(listRegion)
X360RegionalGames = [0]*len(listRegion)
XOneRegionalGames = [0]*len(listRegion)
avgPS3RegionalSales = [0]*len(listRegion)
avgPS4RegionalSales = [0]*len(listRegion)
avgX360RegionalSales = [0]*len(listRegion)
avgXOneRegionalSales = [0]*len(listRegion)

for game in videoGameData[1:]:
	if game[2]=='PS3':
		for i in range(4):
			PS3RegionalSales[i]+=float(game[6+i])
			PS3RegionalGames[i]+=1
	elif game[2]=='PS4':
		for i in range(4):
			PS4RegionalSales[i]+=float(game[6+i])
			PS4RegionalGames[i]+=1
	elif game[2]=='X360':
		for i in range(4):
			X360RegionalSales[i]+=float(game[6+i])
			X360RegionalGames[i]+=1
	elif game[2]=='XOne':
		for i in range(4):
			XOneRegionalSales[i]+=float(game[6+i])
			XOneRegionalGames[i]+=1

for list in [PS3RegionalSales,PS4RegionalSales,XOneRegionalSales,X360RegionalSales]:
	for i in range(len(PS3RegionalSales)):
		list[i]=round(list[i],2)




for i in range(len(listRegion)):
	avgPS3RegionalSales[i] = PS3RegionalSales[i]/PS3RegionalGames[i]
	avgPS4RegionalSales[i] = PS4RegionalSales[i]/PS4RegionalGames[i]
	avgX360RegionalSales[i] = X360RegionalSales[i]/X360RegionalGames[i]
	avgXOneRegionalSales[i] = XOneRegionalSales[i]/XOneRegionalGames[i]


plt.figure(7)
width = 0.3
x = np.arange(len(listRegion))
VS1 = plt.subplot(111) #VS1 = versus 1 
VS1.bar(x-width/2,avgPS3RegionalSales,color='b',label='PS3',width=0.25)
VS1.bar(x+width/2,avgX360RegionalSales,color='g',label='X360',width=0.25)
VS1.set_xticks(x)
VS1.set_xticklabels(listRegion)
VS1.legend()
plt.title('Average regional sales per platform(PS3 vs X360)',size=20)


plt.figure(8)
width = 0.3
x = np.arange(len(listRegion))
VS2 = plt.subplot(111) #VS2 = versus 2
VS2.bar(x-width/2,avgPS4RegionalSales,color='b',label='PS4',width=0.25)
VS2.bar(x+width/2,avgXOneRegionalSales,color='g',label='XOne',width=0.25)
VS2.set_xticks(x)
VS2.set_xticklabels(listRegion)
VS2.legend()
plt.title('Average regional sales per platform (PS4 vs XOne)',size=20)
plt.show()