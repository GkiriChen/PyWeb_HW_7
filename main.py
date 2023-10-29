from sqlalchemy.orm import joinedload
from sqlalchemy import func

from database.connect_db import session
from database.models7 import *
from seed.create_seed import start_seeds

# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.


def get_students_5():
    
    print("Знайти 5 студентів із найбільшим середнім балом з усіх предметів.")
    print()
    
    top_students = session.query(Student.name, func.round(func.avg(Grade.rating), 2)).join(
        Student, Student.id == Grade.student_id).group_by(Student.name).order_by(
        func.avg(Grade.rating).desc()).limit(5).all()

    for res in top_students:
        print(f"Студент {res[0]}, Середній бал - {res[1]}")
    


# Знайти студента із найвищим середнім балом з певного предмета.


def get_discep():
    
    print("Знайти студента із найвищим середнім балом з певного предмета.")
    print()

    disciplines = session.query(Discipline).all()
    discep_list = "; ".join(f"{i.discipline}" for i in disciplines)
    print(discep_list)
    
    discep = input(
        'Введи назву предмета з списку вище для пошуку студента з найвищім середнім балом->>> ')

    discep_avg = session.query(Student.name, Grade.discipline, func.round(func.avg(Grade.rating), 2)).join(
        Student, Student.id == Grade.student_id).filter(
        Grade.discipline == discep).group_by(Student.name, Grade.discipline).order_by(func.avg(Grade.rating).desc()).limit(1).all()

    print()

    print(f"Студент {discep_avg[0][0]} по предмету {discep_avg[0][1]}, має найвиший середній бал - {discep_avg[0][2]}")


# Знайти середній бал у групах з певного предмета.
def find_group_avg_discep():
    
    print("Знайти середній бал у групах з певного предмета.")
    print()

    disciplines = session.query(Discipline).all()
    discep_list = "; ".join(f"{i.discipline}" for i in disciplines)
    print(discep_list)
    
    discep = input(
        'Введи назву предмета з списку вище для пошуку середньго балу по групам->>> ')
   
    discep_avg = session.query(Grade.discipline, Group.namber, func.round(func.avg(Grade.rating), 2)).join(
        Group, Group.student_id == Grade.student_id).filter(
            Grade.discipline == discep).group_by(Group.namber, Grade.discipline).order_by(
                func.round(func.avg(Grade.rating), 2).desc()).all()
 
    print()
    
    for res in discep_avg:

        print(f"Група {res[1]},  Середній бал - {res[2]}")

    
# Знайти середній бал на потоці (по всій таблиці оцінок).
def find_AVG_rating():
    
    print("Знайти середній бал на потоці (по всій таблиці оцінок).")
    print()

    avg_rating = session.query(func.round(func.avg(Grade.rating), 2)).all()
    print(f"Середній бал на потоці - {avg_rating[0][0]}")


# Знайти, які курси читає певний викладач.
def find_discipline_teacher():
    
    print("Знайти, які курси читає певний викладач.")
    print()

    teachers = session.query(Teacher.name).all()
    teacher_list = "; ".join(f"{i.name}" for i in teachers)
    print(teacher_list)
    
    teacher = input('Введи вчителя зі списку вище для пошука предметів які він веде->>> ')

    discep_list = session.query(Discipline.discipline).join(Teacher, Discipline.teacher_id == Teacher.id).filter(
        Teacher.name == teacher).all()
    res = "; ".join(f"{i[0]}" for i in discep_list)
    
    print()
    print(f"{teacher} веде таки предмети як {res}")

# Знайти список студентів у певній групі.
def get_all_statudents_from_group():

    print("Знайти список студентів у певній групі.")
    print()
    
    group = input('Введи номер групи від 1 до 3 ->>> ')
    
    if group in ['1','2','3']:
    
        students_list = session.query(Student.name).join(Group, Student.id == Group.student_id).filter(Group.namber == group).all()
        students_list1 = "; ".join(f"{i[0]}" for i in students_list)
        print(f"Всього у группі '{group}' {len(students_list)} студентів,\nповний список студентів - {students_list1}")
    
    else:
    
        print("Ти ввів неіснуючий номер группи")

