import os
import requests
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")  # Аккаунт, за которым следим

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

def get_twitter_data(username):
    """ Получает данные о последнем посте пользователя в Сети X """
    url = f"https://api.twitter.com/2/users/by/username/{username}?user.fields=id"
    headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}
    
    user_response = requests.get(url, headers=headers).json()
    user_id = user_response.get("data", {}).get("id")
    if not user_id:
        return "Ошибка: Не удалось получить ID пользователя"
    
    tweets_url = f"https://api.twitter.com/2/users/{user_id}/tweets?tweet.fields=public_metrics&max_results=5"
    tweets_response = requests.get(tweets_url, headers=headers).json()
    tweets = tweets_response.get("data", [])
    
    if not tweets:
        return "Ошибка: Нет постов"
    
    latest_tweet = tweets[0]  # Берем последний пост
    metrics = latest_tweet.get("public_metrics", {})
    return (f"Последний пост: https://x.com/{username}/status/{latest_tweet['id']}\n"
            f"❤ Лайки: {metrics.get('like_count', 0)}\n"
            f"🔁 Ретвиты: {metrics.get('retweet_count', 0)}\n"
            f"💬 Цитаты: {metrics.get('quote_count', 0)}")

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: Message):
    await message.answer("Привет! Я бот, анализирующий реакции на посты в X (Twitter).\n"
                         "Отправь /stats, чтобы увидеть данные о последнем посте!")

@dp.message_handler(commands=["stats"])
async def send_twitter_stats(message: Message):
    response_text = get_twitter_data(TWITTER_USERNAME)
    await message.answer(response_text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
