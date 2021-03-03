from typing import Callable

__cached = {}


# TODO comments
def caching(function: Callable, *args):
    global __cached
    if function in __cached.keys():
        if args and args in __cached[function].keys():
            return __cached[function][args]
        elif args and args not in __cached[function].keys():
            __cached[function][args] = function(*args)
            return __cached[function][args]

        return __cached[function]
    else:
        if args:
            __cached[function] = {args: function(*args)}
            return __cached[function][args]

        __cached[function] = function()
        return __cached[function]
