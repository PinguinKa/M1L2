import telebot
    # Инициализация бота с использованием его токена
bot = telebot.TeleBot("ТУТ СЕКРЕТНЫЙ ТОКЕН")

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Запуск бота
bot.polling()
