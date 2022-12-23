import os
import bs4
import requests
from bs4 import BeautifulSoup


from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, CarouselTemplate, CarouselColumn

line_bot_api = LineBotApi('ais+Wjhq4dxNDBMXM3etNFEN/7trYXmfC/sXN0UCyeaw/1xPMD8AGsteMUHdCqAgLXSwRsFT6FsmEupLPGdPVV7MrQOe7jkuVBKcs8gDeOuc8ZT4wmeQMFigBTPfTjuIA2zQ3io0zwj9xESyLbMBaAdB04t89/1O/w1cDnyilFU=')

ngrok_url = "https://4672-182-234-148-141.jp.ngrok.io"

def send_text_message(reply_token, text):
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    return "OK"

def send_button_mainpage(event):
    im_url = "/imgs/logo.jpg"
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='土虱嫂(開元分店)',
                    text='點選下方按鈕取得資訊',
                    actions=[
                        MessageTemplateAction(
                            label='菜單',
                            text='菜單'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='土虱嫂(開元分店)',
                    text='點選下方按鈕取得資訊',
                    actions=[
                        MessageTemplateAction(
                            label='店家資訊',
                            text='店家資訊'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='土虱嫂(開元分店)',
                    text='點選下方按鈕取得資訊',
                    actions=[
                        MessageTemplateAction(
                            label='當月活動',
                            text='當月活動'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='土虱嫂(開元分店)',
                    text='點選下方按鈕取得資訊',
                    actions=[
                        MessageTemplateAction(
                            label='訂餐',
                            text='訂餐'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_button_menu(event):
    im_url = "/imgs/logo.jpg"
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='菜單',
                    text='點選下方按鈕看圖片',
                    actions=[
                        MessageTemplateAction(
                            label='當歸土虱 頭$90 中$80 尾$80',
                            text='當歸土虱'
                        ),
                        MessageTemplateAction(
                            label='藥頭排骨 $90',
                            text='藥頭排骨'
                        ),
                        MessageTemplateAction(
                            label='土虱蛋 小$30 大$50',
                            text='土虱蛋'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='菜單',
                    text='點選下方按鈕看圖片',
                    actions=[
                        MessageTemplateAction(
                            label='肉燥飯 $20',
                            text='肉燥飯'
                        ),
                        MessageTemplateAction(
                            label='白飯 $10',
                            text='白飯'
                        ),
                        MessageTemplateAction(
                            label='滷蛋$10 & 油豆腐$10 ',
                            text='滷蛋&油豆腐'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='菜單',
                    text='點選下方按鈕回主頁',
                    actions=[
                        MessageTemplateAction(
                            label='回主頁',
                            text='回主頁'
                        ),
                        MessageTemplateAction(
                            label='回主頁',
                            text='回主頁'
                        ),
                        MessageTemplateAction(
                            label='回主頁',
                            text='回主頁'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_button_information(event):
    im_url = "/imgs/logo.jpg"
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='店家資訊',
                    text='點選下方按鈕獲取資訊',
                    actions=[
                        MessageTemplateAction(
                            label='營業時間',
                            text='營業時間'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='店家資訊',
                    text='點選下方按鈕獲取資訊',
                    actions=[
                        MessageTemplateAction(
                            label='電話',
                            text='電話'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='店家資訊',
                    text='點選下方按鈕獲取資訊',
                    actions=[
                        MessageTemplateAction(
                            label='地址',
                            text='地址'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='店家資訊',
                    text='點選下方按鈕回主頁',
                    actions=[
                        MessageTemplateAction(
                            label='回主頁',
                            text='回主頁'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_button_promotion(event):
    im_url = "/imgs/logo.jpg"
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='本月促銷',
                    text='點選下方按鈕獲取促銷資訊',
                    actions=[
                        MessageTemplateAction(
                            label='促銷',
                            text='促銷'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='本月促銷',
                    text='點選下方按鈕回主頁',
                    actions=[
                        MessageTemplateAction(
                            label='回主頁',
                            text='回主頁'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_button_order(event):
    im_url = "/imgs/logo.jpg"
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='訂餐',
                    text='訂餐完成後點選下方按鈕',
                    actions=[
                        MessageTemplateAction(
                            label='訂餐完成',
                            text='訂餐完成'
                        ),
                        MessageTemplateAction(
                            label='訂餐完成',
                            text='訂餐完成'
                        ),
                        MessageTemplateAction(
                            label='訂餐完成',
                            text='訂餐完成'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='訂餐',
                    text='點選下方按鈕來訂餐',
                    actions=[
                        MessageTemplateAction(
                            label='當歸土虱 頭 $90',
                            text='當歸土虱頭'
                        ),
                        MessageTemplateAction(
                            label='當歸土虱 中 $80',
                            text='當歸土虱中'
                        ),
                        MessageTemplateAction(
                            label='當歸土虱 尾 $80',
                            text='當歸土虱尾'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='訂餐',
                    text='點選下方按鈕來訂餐',
                    actions=[
                        MessageTemplateAction(
                            label='藥頭排骨 $90',
                            text='藥頭排骨'
                        ),
                        MessageTemplateAction(
                            label='藥頭排骨 $90',
                            text='藥頭排骨'
                        ),
                        MessageTemplateAction(
                            label='藥頭排骨 $90',
                            text='藥頭排骨'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='訂餐',
                    text='點選下方按鈕來訂餐',
                    actions=[
                        MessageTemplateAction(
                            label='土虱蛋 小$30',
                            text='土虱蛋(小)'
                        ),
                        MessageTemplateAction(
                            label='土虱蛋 小$30',
                            text='土虱蛋(小)'
                        ),
                        MessageTemplateAction(
                            label='土虱蛋 大$50',
                            text='土虱蛋(大)'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='訂餐',
                    text='點選下方按鈕來訂餐',
                    actions=[
                        MessageTemplateAction(
                            label='白飯 $10',
                            text='白飯'
                        ),
                        MessageTemplateAction(
                            label='白飯 $10',
                            text='白飯'
                        ),
                        MessageTemplateAction(
                            label='白飯 $10',
                            text='白飯'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='訂餐',
                    text='點選下方按鈕來訂餐',
                    actions=[
                        MessageTemplateAction(
                            label='肉燥飯 $20',
                            text='肉燥飯'
                        ),
                        MessageTemplateAction(
                            label='肉燥飯 $20',
                            text='肉燥飯'
                        ),
                        MessageTemplateAction(
                            label='肉燥飯 $20',
                            text='肉燥飯'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='訂餐',
                    text='點選下方按鈕來訂餐',
                    actions=[
                        MessageTemplateAction(
                            label='油豆腐 $10',
                            text='油豆腐'
                        ),
                        MessageTemplateAction(
                            label='滷蛋 $10',
                            text='滷蛋'
                        ),
                        MessageTemplateAction(
                            label='滷蛋 $10',
                            text='滷蛋'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=ngrok_url+im_url,
                    title='訂餐',
                    text='點選下方按鈕回主頁',
                    actions=[
                        MessageTemplateAction(
                            label='回主頁',
                            text='回主頁'
                        ),
                        MessageTemplateAction(
                            label='回主頁',
                            text='回主頁'
                        ),
                        MessageTemplateAction(
                            label='回主頁',
                            text='回主頁'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_button_asknum(event):
    #im_url = "/imgs/logo.jpg"
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    #thumbnail_image_url=ngrok_url+"/imgs/catfish.jpg",
                    title='你要幾份'+event.message.text+'?',
                    text='點選下方按鈕來選擇',
                    actions=[
                        MessageTemplateAction(
                            label='0份',
                            text='0'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url=ngrok_url+"/imgs/catfish.jpg",
                    title='你要幾份'+event.message.text+'?',
                    text='點選下方按鈕來選擇',
                    actions=[
                        MessageTemplateAction(
                            label='1份',
                            text='1'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url=ngrok_url+"/imgs/catfish.jpg",
                    title='你要幾份'+event.message.text+'?',
                    text='點選下方按鈕來選擇',
                    actions=[
                        MessageTemplateAction(
                            label='2份',
                            text='2'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url=ngrok_url+"/imgs/catfish.jpg",
                    title='你要幾份'+event.message.text+'?',
                    text='點選下方按鈕來選擇',
                    actions=[
                        MessageTemplateAction(
                            label='3份',
                            text='3'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url=ngrok_url+"/imgs/catfish.jpg",
                    title='你要幾份'+event.message.text+'?',
                    text='點選下方按鈕來選擇',
                    actions=[
                        MessageTemplateAction(
                            label='4份',
                            text='4'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url=ngrok_url+"/imgs/catfish.jpg",
                    title='你要幾份'+event.message.text+'?',
                    text='點選下方按鈕來選擇',
                    actions=[
                        MessageTemplateAction(
                            label='5份',
                            text='5'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url=ngrok_url+"/imgs/catfish.jpg",
                    title='你要幾份'+event.message.text+'?',
                    text='點選下方按鈕來選擇',
                    actions=[
                        MessageTemplateAction(
                            label='6份',
                            text='6'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url=ngrok_url+"/imgs/catfish.jpg",
                    title='你要幾份'+event.message.text+'?',
                    text='點選下方按鈕來選擇',
                    actions=[
                        MessageTemplateAction(
                            label='7份',
                            text='7'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url=ngrok_url+"/imgs/catfish.jpg",
                    title='你要幾份'+event.message.text+'?',
                    text='點選下方按鈕來選擇',
                    actions=[
                        MessageTemplateAction(
                            label='8份',
                            text='8'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url=ngrok_url+"/imgs/catfish.jpg",
                    title='你要幾份'+event.message.text+'?',
                    text='點選下方按鈕來選擇',
                    actions=[
                        MessageTemplateAction(
                            label='9份',
                            text='9'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_button_keepordering(event,keep_order1,keep_order2):
    im_url = "/imgs/logo.jpg"
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    #thumbnail_image_url=ngrok_url+im_url,
                    title='繼續訂餐',
                    text=keep_order1,
                    actions=[
                        MessageTemplateAction(
                            label='繼續訂餐',
                            text='繼續訂餐'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url=ngrok_url+im_url,
                    title='繼續訂餐',
                    text=keep_order2+'\n點下方按鈕繼續訂餐',
                    actions=[
                        MessageTemplateAction(
                            label='繼續訂餐',
                            text='繼續訂餐'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_button_orderfinish(event,finish_message1,finish_message2):
    im_url = "/imgs/logo.jpg"
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    #thumbnail_image_url=ngrok_url+im_url,
                    title='訂餐完成',
                    text=finish_message1,
                    actions=[
                        MessageTemplateAction(
                            label='返回',
                            text='返回'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url=ngrok_url+im_url,
                    title='訂餐完成',
                    text=finish_message2+'\n點下方按鈕返回',
                    actions=[
                        MessageTemplateAction(
                            label='返回',
                            text='返回'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_notavailble(event):
    send_text_message(event.reply_token,'此部份還在開發中!\n輸入"回主頁"來回到主頁')
    return "OK"

def send_catfishimage(event):
    im_url = "/imgs/catfish.jpg"
    img_url = ngrok_url + im_url
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=img_url,
                    title='當歸土虱',
                    text='點下方按鈕繼續看菜單',
                    actions=[
                        MessageTemplateAction(
                            label='繼續看菜單',
                            text='繼續看菜單'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_porkribsimage(event):
    im_url = "/imgs/porkribs.jpg"
    img_url = ngrok_url + im_url
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=img_url,
                    title='藥頭排骨',
                    text='點下方按鈕繼續看菜單',
                    actions=[
                        MessageTemplateAction(
                            label='繼續看菜單',
                            text='繼續看菜單'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_catfisheggimage(event):
    im_url = "/imgs/catfishegg.jpg"
    img_url = ngrok_url + im_url
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=img_url,
                    title='土虱蛋',
                    text='點下方按鈕繼續看菜單',
                    actions=[
                        MessageTemplateAction(
                            label='繼續看菜單',
                            text='繼續看菜單'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_mincedporkimage(event):
    im_url = "/imgs/mincedpork.jpg"
    img_url = ngrok_url + im_url
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=img_url,
                    title='肉燥飯',
                    text='點下方按鈕繼續看菜單',
                    actions=[
                        MessageTemplateAction(
                            label='繼續看菜單',
                            text='繼續看菜單'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_riceimage(event):
    im_url = "/imgs/rice.jpg"
    img_url = ngrok_url + im_url
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=img_url,
                    title='白飯',
                    text='點下方按鈕繼續看菜單',
                    actions=[
                        MessageTemplateAction(
                            label='繼續看菜單',
                            text='繼續看菜單'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_eggandtofuimage(event):
    im_url = "/imgs/eggandtofu.jpg"
    img_url = ngrok_url + im_url
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=img_url,
                    title='滷蛋&油豆腐',
                    text='點下方按鈕繼續看菜單',
                    actions=[
                        MessageTemplateAction(
                            label='繼續看菜單',
                            text='繼續看菜單'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_button_discount(event):
    im_url = "/imgs/catfishegg.jpg"
    img_url = ngrok_url + im_url
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    #thumbnail_image_url=img_url,
                    title='促銷活動',
                    text='現在沒有任何促銷活動!',
                    actions=[
                        MessageTemplateAction(
                            label='繼續',
                            text='繼續'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_button_businesshours(event):
    im_url = "/imgs/catfishegg.jpg"
    img_url = ngrok_url + im_url
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    #thumbnail_image_url=img_url,
                    title='營業時間',
                    text="星期一 17:30~01:00\n"+"星期二 17:30~01:00\n"+"星期三 17:30~01:00\n",
                    actions=[
                        MessageTemplateAction(
                            label='繼續查看',
                            text='繼續查看'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url=img_url,
                    title='營業時間',
                    text="星期四 17:30~01:00\n"+"星期五	17:30~01:00\n"+"星期六	休息\n"+"星期日	休息",
                    actions=[
                        MessageTemplateAction(
                            label='繼續查看',
                            text='繼續查看'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_button_phonenum(event):
    im_url = "/imgs/catfishegg.jpg"
    img_url = ngrok_url + im_url
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    #thumbnail_image_url=img_url,
                    title='電話',
                    text='063022830',
                    actions=[
                        MessageTemplateAction(
                            label='繼續查看',
                            text='繼續查看'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"

def send_button_address(event):
    im_url = "/imgs/catfishegg.jpg"
    img_url = ngrok_url + im_url
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    #thumbnail_image_url=img_url,
                    title='地址',
                    text="710台南市永康區中山南路96號",
                    actions=[
                        MessageTemplateAction(
                            label='繼續查看',
                            text='繼續查看'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"


    