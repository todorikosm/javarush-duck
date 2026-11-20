# Студент - это звучит гордо.

# Напишите программу, которая создает словарь с информацией о студенте (name и age).
# Программа должна:
# Добавить новый элемент "university" в словарь.
# Добавить элемент "city" только в том случае, если его еще нет в словаре.
# Добавить несколько новых элементов с использованием метода update().
# Вывести обновленный словарь после каждого добавления.

# Напишите тут ваш код

student_info = {
    "name": "Sergey Todoriko",
    "age": 38
}

student_info["university"] = "MAMI"
print(student_info)

if "city" not in student_info:
    student_info["city"] = "Moscow"
print(student_info)

updates = {"school": 360, "car": "MB"}
student_info.update(updates)
print(student_info)


