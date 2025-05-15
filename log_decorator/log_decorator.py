from logging import info
from functools import wraps

def log_call(meth):
    @wraps(meth)
    def fn(*args, **kwargs):
        argrepr = [repr(arg) for arg in args]
        kwargrepr = [f"{key}={value!r}" for key, value in kwargs.items()]
        reperlist = ', '.join(argrepr + kwargrepr)
        info(f"Calling: {meth.__name__}({reperlist})")
        return meth(*args, **kwargs)
    return fn
