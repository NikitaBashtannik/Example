import re
import string
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
#Открываем файл с помощью встроенной функции open, указываем режим чтения и кодировку. 
#Читаем всё содержимое файла, в результате получаем строку text:
f = open('pushkin-metel.txt', "r", encoding="utf-8")
text = f.read()
type(text)
#получаем длину текста
len(text)
text[:300]
# перевод в единый регистр (например, нижний)
text = text.lower()
#string.punctuation представляет собой строку. Набор специальных символов, 
# которые будут удалены
string.punctuation
type(string.punctuation)
spec_chars = string.punctuation + '\n\xa0«»\t—…' 
#Для удаления символов используем поэлементную обработку строки 
text = "".join([ch for ch in text if ch not in spec_chars])
text = re.sub('\n', '', text)
#Можно объявить простую функцию, которая удаляет указанный набор символов из исходного текста:
def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])
#Её можно использовать как для удаления спец.символов, так и для удаления цифр из исходного текста:
text = remove_chars_from_text(text, spec_chars)
text = remove_chars_from_text(text, string.digits)
#Для последующей обработки очищенный текст необходимо разбить на составные части — токены
text_tokens = word_tokenize(text)
text_tokens[:10]
#Для применения инструментов частотного анализа библиотеки NLTK необходимо список токенов преобразовать к классу Text, который входит в эту библиотеку:
text = nltk.Text(text_tokens)
text[:10]
#Для подсчёта статистики распределения частот слов в тексте применяется класс FreqDist (frequency distributions):
fdist = FreqDist(text)
with open("result.txt","w") as file:
    #most_common для получения списка кортежей с наиболее часто встречающимися токенами
    file.write(fdist.most_common(5))