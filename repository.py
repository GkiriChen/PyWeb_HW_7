import sqlite3

from faker import Faker 
import random

def create_db():
    with open('init_todo.sql', 'r') as f:
        sql = f.read()
    
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.executescript(sql)
    print('Create_DB')
    print('-----------------------------')

def populate_db():
    
    ##Create students    
    users_sql_command = "\n".join(f"INSERT INTO users (name) VALUES ('{Faker().name()}');" for _ in range(30))
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.executescript(users_sql_command)
        cur.execute("SELECT id from users;")        
        user_ids = [obj[0] for obj in cur.fetchall()]        
        print('students -',user_ids)
    print('-----------------------------')

    ##Create groups    
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute("SELECT name FROM users")
        result = cur.fetchall()
        #print(result)

    for i in range(1,4):                
        group_users_sql_command = "\n".join(f"INSERT INTO groups_users (group_us, name) VALUES ({i}, '{n[0]}');" for n in result[(i*10-10):(i*10)])
        
        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.executescript(group_users_sql_command)  
    
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from groups_users;")        
        user_ids = [obj for obj in cur.fetchall()]                
        print('Create groups')
    print('-----------------------------')

    ##Create teacher
    teacher_sql_command = "\n".join(f"INSERT INTO teacher (name) VALUES ('{Faker().name()}');" for _ in range(random.randint(3,5)))
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.executescript(teacher_sql_command)
        cur.execute("SELECT * from teacher;")        
        user_ids = [obj[1] for obj in cur.fetchall()]        
        print('teacher -', user_ids)
    print('-----------------------------')

    ##Create disciplines    
    #teacher_sql_command = "\n".join(f"INSERT INTO discipline (discipline, name) VALUES ('{Faker().job()}', '{f"SELECT name FROM teacher Order by random() limit"}');" for _ in range(random.randint(5,8)))
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        for _ in range(random.randint(5,8)):
            cur.execute("SELECT name FROM teacher ORDER BY random() limit 1;")
            name_teacher = cur.fetchone()            
            cur.execute(f"INSERT INTO disciplines (discipline, name) VALUES ('{Faker().job()}', '{name_teacher[0]}');")        
        cur.execute("SELECT * from disciplines;")        
        user_ids = [obj for obj in cur.fetchall()]        
        print('discipline -', user_ids)    
    print('-----------------------------')

    ##Create grades
    
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute("SELECT name FROM users;")
        amount_disc = cur.fetchall()   
        cur.execute("SELECT discipline FROM disciplines;")
        discipline = cur.fetchall()
        for _ in range(len(amount_disc)):
            #print(name_us[0], random.choice(discipline)[0])
            grades_sql_command = "\n".join(f"INSERT INTO grades (name, discipline, rating, date_gr) VALUES ('{random.choice(amount_disc)[0]}','{random.choice(discipline)[0]}', {random.randint(1,10)}, '{Faker().date_between(start_date='-1y')}');" for i in range(random.randint(10,20)))            
            cur.executescript(grades_sql_command)
        cur.execute("SELECT count(id) from grades;")                
        print('grades -', cur.fetchone()[0])
    


def check_db():
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from users;")
        result = cur.fetchall()
    print(result)
    print('-----------------------------')

    # with sqlite3.connect('todo.db') as con:
    #     cur = con.cursor()
    #     cur.execute("SELECT * from tasks;")
    #     result = cur.fetchall()
    # print(result)

    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from groups_users;")
        result = cur.fetchall()
    print(result)


def select(table_name:str, condition=None):
    if condition is not None:
        querry = f"SELECT * FROM {table_name} WHERE {condition};"
    else:
        querry = f"SELECT * FROM {table_name};"


    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(querry)
        result = cur.fetchall()
    return result

def delete(table_name:str, condition=None):
    if condition is not None:
        querry = f"DELETE  FROM {table_name} WHERE {condition};"
    else:
        querry = f"DELETE  FROM {table_name};"


    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(querry)
        result = cur.fetchall()
    return result


def init_db():
    create_db()
    populate_db()    
    #check_db()

init_db()

