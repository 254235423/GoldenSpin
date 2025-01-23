from flask import Flask, render_template
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Создаем Flask-приложение для сайта
app = Flask(__name__)

@app.route("/")
def homepage():
    return '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>GOLDEN SPIN</title>
        <style>
            body {
                background-color: #6F584B;
                margin: 0;
            }
            .game {
                width: 100%;
                height: 65vh;
                background-color: #594236;
                border-radius: 40px 40px 0 0;
            }
            .name {
                background-color: #6F584B;
                width: 100%;
                height: 15vh;
            }
            h1 {
                color: #362a24;
                text-align: center;
                padding: auto;

            }
            .money {
                width: 150px;
                height: 40px;
                background: #6F584B;
                margin: auto;
                margin-top: 20px;
                padding-top: 0;
            }
            .setting {
                width: 100%;
                height: 50px;
                background-color: #6F584B;
                display: flex;
                justify-content: center;
                gap: 8px;
                margin-top: 6px;
            }
            img {
                width: 20px;
            }
            button {
                background-color: #362a24;
                border: none;
                border-radius: 10px;
                width: 70px;
                height: 50px;
            }
        </style>
    </head>
    <body>
        <div class="name">
            <h1>GOLDEN SPIN</h1>
        </div>
        <div class="game">
            <div class="money">
                <h1>0.00 ₽</h1>
                
            </div>
        </div>
        <div class="setting">
            <button id="news"><img src="/4.png">Новости</button>
            <button id="gift"><img src="/3.png">Подарок</button>
            <button id="friends"><img src="/1.png">Друзья</button>
            <button id="tasks"><img src="/2.png">Задания</button>
        </div>
        <script>
            document.getElementById('news').addEventListener('click', function() {
                window.location.href = 'news.html';
            });
            document.getElementById('gift').addEventListener('click', function() {
                window.location.href = 'gift.html';
            });
            document.getElementById('friends').addEventListener('click', function() {
                window.location.href = 'friend.html';
            });
            document.getElementById('tasks').addEventListener('click', function() {
                window.location.href = 'tasks.html';
            });
        </script>
    </body>
    </html>
    '''

# Настраиваем Telegram-бота
TOKEN = "7246921568:AAE3_vLndiIC1xjabXCaYAOrbgcf3qUN9t0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start"""
    # Кнопка для открытия сайта
    keyboard = [
        [InlineKeyboardButton("Открыть Golden Spin", url="http://127.0.0.1:5000")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Добро пожаловать в Golden Spin! Нажмите кнопку ниже, чтобы открыть сайт.", reply_markup=reply_markup)

def main():
    # Создаем приложение Telegram
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))

    # Запускаем Telegram-бота
    application.run_polling()

if __name__ == "__main__":
    import threading

    # Запускаем Flask-сервер в отдельном потоке
    threading.Thread(target=lambda: app.run(port=5000, debug=False, use_reloader=False)).start()

    # Запускаем Telegram-бота
    main()