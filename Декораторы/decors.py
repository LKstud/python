#Функции -  объекты первого класса
#Их можно присваивать переменным, передавать в другие функции и возвращать из функций

#декоратор "вручную"
def my_decorator(func):
    def wrapper():
        print("до")
        func()
        print("после")
    return wrapper

#функция, которую декорируем:
def hello():
    print("Hello!")

hello = my_decorator(hello)
hello() #сделает вызов wrapper

@my_decorator
def hello():
    print("Hello!")