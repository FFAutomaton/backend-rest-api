from flask_restful import Resource
from telegram_bot import BotHandler, ambassador



class TelegramBot(Resource):
    def get(self):
        ambassador.greet()
        return "telegram"

    def post(self):
        pass
