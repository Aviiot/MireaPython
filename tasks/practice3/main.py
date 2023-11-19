def task1():

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "Hello, world!"

    if __name__ == "__main__":
        app.run()


def task2():
    with open("output.txt", "w") as file:
        while True:
            input_str = input("Введите строку")
            if input_str.lower() == "стоп":
                break
            file.write(input_str + "\n")


def task3():
    from flask import Flask, render_template, request

    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/add_to_file", methods=["POST"])
    def add_to_file():
        input_str = request.form["input_str"]
        if input_str.lower() != "стоп":
            with open("output.txt", "a") as file:
                file.write(input_str + "\n")
        return render_template("index.html")

    @app.route("/view_file")
    def view_file():
        content = []
        with open("output.txt", "r") as file:
            content = file.readlines()
        return render_template("view_file.html", content=content)

    if __name__ == "__main__":
        app.run()


def task4():
    import sqlite3

    conn = sqlite3.connect("users.db")

    conn.execute(
        """CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    birth_year INTEGER,
                    occupation TEXT)"""
    )

    while True:
        name = input("Введите ФИО пользователя (для выхода введите 'стоп'): ")
        if name.lower() == "стоп":
            break

        birth_year = input("Введите год рождения пользователя: ")
        occupation = input("Введите род деятельности пользователя: ")

        conn.execute(
            "INSERT INTO users (name, birth_year, occupation) VALUES (?, ?, ?)",
            (name, birth_year, occupation),
        )
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


def task5():
    from flask import Flask, render_template, request, redirect
    import sqlite3
    import random

    app = Flask(__name__)
    db_name = "users.db"

    @app.route("/")
    def index():
        conn = sqlite3.connect(db_name)

        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        conn.close()
        return render_template("index_2.html", rows=rows)

    @app.route("/add_random", methods=["POST"])
    def add_random():
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        random_name = "Random User " + str(random.randint(1, 100))
        random_birth_year = random.randint(1950, 2000)
        random_occupation = "Occupation " + str(random.randint(1, 5))
        cursor.execute(
            "INSERT INTO users (name, birth_year, occupation) VALUES (?, ?, ?)",
            (random_name, random_birth_year, random_occupation),
        )
        conn.commit()
        conn.close()
        return redirect("/")

    @app.route("/delete_row", methods=["POST"])
    def delete_row():
        row_id = request.form["row_id"]
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=?", (row_id,))
        conn.commit()
        conn.close()
        return redirect("/")

    if __name__ == "__main__":
        app.run()


