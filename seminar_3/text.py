"""В большой текстовой строке text подсчитать количество встречаемых
слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр
символов. Слова разделяются пробелами. Такие слова как don t, it s,
didn t итд (после того, как убрали знак препинания апостроф) считать
двумя словами. Цифры за слова не считаем. Отсортируйте по убыванию
значения количества повторяющихся слов. Слова выведите в обратном
алфавитном порядке."""
import re

text: str = "The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!"

text: list[str] = re.sub(r'[,.!?;:"()0-9-]', '',
                         text.replace("'", " ")).lower().split()

result: dict[str, int] = {}
for word in text:
    result[word] = result.setdefault(word, 0) + 1
print(sorted(result.items(), key=lambda item: item[::-1], reverse=True)[:10])
