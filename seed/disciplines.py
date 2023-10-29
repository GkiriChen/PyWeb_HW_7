import random
from faker import Faker

import sys
sys.path.append('.')

from database.connect_db import session
from database.models7 import Discipline, Teacher


# ----Create disciolines----#
def create_disciolines():

    teachers = session.query(Teacher).all()
    
    for _ in range(random.randint(5, 9)):

        teacher = random.choice(teachers)
        #print(Faker().job())
        disciline = Discipline(
            discipline=Faker().job(),
            teacher_id=teacher.id
        )

        session.add(disciline)
    session.commit()

def check_teachers():

    teachers_list = session.query(Teacher.id).all()
    #print(teachers_list)
    
    for teacher in teachers_list:
        #print(teacher[0])
        res = session.query(Discipline.discipline).filter(Discipline.teacher_id == teacher[0]).all()
        if res != []:
            pass
        else:
            #print(res)
            teacher_del = session.query(Teacher.name).filter(Teacher.id == teacher[0]).all()
            print(f"У вчителя {teacher_del[0][0]} відсутні предмети тому він/вона видаляється з бази")
           
            del_t = session.query(Teacher).filter(Teacher.id == teacher[0]).delete()
            session.commit()


if __name__ == '__main__':
    #create_disciolines()
    check_teachers()