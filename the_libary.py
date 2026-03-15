# Beta v0.4

from time import sleep

def start():
	print("\n         📚 Моя Библиотека\n")
	print("1. Вывести информацию о книгах (> 1)")
	print("2. Добавить книгу (> 1)")
	print("3. Изменить статус прочтения")
	print("4. Удалить книгу (> 1)")
	print("5. Выйти из Библиотеки")
	print("-------------------------------------\n")
	print("Примечание: (> 1) означает что есть под-варианты для выполнения точного действия\n")

def book_info():
	print(f"📔 Информация о книге №{count}:")
	print()
	print(f"Название: {THE_LIBRARY[i]['title']}")
	print(f"Автор: {THE_LIBRARY[i]['author']}")
	print(f"Год: {THE_LIBRARY[i]['year']}")
	print(f"Прочитано: {THE_LIBRARY[i]['read']}\n")

start()

THE_LIBRARY = [{"title" : "Бусидо",
	"author" : "Юдзан Дайдодзи",
	"year" : "1998",
	"read" : False},

	{"title" : "Хагакурэ",
	"author" : "Юдзан Дайдодзи",
	"year" : "2000",
	"read" : False},

	{"title" : "Метро 2033",
	"author" : "Дмитрий Глуховский",
	"year" : "2005",
	"read" : True}
]

try:
	library_menu = int(input("Выберите пункт: "))
except ValueError:
	print('❌ Неверно. Вводите только цифры.')
	library_menu = 0

# Выйти из Библиотеки
while library_menu != 5:

	count = 0

	# Вывести информацию о книгах
	if library_menu == 1:
		print("1. Вывести все книги")
		print("2. Поиск по названию")
		print("3. Фильтровать по авторам")
		print("4. Фильтровать по статусу прочтения")
		print("-------------------------------------")

		books_filter = int(input("Выберите пункт: "))

		# Вывести все книги
		if books_filter == 1:
			for i in range(0, len(THE_LIBRARY)):
				count += 1
				book_info()

				if THE_LIBRARY[i]['read'] == True:
					print(f"Статус: Прочитано 📗\n")
				else:
					print(f"Статус: Непрочитано 📕\n")
				sleep(1)
			sleep(1)

		elif books_filter == 2:
			search = str(input("Поиск (по названию): "))
			if search != "":
				print(f"\n🔎 Поиск: {search}")
				print("Возможные варианты: ")

				count = 0

				for i in range(0, len(THE_LIBRARY)):
					if search in THE_LIBRARY[i]['title']:
						count += 1
						book_info()
					sleep(1)
				print("---------------------------")
			else:
				print("❌ Ошибка. Пустая строка")

		# Фильтровать по авторам
		elif books_filter == 3:
			
			author_info = str(input("Введите ФИО Автора: ")).title()
			author_isvalid = ""
			count = 0
			
			for i in range(0, len(THE_LIBRARY)):
				if author_info == THE_LIBRARY[i]['author'].title():
					author_isvalid = THE_LIBRARY[i]

			if author_isvalid != "":
				print(f"Книги автора: {author_isvalid['author']}")
				print("-----------------------------------")

				for i in range(0, len(THE_LIBRARY)):
					if author_isvalid['author'] in THE_LIBRARY[i]['author']:
						count += 1
						book_info()
						sleep(1)
				print("\n-----------------------------------")
			else:
				print()
				print("Такого автора нет в Библиотеке!")

		# Фильтровать по статусу прочтения
		elif books_filter == 4:
			print("1. Вывести прочитанные")
			print("2. Вывести непрочитанные")

			isread_filter = int(input("Выберите пункт: "))
			count = 0

			# Прочитанные книги
			if isread_filter == 1:
				print("\nНиже прочитанные вами книги:")
				print("---------------------------")
				for i in range(0, len(THE_LIBRARY)):
					if THE_LIBRARY[i]['read'] == True:
						count += 1
						book_info()
					sleep(1)
				print("---------------------------")

			# Непрочитанные книги
			elif isread_filter == 2:
				print("\nНиже НЕпрочитанные вами книги:")
				print("---------------------------")
				for i in range(0, len(THE_LIBRARY)):
					if THE_LIBRARY[i]['read'] == False:
						count += 1
						book_info()
					sleep(1)
				print("---------------------------")

	# Добавить книгу
	elif library_menu == 2:
		# nb = New Book
		nb_name = str(input("Введите название новой книги: "))
		nb_author = str(input("Автор новой книги: "))
		nb_year = str(input("Дата выхода: "))
		nb_isread = int(input("Прочитано/Непрочитано? (1, 2): "))

		if nb_isread == 1:
			nb_isread = True
		else:
			nb_isread = False

		# nb = New Book
		nb = {"title" : nb_name, "author" : nb_author, "year" : nb_year, "read" : nb_isread}

		THE_LIBRARY.append(nb)
		print("\n📗 Книга успешно добавлена")
		sleep(1)

	# Изменить статус о прочтении
	elif library_menu == 3:
		print("\n")
		for i in range(0, len(THE_LIBRARY)):
			print(f"📔 Название: «{THE_LIBRARY[i]['title']}»")
			if THE_LIBRARY[i]['read'] == True:
				print(f"Статус: Прочитано 📗\n")
			else:
				print(f"Статус: Непрочитано 📕\n")
			sleep(1)

		book_change_status = int(input("Выберите книгу для смены статуса: "))
		book_isvalid = ""

		print("---------------------------------")

		for j in range(0, len(THE_LIBRARY)):
			if book_change_status - 1 == j:
				book_isvalid = "YES"
				print(f"📔 Название: {THE_LIBRARY[j]['title']}")
				
				if THE_LIBRARY[j]['read'] == True:
					THE_LIBRARY[j]['read'] = False
					print(f"\nСтатус: Непрочитано (Только что)")
					print("---------------------------------")
					sleep(1)

				elif THE_LIBRARY[j]['read'] == False:
					THE_LIBRARY[j]['read'] = True
					print(f"\nСтатус: Прочитано (Только что)")
					print("---------------------------------")
					sleep(1)

		if book_isvalid == "":
			print("❌ Нет книги с таким №")

		print("Примечание: Если книга была 'прочитана', статус изменится на 'Непрочитано' и наоборот.\n")

	# Удалить книгу
	elif library_menu == 4:
		try:
			delete_book = int(input("Введите № книги для удаления: "))
			book_isvalid = ""

			for i in range(0, len(THE_LIBRARY)):

				if delete_book - 1 == i:
					book_isvalid = "YES"
					print("Будет удалена следующая книга: \n")
					count = delete_book
					book_info()
					sleep(1)

					confirm = str(input("Удалить?(Y/N): ")).lower()

					if confirm == 'y':
						del THE_LIBRARY[i]
						sleep(1)
						print("Книга была удалена.")
						sleep(1)

					elif confirm == 'n':
						print("Операция прервана.")
						sleep(1)

					else:
						print("Вводите только Y или N.")
						sleep(1)

			if book_isvalid == "":
				print("❌ Нет книги с таким №")

		except ValueError:
			print("❌ Ошибка. Вы ввели не цифры.")
			sleep(1)

	start()

	try:
		library_menu = int(input("Выберите пункт: "))
	except ValueError:
		print("❌ Ошибка. Вы ввели не цифры.\n")
		library_menu = 0
