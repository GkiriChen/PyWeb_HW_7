import sys
sys.path.append('.')

from faker import Faker

from database.connect_db import session 
from database.models7 import Student


# ----Create students----#
def create_students():

    for _ in range(1, 31):
        name_stud = Faker().name()
        email=name_stud.lower().replace(' ', '_') + '@gmail.com'

        #print(name_stud,'<--->', email)
        student = Student(
            name=name_stud,
            email=email
        )

        session.add(student)
    session.commit()


if __name__ == '__main__':
    create_students()
