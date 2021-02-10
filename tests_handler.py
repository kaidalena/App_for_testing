import uuid


def generate_uuid_v1():
    guid = uuid.uuid1()
    return str(guid)


def decorator_function(func):
  def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
  wrapper.__name__ = func.__name__
  return wrapper
