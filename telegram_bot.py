import requests
# import datetime
# import telegram
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config.local import telegram_token


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        self.status = requests.get(self.api_url + 'getMe')
        self.offset = None

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        print('get last update alive')
        get_result = self.get_updates()
        print(get_result)
        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

    def _get_last_variables(self):
        last_update = ambassador.get_last_update()
        self.last_update = self.get_last_update()
        self.last_update_id = last_update['update_id']
        self.last_chat_text = last_update['message']['text']
        self.last_chat_id = last_update['message']['chat']['id']
        self.last_chat_name = last_update['message']['chat']['first_name']
        BotHandler._update_offset(self)
        return self

    def _update_offset(self):
        self.offset = self.last_update_id + 1
        print('offset is', self.offset)

    def actions(self, last_update):
        routes = ['/start', '/ensonneoldu', '/kirmizialarm']
        action = last_update['message']['text']
        if action == '/start':
            return 'start works \n /ensonneoldu \n /kirmizialarm'
        elif action == '/ensonneoldu':
            return 'hicbisiiii'
        pass
    @staticmethod
    def telegram_main():
        new_offset = None
        ambassador.get_updates(new_offset)
        last_update = ambassador.get_last_update()
        last_update_id = last_update['update_id']
        # last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        # message = greet_bot.actions(last_update)
        message = 'anan'
        ambassador.send_message(last_chat_id, message)
        # print('last chat text', last_chat_text)
        new_offset = last_update_id + 1

    def greet(self):
        BotHandler._get_last_variables(self)
        message = 'Selamlar ' + self.last_chat_name + '\n Nasil yardimci olabilirim??' + '\n Botun farkli fonksiyonlarini gorebilmek icin /routes yazman yeterli'
        last_chat_id = self.last_chat_id
        ambassador.send_message(last_chat_id, message)


ambassador = BotHandler(telegram_token)

