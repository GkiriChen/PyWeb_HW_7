import random
from faker import Faker

from datebase.connect_db import session
from datebase.models7 import Group, Student


# ----Create groups----#
def create_groups():

    students = session.query(Student).all()

    for student in students:
        group = Group(
            namber=random.randint(1, 3),
            student_id=student.id
        )

        session.add(group)
    session.commit()


if __name__ == '__main__':
    create_groups()
