import numpy as np
import pandas as pd


from .utils import if_x_has_method, as_description_function, is_scalar_nan, not_scalar_nan


@as_description_function
def n(x) -> int:
    """ Counter number of elements in x"""
    return len(x)

@as_description_function
@if_x_has_method
def nunique(x, dropna=True) -> int:
    if dropna:
        return len(set(filter(not_scalar_nan, x)))
    else:
        return len(set(x))

@as_description_function
@if_x_has_method
def count(x) -> int:
    """ Count number of non-null values in x"""
    return sum(not is_scalar_nan(i) for i in x)

@as_description_function
def n_missing(x) -> int:
    """ Count number of null values in x"""
    if hasattr(x, 'isnull'):
        return x.isnull().sum()
    return sum(is_scalar_nan(i) for i in x)

@as_description_function
def pct_missing(x) -> float:
    """ Percentage of null values in x"""
    if hasattr(x, 'isnull'):
        return x.isnull().sum()
    return np.mean(sum(is_scalar_nan(i) for i in x))

@as_description_function
@if_x_has_method
def value_counts(x, normalize=False, sort=True, ascending=False,
                 bins=None, dropna=True) -> pd.Series:
    raise NotImplementedError('Only supports Pandas Series')

@as_description_function
@if_x_has_method
def quantile(x, q, interpolation='linear') -> pd.Series:
    qt = np.quantile(list(filter(not_scalar_nan, x)), q, interpolation=interpolation)
    return pd.Series(qt, index=q)

@as_description_function
@if_x_has_method
def mean(x) -> float:
    return np.mean(x)

@as_description_function
@if_x_has_method
def median(x) -> float:
    return np.median(list(filter(not_scalar_nan, x)))

@as_description_function
@if_x_has_method
def std(x, ddof=1) -> float:
    """ Note: call std() with keyword arguments only!"""
    return np.std(list(filter(not_scalar_nan, x)), ddof=ddof)


@as_description_function
@if_x_has_method
def skew(x) -> float:
    raise NotImplementedError('Only supports Pandas Series')


@as_description_function
@if_x_has_method
def kurtosis(x) -> float:
    raise NotImplementedError('Only supports Pandas Series')



