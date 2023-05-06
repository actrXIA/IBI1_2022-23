import matplotlib.pyplot as plt

costs=[1,8,15,7,5,14,43,40]
olympic_games=["Los Angeles 1984","Seoul 1988","Barcelona 1992","Atlanta 1996","Sydeny 2000","Athens 2003","Beijing 2008","London 2012"]

for n in range (0,8):
 print (olympic_games[n],"costs",costs[n],"billions $")

plt.bar(olympic_games,costs)
plt.show()
