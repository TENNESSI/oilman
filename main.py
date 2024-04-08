from auth import token
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from keyboards import StartKeyboard
from aiogram.enums import ParseMode
import json
from aiogram import F
import loguru

bot = Bot(token=token, parse_mode = "HTML")

dp = Dispatcher()

def getmsg_meta(case):
	return f"zaglushka ({case})"

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
	await message.answer("потыкай на кнопки", reply_markup=StartKeyboard())

@dp.message()
async def echo(message: types.Message):
	await message.answer(message.text, reply_markup=StartKeyboard())

@dp.message(F.text.lower() == "кнопка1")
async def send_meta(message: types.Message):
	await message.answer(getmsg_meta("кнопка1"))

@dp.message(F.text.lower() == "кнопка2")
async def send_meta(message: types.Message):
	await message.answer(getmsg_meta("кнопка2"))

@dp.message(F.text.lower() == "кнопка3")
async def send_meta(message: types.Message):
	await message.answer(getmsg_meta("кнопка3"))

@dp.message(F.text.lower() == "кнопка4")
async def send_meta(message: types.Message):
	await message.answer(getmsg_meta("кнопка4"))


@dp.message(F.text.lower() == "кнопка5")
async def send_meta(message: types.Message):
	await message.answer(getmsg_meta("кнопка5"))


@dp.message(F.text.lower() == "кнопка6")
async def send_meta(message: types.Message):
	await message.answer(getmsg_meta("кнопка6"))

async def main():
	await dp.start_polling(bot)

if __name__ == '__main__':
	asyncio.run(main())

# emoji="🎲"