import sqlite3

connect = sqlite3.connect('User.db')

cursor = connect.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users(
        name TEXT NOT NULL, 
        age INTEGER, 
        hobby TEXT NOT NULL
    )
    '''
)

connect.commit()


def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")


# add_user("Ardager", 26, 'Гонки')
# add_user("Вася", 45, 'бегать')
# add_user('Олег', 11, 'ничего')
# add_user('Саша', 20, "гонки")


def get_all_users(name):
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    for i in range(len(users)):
        for j in range(len(users[i])):
            if users[i][j] == name:
                return f"NAME: {users[i][0]}, AGE: {users[i][1]}, hobby: {users[i][2]}"


print(get_all_users('Саша'))
