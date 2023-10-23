from repository import init_db

from models import Task, User,Groups_users,Grades, Discipline


#init_db()

#print(User.get_all_users_from_db())

# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
User.find_busiest()
# Знайти студента із найвищим середнім балом з певного предмета.
User.find_busiest_discep()
# Знайти середній бал у групах з певного предмета.
Discipline.find_group_avg_discep()
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
