



from aiogram.types import ReplyKeyboardMarkup, \
    KeyboardButton



btnHello = KeyboardButton('Привет! 👋')


greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnHello)

day1 = KeyboardButton('Понедельник')
day2 = KeyboardButton('Вторник')
day3 = KeyboardButton('Среда')
day4 = KeyboardButton('Четверг')
day5 = KeyboardButton('Пятница')

alldays = ReplyKeyboardMarkup().add(day1).add(day2).add(day3).add(day4).add(day5)

