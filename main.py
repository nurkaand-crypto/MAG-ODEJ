

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8543747397:AAHNT32JJh4K9Cv4_gGw5D071oVNB4Rg2YY"
bot = telebot.TeleBot(TOKEN)

users = {}

# ▶️ старт с кнопками
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()

    continue_btn = InlineKeyboardButton(
        "🛒 Продолжить заказ",
        callback_data="continue_order"
    )

    back_btn = InlineKeyboardButton(
        "🔙 Вернуться в магазин",
         url="http://127.0.0.1:5500/mag-odej/html.html"  # ← вставь сюда свой сайт или файл
    )

    markup.add(continue_btn)
    markup.add(back_btn)

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать!\n\nВыберите действие:",
        reply_markup=markup
    )

# ▶️ нажали "продолжить"
@bot.callback_query_handler(func=lambda call: call.data == "continue_order")
def continue_order(call):
    msg = bot.send_message(call.message.chat.id, "Введите ваше имя:")
    bot.register_next_step_handler(msg, get_name)

# 📌 имя
def get_name(message):
    users[message.chat.id] = {}
    users[message.chat.id]['name'] = message.text

    msg = bot.send_message(message.chat.id, "📱 Введите номер телефона:")
    bot.register_next_step_handler(msg, get_phone)

# 📌 телефон
def get_phone(message):
    if message.chat.id not in users:
        bot.send_message(message.chat.id, "⚠️ Нажмите /start")
        return

    users[message.chat.id]['phone'] = message.text

    name = users[message.chat.id]['name']
    phone = users[message.chat.id]['phone']

    bot.send_message(
        message.chat.id,
        f"✅ Заказ успешно отправлен!\n\n👤 Имя: {name}\n📱 Телефон: {phone}"
    )

    # 🔁 после заказа снова кнопки
    start(message)

# 🚀 запуск
bot.polling(none_stop=True)