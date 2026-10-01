text = input("Введите строку: ")
separator = input("Введите знак-разделитель: ")

words = text.split(separator)

# Убираем пробелы и пустые элементы
words = [word.strip() for word in words if word.strip()]

if words:
    shortest = min(words, key=len)
    print("Самое короткое слово:", shortest)
    print("Количество букв:", len(shortest))
else:
    print("Слова не найдены.")