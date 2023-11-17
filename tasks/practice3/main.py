def task1():

    from flask import Flask


    app = Flask(__name__)


    @app.route('/')
    def hello_world():
        return 'Hello, world!'


    if __name__ == '__main__':
        app.run()

def task2():
    with open('output.txt', 'w') as file:
        while True:
            input_str = input("Введите строку")
            if input_str.lower() == 'стоп':
                break
            file.write(input_str + '\n')

def task3():
    from flask import Flask, render_template, request

    app = Flask(__name__)
    @app.route('/')
    def index():
        return render_template('index.html')
    @app.route('/add_to_file', methods=['POST'])
    def add_to_file():
        input_str = request.form['input_str']
        if input_str.lower() != 'стоп':
            with open('output.txt', 'a') as file:
                file.write(input_str + '\n')
        return render_template('index.html')

    @app.route('/view_file')
    def view_file():
        content = []
        with open('output.txt', 'r') as file:
            content = file.readlines()
        return render_template('view_file.html', content=content)

    if __name__ == '__main__':
        app.run()

def task4():
    import sqlite3

    conn = sqlite3.connect('users.db')

    conn.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    birth_year INTEGER,
                    occupation TEXT)''')

    while True:
        name = input("Введите ФИО пользователя (для выхода введите 'стоп'): ")
        if name.lower() == 'стоп слово':
            break

        birth_year = input("Введите год рождения пользователя: ")
        occupation = input("Введите род деятельности пользователя: ")


        conn.execute("INSERT INTO users (name, birth_year, occupation) VALUES (?, ?, ?)",
                     (name, birth_year, occupation))
        conn.commit()

    print("Содержимое базы данных:")
    cursor = conn.execute("SELECT * FROM users")
    for row in cursor:
        print("ID:", row[0])
        print("ФИО:", row[1])
        print("Год рождения:", row[2])
        print("Род деятельности:", row[3])
        print("----------------------------------")


    conn.close()

