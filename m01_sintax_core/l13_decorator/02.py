# Декораторы могут принимать аргументы, что позволяет гибко настраивать их поведение.

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)

        return wrapper

    return decorator_repeat

@repeat(num_times=3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")


# Объяснение
# Декоратор с аргументами (repeat): Эта функция принимает аргумент num_times и возвращает декоратор decorator_repeat.
# Декоратор (decorator_repeat): Этот декоратор принимает функцию func и возвращает новую функцию wrapper,
# которая вызывает func num_times раз.
# Функция с декоратором (say_hello): Функция say_hello вызывается трижды благодаря декоратору repeat.