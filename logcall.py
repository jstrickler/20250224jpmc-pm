from functools import wraps
import logging

logging.basicConfig(
    filename="deco.log",
    format="%(levelname)s %(asctime)s %(message)s",
    datefmt="%x-%X",
    level=logging.INFO,
)

def logcall(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        logging.info("Called %s", func.__name__)
        return func(*args, **kwargs)
    return _wrapper



