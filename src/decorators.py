from functools import wraps


def log(filename):
    """Декоратор log, который выполняет команды перед и после вызова функции."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if filename:
                msg = f"{func.__name__} {result}\n" + f"{func.__name__} ok\n"
                with open(filename, "a") as file:
                    file.write(msg)
            else:
                msg = f"my_function error: {ValueError}: {args}, {kwargs}"
                print(msg)
                raise ValueError(msg)
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    """Функция суммирования my_function(x + y)"""
    return x + y


my_function(1, 2)
