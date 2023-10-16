# https://github.com/Aviiot/mirea-python/blob/main/tasks/practice1/main.py



import tkinter as tk
import random

def task1():
    def calculate():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            operation = entry3.cget("text")

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            elif operation == '**':
                result = num1 ** num2
            elif operation == '%':
                result = num1 % num2
            elif operation == '√':
                result = num1 ** (1/num2)
            else:
                result = 'Invalid operation'

            label.config(text='Result: {:.2f}'.format(result))
        except ValueError:
            label.config(text='Invalid input')


    def set_operation(op):
        entry3.config(text=op)
        calculate()


    root = tk.Tk()
    root.title("Calculator")
    root.geometry("300x200") 

    label1 = tk.Label(root, text="Number 1:")
    label1.pack()
    entry1 = tk.Entry(root)
    entry1.pack()

    label2 = tk.Label(root, text="Number 2:")
    label2.pack()
    entry2 = tk.Entry(root)
    entry2.pack()

    entry3 = tk.Label(root, text="")
    entry3.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    buttons = ['+', '-', '*', '/', '**', '%', '√']
    for btn_text in buttons:
        button = tk.Button(button_frame, text=btn_text, command=lambda text=btn_text: set_operation(text))
        button.pack(side=tk.LEFT)

    entry1.bind("<KeyRelease>", lambda event: calculate())
    entry2.bind("<KeyRelease>", lambda event: calculate())

    label = tk.Label(root, text="Result: ")
    label.pack()

    root.mainloop()
def task2():
    def generate_phrase(nouns, verbs, phrase_type):
        phrase_formats = {
            "nvn": "{noun}-{verb}-{noun}",
            "vnn": "{verb}-{noun}-{noun}",
            "nnv": "{noun}-{noun}-{verb}"
        }
        return phrase_formats.get(phrase_type, "Invalid phrase type").format(
            noun=random.choice(nouns),
            verb=random.choice(verbs)
        )

    nouns = []
    print("Enter nouns (type 'stop' to exit):")
    while (noun := input()) != "stop":
        nouns.append(noun)

    verbs = []
    print("Enter verbs (type 'stop' to exit):")
    while (verb := input()) != "stop":
        verbs.append(verb)

    count = int(input("Enter the number of phrases to generate:"))

    print("Generated phrases:")
    phrase_types = ["nvn", "vnn", "nnv"]
    for _ in range(count):
        phrase_type = random.choice(phrase_types)
        phrase = generate_phrase(nouns, verbs, phrase_type)
        print(phrase)
def task3():
    def check_spelling(etalon_words, sentence):
        errors = []
        words = sentence.split()

        for word in words:
            is_valid = False
            for etalon_word in etalon_words: 
                if len(word) == len(etalon_word): 
                    is_word_valid = True 
                    for i in range(len(word)):
                        if word[i] != etalon_word[i]:
                            is_word_valid = False
                            break
                    if is_word_valid:
                        is_valid = True
                        break

            if not is_valid:
                errors.append(word)

        return errors

    etalon_words = input("Enter the reference words separated by spaces: ").split()
    sentence = input("Enter the sentence: ")

    errors = check_spelling(etalon_words, sentence)

    if len(errors) == 0:
        print("No errors found in the sentence")
    else:
        print("Words with errors:")
        for error in errors:
            print(error)
def task4():
    import time
    def start_timer():
        hours = int(hours_entry.get())
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())

        total_seconds = hours * 3600 + minutes * 60 + seconds

        def update_timer():
            nonlocal total_seconds

            if total_seconds > 0:
                hours = total_seconds // 3600
                minutes = (total_seconds % 3600) // 60
                seconds = (total_seconds % 3600) % 60

                timer_label["text"] = f"Time remaining: {hours:02d}:{minutes:02d}:{seconds:02d}"
                total_seconds -= 1
                timer_label.after(1000, update_timer)
            else:
                timer_label["text"] = "Time вышло"

        start_button.configure(state="disabled")        
        update_timer()


    root = tk.Tk()
    root.title("Timer")

    hours_label = tk.Label(root, text="Hours:")
    hours_label.pack()
    hours_entry = tk.Entry(root)
    hours_entry.pack()

    minutes_label = tk.Label(root, text="Minutes:")
    minutes_label.pack()
    minutes_entry = tk.Entry(root)
    minutes_entry.pack()

    seconds_label = tk.Label(root, text="Seconds:")
    seconds_label.pack()
    seconds_entry = tk.Entry(root)
    seconds_entry.pack()

    start_button = tk.Button(root, text="Start", command=start_timer)
    start_button.pack()

    timer_label = tk.Label(root, text="Time remaining: ")
    timer_label.pack()

    root.mainloop()
