from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split


def create_moons():
    X, y = make_moons(n_samples=100, noise=0.25, random_state=3)
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,
                                                        random_state=42)
    return X_train, X_test, y_train, y_test


