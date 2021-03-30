def caching(f):
    """
    Decorator
    Improving performance by saving result of function into a dict

    :param f: function
    :return: cached result of function
    """
    f.cache = {}

    def _f(*args, **kwargs):
        if args not in f.cache:
            f.cache[args] = f(*args, **kwargs)
        return f.cache[args]

    return _f
