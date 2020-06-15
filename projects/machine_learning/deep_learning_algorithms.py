#!/usr/bin/python
import sys
import mglearn
import matplotlib.pyplot as plt
from IPython.display import display
import numpy as np
from sklearn.neural_network import MLPClassifier
import two_moons_dataset
import cancer_dataset
from sklearn.model_selection import train_test_split


which_alg = (sys.argv[1])
# neural networks == deep learning
# Multilayer perceptrons (MLPs): genrealizations of linear models
#  that perform multiple stages of processing to come to a decision

# TODO: FIGURE OUT HOW TO GET DISPLAY TO DO MORE THAN JUST PRINT IN THE TERMINAL
if "example" in which_alg:
    if which_alg == "example logistic regression":
        display(mglearn.plots.plot_logistic_regression_graph())
    elif which_alg == "example multilayer perception one hidden layer":
        display(mglearn.plots.plot_single_hidden_layer_graph())
    elif which_alg == "example relu tanh":
        line = np.linspace(-3, 3, 100)
        plt.plot(line, np.tanh(line), label="tanh")
        plt.plot(line, np.maximum(line, 0), label="relu")
        plt.legend(loc="best")
        plt.xlabel("x")
        plt.ylabel("relu(x), tanh(x)")
    elif which_alg == "example multilayer perception two hidden layer":
        display(mglearn.plots.plot_two_hidden_layer_graph())
    else:
        print("You have not supplied the right argument. \n Values are:")
elif 'moon' in which_alg:
    X_train, X_test, y_train, y_test = two_moons_dataset.create_moons()
    if 'multi moon' not in which_alg:
        if which_alg == 'moon 100':
            mlp = MLPClassifier(solver='lbfgs', random_state=0).fit(X_train, y_train)
        elif which_alg == 'moon 10':
            mlp = MLPClassifier(solver='lbfgs', random_state=0, hidden_layer_sizes=[10]).fit(X_train, y_train)
        elif which_alg == 'moon layers':
            mlp = MLPClassifier(solver='lbfgs', random_state=0, hidden_layer_sizes=[10, 10]).fit(X_train, y_train)
        elif which_alg == 'moon layers with tanh':
            mlp = MLPClassifier(solver='lbfgs', random_state=0, hidden_layer_sizes=[10, 10]).fit(X_train, y_train)
            mlp.fit(X_train, y_train)
        else:
            print("You have not supplied the right argument. \n Values are:")
            pass

        mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
        mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
        plt.xlabel("Feature 0")
        plt.ylabel("Feature 1")
    elif 'multi moon' in which_alg:
        if which_alg == 'multi moon 1':
            fig, axes = plt.subplots(2, 4, figsize=(20, 0))
            for axx, n_hidden_nodes in zip(axes, [10, 100]):
                for ax, alpha in zip(axx, [0.0001, 0.01, 0.1, 1]):
                    mlp = MLPClassifier(solver='lbfgs', random_state=0,
                                        hidden_layer_sizes=[n_hidden_nodes, n_hidden_nodes],
                                        alpha=alpha)
                    mlp.fit(X_train, y_train)
                    mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3, ax=ax)
                    mglearn.discrete_scatter(X_train[:,0], X_train[:,1], y_train, ax=ax)
                    ax.set_title("n_hidden=[{}], {}]\nalpha={:.4f}".format(
                        n_hidden_nodes, n_hidden_nodes, alpha
                    ))
        elif which_alg == 'multi moon 2':
            fig, axes = plt.subplots(2, 4, figsize=(20, 8))
            for i, ax in enumerate(axes.ravel()):
                mlp = MLPClassifier(solver='lbfgs', random_state=i,
                                    hidden_layer_sizes=[100, 100])
                mlp.fit(X_train, y_train)
                mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3, ax=ax)
                mglearn.discrete_scatter(X_train[:,0], X_train[:,1], y_train, ax=ax)
elif "cancer" in which_alg:
    # check if this set is updated and if that could be affecting what gets returned
    cancer = cancer_dataset.create_cancer()
    if which_alg == "cancer per feature":
        print("Cancer data per-feature maxima:\n{}".format(cancer.data.max(axis=0)))
    else:
        X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target,
                                                            random_state=0)
        mlp = MLPClassifier(random_state=42)
        mlp.fit(X_train, y_train)

        if which_alg == "cancer mlp":

            print("Accuracy on training set: {:.2f}".format(mlp.score(X_train, y_train)))
            print("Accuracy on test set: {:.2f}".format(mlp.score(X_test, y_test)))
        elif which_alg == "plot cancer":
            plt.figure(figsize=(20, 5))
            plt.imshow(mlp.coefs_[0], interpolation='none', cmap='viridis')
            plt.yticks(range(30), cancer.feature_names)
            plt.xlabel("Columns in weight matrix")
            plt.ylabel("Input feature")
            plt.colorbar()
        else:
            # compute the mean value per feature on the training set
            mean_on_train = X_train.mean(axis=0)
            # computer the standard deviation
            std_on_train = X_train.std(axis=0)

            # subtract the mean, and scale by inverse standard deviation
            # afterward, mean=0 and std=1
            X_train_scaled = (X_train - mean_on_train) / std_on_train
            # use THE SAME transformation (using train mean and std) on the test set
            X_test_scaled = (X_test - mean_on_train) / std_on_train

            if which_alg == "cancer mlp 2":
                mlp2 = MLPClassifier(random_state=0)
                mlp2.fit(X_train_scaled, y_train)

                print("Accuracy on training set: {:.3f}".format(
                    mlp2.score(X_train_scaled, y_train)
                ))
                print("Accuracy on test set: {:.3f}".format(mlp2.score(X_test_scaled, y_test)))
            elif which_alg == "cancer mlp 3":
                mlp3 = MLPClassifier(max_iter=1000, random_state=0)
                mlp3.fit(X_train_scaled, y_train)

                print("Accuracy on training set: {:.3f}".format(
                    mlp3.score(X_train_scaled, y_train)
                ))
                print("Accuracy on test set: {:.3f}".format(mlp3.score(X_test_scaled, y_test)))
            elif which_alg == "cancer mlp 4":
                mlp4 = MLPClassifier(max_iter=1000, alpha=1, random_state=0)
                mlp4.fit(X_train_scaled, y_train)

                print("Accuracy on training set: {:.3f}".format(
                    mlp4.score(X_train_scaled, y_train)
                ))
                print("Accuracy on test set: {:.3f}".format(mlp4.score(X_test_scaled, y_test)))

            else:
                print("You have not supplied the right argument. \n Values are:")
else:
    print("You have not supplied the right argument. \n Values are:")

if plt:
    plt.show()