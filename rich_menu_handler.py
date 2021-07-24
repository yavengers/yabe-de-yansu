from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


def menu_a(line_bot_api, event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="リッチメニューのAが押されたでやんす")
    )
