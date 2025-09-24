import csv
library = {
    "Война и мир": {
        "author": "Л. Толстой",
        "year": 1869,
        "ratings": [5, 4, 5]
    },
    "Преступление и наказание": {
        "author": "Ф. Достоевский",
        "year": 1866,
        "ratings": [5, 5, 4]
    }
}

maxRating = 5
csvFilename = "library.csv"

def addBook():
    print("\n--- Добавить книгу ---")
    nameBook = input('Введите название книги: ').strip()
    if not nameBook:
        print('Название не может быть пустым')
        return
    if nameBook in library:
        print('Книга с таким названием уже есть в библиотеке')
        return

    author = input('Введите имя автора').strip()
    if not author:
        print('Имя автора не может быть пустым')
        return
    year = None
    if year is None:
        try:
            yearStr = input('Введите год выпуска книги').strip()
            yearStr = int(yearStr)
            if yearStr < 0 or yearStr > 2025:
                print(f"Книга не могла быть написана в {yearStr} году")
                year = None
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите год числом.")
    ratings = []
    while True:
        ratingStr = input('Введите рейтинг.(максимальное значение рейтинга 5.0, или оставьте пустым для завершения):').strip()
        if not ratingStr:
            break
        try:
            rating = int(ratingStr)
            if 1 <= rating <= maxRating:
                ratings.append(rating)
            else:
                print(f'Оценка должна быть от 1 до {maxRating}')
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите оценку числом.")
    library[nameBook] = {
        "author": author,
        "year": year,
        "ratings": ratings
    }
    print(f'Книга {nameBook} успешно добавлена')
def showAllBooks():
    print("\n--- Все книги в библиотеке ---")
    print(library)
    if not library:
        print('Ваша библиотека пуста, но вы можете добавить в нее книги нажав цифру 1')
        return
def findBookByName():
    print("\n--- Найти книгу по названию ---")
    searchName = input('Введите название книги которую вы хотите найти')
    if not searchName:
        print("Название книги для поиска не может быть пустым.")
        return

    found = False
    for nameBook, bookData in library.items():
        if  searchName.lower() in nameBook.lower():
            avgRating = sum(bookData["ratings"]) / len(bookData["ratings"]) if bookData["ratings"] else "нет оценок"
            print(
                f"Найдена книга: Название: {nameBook}, Автор: {bookData['author']}, Год: {bookData['year']}, Средняя оценка: {avgRating:.2f}" if
                bookData[
                    "ratings"] else f"Найдена книга: Название: {nameBook}, Автор: {bookData['author']}, Год: {bookData['year']}, Средняя оценка: нет оценок")
            found = True
            break
    else:
        print(f"Книга с названием '{searchName}' не найдена.")
def deleteBook():
    print("\n--- Удалить книгу ---")
    deleteNameBook = input('Введите название книги которую хотите удалить').strip()
    if not deleteNameBook:
        print('Название для удаления не может быть пустым')
        return
    if deleteNameBook in library:
        del library[deleteNameBook]
        print(f"Книга с названием {deleteNameBook} удалена из вашей библиотеки")
    else:
        print(f"Книги с названием {deleteNameBook}не существует")
def addRatingToBook():
    print("\n --- Добавить новую оценку книге ---")
    title = input("Введите название книги, к которой хотите добавить оценку: ").strip()
    if not title:
        print('Название книги не может быть пустым')
        return
    if title not in library:
        print(f'Книги с названием {title} нет в библиотеке')
        return
    while True:
        ratingStr = input(f"Введите новую оценку книги (от 1 до {maxRating}, или оставьте пустым для завершения): ").strip()
        if not ratingStr:
            break
        try:
            rating = int(ratingStr)
            if 1 <= rating <= maxRating:
                library[title]["ratings"].append(rating)
                print(f"Оценка {rating} успешно добавлена к книге '{title}'.")
            else:
                print(f"Оценка должна быть в диапазоне от 1 до {maxRating}.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите оценку числом.")
def showBooksAfterYear():
    print("\n--- Книги, выпущенные после определённого года ---")
    yearFilter = None
    while yearFilter is None:
        try:
            yearStr = input("Введите год, после которого вы хотите увидеть книги: ").strip()
            yearFilter = int(yearStr)
            if yearFilter <= 0:
                print("Год должен быть положительным числом.")
                yearFilter = None
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите год числом.")

    print(f"\nКниги, выпущенные после {yearFilter} года:")
    foundBooks = []
    for title, bookData in library.items():
        if bookData["year"] > yearFilter:
            foundBooks.append((title, bookData))

    if not foundBooks:
        print("Книг, выпущенных после указанного года, не найдено.")
    else:
        # Сортировка по году издания
        sortedBooks = sorted(foundBooks, key=lambda item: item[1]["year"])
        for title, bookData in sortedBooks:
            avgRating = sum(bookData["ratings"]) / len(bookData["ratings"]) if bookData["ratings"] else "нет оценок"
            print(f"Название: {title}, Автор: {bookData['author']}, Год: {bookData['year']}, Средняя оценка: {avgRating:.2f}" if bookData["ratings"] else f"Название: {title}, Автор: {bookData['author']}, Год: {bookData['year']}, Средняя оценка: нет оценок")