# Знайти оцінки студентів в окремій групі з певного предмета.
def find_rating_students_disce_of_group():
    
    print("Знайти оцінки студентів в окремій групі з певного предмета.")
    print()

    group = input('Введи номер групи від 1 до 3 ->>> ')
    
    if group in ['1','2','3']:
    
        disciplines = session.query(Discipline).all()
        discep_list = "; ".join(f"{i.discipline}" for i in disciplines)
        print(discep_list)
    
        discep = input(
        'Введи назву предмета з списку вище для пошуку середньго балу по групам->>> ')
        students_reting = session.query(Student.name, Grade.rating, Grade.date_gr).join(
            Grade, Grade.student_id == Student.id).join(Group).filter(
                Group.namber == group, Grade.discipline == discep).order_by(Student.name, Grade.date_gr).all()
        
        print()
        
        for i in students_reting:
    
                print(f"{i[0]}, {i[1]}, {i[2]}")

#Знайти список курсів які відвідує певний учень.
def find_list_discip_or_stud():
    
    print("Знайти список курсів які відвідує певний учень.")
    print()

    students_list = session.query(Student.name).all()
    students_list = "; ".join(f"{i[0]}" for i in students_list)
    print(students_list)
    
    student = input('Введи учня зі списку вище ->>> ')

    discip_list = session.query(Grade.discipline).join(Student, Student.id == Grade.student_id).filter(
        Student.name == student).group_by(Grade.discipline).all()
    
    print()

    print(f"Учень {student} відвідує наступні курси:")
    
    for res in discip_list:
    
        print(res[0])

# Знайти середній бал, який ставить певний викладач зі своїх предметів.
def find_AVG_teacher_disce():
    
    print("Знайти середній бал, який ставить певний викладач зі своїх предметів.")
    print()

    teachers = session.query(Teacher.name).all()
    teacher_list = "; ".join(f"{i.name}" for i in teachers)
    print(teacher_list)
    
    teacher = input('Введи вчителя зі списку вище для пошука предметів які він веде->>> ')
    
    teacher_AVG = session.query(func.round(func.avg(Grade.rating), 2)).join(
        Discipline, Discipline.discipline == Grade.discipline).join(Teacher, Teacher.id == Discipline.teacher_id).filter(
        Teacher.name == teacher).all()
    
    print()
    
    print(f"Среденій бал учнів {teacher} - {teacher_AVG[0][0]}")

# Список курсів, які певному студенту читає певний викладач
def find_disce_of_teacher():

    print("Список курсів, які певному студенту читає певний викладач")
    print()

    teachers_list = session.query(Teacher.name).all()
    teachers_list = "; ".join(f"{i[0]}" for i in teachers_list)
    print(teachers_list)
    
    teacher = input('Введи вчителя зі списку ->>> ')

    students_list = session.query(Student.name).join(Grade, Grade.student_id == Student.id).join(
        Discipline, Grade.discipline == Discipline.discipline).join(
            Teacher, Teacher.id == Discipline.teacher_id).filter(Teacher.name == teacher).group_by(
               Student.name).all()
    students_list = "; ".join(f"{i[0]}" for i in students_list)
    print(students_list)
    
    student = input('Введи учня зі списку вище ->>> ')

    discip_list = session.query(Discipline.discipline).join(Teacher, Teacher.id == Discipline.teacher_id).join(
        Grade, Grade.discipline == Discipline.discipline).join(Student, Student.id == Grade.student_id).filter(
            Student.name == student, Teacher.name == teacher).group_by(Discipline.discipline).all()
    discipline = "; ".join(f"{i[0]}" for i in discip_list)
    
    print()
    
    print(f"Вчитель {teacher} читає учню {student}  наступні курси: {discipline}")

if __name__ == '__main__':
    start_seeds()
    print('Заповнення таблиць закінчено')
    print("1---------------------------")
    get_students_5()
    print("2---------------------------")
    get_discep()
    print("3---------------------------")
    find_group_avg_discep()
    print("4---------------------------")
    find_AVG_rating()
    print("5---------------------------")
    find_discipline_teacher()
    print("6---------------------------")
    get_all_statudents_from_group()
    print("7---------------------------")
    find_rating_students_disce_of_group()
    print("8---------------------------")
    find_AVG_teacher_disce()
    print("9---------------------------")
    find_list_discip_or_stud()
    print("10---------------------------")
    find_disce_of_teacher()
    print("Кінець")
