# Beta v0.4

from time import sleep

def start():
	print("\n         📚 Моя Библиотека\n")
	print("1. Вывести информацию о книгах")
	print("2. Добавить книгу")
	print("3. Изменить статус прочтения")
	print("4. Удалить книгу")
	print("-------------------------------------")
	print("5. Выйти из Библиотеки")
	print("-------------------------------------")

def book_info(book_num):
	print(f"\n📔 Информация о книге №{book_num}:")
	print()
	print(f"Название: {THE_LIBRARY[i]['title']}")
	print(f"Автор: {THE_LIBRARY[i]['author']}")
	print(f"Год: {THE_LIBRARY[i]['year']}")
	print(f"Прочитано: {('Нет 📕', 'Да 📗')[THE_LIBRARY[i]['read']]}")

start()

THE_LIBRARY = [
			{"title" : "Бусидо", "author" : "Юдзан Дайдодзи", "year" : "1998", "read" : False},
			{"title" : "Хагакурэ", "author" : "Юдзан Дайдодзи", "year" : "2000", "read" : False},
			{"title" : "Метро 2033", "author" : "Дмитрий Глуховский", "year" : "2005", "read" : True}
]

select_option = -1

while select_option != 5:

	book_num = 0

	# Вывести информацию о книгах
	if select_option == 1:
		print("1. Вывести все книги")
		print("2. Поиск по названию")
		print("3. Фильтровать по авторам")
		print("4. Фильтровать по статусу прочтения")
		print("-------------------------------------")

		select_filter = int(input("Выберите пункт: "))

		# Вывести все книги
		if select_filter == 1:
			for i in range(0, len(THE_LIBRARY)):
				book_num += 1
				book_info(book_num)
				sleep(1)
			sleep(1)

		elif select_filter == 2:

			search_book = input("Поиск (по названию): ")

			if search_book == "":
				print("❌ Ошибка. Пустая строка")
			else:
				print(f"\n🔎 Поиск: {search_book}")
				print("Возможные варианты: ")

				book_num = 0

				for i in range(0, len(THE_LIBRARY)):
					if search_book in THE_LIBRARY[i]['title']:
						book_num += 1
						book_info(book_num)
					sleep(1)
				print("---------------------------")

		# Фильтровать по авторам
		elif select_filter == 3:
			
			author_fio = input("Введите ФИО Автора: ").title()
			found_author = ""
			book_num = 0
			
			for i in range(0, len(THE_LIBRARY)):
				if author_fio == THE_LIBRARY[i]['author'].title():
					found_author = THE_LIBRARY[i]

			if found_author == "":
				print("\nТакого автора нет в Библиотеке!")
			else:
				print(f"Книги автора: {found_author['author']}")
				print("-----------------------------------")

				for i in range(0, len(THE_LIBRARY)):
					if found_author['author'] in THE_LIBRARY[i]['author']:
						book_num += 1
						book_info(book_num)
						sleep(1)
				print("\n-----------------------------------")

		# Фильтровать по статусу прочтения
		elif select_filter == 4:
			print("1. Вывести прочитанные")
			print("2. Вывести непрочитанные")

			select_category = int(input("Выберите пункт: "))
			book_num = 0

			# Прочитанные книги
			if select_category == 1:
				print("\nНиже прочитанные вами книги:")
				print("---------------------------")
				for i in range(0, len(THE_LIBRARY)):
					if THE_LIBRARY[i]['read']:
						book_num += 1
						book_info(book_num)
					sleep(0.5)
				print("---------------------------")

			# Непрочитанные книги
			elif select_category == 2:
				print("\nНиже НЕпрочитанные вами книги:")
				print("---------------------------")
				for i in range(0, len(THE_LIBRARY)):
					if THE_LIBRARY[i]['read'] == False:
						book_num += 1
						book_info(book_num)
					sleep(0.5)
				print("---------------------------")

	# Добавить книгу
	elif select_option == 2:
		name = str(input("Введите название новой книги: "))
		author = str(input("Автор новой книги: "))
		date_book = str(input("Дата выхода: "))
		read_status = int(input("Прочитано/Непрочитано? (1, 2): "))

		if read_status == 1:
			read_status = True
		else:
			read_status = False

		new_book = {"title" : name, "author" : author, "year" : date_book, "read" : read_status}

		THE_LIBRARY.append(new_book)
		print("\n📗 Книга успешно добавлена")
		sleep(1)

	# Изменить статус о прочтении
	elif select_option == 3:
		for i in range(0, len(THE_LIBRARY)):
			print(f"📔 Название: «{THE_LIBRARY[i]['title']}»")
			print(f"Прочитано: {('Нет 📕', 'Да 📗')[THE_LIBRARY[i]['read']]}\n")

		change_status = int(input("Выберите книгу для смены статуса: "))
		found_book = False

		print("---------------------------------")

		for j in range(0, len(THE_LIBRARY)):
			if change_status - 1 == j:
				found_book = True
				print(f"📔 Название: {THE_LIBRARY[j]['title']}")

				if THE_LIBRARY[j]['read']:
					THE_LIBRARY[j]['read'] = False
					print(f"\nСтатус: Непрочитано (Только что)")
					print("---------------------------------")
				elif THE_LIBRARY[j]['read'] == False:
					THE_LIBRARY[j]['read'] = True
					print(f"\nСтатус: Прочитано (Только что)")
					print("---------------------------------")

		print(('❌ Нет книги с таким №', '')[found_book])
		print("Примечание: Если книга была 'прочитана', статус изменится на 'Непрочитано' и наоборот.\n")

	# Удалить книгу
	elif select_option == 4:

		found_book = False

		try:
			delete_book = int(input("Введите № книги для удаления: "))
		except ValueError:
			print("❌ Ошибка. Вы ввели не цифры.")
			sleep(0.5)
			select_option = -1

		for i in range(0, len(THE_LIBRARY)):
			if delete_book - 1 == i:
				found_book = True
				print("Будет удалена следующая книга: \n")
				book_num = delete_book
				book_info(book_num)
				sleep(1)
				
				confirm = str(input("Удалить?(Y/N): ")).lower()
				
				if confirm == 'y':
					del THE_LIBRARY[i]
					print("Книга была удалена.")
					sleep(0.5)
				elif confirm == 'n':
					print("Операция прервана.")
					sleep(0.5)
				else:
					print("Вводите только Y или N.")
					sleep(0.5)

		print(('❌ Нет книги с таким №', '')[found_book])

	start()

	try:
		select_option = int(input("Выберите пункт: "))
	except ValueError:
		print("❌ Ошибка. Вы ввели не цифры.\n")
		select_option = -1
