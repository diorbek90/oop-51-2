import sqlite3

connect = sqlite3.connect('User.db')

cursor = connect.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(40) NOT NULL,
    age INTEGER NOT NULL,
    hobby TEXT)
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS grades(
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    subject VARCHAR(50) NOT NULL,
    grade INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    
    )
    """
)

connect.commit()


def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f'Пользователь {name} добавлен!')


def add_grade(user_id, subject, grade):
    cursor.execute(
        'INSERT INTO grades(user_id, subject, grade) VALUES (?, ?, ?)',
        (user_id, subject, grade)
    )
    connect.commit()
    print(f'Оценка добавлена для пользователья с id {user_id}!')


# add_user('Ardager', 23, 'swim')
# add_user('Oleg', 23, 'swim')
# add_user('John', 23, 'swim')
# add_user('Doe', 23, 'swim')
# add_user('Anna', 23, 'swim')
#
#
# add_grade(4, 'Алгебра', 5)
# add_grade(3, 'Алгебра', 5)
# add_grade(2, 'Алгебра', 5)
# add_grade(1, 'Алгебра', 5)
# add_grade(4, 'Изо', 2)
# add_grade(3, 'Изо', 2)
# add_grade(2, 'Изо', 2)
# add_grade(1, 'Изо', 2)


def get_user_with_grade():
    cursor.execute(
        """
        SELECT users.name, grades.subject, grades.grade 
        FROM users 
        INNER JOIN grades ON users.user_id = grades.user_id
        """
    )

    users = cursor.fetchall()

    print(users)
    print("\n\n")

    for i in users:
        print(f'NAME: {i[0]}, SUBJECT: {i[1]} GRADE: {i[2]}')


# Домашняя задания
def update_grade(grade_id, new_grade):
    cursor.execute(
        'UPDATE grades SET grade = ? WHERE grade_id = ?',
        (new_grade, grade_id)
    )
    connect.commit()
    print(f'subject id {grade_id} updated !!')


update_grade(3, 4)
