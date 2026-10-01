text = input("Введите строку: ")

words = text.split()

if words:
    longest = max(words, key=len)
    print("Самое длинное слово:", longest)
    print("Количество букв:", len(longest))
else:
    print("Строка пустая.")