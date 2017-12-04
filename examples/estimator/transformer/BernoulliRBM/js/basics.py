# -*- coding: utf-8 -*-

from sklearn.neural_network import BernoulliRBM
from sklearn.datasets import load_digits
from sklearn_porter import Porter



samples = load_digits()
X = samples.data
y = samples.target

tfer = BernoulliRBM(random_state=0, n_iter=10, verbose=True)
tfer.fit(X, y)

porter = Porter(tfer, language='js', method='transform')
output = porter.export()
print(output)

"""

"""