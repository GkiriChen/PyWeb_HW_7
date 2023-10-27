from faker import Faker

from datebase.connect_db import session
from datebase.models7 import Student


# ----Create students----#
def create_students():

    for _ in range(1, 31):
        name_stud = Faker().name()
        student = Student(
            name=name_stud,
            email=name_stud.replace('-', '_') + '@gmail.com'
        )

        session.add(student)
    session.commit()


if __name__ == '__main__':
    create_students()
