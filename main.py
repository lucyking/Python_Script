import sys
import inspect

import re
from decorator import decorator


def test_decorator_fx(method, *args, **kwargs):
    print '[0]', args[0]
    print '[>>>] Here is the self dec fx'
    return method(*args, **kwargs)


def _run_on_failure_decorator(method, *args, **kwargs):
    try:
        print '[0]', args[0]
        print "Take Screenshot"
        return method(*args, **kwargs)
    except Exception, err:
        self = args[0]
        if hasattr(self, '_run_on_failure'):
            self._run_on_failure()
        raise


class A(object):
    def add(self, a, b):
        print a + b
        return a + b

    def sub(self, a, b):
        print a - b
        return a - b


# class B(A):
class B(type):
    def __new__(cls, clsname, bases, dict):
        if decorator:
            for name, method in dict.items():
                if not name.startswith('_') and inspect.isroutine(method):
                    # dict[name] = decorator(test_decorator_fx,method)
                    # """
                    if (re.search("multi", name)):
                        dict[name] = decorator(_run_on_failure_decorator, method)
                    else:
                        dict[name] = decorator(test_decorator_fx, method)
                        # """
        return type.__new__(cls, clsname, bases, dict)


class MB(A):
    __metaclass__ = B

    def multi(self, a, b):
        print a * b
        return a * b

    def add(self, a, b):
        print a + b
        return a + b

    def sub(self, a, b):
        print a - b
        return a - b


class Alpha(object):
    def __init__(self):
        self.var = 0

    def increase(self):
        self.var += 1
        print self.var
