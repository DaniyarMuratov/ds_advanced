import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

anime_data = pd.read_csv("anime_info.csv")

x = anime_data["vote"]
y = anime_data["rating"]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(i):
 return slope * i + intercept


mymodel = list(map(myfunc, x))


plt.scatter(x, y)
plt.plot(x, mymodel)
plt.ylim(ymin=-1, ymax=11)
plt.xlim(xmin=-10, xmax=1000)
plt.xlabel("Vote")
plt.ylabel ("Rating")
plt.show()