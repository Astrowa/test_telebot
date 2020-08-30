import pyowm
import telebot
import test_telebot.test_telebot.basedate as basedate
from telebot import types



owm = pyowm.OWM('599a020b0f5dd1fbda37da885fd05d09', language = "ru")
bot = telebot.TeleBot("1222661818:AAGegQC8g16wOeXX2mFV4ooEddDoXEISb0c")#надо не забывать менять на фейк



@bot.message_handler(commands=['start'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(row_width=2)
	itembtn1 = types.KeyboardButton('Привет')
	itembtn2 = types.KeyboardButton('Илюха')
	itembtn3 = types.KeyboardButton('Погода')
	itembtn4 = types.KeyboardButton('Стикер')
	markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
	bot.send_message(message.chat.id, "Выбери один из вариантов снизу:", reply_markup=markup)
	#написать нормальный туториал и подсказку /start


@bot.message_handler(content_types=['text'])
def send_simpe_echo(message):
	if message.text.lower() == "привет":
		return bot.send_message(message.chat.id, ('Привет, ' + message.from_user.first_name))#мложно что-нибудь сюда например подсказку или туториал
	elif message.text.lower() == 'илюха':
		bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAICG18S7-vvhHJDomG6xgZKBp47t9F9AALyAAP0exkAATs4WmUkIehgGgQ')#возможно стоит убрать
	elif message.text == 'Погода':
		markup1 = types.ReplyKeyboardMarkup(row_width=2)
		itembtn4 = types.KeyboardButton('Выход')
		# itembtn5 = types.KeyboardButton('Выход')
		markup1.add(itembtn4)
		send = bot.send_message(message.chat.id, 'Введите название города', reply_markup=markup1)
		bot.register_next_step_handler(send, send_weather)
	elif message.text.lower() == 'стикер':
		keks = basedate.random_sticker()
		print(keks)
		print(type(keks))
		bot.send_sticker(message.chat.id, keks[0])



def send_weather(message):
	if message.text == 'Выход':
		welcome(message)
	else:
		if message.content_type == 'text':
			try:
				print(message)
				print(message.content_type)
				observation = owm.weather_at_place(message.text)
				w = observation.get_weather()
				print(w)
				temp = w.get_temperature('celsius')["temp"]
				cous = observation.get_location()
				print(cous)
				LATITUDE = cous.get_lat()  # получилось достать lat
				LONGITUDE = cous.get_lon()
				print(LATITUDE)
				print(LONGITUDE)
				print(message.chat.id)
				bot.send_location(message.chat.id, LATITUDE, LONGITUDE)
				# bot.send_location(message.chat_id, cous.lat, cous.lon)
				# как-то вытащить lat и lon с cous - это координаты на геометку

				answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
				answer += "Температура: " + str(temp) + "\n\n"

				bot.send_message(message.chat.id, answer)
				welcome(message)
			except:
				send = bot.send_message(message.chat.id, 'Напиши название города правильно')
				bot.register_next_step_handler(send, send_weather)
		elif message.content_type == 'location':
			send_location(message)



@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
	bd_list_all = basedate.read_sql()
	print(message)#нужно читать БД только при запуске, а не каждый раз при добавлении
	print(type(message))#возможно стоило объявить список глобальным
	update_table = message.sticker.file_id#похоже нужно ещё брать уникальный код файла
	unique_id = message.json['sticker']['thumb']['file_unique_id']
	print('Уникальный', unique_id)
	t = [[update_table, unique_id]]
	print(update_table)
	print(t)
	print(type(t))
	print(bd_list_all)
	print('fgfg', type(bd_list_all))
	print(len(bd_list_all))
	check = 0
	for i in range(len(bd_list_all)):
		if bd_list_all[i][1] == unique_id:#file_unique_id всегда одинаковый, а sticker.file_id разный
			check += 1
	if check == 1:
		print('Такой стикер уже есть')
	else:
		basedate.sql_function(t)
	#нужно замутить БД с id стикеров, чтобы потом из неё выбирать рандомный



@bot.message_handler(content_types=['location'])
def send_location(message):
	print(message)
	print(message.location)
	#location_name = message.location.name
	LONGITUDE_USER = message.location.longitude
	LATITUDE_USER = message.location.latitude
	print(LONGITUDE_USER)
	print(LATITUDE_USER)
	wether_place = owm.weather_at_coords(LATITUDE_USER, LONGITUDE_USER)
	weat = wether_place.get_weather()
	print(weat)
	temps = weat.get_temperature('celsius')["temp"]
	print(temps)
	answerer = "Сейчас " + weat.get_detailed_status() + "\n"
	answerer += "Температура: " + str(temps) + "\n\n"
	bot.send_message(message.chat.id, answerer)
	#нужно перенести исполнение после нажатия на кнопку погода

#подсказку на неопознаные команды


bot.polling( none_stop = True)

"""import random

print(random.__all__)"""