import inspect

recursion_limit = 100


def recursion_limiter(function):
    def RecursionWrapper(*args, **kwargs):
        if len(inspect.stack()) / 2 > recursion_limit:
            raise RecursionError(
                f"maximum recursion depth exceeded for function {function.__name__}"
            )
        return function(*args, **kwargs)

    return RecursionWrapper


@recursion_limiter
def my_function(entier):
    if entier <= 0:
        return 0
    return my_function(entier - 1)


print(my_function(20))

# def f(entier):
#    return f(entier)


# f(100)
