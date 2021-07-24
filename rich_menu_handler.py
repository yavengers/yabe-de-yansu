from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from model import user


class rich_menu_handler:
    def __init__(self, line_bot_api, event):
        self.line_bot_api = line_bot_api
        self.event = event
        self.user = user.User()

    def menu_a(self):
        self.line_bot_api.reply_message(
            self.event.reply_token,
            TextSendMessage(text="名前を入力するでやんす")
        )

    def menu_c(self):
        response_text = "userId: " + self.event.source.user_id + "\n" + "リッチメニューのCが押されたでやんす"
        self.line_bot_api.reply_message(
            self.event.reply_token,
            TextSendMessage(text=response_text)
        )