def task5():

    task5 = tk.Tk()
    task5.title("Generating")

    def generate_character():
        names = ["John", "Alice", "Bob", "Eve"]
        classes = ["Warrior", "Mage", "Rogue"]
        parameters = ["Strength", "Agility", "Intelligence", "Charisma"]
        special = ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]
        skills = ["Stealth", "Archery", "Magic", "Lockpicking"]

        character = {
            "Name": random.choice(names),
            "Age": random.randint(18, 40),
            "Class": random.choice(classes),
            "Parameters": {parameter: random.randint(1, 10) for parameter in parameters},
            "Special": {stat: random.randint(1, 10) for stat in special},
            "Skills": random.sample(skills, random.randint(1, len(skills)))
        }

        character_text.insert(tk.END, "Name: {}\n".format(character["Name"]))
        character_text.insert(tk.END, "Age: {}\n".format(character["Age"]))
        character_text.insert(tk.END, "Class: {}\n".format(character["Class"]))

        character_text.insert(tk.END, "Parameters:\n")
        for parameter, value in character["Parameters"].items():
            character_text.insert(tk.END, "  {}: {}\n".format(parameter, value))

        character_text.insert(tk.END, "Special:\n")
        for stat, value in character["Special"].items():
            character_text.insert(tk.END, "  {}: {}\n".format(stat, value))

        character_text.insert(tk.END, "Skills:\n")
        for skill in character["Skills"]:
            character_text.insert(tk.END, "  {}\n".format(skill))
        character_text.insert(tk.END, "\n")

    generate_button = tk.Button(task5, text="Generate Character", command=generate_character)
    generate_button.pack()

    character_text = tk.Text(task5, width=40)
    character_text.pack()

    task5.mainloop()
def task6():
    print('а что сделать?')
def task7():

    industries = [
        "Сельское хозяйство",
        "Легкая промышленность",
        "Тяжелая промышленность группы А",
        "Тяжелая промышленность группы Б",
        "Военно промышленный комплекс",
        "Наука",
        "Химическая промышленность"
    ]

    repuplics = [
        "Республика1",
        "Республика2",
        "Республика3"
    ]

    information = {}
    for republic in repuplics:
        information[republic] = {}
        for industry in industries:
            information[republic][industry] = random.choice(["избыточно развитые", "сбалансированно развитые", "слабо развитые"])

    least_developed_industry = ""
    least_developed_count = 0

    most_developed_industry = ""
    most_developed_count = 0

    balanced_industry = ""
    balanced_count = 0

    for industry in industries:
        developed_count = 0
        undeveloped_count = 0
        
        for republic, industries_data in information.items():
            if industries_data[industry] == "избыточно развитые":
                developed_count += 1
            elif industries_data[industry] == "слабо развитые":
                undeveloped_count += 1
        
        if undeveloped_count > least_developed_count:
            least_developed_industry = industry
            least_developed_count = undeveloped_count
            
        if developed_count > most_developed_count:
            most_developed_industry = industry
            most_developed_count = developed_count
            
        if abs(developed_count - undeveloped_count) > balanced_count:
            balanced_industry = industry
            balanced_count = abs(developed_count - undeveloped_count)

    print(f"1. Самая отстающая отрасль: {least_developed_industry}")
    print(f"   В скольких республиках отстает?: {least_developed_count}")
    print(f"2. Самая развитая отрасль: {most_developed_industry}")
    print(f"   В скольких республиках развитая?: {most_developed_count}")
    print(f"3. Самая сбалансированная отрасль: {balanced_industry}")
    print(f"   В скольких республиках сбалансирована?: {balanced_count}\n")
    

    for republic, industries_data in information.items():
        developed_count = sum(1 for industry, status in industries_data.items() if status == "избыточно развитые")
        undeveloped_count = sum(1 for industry, status in industries_data.items() if status == "слабо развитые")
        print(f"Статистика развития в республике '{republic}':")
        print(f"   Развитые отрасли: {developed_count}")
        print(f"   Слаборазвитые отрасли: {undeveloped_count}")
        print(f"   Разница: {undeveloped_count - developed_count}")
        
def main():
    main_window = tk.Tk()
    main_window.title("main window")

    main_button_frame = tk.Frame(main_window)
    main_button_frame.pack()

    tasks = [
        ("Задание №1", task1),
        ("Задание №2", task2),
        ("Задание №3", task3),
        ("Задание №4", task4),
        ("Задание №5", task5),
        ("Задание №6", task6),
        ("Задание №7", task7)
    ]

    for text, command in tasks:
        button = tk.Button(main_button_frame, text=text, command=command)
        button.pack()

    main_window.mainloop()

if __name__ == "__main__":
    main()
    