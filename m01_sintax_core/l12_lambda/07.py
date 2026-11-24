def get_password_checker(password):

    def checker(user_password):
        nonlocal password
        return user_password == password


    def get_pwd(show_password = False):
        return password if show_password else "*" * len(password)

    return checker, get_pwd

login, password = get_password_checker("qwerty1234")

print(login("1234"))
print(login("5678"))
print(login("qwerty1234"))