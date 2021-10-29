def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        print(cache)
        return result

    print(cache)

    return memoized_func


@memoize
def add(a, b):
    print(a + b)


add(1, 3)