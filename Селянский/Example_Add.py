from db_helper import Student
# создать объект базы данных
database_students = Student()
# логика
# добавление записи


def add_command(name, sale_name, sale, mine_name):
 database_students.insert(name, sale_name, sale, mine_name)
# просмотр всех записей


def view_command():
 for row in database_students.view():
    print(row)
# основная программа в консоли
# добавление записи
for i in range(1):
 add_command(input("Введите название: "),
 input("Введите ед измерения: "),
 float(input("Введите цену: ")),
 input("Введите месторождение: "))
# просмотр всех записей
view_command()
