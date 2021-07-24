from rich_menu_handler import rich_menu_handler
from types import resolve_bases
from typing import Text
from flask import Flask, request, abort
import os
import json
import requests


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

request_header = "Authorization: Bearer %s" % YOUR_CHANNEL_ACCESS_TOKEN


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
    rm_handler = rich_menu_handler(line_bot_api, event, scenario)
    prev_message_id = 0
    prev_message_text = ""
    if event.message.text == scenario['rich_menu_scenario']['register_user']['trigger_message']:
        prev_message_id = rm_handler.menu_a()
        prev_message_text = requests.get(
            "https://api-data.line.me/v2/bot/message/{}/content".format(prev_message_id), headers=request_header)
        print(prev_message_text)
    elif event.message.text == scenario['rich_menu_scenario']['get_time_now']['trigger_message']:
        prev_message_id = rm_handler.menu_c()
        prev_message_text = requests.get(
            "https://api-data.line.me/v2/bot/message/{}/content".format(prev_message_id), headers=request_header)
        print(prev_message_text)
    else:
        response_message = event.message.text + "でやんす"
        prev_message_id = event.message.id
        prev_message_text = requests.get(
            "https://api-data.line.me/v2/bot/message/%s/content" % str(prev_message_id), headers=request_header)
        print(prev_message_text)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=response_message)
        )


if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
