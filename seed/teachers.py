import sys
sys.path.append('.')

from faker import Faker

from database.connect_db import session
from database.models7 import Teacher


## ----Create teachers----#
def create_teachers():

    for _ in range(1, 5):
        name_stud = Faker().name()

        teacher = Teacher(
            name=name_stud,
            email=name_stud.replace(' ', '_') + '@gmail.com'
        )

        session.add(teacher)
    session.commit()


if __name__ == '__main__':
    create_teachers()
