from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import menu
from loader import bot
start_router: Router = Router()





@start_router.message(Command("start"))
async def start(message: Message):
    await message.answer("Assalomu alaykum xush kelibisiz!")
    await message.answer("Serialni ko'rish uchun tugmalardan birini bosing!", reply_markup=menu)

    









       


