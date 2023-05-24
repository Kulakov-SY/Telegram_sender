import asyncio
import logging
import time

from aiogram import Bot, Dispatcher, types
from flask import Flask  # pip install "flask[async]"
from flask import request  # pip install aioflask
from asgiref.wsgi import WsgiToAsgi
import os
from PyPDF2 import PdfReader, PdfWriter  # python -m pip install PyPDF2

flask_server = Flask(__name__)
asgi_app = WsgiToAsgi(flask_server)
API_TOKEN = 'YOUR_TOKEN'  # основной
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('broadcast')
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


# Обработчик POST-запроса
@flask_server.route('/', methods=['PUT', 'POST'])
async def handler():
    if request.method == 'POST':
        try:
            # Создаем директорию "output_pdf", если она не существует
            os.makedirs('output_pdf', exist_ok=True)

            # Получаем данные с аргументом "group_id"
            body = request.data
            args = request.args.to_dict()
            group_id = args.get("group_id")

            # Записываем данные в созданный PDF
            if group_id != '' or group_id is not None:
                input_path = os.path.abspath(f'output_pdf\\{group_id}\\Отчёт.pdf')
                file = open(input_path, "wb")
                file.write(body)
                file.close()

                # Убираем лишние страницы в pdf
                convert2(input_file=input_path)

                # Отправляем файл в группу group_id, при отсутствии ответа - повтор до 5 раз
                with open(input_path, "rb") as file:
                    try:
                        for i in range(5):
                            sent_message = await bot.send_document(int(group_id), file)
                            await asyncio.sleep(1)  # 20 messages per second (Limit: 30 messages per second)
                            if sent_message.message_id is not None:
                                break
                            file.close()
                            time.sleep(3)

                        # Отправляем сообщение об успешной отправке
                        await bot.send_message(-1001814815550, str('|' + group_id + '| = OK'))

                    except Exception as exc:
                        await bot.send_message(-1001814815550, str('|' + group_id + f'| = NOK, ошибка: {exc}'))

            return f'OK'
        except Exception as exc:
            await bot.send_message(-1001814815550, str(f'Ошибка: {exc}'))
            await asyncio.sleep(.05)

# Старт сервера
async def start_file_server():
    flask_server.run(host='0.0.0.0', port=8000)

# Удаляем лишние страницы
def convert2(input_file):
    try:
        pdf_path = os.path.abspath(input_file)
        input_pdf = PdfReader(str(pdf_path))
        pdf_writer = PdfWriter()
        for n in range(0, 5):
            page = input_pdf.pages[n]
            pdf_writer.add_page(page)

        with open(input_file, "wb") as output_file2:
            pdf_writer.write(output_file2)

    except Exception as e:
        print("Failed, try again")
        print(str(e))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_file_server())
    loop.close()
