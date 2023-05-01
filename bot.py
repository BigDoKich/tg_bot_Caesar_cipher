import telebot
import config
import mydef

from requests.exceptions import ReadTimeout
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	#keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item1 = types.KeyboardButton(text="Шифровать")
	item2 = types.KeyboardButton(text="Расшифровать")
	#adding keys
	markup.add(item1, item2)
	#First message
	mess = f"Приветствую, {message.from_user.first_name}!\nЯ - Шифр Цезаря, бот созданный для шифрования/расшифрования текста.\nПо умолчанию сдвиг алфавита стоит 1, но если хотите другой, то напишите число сдвига в конце шифруемого/расшифруемого сообщения."
	bot.send_message(message.chat.id, mess, reply_markup = markup)
	mess = "Чтобы начать, нажмите на кнопку того, что вы хотите сделать с сообщением."
	bot.send_message(message.chat.id, mess, reply_markup = markup)

flag = 0

@bot.message_handler(content_types=['text'])
def ROT1(message):
	global flag
	text = message.text
	#Default step 1
	step = 1
	#Checking for a number for a step
	for i in text:
		if(i.isdigit()):
			step = i
			break
	if flag == 1:
		bot.send_message(message.chat.id, mydef.encrypt_rot1(text, int(step)))
		flag = 0
	elif flag == 2:
		bot.send_message(message.chat.id, mydef.decrypt_rot1(text, int(step)))
		flag = 0
	elif text == 'Шифровать':
		flag = 1
		bot.send_message(message.chat.id, "Введите сообщение, которое нужно зашифровать.")
	elif message.text == 'Расшифровать':
		flag = 2
		bot.send_message(message.chat.id, "Введите сообщение, которое нужно расшифровать.")
# RUN
try:
	bot.polling(none_stop=True)
except ReadTimeout:
	pass

