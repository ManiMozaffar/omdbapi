from functools import wraps
from typing import Callable


def capacity_controller(threshold) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs) -> int:
            result = func(*args, **kwargs)
            if result > threshold:
                return threshold
            return result
        return wrapper
    return decorator
