from dotenv import load_dotenv
from comics_api import get_comics
import asyncio
import os
import aiohttp
import logging



logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def main():
    load_dotenv()
    token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    waiting_period = 8
    logging.info("🚀 Бот запущен!")
    while True:
        await asyncio.sleep(waiting_period)
        comics = get_comics()
        image_comics = comics['img']
        comment = comics['alt']
        await send_photo(image_comics, comment, chat_id, token)



async def send_photo(url_picture, comment, chat_id, token):
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    data = {
        "chat_id": chat_id,
        "photo": url_picture,
        "caption": comment
    }


    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            if response.status == 200:
                logging.info("✅ Фото отправлено успешно!")
            else:
                logging.error(f"❌ Ошибка отправки фото: {response.status}")



if __name__ == "__main__":
    asyncio.run(main())
