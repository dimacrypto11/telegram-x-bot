Telegram X Reactions Bot

A Telegram bot that tracks reactions (likes, retweets, quotes) on the latest posts of a specified X (Twitter) account using Twitter API v2 and aiogram.

Features

Fetches engagement data for the latest post.

Uses Twitter API v2 for real-time metrics.

Built with aiogram for efficient Telegram bot handling.

Setup

Clone the repository:
git clone https://github.com/your-username/telegram-x-bot.git
cd telegram-x-bot

Install dependencies:
pip install -r requirements.txt

Create a .env file and add your credentials:
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TWITTER_BEARER_TOKEN=your_twitter_bearer_token
TWITTER_USERNAME=your_twitter_username

Run the bot:
python bot.py

Usage

Start the bot and send /stats to get engagement data for the latest post.

Simple and efficient social media analytics in your Telegram!
