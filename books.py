books = []

def menu(books):
	for num, option in enumerate(books):
		num += 1
		print(f"{num}.{option}")
	print("\nЧто будете делать?\n")
	options =["Чтобы добавить книгу нажмите",
	"Чтобы удалить книгу нажмите",
	"Чтобы найти книгу"]
	option = choose_option(options)
	if option == 1:
		name = input("\nВведите название книги: ")
		author = input("Введите автора книги: ")
		year = input("Введите год написания книги: ")
		add_book(name, author, year)
		return menu(books)
	if option == 2:
		print("Какую книгу желаете удалить?")
		option = choose_option(books)
		option -= 1
		books.pop(option)
		return menu(books)
	if option == 3:
		pass

def add_book(name: str, author: str, year: int) -> dict:
	book = {
	"название": name,
	"автор": author,
	"год": year 
	}
	books.append(book)


def choose_option(options: list) -> int:
	for num, option in enumerate(options):
		num += 1
		print(f"{num}.{option}")
	option = input("\nВведите номер варианта и нажмите ENTER: ")
	try:
		option = int(option)
	except ValueError:
		print("\nВвод дожен быть целым не отрицательным числом")
		return choose_option(options)
	else:
		if option <= len(options) and option > 0:
			return option
		else:
			print("Нет такого выбора")
			return choose_option(options)

menu(books)