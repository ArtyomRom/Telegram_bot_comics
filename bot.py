from dotenv import load_dotenv
from comics_api import get_comic
from telegram import Bot
import os
import logging


def send_photo(image_comic, comment, chat_id, token):
    bot = Bot(token=token)
    bot.send_photo(chat_id=chat_id, photo=image_comic, caption=comment)


def main():
    load_dotenv()
    token = os.environ['TG_TOKEN']
    chat_id = os.environ['CHAT_ID']
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)
    logger.info("🚀 Бот запущен!")
    comic = get_comic()
    image_comic = comic['img']
    comment = comic['alt']
    try:
        send_photo(image_comic, comment, chat_id, token)
        logger.info("✅ Фото отправлено успешно!")
    except Exception as e:
        logger.error(f"❌ Ошибка отправки фото: {e}")


if __name__ == "__main__":
    main()
