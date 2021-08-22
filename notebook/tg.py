from aiogram import Bot, Dispatcher, types, executor

import buttons as kb



bot = Bot('1602089269:AAG9_6ayv-RldHq7_DDBL3ZxYNUt-vZetfQ')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def on_message(message: types.Message):
    await bot.send_message(message.from_user.id, "Рассписание на ... :",
    	reply_markup = kb.alldays)




@dp.message_handler(text = ['Понедельник'])
async def on_message(message : types.Message):
    await bot.send_message(message.from_user.id,"Понедельник :\n 6) Физ-ра\n7) Математика\n8) История\n9) География\n10) Русский язык\n11) Англ.яз (1-ая группа)")

@dp.message_handler(text = ['Вторник'])
async def on_message(message : types.Message):
	await bot.send_message(message.from_user.id,"Вторник : \n 6) Информатика (1-ая группа)/Узб.яз(2-ая группа)\n7) Ботаника\n8) Узб.яз(1-ая группа)/Англ.яз(2-ая группа)\n9) Литература\n10) Математика\n11) Технология\n12) Технология")
	
@dp.message_handler(text = ['Среда'])
async def on_message(message : types.Message):
	await bot.send_message(message.from_user.id,"Среда : \n7) Русский язык\n8) Узбекский язык\n9) История\n10) Математика\n11) Английский язык(1 и 2 группа)")

@dp.message_handler(text = ['Четверг'])
async def on_message(message : types.Message):
	await bot.send_message(message.from_user.id,"Четверг : \n6) Физ-ра\n7) Узб.яз(1-ая группа)/Англ.яз(2-ая группа)\n8) Русский язык\n9) Математика\n10) Музыка")

@dp.message_handler(text = ['Пятница'])
async def on_message(message : types.Message):
	await bot.send_message(message.from_user.id,"Пятница : \n7) Информатика (2-ая группа)\n8) Литература\n9) Математика\n10) Англ.яз(1-ая группа)/Узб.яз(2-ая группа)\n11) Воспитание")

@dp.message_handler()
async def on_message(message : types.Message):
    await bot.send_message(message.from_user.id,"Выберите из предложенного или введите название дня недели")


help_message = ("""
    Доступные команды:,\n
	/start - приветствие,
	/stop - прощание,
	"""
)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)






if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True )

