from functools import wraps


def decorator_without_args(function):
    # import pdb; pdb.set_trace()
    @wraps(function)
    def new_inner():
        print("entering", function.__name__)
        function()
        print("exiting", function.__name__)
    return new_inner


def log_decorator(log_enabled):
    def actual_decorator(func):
        wraps(func)
        def wrapper(*args, **kwargs):
            if log_enabled:
                print("Calling Function: " + func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator


@log_decorator(True)
def print_args(*args):
    for arg in args:
        print(arg)


# print_args(1, 2, 3)


def make_html(element):
    def actual_decorator(func):
        wraps(func)
        def wrapper(*args,**kwargs):
            print("starting func: " + func.__name__)
            start_tag = "<" + element +">"
            end_tag = "</"+ element + ">"
            # print(args)
            new_args = [start_tag + arg + end_tag for arg in args ]
            # print(new_args)
            for key in kwargs.keys():
                kwargs[key] = start_tag + kwargs[key] + end_tag
                # print(kwargs)
            return func(new_args, **kwargs)
        return wrapper
    return actual_decorator


@make_html('p')
def get_text(text):
    print(text)


get_text("YAAAY")


# # PythonDecorators/entry_exit_function.py
# def entry_exit(f):
#     def new_f():
#         print("Entering", f.__name__)
#         f()
#         print("Exited", f.__name__)
#     return new_f

@decorator_without_args
def func1():
    print("inside func1()")
    return 1

@decorator_without_args
def func2():
    print("inside func2()")
    return 1

# func1()
# func2()
#
# print(func1.__name__)