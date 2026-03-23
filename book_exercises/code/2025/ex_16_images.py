import sklearn
import numpy as np
import matplotlib.pyplot as plt
import seaborn

data = sklearn.datasets.fetch_olivetti_faces()
print(0)

images = data["images"]

m = 5
n = 5
fig, ax = plt.subplots(m,n)
for i in range(m):
    for j in range(n):
        image = images[i*n + j, :, :]
        ax[i, j].imshow(image)
plt.show()

