import sklearn
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

iris = sklearn.datasets.load_iris(as_frame=True)

# Rename classes using the iris target names
iris.frame["target"] = iris.target_names[iris.target]
_ = sns.pairplot(iris.frame, hue="target")

plt.show()
