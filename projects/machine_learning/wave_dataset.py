import mglearn
import matplotlib.pyplot as plt


def create_wave(n_samples=40):
    X, y = mglearn.datasets.make_wave(n_samples)

    return X, y


def plot_wave():
    X, y = create_wave()

    plt.plot(X, y, 'o')
    plt.ylim(-3, 3)
    plt.xlabel("Feature")
    plt.ylabel("Target")

    return plt

# need to add this or else the above will not plot
if __name__ == "__main__":
    plot_wave()
    plt.show()

