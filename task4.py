text = input("Введите строку: ")
word = input("Введите слово для поиска: ")

words = text.split()

if word in words:
    print("Слово найдено в строке.")
else:
    print("Слово не найдено.")