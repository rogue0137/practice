import mglearn
import matplotlib.pyplot as plt


# EXAMPLE OF SYNTHETIC TWO-CLASSIFICATION DATASET
# generate dataset
X, y = mglearn.datasets.make_forge()

# plot dataset
mglearn.discrete_scatter(X[:,0], X[:,1],y)
plt.legend(["Class 0", "Class 1"], loc=4)
plt.xlabel("First feature")
plt.ylabel("Second feature")
print("X.shape: {}".format(X.shape))

# output : X.shape (26,2)
# this means the dataset consists of 26 data points with 2 features
