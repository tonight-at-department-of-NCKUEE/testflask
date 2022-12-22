from transitions.extensions import GraphMachine
from utility import send_button_address,send_button_phonenum,send_button_businesshours,send_button_discount,send_button_keepordering,send_button_orderfinish,send_button_asknum,send_button_order,send_button_promotion,send_text_message,send_button_information,send_button_menu,send_button_mainpage,send_notavailble,send_catfishimage,send_porkribsimage,send_catfisheggimage,send_mincedporkimage,send_eggandtofuimage,send_riceimage

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        self.food = '?'
        self.orderlist={}
        self.orderlist["當歸土虱頭"]='0'
        self.orderlist["當歸土虱中"]='0'
        self.orderlist["當歸土虱尾"]='0'
        self.orderlist["藥頭排骨"]='0'
        self.orderlist["土虱蛋(小)"]='0'
        self.orderlist["土虱蛋(大)"]='0'
        self.orderlist["白飯"]='0'
        self.orderlist["肉燥飯"]='0'
        self.orderlist["油豆腐"]='0'
        self.orderlist["滷蛋"]='0'
        self.price={}
        self.price["當歸土虱頭"]=90
        self.price["當歸土虱中"]=80
        self.price["當歸土虱尾"]=80
        self.price["藥頭排骨"]=90
        self.price["土虱蛋(小)"]=30
        self.price["土虱蛋(大)"]=50
        self.price["白飯"]=10
        self.price["肉燥飯"]=20
        self.price["油豆腐"]=10
        self.price["滷蛋"]=10
        

    #mainpage
    def is_going_to_mainpage(self, event):
        text = event.message.text
        return True
    def on_enter_mainpage(self, event):
        send_button_mainpage(event)

    #backmainpage
    def is_going_to_backmainpage(self, event):
        text = event.message.text
        return text == '回主頁'
    def on_enter_backmainpage(self, event):
        send_button_mainpage(event)

    #menu
    def is_going_to_menu(self, event):
        text = event.message.text
        return text == '菜單' 
    def on_enter_menu(self, event):
        send_button_menu(event)


    #catfish
    def is_going_to_catfish(self, event):
        text = event.message.text
        return text == "當歸土虱"
    def on_enter_catfish(self, event):
        send_catfishimage(event)
        #self.advance(event)
        

    #porkribs
    def is_going_to_porkribs(self, event):
        text = event.message.text
        return text == "藥頭排骨"
    def on_enter_porkribs(self, event):
        send_porkribsimage(event)
        #self.advance(event)

    #catfishegg
    def is_going_to_catfishegg(self, event):
        text = event.message.text
        return text == "土虱蛋"
    def on_enter_catfishegg(self, event):
        send_catfisheggimage(event)
        #self.advance(event)

    #mincedpork
    def is_going_to_mincedpork(self, event):
        text = event.message.text
        return text == "肉燥飯"
    def on_enter_mincedpork(self, event):
        send_mincedporkimage(event)
        #self.advance(event)
    
    #rice
    def is_going_to_rice(self, event):
        text = event.message.text
        return text == "白飯"
    def on_enter_rice(self, event):
        send_riceimage(event)
        #self.advance(event)

    #eggandtofu
    def is_going_to_eggandtofu(self, event):
        text = event.message.text
        return text == "滷蛋&油豆腐"
    def on_enter_eggandtofu(self, event):
        send_eggandtofuimage(event)
        #self.advance(event)
    
    #backmenu
    def is_going_to_backmenu(self, event):
        text = event.message.text
        return text == '繼續看菜單'
    def on_enter_backmenu(self, event):
        send_button_menu(event)
        

    #information
    def is_going_to_information(self, event):
        text = event.message.text
        return text == "店家資訊"
    def on_enter_information(self, event):
        send_button_information(event)

    #backinformation
    def is_going_to_backinformation(self, event):
        text = event.message.text
        return text == "繼續查看"
    def on_enter_backinformation(self, event):
        send_button_information(event)

    #businesshours
    def is_going_to_businesshours(self, event):
        text = event.message.text
        return text == "營業時間"
    def on_enter_businesshours(self, event):
        #message="星期一	17:30~01:00\n"+"星期二	17:30~01:00\n"+"星期三	17:30~01:00\n"+"星期四	17:30~01:00\n"+"星期五	17:30~01:00\n"+"星期六	休息\n"+"星期日	休息"
        send_button_businesshours(event)

    #phonenum
    def is_going_to_phonenum(self, event):
        text = event.message.text
        return text == "電話"
    def on_enter_phonenum(self, event):
        send_button_phonenum(event)
        

    #address
    def is_going_to_address(self, event):
        text = event.message.text
        return text == "地址"
    def on_enter_address(self, event):
        #address = "710台南市永康區中山南路96號\n"+"https://maps.app.goo.gl/4qdsojWRtQQkDZP48?g_st=ic"
        send_button_address(event)
        
    #promotion
    def is_going_to_promotion(self, event):
        text = event.message.text
        return text == "當月活動"
    def on_enter_promotion(self, event):
        send_button_promotion(event)

    #discount
    def is_going_to_discount(self, event):
        text = event.message.text
        return text == "促銷"
    def on_enter_discount(self, event):
        send_button_discount(event)

    #backpromotion
    def is_going_to_backpromotion(self, event):
        text = event.message.text
        return text == "繼續"
    def on_enter_backpromotion(self, event):
        pass
        
        
    #order
    def is_going_to_order(self, event):
        text = event.message.text
        return text == "訂餐"
    def on_enter_order(self, event):
        send_button_order(event)

    #asknum
    def is_going_to_asknum(self, event):
        text = event.message.text
        if(text == "當歸土虱頭" or text == "當歸土虱中" or text == "當歸土虱尾" or text == "白飯"
        or text == "藥頭排骨" or text == "土虱蛋(大)" or text == "土虱蛋(小)"
        or text == "肉燥飯" or text == "滷蛋" or text == "油豆腐"):
            self.food = text
        return (text == "當歸土虱頭" or text == "當歸土虱中" or text == "當歸土虱尾" or text == "白飯"
        or text == "藥頭排骨" or text == "土虱蛋(大)" or text == "土虱蛋(小)"
        or text == "肉燥飯" or text == "滷蛋" or text == "油豆腐")
    def on_enter_asknum(self, event):
        send_button_asknum(event)

     #record
    def is_going_to_record(self, event):
        text = event.message.text
        self.orderlist[self.food] = text
        return (text == "1" or text == "2" or text == "3" or text == "4"
        or text == "5" or text == "6" or text == "7" or text == "8"
        or text == "9" or text == "0")
    def on_enter_record(self, event):
        message = "你目前點了"+self.orderlist[self.food]+"個"+self.food+"\n"
        if(self.orderlist["當歸土虱頭"]!="0" and "當歸土虱頭"!=self.food):
            message+=self.orderlist["當歸土虱頭"]+"個當歸土虱頭"+"\n"
        if(self.orderlist["當歸土虱中"]!="0" and "當歸土虱中"!=self.food):
            message+=self.orderlist["當歸土虱中"]+"個當歸土虱中"+"\n"
        if(self.orderlist["當歸土虱尾"]!="0" and "當歸土虱尾"!=self.food):
            message+=self.orderlist["當歸土虱尾"]+"個當歸土虱尾"+"\n"
        if(self.orderlist["藥頭排骨"]!="0" and "藥頭排骨"!=self.food):
            message+=self.orderlist["藥頭排骨"]+"個藥頭排骨"+"\n"
        if(self.orderlist["土虱蛋(小)"]!="0" and "土虱蛋(小)"!=self.food):
            message+=self.orderlist["土虱蛋(小)"]+"個土虱蛋(小)"+"\n"
        if(self.orderlist["土虱蛋(大)"]!="0" and "土虱蛋(大)"!=self.food):
            message+=self.orderlist["土虱蛋(大)"]+"個土虱蛋(大))"+"\n"
        if(self.orderlist["肉燥飯"]!="0" and "肉燥飯"!=self.food):
            message+=self.orderlist["肉燥飯"]+"個肉燥飯"+"\n"
        if(self.orderlist["白飯"]!="0" and "白飯"!=self.food):
            message+=self.orderlist["白飯"]+"個白飯"+"\n"
        if(self.orderlist["滷蛋"]!="0" and "滷蛋"!=self.food):
            message+=self.orderlist["滷蛋"]+"個滷蛋"+"\n"
        if(self.orderlist["油豆腐"]!="0" and "油豆腐"!=self.food):
            message+=self.orderlist["油豆腐"]+"個油豆腐"+"\n"
        message += "你還要點什麼嗎?"
        send_button_keepordering(event,message)
        

    #orderfinish
    def is_going_to_orderfinish(self, event):
        text = event.message.text
        return self.food!='?' and text == '訂餐完成' 
    def on_enter_orderfinish(self, event):
        message = "你總共點了"+self.orderlist[self.food]+"個"+self.food+"\n"
        cost = eval(self.orderlist[self.food])*self.price[self.food]
        if(self.orderlist["當歸土虱頭"]!="0" and "當歸土虱頭"!=self.food):
            message+=self.orderlist["當歸土虱頭"]+"個當歸土虱頭"+"\n"
            cost += eval(self.orderlist["當歸土虱頭"])*self.price["當歸土虱頭"]
        if(self.orderlist["當歸土虱中"]!="0" and "當歸土虱中"!=self.food):
            message+=self.orderlist["當歸土虱中"]+"個當歸土虱中"+"\n"
            cost += eval(self.orderlist["當歸土虱中"])*self.price["當歸土虱中"]
        if(self.orderlist["當歸土虱尾"]!="0" and "當歸土虱尾"!=self.food):
            cost += eval(self.orderlist["當歸土虱尾"])*self.price["當歸土虱尾"]
            message+=self.orderlist["當歸土虱尾"]+"個當歸土虱尾"+"\n"
        if(self.orderlist["藥頭排骨"]!="0" and "藥頭排骨"!=self.food):
            message+=self.orderlist["藥頭排骨"]+"個藥頭排骨"+"\n"
            cost += eval(self.orderlist["藥頭排骨"])*self.price["藥頭排骨"]
        if(self.orderlist["土虱蛋(小)"]!="0" and "土虱蛋(小)"!=self.food):
            message+=self.orderlist["土虱蛋(小)"]+"個土虱蛋(小)"+"\n"
            cost += eval(self.orderlist["土虱蛋(小)"])*self.price["土虱蛋(小)"]
        if(self.orderlist["土虱蛋(大)"]!="0" and "土虱蛋(大)"!=self.food):
            message+=self.orderlist["土虱蛋(大)"]+"個土虱蛋(大))"+"\n"
            cost += eval(self.orderlist["土虱蛋(大)"])*self.price["土虱蛋(大)"]
        if(self.orderlist["肉燥飯"]!="0" and "肉燥飯"!=self.food):
            message+=self.orderlist["肉燥飯"]+"個肉燥飯"+"\n"
            cost += eval(self.orderlist["肉燥飯"])*self.price["肉燥飯"]
        if(self.orderlist["白飯"]!="0" and "白飯"!=self.food):
            message+=self.orderlist["白飯"]+"個白飯"+"\n"
            cost += eval(self.orderlist["白飯"])*self.price["白飯"]
        if(self.orderlist["滷蛋"]!="0" and "滷蛋"!=self.food):
            message+=self.orderlist["滷蛋"]+"個滷蛋"+"\n"
            cost += eval(self.orderlist["滷蛋"])*self.price["滷蛋"]
        if(self.orderlist["油豆腐"]!="0" and "油豆腐"!=self.food):
            message+=self.orderlist["油豆腐"]+"個油豆腐"+"\n"
            cost += eval(self.orderlist["油豆腐"])*self.price["油豆腐"]
        message += "一共" + str(cost) +"元"
        send_button_orderfinish(event,message)
        self.food = '?'
        self.orderlist["當歸土虱頭"]='0'
        self.orderlist["當歸土虱中"]='0'
        self.orderlist["當歸土虱尾"]='0'
        self.orderlist["藥頭排骨"]='0'
        self.orderlist["土虱蛋(小)"]='0'
        self.orderlist["土虱蛋(大)"]='0'
        self.orderlist["白飯"]='0'
        self.orderlist["肉燥飯"]='0'
        self.orderlist["油豆腐"]='0'
        self.orderlist["滷蛋"]='0'
        

    #backorder
    def is_going_to_backorder(self, event):
        text = event.message.text
        return text == '返回' or text == '繼續訂餐'
    def on_enter_backorder(self, event):
        pass

    
        
        
    
