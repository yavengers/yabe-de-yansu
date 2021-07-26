from datetime import datetime, time
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from model import user


class rich_menu_handler:
    def __init__(self, line_bot_api, event, scenario):
        self.line_bot_api = line_bot_api
        self.event = event
        self.scenario = scenario
        self.response_text = ""

    def menu_a(self):
        self.response_text = self.scenario['rich_menu_scenario']['register_user']['response_text'] + \
            "\n" + self.event.message.id
        self.reply()
        return self.event.message.id

    def menu_c(self):
        self.response_text = datetime.now().strftime('%Y年%m月%d日 %H:%M:%S') + \
            "\n" + self.event.message.id
        self.reply()
        return self.event.message.id

    def reply(self):
        userId = self.event.source.user_id
        self.line_bot_api.reply_message(
            self.event.reply_token,
            TextSendMessage(text=self.response_text + "\n" + userId)
        )
