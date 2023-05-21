from functools import wraps


def capacity_controller(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                return threshold
            return result
        return wrapper
    return decorator
