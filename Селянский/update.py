from db_helper import Student
# создать объект базы данных

database_students = Student()


# удаление по id ископаемого
def update_command(id, name, sale_name, sale, mine_name):
 database_students.update(id, name, sale_name, sale, mine_name)
 print(f"Данные ископаемого с id = {id} обновлены")


# просмотр всех записей
def view_command():
 for row in database_students.view():
    print(row)



# основная программа
print("Список ископаемых")
view_command()
id_update = int(input("Введите id ископаемого "))
print("Укажите новые данные: ")
name = input("Название: ")
sale_name = input("Ед измерения: ")
sale = float(input("Цена: "))
mine_name = input("Месторождение: ")
update_command(id_update, name, sale_name, sale, mine_name)
print("Список ископаемых")
view_command()
