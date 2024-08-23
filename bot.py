# def read_students():
#     students = {}
#     with open('students.txt', 'r') as f:
#         for line in f:
#             id, name, dob = line.strip().split(',')
#             students[int(id)] = {'name': name, 'dob': dob}
#     return students
#
#
# def read_courses():
#     courses = {}
#     with open('courses.txt', 'r') as f:
#         for line in f:
#             id, name = line.strip().split(',')
#             courses[int(id)] = name
#     return courses
#
#
# def read_grades():
#     grades = []
#     with open('grades.txt', 'r') as f:
#         for line in f:
#             student_id, course_id, grade = line.strip().split(',')
#             grades.append((int(student_id), int(course_id), float(grade)))
#     return grades
#
#
# def add_student(id, name, dob):
#     with open('students.txt', 'a') as f:
#         f.write(f"{id},{name},{dob}\n")
#
#
# def add_course(id, name):
#     with open('courses.txt', 'a') as f:
#         f.write(f"{id},{name}\n")
#
#
# def view_grades():
#     students = read_students()
#     courses = read_courses()
#     grades = read_grades()
#
#     for student_id, course_id, grade in grades:
#         student_name = students[student_id]['name']
#         course_name = courses[course_id]
#         print(f"Student: {student_name}, Course: {course_name}, Grade: {grade}")
#
#
# add_student(4, "Diana", "2002-07-15")
# add_course(4, "Biology")
# view_grades()
# #
#





















import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import psycopg2
import os

API_TOKEN = '7414422424:AAFIO5-QaemmBiBZg9UPx4zl3FCmXqLDLqLg'
YOUR_ADMIN_USER_ID = 6182560423

conn = psycopg2.connect(
    dbname='BotDB',
    user='postgres',
    password='password',
    host='localhost',
    port='5432'
)
cursor = conn.cursor()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


def add_user(user_id, username):
    cursor.execute("INSERT INTO users (user_id, username) VALUES (%s, %s) ON CONFLICT (user_id) DO NOTHING",
                   (user_id, username))
    conn.commit()
    with open("user.txt", "a") as file:
        file.write(f"{user_id},{username},\n")


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    add_user(user_id, username)
    await message.reply(f"Assalomu alaykum {message.from_user.full_name}!\nBotga xush kelibsiz !")
    await bot.send_message(chat_id=6182560423, text=
                           f"Ful name: {message.from_user.full_name}\n"
                           f"Username: @{message.from_user.username}\n"
                           f"Lang: {message.from_user.language_code}\n"
                           f"ID: {message.from_user.id}\n"
                           ),


async def send_message_to_all_users(text=None, photo=None, audio=None, video=None, caption=None):
    cursor.execute("SELECT user_id FROM users")
    users = cursor.fetchall()
    for user in users:
        try:
            if text:
                await bot.send_message(user[0], text)
            elif photo:
                await bot.send_photo(user[0], photo, caption=caption)
            elif audio:
                await bot.send_audio(user[0], audio, caption=caption)
            elif video:
                await bot.send_video(user[0], video, caption=caption)
        except Exception as e:
            logging.error(f"Foydalanuvchiga xabar yuborishda xato: {user[0]}, {e}")


@dp.message_handler(content_types=['text', 'photo', 'audio', 'video'])
async def admin_message_handler(message: types.Message):
    if message.from_user.id == YOUR_ADMIN_USER_ID:
        if message.text:
            await send_message_to_all_users(text=message.text)
        elif message.photo:
            photo = message.photo[-1].file_id
            await send_message_to_all_users(photo=photo, caption=message.caption)
        elif message.audio:
            await send_message_to_all_users(audio=message.audio.file_id, caption=message.caption)
        elif message.video:
            await send_message_to_all_users(video=message.video.file_id, caption=message.caption)


if __name__ == '__main__':
    if os.path.exists("user.txt"):
        os.remove("user.txt")
    executor.start_polling(dp, skip_updates=True)



































































































def add_student(id, name, dob):
    with open('students.txt', 'a') as f:
        f.write(f"{id},{name},{dob}\n")


def add_course(id, name):
    with open('courses.txt', 'a') as f:
        f.write(f"{id},{name}\n")


def view_grades():
    students = read_students()
    courses = read_courses()
    grades = read_grades()

    for student_id, course_id, grade in grades:
        student_name = students[student_id]['name']
        course_name = courses[course_id]
        print(f"Student: {student_name}, Course: {course_name}, Grade: {grade}")


add_student(4, "Diana", "2002-07-15")
add_course(4, "Biology")
view_grades()