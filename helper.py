def decorator_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            print(f'[ERROR] {ex}')
    wrapper.__name__ = func.__name__
    return wrapper