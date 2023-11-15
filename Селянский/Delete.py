from db_helper import Student
# создать объект базы данных
database_students = Student()
# удаление по id ископаемого


def delete_command(id):
 database_students.delete(id)
 print(f"Данные ископаемого с id = {id} удалены")
# просмотр всех записей


def view_command():
 for row in database_students.view():
    print(row)
# основная программа
print("Список ископаемых")
view_command()
id_delete = int(input("Введите id ископаемого "))
delete_command(id_delete)
print("Список ископаемых")
view_command()
