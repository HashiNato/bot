from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.inline import first
from states import States_w, States_clear
import random


making_list = []
@dp.message_handler(commands='making')
async def bot(message: types.Message):
    await States_w.States_run.set()
    await message.answer("Введіть дату дня (від 1 до 28-31) в який "
                         "ви хочете піти на фільм?.")

@dp.message_handler(state=States_w.States_run)
async def bot(message: types.Message):
    await States_w.States_day.set()
    making_list.append(message.text)
    await message.answer(f'{making_list[0]} числа - чудовий вибір! '
                         f'Напишіть час в який вамбуде зручно прийти?.')

@dp.message_handler(state=States_w.States_day)
async def bot(message: types.Message):
    await States_w.States_time.set()
    making_list.append(message.text)
    await message.answer(f'Ви хочете забронювати місце на {making_list[0]} '
                         f'вересня о {making_list[1]}.Чи підтверджуєте ви цю дату?(Так/Ні)')

@dp.message_handler(state=States_w.States_time)
async def bot(message: types.Message):
    await States_w.States_seats.set()
    making_list.append(message.text)
    await message.answer("Виберіть собі ряд (A-H) і місце (1-15)")

##
        await message.answer(f'Чудово! Ось ваше місце: {making_list[2]}. Будемо чекати на вас!')
        with open('making_file.txt', 'a') as f:
            user_info = " ".join(making_list)
            f.write(f'{user_info}\n')
        making_list.clear()
        await dp.current_state().reset_state()
    else:
        await message.answer("Похід на фільм відмінений. Якщо хочете записатися на інший день/час - скористайтеся командою /making")
        making_list.clear()
        await dp.current_state().reset_state()

@dp.message_handler (commands="tr")
async def bot_echo(mesage: types.Message):
    await mesage.answer(f"Натисніть на кнопку", reply_markup=first)

@dp.callback_query_handlers (test="bottonipressed")
async def second_stop(call: types.CallbackQuery):
    await call.message.answer("Done!!!!")

#для echo
@dp.message_handler(commands='exo')
async def process_start_command(message: types.Message):
    await message.reply("Хей гайс!", reply_markup=kb.greet_kb)
