from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


class rich_menu_handler:
    def __init__(self, line_bot_api, event):
        self.line_bot_api = line_bot_api
        self.event = event

    def menu_a(self):
        self.line_bot_api.reply_message(
            self.event.reply_token,
            TextSendMessage(text="リッチメニューのAが押されたでやんす")
        )
