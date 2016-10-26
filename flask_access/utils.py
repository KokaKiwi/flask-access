import inspect
from functools import update_wrapper, wraps


def parametrable_wrapper_function(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if len(args) > 0:
            return f()(args[0])
        return f(*args, **kwargs)
    return wrapper
