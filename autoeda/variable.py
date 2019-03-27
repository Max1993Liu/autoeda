from .describe import *


class Variable:
    """ Base class for variables """
    # type needs to be set by subclasses
    type = 'base'

    def __init__(self, x):
        self.data = x
        self.description = dict()

    def __repr__(self):
        return repr(self.data)

    n = n
    count = count
    n_missing = n_missing
    pct_missing = pct_missing
    nunique = nunique
    value_counts = value_counts


class NumVariable(Variable):
    """ Numerical Variable """
    type = 'numerical'

    mean = mean
    median = median
    std = std
    skew = skew
    kurtosis = kurtosis
    quantile = quantile


class CatVariable(Variable):
    """ Categorical Variable """
    type = 'categorical'

