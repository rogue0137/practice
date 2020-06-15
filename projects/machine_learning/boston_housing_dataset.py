import mglearn
from sklearn.datasets import load_boston


def create_boston():
    boston = load_boston()

    return boston


def boston_extends():
    X, y = mglearn.datasets.load_extended_boston()

    return X, y


if __name__ == "__main__":
    original_boston = create_boston()
    print("Data shape: {}".format(original_boston.data.shape))
    X, y = boston_extends()
    print("X.shape: {}".format(X.shape))
