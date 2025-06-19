import inspect
def strict(func):
    def wrapped_function(*args):
        fsig = inspect.signature(func)
        params={k:v for k,v in zip(fsig.parameters, args)}
        for k, v in fsig.parameters.items():
            if not isinstance(params[k], v.annotation):
                raise TypeError('Type mismatch')
        return func(*args)
    return wrapped_function

@strict
def sum_two(a:int, b:int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError

