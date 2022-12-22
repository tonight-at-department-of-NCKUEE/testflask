

# 汽車類別
class Cars:
    # 建構式
    def __init__(self):
        self.color = "無"  # 顏色屬性
        self.seat = "無"  # 座位屬性
    # 方法(Method)
    def drive(self):
        self.color = "綠"
        print(f"My car is {self.color} and {self.seat} seats.{1+eval('10')}")
 
c = Cars()
c.drive()
