
from repository import select
import sqlite3


class Task:
    TABLE_NAME = 'tasks'

    def __init__(self, name: str, description: str, owner: int):
        self.name = name
        self.description = description
        self.owner = owner

    def __repr__(self) -> str:
        return f"TODO: {self.name}, description {self.description}, Owner: {self.owner}"

    @classmethod
    def get_all_tasks_from_db(cls):
        tasks = list()
        for task_data in select(cls.TABLE_NAME):
            tasks.append(
                cls(name=task_data[1], description=task_data[2], owner=task_data[3]))
        return tasks

    @classmethod
    def get_user_tasks_from_db(cls, user_id: int):
        tasks = list()
        for task_data in select(cls.TABLE_NAME, condition=f" owner_id={user_id} "):
            tasks.append(
                cls(name=task_data[1], description=task_data[2], owner=task_data[3]))
        return tasks


class User:
    TABLE_NAME = 'users'

    def __init__(self, _id: int, name: str):
        self._id = _id
        self.name = name

    def __repr__(self) -> str:
        return f"ID {self._id}, Name {self.name}"

    @classmethod
    def get_all_users_from_db(cls):
        print('------------------------------')
        users = list()
        for user_data in select(cls.TABLE_NAME):
            users.append(cls(_id=user_data[0], name=user_data[1]))
        return users

    @classmethod
    def find_busiest(cls):
        print('------------------------------')
        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute(
                "SELECT ROUND(AVG(rating), 2), name FROM grades GROUP BY name ORDER BY AVG(rating) DESC limit 5;")
            # res = cur.fetchall()
            for res in cur.fetchall():
                print(f"{res[1]},  Середній бал - {res[0]}")

    @classmethod
    def find_busiest_discep(cls):
        print('------------------------------')
        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute("SELECT discipline FROM disciplines;")
            discep_list = cur.fetchall()
            discep_list = "; ".join(f"{i[0]}" for i in discep_list)
            print(discep_list)
            discep = input(
                'Введи назву предмета з списку вище для пошуку студента з найвищім середнім балом->>> ')
            cur.execute(
                f"SELECT  name, discipline, ROUND(AVG(rating),2) FROM grades WHERE discipline='{discep}' GROUP BY name ORDER BY AVG(rating) DESC limit 1;")
            # res = cur.fetchall()
            for res in cur.fetchall():
                print(f"{res[0]}, {res[1]},  Середній бал - {res[2]}")


class Groups_users:
    TABLE_NAME = 'groups_users'

    def __init__(self, _id: int, group_us: int, name: str):
        self._id = _id
        self.group_us = group_us
        self.name = name

    @classmethod
    def get_all_statudents_from_group(cls):
        print('------------------------------')
        group = input('Введи номер групи від 1 до 3 ->>> ')
        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute(
                f"SELECT name FROM groups_users WHERE group_us='{group}';")
            students_list = cur.fetchall()
            students_list = "; ".join(f"{i[0]}" for i in students_list)
            print(f"Список студентів группи {group} - {students_list}")


class Teacher:
    TABLE_NAME = 'teachers'

    def __init__(self, _id: int, name: str):
        self._id = _id
        self.name = name


class Discipline:
    TABLE_NAME = 'disciplines'

    def __init__(self, _id: int, discipline: str, name: str):
        self._id = _id
        self.discipline = discipline
        self.name = name

    @classmethod
    def find_group_avg_discep(cls):
        print('------------------------------')
        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute("SELECT discipline FROM disciplines;")
            discep_list = cur.fetchall()
            discep_list = "; ".join(f"{i[0]}" for i in discep_list)
            print(discep_list)
            discep = input(
                'Введи назву предмета з списку вище для пошуку середньго балу по групам->>> ')
            cur.execute(
                f"SELECT grades.discipline, ROUND(AVG(grades.rating),2), groups_users.group_us FROM grades JOIN groups_users ON groups_users.name=grades.name WHERE grades.discipline='{discep}'  GROUP BY groups_users.group_us;")
            # res = cur.fetchall()
            for res in cur.fetchall():
                print(f"{res[0]}, {res[1]},  Група - {res[2]}")

    @classmethod
    def find_discipline_teacher(cls):
        print('------------------------------')
        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute("SELECT name FROM teacher;")
            teacher_list = cur.fetchall()
            teacher_list = "; ".join(f"{i[0]}" for i in teacher_list)
            print(teacher_list)
            teacher = input(
                'Введи вчителя зі списку вище для пошука предметів які він веде->>> ')
            cur.execute(
                f"SELECT discipline FROM disciplines WHERE name='{teacher}';")
            res = "; ".join(f"{i[0]}" for i in cur.fetchall())
            print(f"{teacher} веде таки предмети як {res}")


