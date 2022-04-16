class Book:

    def __init__(self, book_title, author, year):
        self.title = book_title
        self.author = author
        self.year = year
        self.quantity = 1


class Person:

    def __init__(self, name):
        self.name = name
        self.rent_book = 0
        self.books = {}


n = input()
books = {}
people = {}


def commands(command, title, author, year=None):
    def add(title, author, year):
        if title in books:
            books[title].quantity += 1
        else:
            books[title] = Book(title, author, year)
        return True

    def rent(name, title):
        if people[name].rent_book == 3:
            return False
        else:
            if title in books:
                if books[title].quantity >= 1 and title not in people[name].books:
                    people[name].rent_book += 1
                    books[title].quantity -= 1
                    people[name].books[title] = title
                    return True
            return False

    def donate(name, title):
        if name in people:
            if title in people[name].books:
                people[name].rent_book -= 1
                books[title].quantity += 1
                del people[name].books[title]
                return True
        return False

    if command == 'dodaj':
        return add(title, author, year)
    elif command == 'wypozycz':
        if title not in people:
            people[title] = Person(title)
        return rent(name=title, title=author)
    elif command == 'oddaj':
        return donate(name=title, title=author)


for i in range(int(n)):
    temp = eval(input())
    command = temp[0].strip()
    title = temp[1].strip()
    author = temp[2].strip()
    if len(temp) > 3:
        year = temp[3]
        print(commands(command, title, author, year))
    else:
        print(commands(command, title, author))
