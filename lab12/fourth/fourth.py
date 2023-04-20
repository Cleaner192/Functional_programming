import datetime

# Считываем содержимое файла с датами
with open('dates.txt', 'r') as file:
    dates = file.readlines()

# Преобразуем каждую дату в объект datetime
dates = [datetime.datetime.strptime(date.strip(), '%Y-%m-%d') for date in dates]

# Вычисляем разницу между каждой датой и текущей датой
now = datetime.datetime.now()
DaysSinceDates = [(now - date).days for date in dates]

# Сортируем список дат по количеству дней между каждой датой и текущей датой
SortedDate = [date for _, date in sorted(zip(DaysSinceDates, dates))]

# Выводим отсортированный список дат
print("Разница между каждой датой и текущей датой (в днях и минутах):")
for days, date in zip(DaysSinceDates, SortedDate):
    minutes = (datetime.datetime.now() - date).total_seconds() // 60
    print(f"{date.strftime('%Y-%m-%d')}: {days} дней, {minutes} минут")

