from rich_menu_handler import rich_menu_handler
from types import resolve_bases
from typing import Text
from flask import Flask, request, abort
import os
import json


from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


app = Flask(__name__)

# シナリオファイルの読み込み
scenario = json.load(open('config.json', 'r'))

# 環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/", methods=['GET'])
def hello():
    return "hello, world"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    rm_handler = rich_menu_handler(line_bot_api, event)
    # if event.message.text == "ユーザ情報を登録するでやんす":
    if event.message.text == scenario['register_user']['trigger_message']:
        rm_handler.menu_a()
    elif event.message.text == "今何時？":
        rm_handler.menu_c()
    else:
        response_message = event.message.text + "でやんす"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=response_message)
        )


if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
