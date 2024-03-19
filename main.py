import telebot
from telebot import types
from datetime import datetime, timedelta
from token_1 import token

bot = telebot.TeleBot(token)

day_names = {
    'Monday': 'Понедельник',
    'Tuesday': 'Вторник',
    'Wednesday': 'Среда',
    'Thursday': 'Четверг',
    'Friday': 'Пятница',
    'Saturday': 'Суббота',
    'Sunday': 'Воскресенье'

}
# Функция для определения четности и номера недели
def get_week_parity_and_number(start_date, target_date):
    days_from_start = (target_date - start_date).days
    start_weekday = start_date.weekday()
    start_week_start = start_date - timedelta(days=start_weekday)
    week_number = (days_from_start + start_weekday) // 7

    # Первая неделя всегда нечетная, даже если начало в середине недели
    week_parity = "нечетная" if (week_number % 2) == 0 else "четная"

    return week_parity, week_number + 1

# Функция для формирования расписания на день
def get_schedule(day_of_week, week_parity, week_number):
    if week_parity == "нечетная":
        schedule = {
            'Monday': {
                1: " - " if week_number in [1, 5, 9, 13, 17] else "Философия (ПР) ауд. А-234",
                2: " - " if week_number in [1, 5, 9, 13, 17] else "Философия (ПР) ауд. А-234",
                3: ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Tuesday': {
                1: 'Физические основы получения информации (ЛАБ) ауд. 188.2' if week_number in [5, 9, 13, 17] else " - ",
                2: 'Физические основы получения информации (ЛАБ) ауд. 188.2' if week_number in [5, 9, 13, 17] else " - ",
                3: ' - ' if week_number in [1, 3, 9, 13, 17] else 'Методы и средства цифровой обработки сигналов (ЛАБ) ауд. 112',
                4: ' - ' if week_number in [1, 3, 9, 13, 17] else 'Методы и средства цифровой обработки сигналов (ЛАБ) ауд. 112',
                5: ' - ',
                6: ' - '
            },
            'Wednesday': {
                1: 'Физические основы получения информации (ЛК) ауд. 110',
                2: ' - ',
                3: 'Теория вероятности и математическая статистика (ЛК) ауд. 326',
                4: 'Физическая культура и спорт (ПР)',
                5: ' - ',
                6: ' - '
            },
            'Thursday': {
                1: 'Методы и средства цифровой обработки сигналов (ЛК) ауд. 110',
                2: 'Методы и средства цифровой обработки сигналов (ПР) ауд. 188.1',
                3: ' - ',
                4: 'Методы и средства цифровой обработки сигналов (ПР) ауд. 188.1',
                5: 'Теория вероятности и математическая статистика (ПР) ауд. 415',
                6: ' - '
            },
            'Friday': {
                1: 'Физические основы получения информации (ЛК) ауд. 110',
                2: ' - ' if week_number == 17 else 'Физические основы получения информации (ПР) ауд. 188.3',
                3: 'Практика решения инженерных задач в приборостроении (ПР) ауд. 111',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Saturday': {
                1: ' - ',
                2: ' - ',
                3: 'Иностранный язык (ПР) ауд. И-320',
                4: 'Иностранный язык (ПР) ауд. И-320',
                5: ' - ',
                6: ' - '
            },
            'Sunday': {
            1: 'Выходной'
            }
        }
    else:
        schedule = {
            'Monday': {
                1: " - " if week_number in [4, 8, 12, 16] else 'Философия (ЛК) ауд. А-234',
                2: " - " if week_number in [4, 8, 12, 16] else 'Философия (ЛК) ауд. А-234',
                3: ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Tuesday': {
                1: "Цифровые измерительные приборы (ЛАБ) ауд. 188.3" if week_number in [10, 14] else ' - ',
                2: "Цифровые измерительные приборы (ЛАБ) ауд. 188.3" if week_number in [10, 14] else ' - ',
                3: ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Wednesday': {
                1: " - " if week_number == 17 else 'Цифровые измерительные приборы (ПР) ауд. 110',
                2: 'Цифровые измерительные приборы (ЛК) ауд. 188.3',
                3: 'Большие данные (ЛК) ауд. 330',
                4: 'Физическая культура и спорт (ПР)',
                5: ' - ',
                6: ' - '
            },
            'Thursday': {
                1: 'Компьютерные средства трёхмерного моделирования и конструирования приборов и систем (ЛК) ауд. 110',
                2: 'Компьютерные средства трёхмерного моделирования и конструирования приборов и систем (ПР) ауд. 111',
                3: 'Компьютерные средства трёхмерного моделирования и конструирования приборов и систем (ПР) ауд. 111',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Friday': {
                1: 'Большие данные (ПР) ауд. 246',
                2: "Практика решения инженерных задач в приборостроении (ПР) ауд. 111" if week_number in [4, 8, 12, 16] else ' - ',
                3: "Практика решения инженерных задач в приборостроении (ПР) ауд. 111" if week_number in [4, 8, 12, 16] else ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Saturday': {
                1: ' - ',
                2: 'Практика решения инженерных задач в приборостроении (ЛК) ауд. 110',
                3: ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Sunday': {
            1: 'Выходной'
            }
        }

    schedule_for_day = schedule[day_of_week]
    
    # Формирование текста расписания
    schedule_text = f'{day_names[day_of_week]} \nНеделя - {week_parity}, номер недели - {week_number}:'
    for lesson_number, lesson_description in schedule_for_day.items():
        schedule_text += f'\n{lesson_number}. {lesson_description}'

    return schedule_text


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton("Узнать расписание на сегодня")
    btn2 = types.KeyboardButton("Узнать расписание на завтра")
    btn3 = types.KeyboardButton("Узнать расписание на всю неделю")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, "Я бот для расписания БПБО-02-22 первой подгруппы. Так как нейросети МИРЭА не могут составить читаемое расписание этим займусь я. Нажав на кнопки ниже вы можете узнать расписание на сегодняшний день, либо на завтрашний, либо на всю неделю.", reply_markup=markup)

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Узнать расписание на сегодня':
        # Определение текущей даты
        target_date = datetime.now()

        # Определение текущего дня недели
        day_of_week = target_date.strftime('%A')

        # Определение четности и номера недели
        start_date = datetime(2024, 2, 9)  # Дата начала занятий
        week_parity, week_number = get_week_parity_and_number(start_date, target_date)

        # Формирование расписания на текущий день
        schedule_text = get_schedule(day_of_week, week_parity, week_number)

        # Отправка расписания пользователю
        bot.send_message(message.from_user.id, schedule_text, parse_mode='Markdown')
    elif message.text == 'Узнать расписание на всю неделю':
        # Определение текущей даты
        target_date = datetime.now()

        # Определение четности и номера недели
        start_date = datetime(2024, 2, 9)  # Дата начала занятий
        week_parity, week_number = get_week_parity_and_number(start_date, target_date)

        # Формирование расписания на всю неделю
        week_schedule_text = ''
        for day_of_week in day_names.keys():
            schedule_text = get_schedule(day_of_week, week_parity, week_number)
            week_schedule_text += f'\n\n{schedule_text}'

        # Отправка расписания пользователю
        bot.send_message(message.from_user.id, week_schedule_text, parse_mode='Markdown')

    elif message.text == 'Узнать расписание на завтра':
        # Определение текущей даты
        target_date = datetime.now()+ timedelta(days=1)

        # Определение текущего дня недели
        day_of_week = target_date.strftime('%A')

        # Определение четности и номера недели
        start_date = datetime(2024, 2, 9)  # Дата начала занятий
        week_parity, week_number = get_week_parity_and_number(start_date, target_date)

        # Формирование расписания на текущий день
        schedule_text = get_schedule(day_of_week, week_parity, week_number)

        # Отправка расписания пользователю
        bot.send_message(message.from_user.id, schedule_text, parse_mode='Markdown')

# Запуск бота
bot.polling(none_stop=True, interval=0)