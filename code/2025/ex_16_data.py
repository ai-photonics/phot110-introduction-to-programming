import sklearn
import matplotlib.pyplot as plt
import numpy as np

#data = sklearn.datasets.load_iris(as_frame=True)
data = sklearn.datasets.load_iris(as_frame=False)
print(data.keys())

iris = data["data"]
target = data["target"]

fig, ax = plt.subplots()
for t in [0, 1, 2]:
    ax.scatter(iris[target==t, 0], iris[target==t, 1], c=t*np.ones((50, 1)))
ax.legend(data["feature_names"])
plt.show()
