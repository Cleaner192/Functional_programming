import nltk

from collections import Counter 

# Считываем текст из файла
with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Приводим текст к нижнему регистру и разбиваем его на слова
words = nltk.word_tokenize(text.lower())

# Удаляем стоп-слова
stop_words = set(nltk.corpus.stopwords.words('russian'))
filtered_words = [word for word in words if word not in stop_words]

# Подсчитываем количество уникальных слов и вхождений каждого слова
WordСounts = Counter(filtered_words)

# Составляем список самых часто встречающихся слов
MostWords = WordСounts.most_common(10)

# Выводим результаты на экран
print(f'Количество уникальных слов: {len(WordСounts)}')
print('Самые часто встречающиеся слова:')
for word, count in MostWords:
    print(f'{word}: {count}')
