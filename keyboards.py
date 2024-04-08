from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types

button_names = ["кнопка1", "кнопка2", "кнопка3", "кнопка4", "кнопка5", "кнопка6"]

def StartKeyboard():
	builder = ReplyKeyboardBuilder()
	for i in button_names:
		builder.add(types.KeyboardButton(text=i))
	builder.adjust(3)
	return builder.as_markup(resize_keyboard=True)