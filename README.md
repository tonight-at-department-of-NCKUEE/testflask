# 土虱嫂(開元分店) 
![](https://i.imgur.com/YbQmow4.png)

主頁面有四個服務選項可供選擇，菜單、店家資訊、當月活動、訂餐，每個選項都以輪盤按鈕的設計來方便使用者選擇不同的選項。使用者只要按下按鈕即可使用各項功能，不用打字輸入，非常方便！

**Line Bot 主要由三個部分所組成**

LINE Bot：透過官方提供的各種 LINE Messaging API 指令來編碼

後端：使用 Flask 構建後端來處理 webhook

FSM：為每個使用者個別建立 python transitions 套件所提供的 FSM，用以管理各使用者當前的狀態

## FSM
![](https://i.imgur.com/3e91rou.png)
## Feature
**菜單**
點擊各項餐點可以觀看圖片
![](https://i.imgur.com/gd85p3q.png)

例如:

當歸土虱

![](https://i.imgur.com/tDmcdoY.png)

藥頭排骨

![](https://i.imgur.com/wpUc2iw.png)


**店家資訊**

點擊按鈕可取得資訊

![](https://i.imgur.com/wL1lwoO.png)

例如:

營業資訊

![](https://i.imgur.com/yS6Xfkt.png)


**當月活動**

![](https://i.imgur.com/tfyhggq.png)



**訂餐**

![](https://i.imgur.com/thycguA.png)
⬆點選要吃的餐點

![](https://i.imgur.com/v9GD3kn.png)
⬆然後選擇份量

![](https://i.imgur.com/9N4I5cl.png)
⬆系統會紀錄並顯示現在點了哪些餐點(由左而右閱讀)

![](https://i.imgur.com/k5o8vO2.png)
⬆點完餐以後按完成訂餐，系統會計算總金額並顯示出來

**其他**

![](https://i.imgur.com/hDaPP6S.png)
⬆完成各項服務後按回主頁即可回到原始畫面並查看其他資訊

## Reference

1. [土虱嫂(開元分店)](https://www.google.com/maps/place/%E5%9C%9F%E8%99%B1%E5%AB%82(%E9%96%8B%E5%85%83%E5%88%86%E5%BA%97)/@23.0127898,120.2246157,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76de0e2cc205:0xb0bffa92850327e1!8m2!3d23.0128171!4d120.2290911) 提供店內餐點圖片與各項資訊 
2. render.com 提供網路伺服器服務
3. [Line bot sdk](https://github.com/line/line-bot-sdk-python) official documentation
