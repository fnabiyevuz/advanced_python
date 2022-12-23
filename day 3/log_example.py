from functools import wraps

import logging


def out_logger(level: str):
    def my_logger(original_function):
        logging.basicConfig(filename=f"{original_function.__name__}.log", level=level)

        @wraps(original_function)
        def wrapper(*args, **kwargs):
            if level == 10:
                logging.debug(
                    f"Ran with args: {args}, and kwargs: {kwargs}")
            elif level == 20:
                logging.info(
                    f"Ran with args: {args}, and kwargs: {kwargs}")
            elif level == 30:
                logging.warning(
                    f"Ran with args: {args}, and kwargs: {kwargs}")
            elif level == 40:
                logging.error(
                    f"Ran with args: {args}, and kwargs: {kwargs}")
            elif level == 50:
                logging.critical(
                    f"Ran with args: {args}, and kwargs: {kwargs}")

            return original_function(*args, **kwargs)

        return wrapper

    return my_logger


def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{original_function.__name__} ran in: {t2} sec")
        return result

    return wrapper


import time


@out_logger(logging.WARNING)
@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f"display_info ran with arguments ({name}, {age})")


display_info("Davron", 25)


# debug     10
# info      20
# warning   30
# error     40
# critical  50