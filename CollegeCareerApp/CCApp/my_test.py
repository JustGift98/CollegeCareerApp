import itertools

import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize

from pyahp.hierarchy import AHPCriterion
from pyahp.methods import EigenvalueMethod
from pyahp.utils import normalize_priorities


# test cases

def calculate_priorities(features, total_point):
    # There are n features, so an n*n 'ones' matrix is composed.
    # The elements on the diagonal are all one.
    n = len(features[0])
    ahp_matrix = np.ones([n, n])

    # The matrix is filled according to ahp calculations.
    for i in range(0, n):
        for j in range(0, n):
            # The element (j,i) equals 1/(i,j)
            if i < j:
                if i == 0:
                    # The first row is the second row of the input list.
                    ahp_matrix[i, j] = float(features[1][j - 1])
                    # Then, the first column is filled.
                    ahp_matrix[j, i] = 1 / float(ahp_matrix[i, j])
                else:
                    # The rest of the cells are filled according to firs row.
                    if ahp_matrix[0, j] > ahp_matrix[0, i]:
                        ahp_matrix[i, j] = ahp_matrix[0, j] - ahp_matrix[0, i] + 1
                    else:
                        ahp_matrix[i, j] = 1 / ((ahp_matrix[0, i] - ahp_matrix[0, j]) + 1)
                    ahp_matrix[j, i] = 1 / float(ahp_matrix[i, j])

    # The matrix is normalized according to axis 0
    normed_matrix = normalize(ahp_matrix, axis=0, norm='l1')

    # Weights are calculated
    weights = normed_matrix.mean(1)
    # The total point is distributed according to weights

    points = total_point * weights
    # Feature names and points are stored in a dataframe

    return dict(zip(features[0], points))




critetia = [['Price', 'Reputation', 'Location', 'Security','Campus'], [4, 3, 2,5,1]]
total_point = 1
print(critetia)
main_dict = print(calculate_priorities(critetia, total_point))
main_dict

