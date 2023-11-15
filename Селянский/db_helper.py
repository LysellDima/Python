import sqlite3
# создание класса БД

class Student:
 # конструктор класса
 def __init__(self):
   self.con = sqlite3.connect("students.db")
   self.cur = self.con.cursor()
   self.cur.execute(
    "CREATE TABLE IF NOT EXISTS iskop "
    "(ID INTEGER PRIMARY KEY,"
    "name TEXT,"
    "sale_name TEXT,"
    "sale REAL,"
    "mine_name TEXT)"
   )
   self.con.commit()
  # сохранить изменения
   self.con.commit()


 def __del__(self):
  # отключение от БД
  self.con.close()


 def view(self):
 # просмотр всех записей в таблице БД
  self.cur.execute("SELECT * FROM iskop")
 # список всех записей из таблицы
  rows = self.cur.fetchall()
  return rows


 def insert(self, name, sale_name, sale, mine_name):
 # добавить запись
  self.cur.execute("INSERT INTO iskop "
                   "VALUES (NULL, ?, ?, ?, ?)", (name, sale_name, sale, mine_name,))
  self.con.commit()


 def update(self, id, name, sale_name, sale, mine_name):
  # редактирование записи
  self.cur.execute("UPDATE iskop SET "
                   "name=?, sale_name=?, sale=?, mine_name=?", (name, sale_name, sale, mine_name,))
  self.con.commit()

 def delete(self, id):
  self.cur.execute("DELETE FROM iskop "
                   "WHERE ID=?", (id,))
  self.con.commit()


 def search(self, name):
   self.cur.execute("SELECT sale_name, sale, mine_name FROM iskop "
                    "WHERE name=?", (name,))
   rows = self.cur.fetchall()
   return rows