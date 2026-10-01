text = input("Введите слова через ; : ")

words = text.split(";")

# Убираем лишние пробелы
words = [word.strip() for word in words if word.strip()]

if words:
    longest = max(words, key=len)
    print("Самое длинное слово:", longest)
    print("Количество букв:", len(longest))
else:
    print("Слова не введены.")