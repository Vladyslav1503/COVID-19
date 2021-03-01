from typing import Callable

__cached = {}


def caching(function: Callable, *args):
    global __cached
    if function in __cached.keys():
        if args:
            return __cached[function][args]

        return __cached[function]
    else:
        if args:
            __cached[function] = {args: function(*args)}
            return __cached[function][args]

        __cached[function] = function()
        return __cached[function]
