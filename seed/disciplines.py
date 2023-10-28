import random
from faker import Faker

from database.connect_db import session
from database.models7 import Discipline, Teacher


# ----Create disciolines----#
def create_disciolines():

    teachers = session.query(Teacher).all()

    for _ in range(random.randint(5, 8)):

        teacher = random.choice(teachers)

        discioline = Discipline(
            discipline=Faker.job(),
            teacher_id=teacher.id
        )

        session.add(discioline)
    session.commit()


if __name__ == '__main__':
    create_disciolines()
