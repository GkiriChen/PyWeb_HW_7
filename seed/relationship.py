import random

from database.connect_db import session
from database.models7 import Student, Teacher, TeacherStubent


def create_rel():

    teachers = session.query(Teacher).all()
    students = session.query(Student).all()

    for student in students:
        teacher = random.choice(teachers)
        rel = TeacherStubent(teacher_id=teacher.id, student_id=student.id)

        session.add(rel)
    session.commit()


if __name__ == '__main__':
    create_rel()