class Grades:
    TABLE_NAME = 'grades'

    def __init__(self, _id: int, name: str, discipline: str, assessment: int, date_gr: str):
        self._id = _id
        self.name = name
        self.discipline = discipline
        self.assessment = assessment
        self.date_gr = date_gr

    @classmethod
    def find_AVG_rating(cls):
        print('------------------------------')
        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute("SELECT ROUND(AVG(rating), 2) FROM grades;")
            res = cur.fetchone()
            print(f"Среденій бал на потоці - {res[0]}")

    @classmethod
    def find_rating_students_disce_of_group(cls):
        print('------------------------------')
        group = input('Введи номер групи від 1 до 3 ->>> ')
        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute("SELECT discipline FROM disciplines;")
            discep_list = cur.fetchall()
            discep_list = "; ".join(f"{i[0]}" for i in discep_list)
            print(discep_list)
            discep = input(
                f'Введи назву предмета з списку вище для отримання оцінок студентів группи {group}->>> ')
            cur.execute(
                f"SELECT grades.name, grades.rating, grades.date_gr FROM grades JOIN groups_users ON groups_users.name=grades.name WHERE groups_users.group_us='{group}' AND grades.discipline='{discep}';")
            res = cur.fetchall()
            for i in res:
                print(f"{i[0]}, {i[1]}, {i[2]}")

    @classmethod
    def find_AVG_teacher_disce(cls):
        print('------------------------------')
        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute("SELECT name FROM teacher;")
            teacher_list = cur.fetchall()
            teacher_list = "; ".join(f"{i[0]}" for i in teacher_list)
            print(teacher_list)
            teacher = input(
                'Введи вчителя зі списку вище для пошука предметів які він веде->>> ')
            cur.execute(
                f"SELECT ROUND(AVG(grades.rating),2)  FROM grades JOIN disciplines ON disciplines.discipline=grades.discipline WHERE disciplines.name='{teacher}' ;")
            res = cur.fetchone()
            print(f"Среденій бал учнів {teacher} - {res[0]}")

    @classmethod
    def find_disce_of_teacher(cls):
        print('------------------------------')
        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute("SELECT name FROM users;")

            students_list = "; ".join(f"{i[0]}" for i in cur.fetchall())
            print(students_list)
            students = input('Введи учня зі списку вище ->>> ')

            cur.execute(
                f"SELECT disciplines.name, disciplines.discipline  FROM disciplines  JOIN grades ON grades.discipline=disciplines.discipline WHERE grades.name='{students}' GROUP BY disciplines.name ;")
            teacher_list = "; ".join(f"{i[0]}" for i in cur.fetchall())
            print(teacher_list)
            teacher = input(
                f'Введи вчителя зі списку вище для пошука предметів які він веде для {students}->>> ')

            cur.execute(
                f"SELECT grades.discipline  FROM grades  JOIN disciplines ON grades.discipline=disciplines.discipline WHERE grades.name='{students}' AND disciplines.name='{teacher}'  GROUP BY grades.discipline;")
            res = "; ".join(f"{i[0]}" for i in cur.fetchall())
            print(
                f"Перелік курсів які читає {teacher} для студента {students} - {res}")
