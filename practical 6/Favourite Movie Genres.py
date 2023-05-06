import matplotlib.pyplot as plt
# data
Movie_genre=["Comedy","Action","Romance","Fantasy","Science-fiction","Horror","Crime","Documentary","History","War"]
Stock=[73,42,38,28,22,19,18,12,8,7]
# draw plot
plt.plot(Movie_genre,Stock)
plt.show()

#draw pie
import numpy as np
y=np.array([73,42,38,28,22,19,18,12,8,7])

plt.pie(y,labels=["Comedy","Action","Romance","Fantasy","Science-fiction","Horror","Crime","Documentary","History","War"])
plt.show()

for n in range(0,10):
 print(Movie_genre[n],"have",Stock[n],"students favors")
