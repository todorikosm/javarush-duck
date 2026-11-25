def my_decorator(func):
    def wrapper():
        print("Перед вызовом функции")
        func()
        print("После вызова функции")

    return wrapper

@my_decorator
def say_hello():
    # say_hello = my_decorator(say_hello)
    print("Hello!")

say_hello()


# Объяснение
#
# Декоратор (my_decorator): Эта функция принимает функцию func в качестве аргумента и возвращает новую функцию wrapper,
# которая вызывает func и добавляет дополнительное поведение до и после ее вызова.
#
# Функция с декоратором (say_hello): Функция say_hello обернута декоратором my_decorator, что добавляет дополнительное
# поведение при ее вызове.