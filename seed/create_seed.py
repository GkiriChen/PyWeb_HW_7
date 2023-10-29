import sys
sys.path.append('.')

from seed.disciplines import check_teachers, create_disciolines
from seed.students import create_students
from seed.teachers import create_teachers
from seed.groups import create_groups
from seed.relationship import create_rel
from seed.grades import create_greads



def start_seeds():
    create_students()
    create_teachers()
    create_rel()
    create_groups()
    create_disciolines()
    check_teachers()
    create_greads()

if __name__ == '__main__':
    start_seeds()