import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Hello Sentaurs")
        result = func(*args, **kwargs)

        print("Bye")
        return result
    return wrapper
    # test