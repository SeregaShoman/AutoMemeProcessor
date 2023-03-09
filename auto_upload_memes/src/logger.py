import logging
import time

class Logger:

    def log(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            print(f"Начало операции {func.__name__} в {time.ctime()}")
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Окончание операции {func.__name__} в {time.ctime()}. Время выполнения: {end_time - start_time} секунд")
            return result
        return wrapper