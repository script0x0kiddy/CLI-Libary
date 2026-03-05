# Beta v0.2

from time import sleep

print("\n         📚 Моя Библиотека\n")
print("1. Вывести информацию о книгах (> 1)")
print("2. Добавить книгу (> 1)")
print("3. Изменить статус прочтения")
print("4. Удалить книгу (> 1)")
print("5. Выйти из Библиотеки")
print("-------------------------------------\n")
print("Примечание: (> 1) означает что есть под-варианты для выполнения точного действия\n")

books = [{"title" : "Бусидо",
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
	select_main = int(input("Выберите пункт: "))
except ValueError:
	print('❌ Неверно. Вводите только цифры.')
	select_main = 0

# Выйти из Библиотеки 
while select_main != 5:

	# Вывести информацию о книгах
	if select_main == 1:
		print("1. Вывести все книги")
		print("2. Фильтровать по авторам")
		print("3. Фильтровать по статусу прочтения")
		print("-------------------------------------")

		select_second = int(input("Выберите пункт: "))
		count = 0


		# Вывести все книги
		if select_second == 1:
			for i in range(0, len(books)):
				count += 1
				print(f"\n📔 Информация о книге №{count}:")
				print()
				print(f"Название: {books[i]['title']}")
				print(f"Автор: {books[i]['author']}")
				print(f"Год: {books[i]['year']}")

				if books[i]['read'] == True:
					print(f"Статус: Прочитано 📗\n")
				else:
					print(f"Статус: Непрочитано 📕\n")
				sleep(1)
			sleep(1)

		# Фильтровать по авторам
		elif select_second == 2:
			
			author_info = str(input("Введите Имя и Фамилию автора: ")).title()
			count = 0
			
			for i in range(0, len(books)):
				if author_info in books[i]['author'].title():
					select_author = books[i]

			print(f"Книги автора: {select_author['author']}")
			print("-----------------------------------")

			for i in range(0, len(books)):
				if select_author['author'] in books[i]['author']:
					count += 1
					print(f"\n📔 Информация о книге №{count}:")
					print()
					print(f"Название: {books[i]['title']}")
					print(f"Автор: {books[i]['author']}")
					print(f"Год: {books[i]['year']}")
					print(f"Прочитано: {books[i]['read']}")
					sleep(1)
			print("\n-----------------------------------")


		# Фильтровать по статусу прочтения
		elif select_second == 3:
			print("1. Вывести прочитанные")
			print("2. Вывести непрочитанные")

			select_filter = int(input("Выберите пункт: "))
			count = 0

			# Прочитанные книги
			if select_filter == 1:
				print("\nНиже прочитанные вами книги:")
				print("---------------------------")
				for i in range(0, len(books)):
					if books[i]['read'] == True:
						count += 1
						print(f"📔 Информация о книге №{count}:")
						print()
						print(f"Название: {books[i]['title']}")
						print(f"Автор: {books[i]['author']}")
						print(f"Год: {books[i]['year']}")
						print(f"Прочитано: {books[i]['read']}\n")
					sleep(1)
				print("---------------------------")

			# Непрочитанные книги
			elif select_filter == 2:
				print("\nНиже НЕпрочитанные вами книги:")
				print("---------------------------")
				for i in range(0, len(books)):
					if books[i]['read'] == False:
						count += 1
						print(f"📔 Информация о книге №{count}:")
						print()
						print(f"Название: {books[i]['title']}")
						print(f"Автор: {books[i]['author']}")
						print(f"Год: {books[i]['year']}")
						print(f"Прочитано: {books[i]['read']}\n")
					sleep(1)
				print("---------------------------")

	# Добавить книгу
	elif select_main == 2:
		new_book_name = str(input("Введите название новой книги: "))
		new_book_author = str(input("Автор новой книги: "))
		new_book_year = str(input("Дата выхода: "))
		new_book_read = int(input("Прочитано/Непрочитано? (1, 2): "))

		if new_book_read == 1:
			new_book_read = True
		else:
			new_book_read = False

		new_book = {"title" : new_book_name, "author" : new_book_author, "year" : new_book_year, "read" : new_book_read}

		books.append(new_book)
		print("\n📗 Книга успешно добавлена")
		sleep(1)

	# Изменить статус о прочтении
	elif select_main == 3:
		print("\n")
		for i in range(0, len(books)):
			print(f"📔 Название: «{books[i]['title']}»")
			if books[i]['read'] == True:
				print(f"Статус: Прочитано 📗\n")
			else:
				print(f"Статус: Непрочитано 📕\n")
			sleep(1)
		select_book = int(input("Выберите книгу для смены статуса: "))
		print("---------------------------------")

		for j in range(0, len(books)):
			if select_book - 1 == j:
				print(f"📔 Название: {books[j]['title']}")
				
				if books[j]['read'] == True:
					books[j]['read'] = False
					print(f"\nСтатус: Непрочитано (Только что)")
					print("---------------------------------")
					sleep(1)
				elif books[j]['read'] == False:
					books[j]['read'] = True
					print(f"\nСтатус: Прочитано (Только что)")
					print("---------------------------------")
					sleep(1)

		print("Примечание: Если книга была 'прочитана', статус изменится на 'Непрочитано' и наоборот.\n")

	# Удалить книгу
	elif select_main == 4:
		try:
			del_book = int(input("Введите № книги для удаления: "))
			for book in range(0, len(books)):
				if del_book - 1 == book:

					print("Будет удалена следующая книга: \n")
					print(f"📔 Информация о книге №{book + 1}:\n")
					sleep(1)
					print(f"Название: {books[book]['title']}")
					print(f"Автор: {books[book]['author']}")
					print(f"Год: {books[book]['year']}")
					print(f"Прочитано: {books[book]['read']}\n")
					sleep(1)

					confirm = str(input("Удалить?(Y/N): ")).lower()

					if confirm == 'y':
						del books[book]
						sleep(1)
						print("Книга была удалена.")
						sleep(1)
					elif confirm == 'n':
						print("Операция прервана.")
						sleep(1)
					else:
						print("Вводите только Y или N.")
						sleep(1)

		except ValueError:
			print("❌ Ошибка. Вы ввели не цифры.")
			sleep(1)

	print("\n         📚 Моя Библиотека\n")
	print("1. Вывести информацию о книгах (> 1)")
	print("2. Добавить книгу (> 1)")
	print("3. Изменить статус прочтения")
	print("4. Удалить книгу (> 1)")
	print("5. Выйти из Библиотеки")
	print("-------------------------------------\n")

	try:
		select_main = int(input("Выберите пункт: "))
	except ValueError:
		print("❌ Ошибка. Вы ввели не цифры.\n")
		select_main = 0
