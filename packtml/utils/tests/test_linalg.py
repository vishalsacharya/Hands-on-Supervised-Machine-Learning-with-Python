# -*- coding: utf-8 -*-

from __future__ import absolute_import

from sklearn.datasets import load_iris
from packtml.utils import linalg

from numpy.testing import assert_array_almost_equal
import numpy as np

iris = load_iris()
X, y = iris.data, iris.target


def test_row_norms():
    means = np.average(X, axis=0)
    X_centered = X - means

    norms = linalg.l2_norm(X_centered, axis=0)
    assert_array_almost_equal(
        norms,
        np.array([ 10.10783524,   5.29269308,
                   21.53749599,   9.31556404]))
