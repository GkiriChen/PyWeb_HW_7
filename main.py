from sqlalchemy.orm import joinedload
from sqlalchemy import func

from datebase.connect_db import session
from datebase.models7 import *

# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.


def get_students_5():
    # SELECT ROUND(AVG(rating), 2), name FROM grades GROUP BY name ORDER BY AVG(rating) DESC limit 5;"

    top_students = session.query(Grade.name, func.round(func.avg(Grade.rating), 2)).group_by(Grade.name).order_by(
        func.avg(Grade.rating).desc()).limit(5).all()

    for res in top_students:
        print(f"{res[0]},  Середній бал - {res[1]}")


# Знайти студента із найвищим середнім балом з певного предмета.


def get_discep():
    disciplines = session.query(Discipline).all()
    discep_list = "; ".join(f"{i.discipline}" for i in disciplines)
    print(discep_list)
    discep = input(
        'Введи назву предмета з списку вище для пошуку студента з найвищім середнім балом->>> ')

    # name, discipline, ROUND(AVG(rating),2)
    discep_avg = session.query(Grade.name, Grade.discipline, func.round(func.avg(Grade.rating), 2)).filter(
        Grade.discipline == discep).group_by(Grade.name).order_by(func.avg(Grade.rating).desc()).limit(1).all()

    print(f"{discep_avg[0]}, {discep_avg[1]},  Середній бал - {discep_avg[2]}")


# Знайти середній бал у групах з певного предмета.


def find_group_avg_discep():
    disciplines = session.query(Discipline).all()
    discep_list = "; ".join(f"{i.discipline}" for i in disciplines)
    print(discep_list)
    discep = input(
        'Введи назву предмета з списку вище для пошуку середньго балу по групам->>> ')
    # SELECT grades.discipline, ROUND(AVG(grades.rating),2), groups_users.group_us FROM grades
    # JOIN groups_users ON groups_users.name=grades.name WHERE grades.discipline='{discep}'
    # GROUP BY groups_users.group_us

    discep_avg = session.query(Grade.discipline, func.round(func.avg(Grade.rating), 2)).join(Group).filter(
        Grade.discipline == discep).group_by(Group.namber).all()


# Знайти середній бал на потоці (по всій таблиці оцінок).
def find_AVG_rating():
    avg_rating = session.query(func.round(func.avg(Grade.rating), 2))


"""

# Знайти середній бал на потоці (по всій таблиці оцінок).
Grades.find_AVG_rating()
# Знайти, які курси читає певний викладач.
Discipline.find_discipline_teacher()
# Знайти список студентів у певній групі.
Groups_users.get_all_statudents_from_group()
# Знайти оцінки студентів в окремій групі з певного предмета.
Grades.find_rating_students_disce_of_group()
# Знайти середній бал, який ставить певний викладач зі своїх предметів.
Grades.find_AVG_teacher_disce()
# Список курсів, які певному студенту читає певний викладач
Grades.find_disce_of_teacher()
"""
