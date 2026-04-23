# Task 1
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
# To write a log record:
#logger.log(logging.INFO, "this string would be logged")


def logger_decorator(func):
    def wrapper(*args, **kwargs):
         value = func(*args, **kwargs)
         if args:
            args_log = args
         else:
            args_log = 'none' 
         if  kwargs:
            kwargs_log = kwargs
         else:
            kwargs_log = 'none' 
         # To display function name in logging file
         func_name = func.__name__
         logger.log(logging.INFO, 
                f"function: {func_name}\n"
                f"positional parameters: {args_log}\n"
                f"keyword parameters: {kwargs_log}\n"
                f"return: {value}")
         return value
    return wrapper

@logger_decorator
def greet():
    return "hello world"
greet()

@logger_decorator
def check_args(*args):
    return True
check_args(2, 1)

@logger_decorator
def check_kwargs(**kwargs):
    return logger_decorator
check_kwargs(age=21)