def showBooksAboveRatingThreshold():
    print("\n--- Книги с рейтингом выше определённого порога ---")
    ratingThreShold = None
    while ratingThreShold is None:
        try:
            ratingStr = input(f"Введите минимальный средний рейтинг (от 1 до {maxRating}): ").strip()
            ratingThreShold = float(ratingStr)
            if not (1 <= ratingThreShold <= maxRating):
                print(f"Рейтинг должен быть в диапазоне от 1 до {maxRating}.")
                ratingThreShold = None
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите рейтинг числом.")

    print(f"\nКниги со средним рейтингом выше {ratingThreShold:.2f}:")
    foundBooks = []
    for title, bookData in library.items():
        if bookData["ratings"]:
            avgRating = sum(bookData["ratings"]) / len(bookData["ratings"])
            if avgRating > ratingThreShold:
                foundBooks.append((title, bookData, avgRating))

    if not foundBooks:
        print("Книг с рейтингом выше указанного порога не найдено.")
    else:
        sortedBooks = sorted(foundBooks, key=lambda item: item[2], reverse=True)
        for title, bookData, avgRating in sortedBooks:
            print(f"Название: {title}, Автор: {bookData['author']}, Год: {bookData['year']}, Средняя оценка: {avgRating:.2f}")
def exportBooksToCsv():

    print("\n--- Экспорт книг в CSV ---")
    try:
        with open(csvFilename, 'w', newline='', encoding='utf-8') as csvFile:
            fieldnames = ['title', 'author', 'year', 'ratings']
            writer = csv.DictWriter(csvFile, fieldnames=fieldnames, delimiter=';')

            writer.writeheader()
            for title, bookData in library.items():
                writer.writerow({
                    'title': title,
                    'author': bookData['author'],
                    'year': bookData['year'],
                    'ratings': ",".join(map(str, bookData['ratings'])) # Оценки сохраняем как строку через запятую
                })
        print(f"Данные успешно экспортированы в файл '{csvFilename}'.")
    except IOError as e:
        print(f"Ошибка ввода-вывода при экспорте в CSV: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка при экспорте в CSV: {e}")
    finally:
        print("Завершение операции экспорта.")
def importBooksFromCsv():
    print("\n--- Импорт книг из CSV ---")
    try:
        with open(csvFilename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            tempLibrary = {}
            for row in reader:
                title = row.get('title')
                author = row.get('author')
                yearStr = row.get('year')
                ratingsStr = row.get('ratings')

                if not all([title, author, yearStr, ratingsStr is not None]):
                    print(f"Пропущена некорректная строка: {row}")
                    continue

                try:
                    year = int(yearStr)
                    if year <= 0:
                        print(f"Пропущена строка с некорректным годом: {row}")
                        continue

                    ratings = [int(r) for r in ratingsStr.split(',') if r.strip()]
                    if not all(1 <= r <= maxRating for r in ratings):
                        print(f"Пропущена строка с некорректными оценками: {row}")
                        continue

                    if title in library:
                        print(f"Внимание: книга '{title}' уже существует и будет перезаписана.")

                    tempLibrary[title] = {
                        "author": author,
                        "year": year,
                        "ratings": ratings
                    }
                except ValueError:
                    print(f"Пропущена строка с некорректными числовыми данными: {row}")
                except Exception as e:
                    print(f"Непредвиденная ошибка при обработке строки {row}: {e}")
            library.update(tempLibrary)
            print(f"Данные успешно импортированы из файла '{csvFilename}'.")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{csvFilename}' не найден. Пожалуйста, сначала экспортируйте данные.")
    except IOError as e:
        print(f"Ошибка ввода-вывода при импорте из CSV: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка при импорте из CSV: {e}")
    finally:
        print("Завершение операции импорта.")





def displayMenu():
    print("\n--- Меню библиотеки ---")
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Найти книгу по названию")
    print("4. Удалить книгу")
    print("5. Добавить новую оценку книге")
    print("6. Вывести книги, выпущенные после определённого года")
    print("7. Показать книги с рейтингом выше определённого порога")
    print("8. Экспортировать книги в CSV")
    print("9. Импортировать книги из CSV")
    print("10. Выход")

def main():
    while True:
        displayMenu()
        choice = input("Выберите действие (введите номер): ").strip()

        if choice == '1':
            addBook()
        elif choice == '2':
            showAllBooks()
        elif choice == '3':
            findBookByName()
        elif choice == '4':
            deleteBook()
        elif choice == '5':
            addRatingToBook()
        elif choice == '6':
            showBooksAfterYear()
        elif choice == '7':
            showBooksAboveRatingThreshold()
        elif choice == '8':
            exportBooksToCsv()
        elif choice == '9':
            importBooksFromCsv()
        elif choice == '10':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите число от 1 до 10.")


if __name__ == "__main__":
    main()
