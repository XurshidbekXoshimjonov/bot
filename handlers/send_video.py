from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import menu
from loader import bot


send_video_router: Router = Router()


@send_video_router.message(F.text == '1-qism')
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAMFZYxAYY31fkDfsj8bons4V4rpHlYAAgQ9AALfZ2FI0Bx3H03fjUMzBA", caption="Marhamat 1-qism\n Eslatib o'tamiz serial uzmovi.com saytidan yuklab olindi!")





@send_video_router.message(F.text == '2-qism')
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAMHZYxDNfkwCQ2eyW_Wyz0f6Ud8R9sAAhg9AALfZ2FIGEkZVIMhIcIzBA", caption="Marhamat 2-qism\n Eslatib o'tamiz serial uzmovi.com saytidan yuklab olindi!")





@send_video_router.message(F.text == '3-qism')
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAMJZYxDnWFsY-FTjGKAPhGbDgEntPIAAiM9AALfZ2FIhqP8FLSQLmozBA", caption="Marhamat 3-qism\n Eslatib o'tamiz serial uzmovi.com saytidan yuklab olindi!")





@send_video_router.message(F.text == '4-qism')
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAMLZYxERpJ7L9djdvK8thPxnhe_ChAAAjw9AALfZ2FIU5T3sMma5LUzBA", caption="Marhamat 4-qism\n Eslatib o'tamiz serial uzmovi.com saytidan yuklab olindi!")





@send_video_router.message(F.text == '5-qism')
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAMNZYxEvCchReM7opeUb2H6xbfyGwsAAkI9AALfZ2FIIBCGnW_GyGYzBA", caption="Marhamat 5-qism\n Eslatib o'tamiz serial uzmovi.com saytidan yuklab olindi!")





@send_video_router.message(F.text == '6-qism')
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAMPZYxFAAHTVHgMx21J0PEUM35KdqzyAAJRPQAC32dhSDHrBNNTfiqOMwQ", caption="Marhamat 6-qism\n Eslatib o'tamiz serial uzmovi.com saytidan yuklab olindi!")





@send_video_router.message(F.text == '7-qism')
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAMRZYxFE2-YdMnAt3S8-7PsxZ6V61YAAmM9AALfZ2FIiayu8qTNvX4zBA", caption="Marhamat 7-qism\n Eslatib o'tamiz serial uzmovi.com saytidan yuklab olindi!")





@send_video_router.message(F.text == '8-qism')
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAMTZYxFNNe76v4jtg_VQ7MEzK9uJtoAAg49AALfZ2FIe6gqHWKJJUszBA", caption="Marhamat 8-qism\n Eslatib o'tamiz serial uzmovi.com saytidan yuklab olindi!")