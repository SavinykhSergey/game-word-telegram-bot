from aiogram import executor
from main_game_cities import *
from bot import create_bot

cr_bot = create_bot()
bot = cr_bot[0]
dp = cr_bot[1]

@dp.message_handler(commands=['start'])
async def command_start_bot(msg : types.Message):
    await bot.send_message(msg.from_user.id, 'Добро пожаловать в игру созданую Tapochek')

# @dp.message_handler()
# async def command_start_game(msg: types.Message):
#     if msg.text == 'game':
#         pass
#         # await choice_game(msg)
#         # preparation_game()
#         # game()
#     else:
#         await bot.send_message(msg.from_user.id, 'Чтобы начать игру введите game')
def keep_messege(lst,text):
    lst.append(text)
    return lst

lst = []

async def test(lst):
    text = keep_messege(lst, '')[-1]
    print(text)

@dp.message_handler()
async def message_bot(msg : types.Message):
    await bot.send_message(msg.from_user.id, 'Напиши слово собака')
    keep_messege(lst, msg.text)
    await test(lst)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

