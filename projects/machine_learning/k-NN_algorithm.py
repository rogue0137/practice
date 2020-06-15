#!/usr/bin/python

import sys
import mglearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsRegressor
import wave_dataset


which_plot = (sys.argv[1])
# TODO : README section on when it's good/bad to use k-NN algorithm
# k-NN algorithm is the simplest machine learning algorithm
# to make a prediction for a new data point,
# the algorithm finds the closest data point in the training dataset
# a.k.a. its "nearest neighbor"
# NOTE: It is important to pre-process your data when using this algorithm

# KNeighbors classifier important params:
# 1) n_neighbors
# 2) how you measure the distance between data points


if which_plot == '1-NN':
    mglearn.plots.plot_knn_classification(n_neighbors=1)

    # must exit the graph to get control of your terminal back

elif which_plot == '3-NN':

    # when considering more than one neighbor, we use "voting" to assign a label
    # a.k.a. we assign the class that is most "frequent"

    mglearn.plots.plot_knn_classification(n_neighbors=3)

elif which_plot == 'forge':

    # Use k-NN with scikit-learn: FORGE

    X, y = mglearn.datasets.make_forge()

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(X_train, y_train)
    print("Test set predictions: {}".format(clf.predict(X_test)))
    print("Test set accuracy: {:.2f}".format(clf.score(X_test, y_test)))

    fig, axes = plt.subplots(1, 3, figsize=(10,3))

    for n_neighbors, ax in zip([1, 3, 9], axes):
        # the fit method returns the object self, so we can instantiate
        # and fit in one line
        # basic gist of what this plotting shows:
        # using few neighbors corresponds to HIGH MODEL COMPLEXITY
        # using many neighbors corresponds to LOW MODEL COMPLEXITY
        clf_two = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X,y)
        mglearn.plots.plot_2d_separator(clf_two, X, fill=True, eps=0.5, ax=ax, alpha=.4)
        mglearn.discrete_scatter(X[:,0],X[:,1], y, ax=ax)
        ax.set_title("{} neigbor(s)".format(n_neighbors))
        ax.set_xlabel("feature 0")
        ax.set_ylabel("feature 1")
    axes[0].legend(loc=3)

elif which_plot == 'cancer':
    # Use k-NN with scikit-learn: CANCER

    cancer = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        cancer.data, cancer.target, stratify=cancer.target, random_state=66
    )

    training_accuracy = []
    test_accuracy = []
    # try n_neighbors from 1 to 10
    neighbors_settings = range(1,11)

    for n_neighbors in neighbors_settings:
        # build the model
        clf_three = KNeighborsClassifier(n_neighbors=n_neighbors)
        clf_three.fit(X_train,y_train)
        # record training set accuracy
        training_accuracy.append(clf_three.score(X_train, y_train))
        # record genraliztaion accuracy
        test_accuracy.append(clf_three.score(X_test, y_test))

    plt.plot(neighbors_settings, training_accuracy, label="training accuracy")
    plt.plot(neighbors_settings, test_accuracy, label="test_accuracy")
    plt.ylabel("Accuracy")
    plt.xlabel("n_neighbors")
    plt.legend()

elif 'wave' in which_plot:

    if which_plot == 'wave 1':
        mglearn.plots.plot_knn_regression(n_neighbors=1)

    elif which_plot == 'wave 3':
        mglearn.plots.plot_knn_regression(n_neighbors=3)

    elif 'regress' in which_plot:
        X, y = wave_dataset.create_wave()

        # split the wave dataset into training and test set
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

        if which_plot == 'regress wave':

            # instantiate the models and set the number of neighbors to consider to 3
            reg = KNeighborsRegressor(n_neighbors=3)
            # fit the model using the training data and training targets
            reg.fit(X_train, y_train)

            print("Test set predictions: \n{}".format(reg.predict(X_test)))
            print("Test set R^2: {:.2f}".format(reg.score(X_test, y_test)))
        elif which_plot == 'regress wave single feature':
            fig, axes = plt.subplots(1, 3, figsize=(15, 4))

            # create 1,000 data points, evenly spaced between -3 and 3
            line = np.linspace(-3, 3, 1000).reshape(-1, 1)
            for n_neighbors, ax in zip([1, 3, 9], axes):
                # make predictions using 1, 3 or 9 neighbors
                reg = KNeighborsRegressor(n_neighbors=n_neighbors)
                reg.fit(X_train, y_train)
                ax.plot(line, reg.predict(line))
                ax.plot(X_train, y_train, '^', c=mglearn.cm2(0), markersize=8)
                ax.plot(X_test, y_test, 'v', c=mglearn.cm2(1), markersize=8)

                ax.set_title(
                    "{} neighbor(s)\n train score: {:.2f} test score: {:.2f}".format(
                        n_neighbors, reg.score(X_train, y_train),
                        reg.score(X_test, y_test)
                    )
                )
                ax.set_xlabel("Feature")
                ax.set_ylabel("Target")
            axes[0].legend(["Model predictions", "Training data/target", "Test data/target"], loc="best")
    else:
        print("You have not supplied the right wave argument.\n Values are:")

else:
    print("You have not supplied the right argument. \n Values are:"
          "'1-NN' \n 3-NN \n forge \n cancer")

if plt:
    plt.show()
