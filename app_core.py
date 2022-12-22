# 載入需要的模組
import os,string

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from utility import send_text_message
from machine import create_machine


app = Flask(__name__,static_folder = "imgs")

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('ais+Wjhq4dxNDBMXM3etNFEN/7trYXmfC/sXN0UCyeaw/1xPMD8AGsteMUHdCqAgLXSwRsFT6FsmEupLPGdPVV7MrQOe7jkuVBKcs8gDeOuc8ZT4wmeQMFigBTPfTjuIA2zQ3io0zwj9xESyLbMBaAdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser('fc5f72bec41b6936377a3f7593b79d6f')

machines = {}

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        
        # Create a machine for new user
        if event.source.user_id not in machines:
            machines[event.source.user_id] = create_machine()

        # Advance the FSM for each MessageEvent
        response = machines[event.source.user_id].advance(event)
        if response == False:
            send_text_message(event.reply_token, "Invalid command, try again")


    return "OK"


if __name__ == "__main__":
    app.run(port = 5002)