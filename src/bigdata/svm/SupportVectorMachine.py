import numpy as np
from sklearn import svm, datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris.data[:, [0, 2]]
y = iris.target


def visualized_data():
    target_names = iris.target_names
    feature_names = iris.feature_names

    n_class = len(set(y))
    print "Number of classes:" + str(n_class)

    plt.figure(figsize=(10, 8))
    for i, c, s in (zip(range(n_class), ['b', 'g', 'r'], ['o', '^', '*'])):
        ix = y == i
        plt.scatter(X[:, 0][ix], X[:, 1][ix], color=c, marker=s, s=60, label=target_names[i])

    plt.legend(loc=2, scatterpoints=1)
    plt.xlabel("feature 1-" + feature_names[0])
    plt.ylabel("feature 2-" + feature_names[2])
    plt.show()  


def train_svm():
    clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
                  decision_function_shape=None, degree=3, gamma='auto', kernel='linear',
                  max_iter=-1, probability=False, random_state=None, shrinking=True,
                  tol=0.001, verbose=False)
    clf.fit(X, y)


if __name__ == '__main__':
    visualized_data()
    # train_svm()
