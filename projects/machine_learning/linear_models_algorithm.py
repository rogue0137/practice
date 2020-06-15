import sys
import wave_dataset
import boston_housing_dataset
import mglearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso


# TODO : FIX THIS ERROR MESSAGE
# /Users/krystalflores/virtual_environments/venv/machine_learning/lib/python3.6/site-packages/scipy/linalg/basic.py:1226:
# RuntimeWarning: internal gelsd driver lwork query error, required iwork dimension not returned.
# This is likely the result of LAPACK bug 0038, fixed in LAPACK 3.2.2 (released July 21, 2010).
# Falling back to 'gelss' driver.


which_line = (sys.argv[1])


def boston_housing_train():
    X, y = boston_housing_dataset.boston_extends()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    return X_train, X_test, y_train, y_test


if which_line == "linear models":
    mglearn.plots.plot_linear_regression_wave()

# linear regression least squares starts here
elif "wave" in which_line:
    if which_line == "wave least squares":
        X, y = wave_dataset.create_wave(60)

        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
        lr = LinearRegression().fit(X_train, y_train)

        print("lr.coef_: {}".format(lr.coef_))
        print("lr.intercept_: {}".format(lr.intercept_))
        print("Training set score: {:.2f}".format(lr.score(X_train, y_train)))
        print("Test set score: {:.2f}".format(lr.score(X_test, y_test)))
elif "boston" in which_line:
    X_train, X_test, y_train, y_test = boston_housing_train()

    lr = LinearRegression().fit(X_train, y_train)

    ridge = Ridge().fit(X_train, y_train)
    ridge10 = Ridge(alpha=10).fit(X_train, y_train)
    ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)

    lasso = Lasso().fit(X_train, y_train)
    # we increase the default setting of "max_iter",
    # otherwise the model would war us that we should increase max_iter
    lasso001 = Lasso(alpha=0.01, max_iter=100000).fit(X_train, y_train)
    lasso00001 = Lasso(alpha=0.0001, max_iter=100000).fit(X_train, y_train)

    if which_line == "boston housing least squares":

        print("Training set score: {:.2f}".format(lr.score(X_train, y_train)))
        print("Test set score: {:.2f}".format(lr.score(X_test, y_test)))

    # ridge regression starts here
    elif which_line == "bostong housing alpha original":

        print("Training set score: {:.2f}".format(ridge.score(X_train, y_train)))
        print("Test set score: {:.2f}".format(ridge.score(X_test, y_test)))

    elif which_line == "boston housing ridge alpha 10":

        print("Training set score: {:.2f}".format(ridge10.score(X_train, y_train)))
        print("Test set score: {:.2f}".format(ridge10.score(X_test, y_test)))
    elif which_line == "boston housing ridge alpha 0.1":

        print("Training set score: {:.2f}".format(ridge01.score(X_train, y_train)))
        print("Test set score: {:.2f}".format(ridge01.score(X_test, y_test)))

    elif which_line == "boston ridge vs linear regression":
        plt.plot(ridge.coef_, 's', label="Ridge alpha 1")
        plt.plot(ridge.coef_, '^', label="Ridge alpha=10")
        plt.plot(ridge.coef_, 'v', label="Ridge alpha=0.1")

        plt.plot(lr.coef_, 'o', label="Linear Regression")
        plt.xlabel("Coefficient index")
        plt.ylabel("Coefficient magnitude")
        plt.hlines(0, 0, len(lr.coef_))
        plt.ylim(-25, 25)
        plt.legend()

    elif which_line == "boston samples":
        mglearn.plots.plot_ridge_n_samples()

    # lasso starts here
    elif which_line == "boston lasso":

        print("Training set score: {:.2f}".format(lasso.score(X_train, y_train)))
        print("Test set score: {:.2f}".format(lasso.score(X_test, y_test)))
        print("Number of features used: {}".format(np.sum(lasso.coef_ != 0)))

    elif which_line == "boston lasso001":

        print("Training set score: {:2f}".format(lasso001.score(X_train, y_train)))
        print("Test set score: {:.2f}".format(lasso001.score(X_test, y_test)))
        print("Number of features used: {}".format(np.sum(lasso001.coef_ != 0)))

    elif which_line == "boston lasso00001":
        print("Training set score: {:2f}".format(lasso00001.score(X_train, y_train)))
        print("Test set score: {:.2f}".format(lasso00001.score(X_test, y_test)))
        print("Number of features used: {}".format(np.sum(lasso00001.coef_ != 0)))

    elif which_line == "boston lasso vs ridge":
        plt.plot(lasso.coef_, 's', label="Lasso alpha=1")
        plt.plot(lasso001.coef_, '^', label="Lasso alpha=0.01")
        plt.plot(lasso00001.coef_, 'v', label="Lasso alpha=0.0001")

        plt.plot(ridge01.coef_, 'o', label="Ridge alpha=0.1")
        plt.legend(ncol=2, loc=(0,1.05))
        plt.ylim(-25,25)
        plt.xlabel("Coefficient index")
        plt.ylabel("Coefficient magnitude")
    else:
        print("You have not supplied the right argument. \n Values are:")
else:
    print("You have not supplied the right argument. \n Values are:")

if plt:
    plt.show()


