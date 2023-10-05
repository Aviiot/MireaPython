import tkinter as tk

def task1():
	def calculate_coordinate_dot(t, x0=0, v=0, a=0):
		print(x0 + v * t + (a * t ** 2) / 2)

	calculate_coordinate_dot(2, 5, 10, 3) # 5 + 10 * 2 + (3 * 2 ** 2) / 2 = 5 + 20 + 6 = 31
	calculate_coordinate_dot(4, -2, 0, -5) # -2 + 0 * 4 + (-5 * 4 ** 2) / 2 = -2 + 0 + (-5 * 16) / 2 = -2 - 40 = -42
	calculate_coordinate_dot(3.5) # 0 + 0 * 3.5 + (0 * 3.5 ** 2) / 2 = 0
def task2():
	def digit_sum(number):
		digit_sum = 0
		while number != 0:
			digit_sum += number % 10
			number //= 10
		print(digit_sum)
	digit_sum(int(input()))
def task3():
	import random
	products = ["рыба", "мясо", "сталь", "игрушки", "одежда", "книги", "электроника", "мебель", "еда", "сок",
				"косметика", "обувь", "инструменты", "автомобили", "спорттовары"]
	how_products = random.randint(1, 15)

	factory1_products = set(random.sample(products, how_products))
	factory2_products = set(random.sample(products, how_products))

	unique_products = factory1_products.intersection(factory2_products)

	print('\nПервый завод: ' + ' '.join(factory1_products))
	print('Второй завод: ' + ' '.join(factory2_products))
	print('Пересечение: ' + ' '.join(unique_products))
def task4():
	dicionary = {
		'Питонов Дмитрий Александрович': {
			'Возраст': '18',
			'Должность': 'Разработчик',
			'Номер рабочего места': '1',
			'Наличие доступа к тайне': 'да'
		},
		'Сиплюсплюсов Александр Дмитриевич': {
			'Возраст': '19',
			'Должность': 'Программист',
            'Номер рабочего места': '2',
            'Наличие доступа к тайне': 'нет'
		},
		'Сишарпова Александра Дмитриевна': {
			'Возраст': '20',
			'Должность': 'Секретарь',
            'Номер рабочего места': '3',
            'Наличие доступа к тайне': 'нет'
		}
	}
	for name, data in dicionary.items():
		print('Имя: ', name)
		print('Информация: ', data)
		print('\n')
def task5():
	import random
	num = random.randint(0, 1)

	try:
		print(10/num)
	except ZeroDivisionError:
		print('деление на 0')
def task6():
	input_string = input('Введите строку: ')
	with open('file.txt', 'a') as f:
		f.write(input_string + '\n')
def task7():
	try:
		with open('file.txt', 'r') as f:
			print(f.read())
	except FileNotFoundError:
		print('Файла нет')

def task8():
	import os
	import shutil
	try:
		shutil.copy('file.txt', 'new_file.txt')
		os.remove('file.txt')
	except FileNotFoundError:
		print('Файла нет')

def main():
	main_window = tk.Tk()
	main_window.title("main window")

	main_button_frame = tk.Frame(main_window)
	main_button_frame.pack()

	try:
		tasks = [
			("Задание №1", task1),
			("Задание №2", task2),
			("Задание №3", task3),
			("Задание №4", task4),
			("Задание №5", task5),
			("Задание №6", task6),
			("Задание №7", task7),
			("Задание №8", task8)
		]

		for text, command in tasks:
			button = tk.Button(main_button_frame, text=text, command=command)
			button.pack()
	except:
		pass

	main_window.mainloop()


if __name__ == "__main__":
	main()
