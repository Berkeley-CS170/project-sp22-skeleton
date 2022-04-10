import contextlib
import sys


class StdoutFileWrapper(contextlib.AbstractContextManager):
    def __enter__(self):
        return sys.stdout

    def __exit__(self, _type, _value, _traceback):
        return None
