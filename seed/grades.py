import random
from faker import Faker

from database.connect_db import session
from database.models7 import Grade, Discipline, Student


# ----Create greads----#
def create_greads():

    disciplines = session.query(Discipline).all()
    students = session.query(Student).all()

    for student in students:

        for _ in range(random.randint(10, 20)):
            gread = Grade(
                name=student.name,
                discipline=random.choice(disciplines).discipline,
                rating=random.randint(1, 10),
                date_gr=Faker().date_between(start_date='-1y')
            )

            session.add(gread)
    session.commit()


if __name__ == '__main__':
    create_greads()
