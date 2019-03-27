import functools
try:
    from sklearn.utils import is_scalar_nan
except:
    import numbers
    import numpy as np

    def is_scalar_nan(x):
        return bool(isinstance(x, (numbers.Real, np.floating)) and np.isnan(x))


def not_scalar_nan(x):
    return not is_scalar_nan(x)


def if_x_has_method(f):
    f_name = f.__name__

    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        x = args[0]
        x_args = args[1:] if len(args) > 1 else []
        if hasattr(x, f_name):
            return getattr(x, f_name)(*x_args, **kwargs)
        else:
            return f(*args, **kwargs)
    return wrapped


def as_description_function(f):
    f_name = f.__name__

    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        args = list(args)
        instance = args[0]
        args[0] = instance.data

        # store the result of description function under the `description` attribute
        result = f(*args, **kwargs)
        instance.description[f_name] = result
        return f(*args, **kwargs)
    return wrapped
