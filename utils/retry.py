import time
from functools import wraps


def retry(max_attempts=3, delay=1):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            last_exception = None

            for attempt in range(max_attempts):

                try:
                    return func(*args, **kwargs)

                except Exception as e:

                    last_exception = e

                    if attempt < max_attempts - 1:
                        time.sleep(delay)

            raise last_exception

        return wrapper

    return decorator
