str = "Not Class Member"

class GString:
    def __init__(self):
        #인스터스 멤버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #파이썬은 명확학 코딩하는 것이 좋다
        print(self.str)

#인스턴스(복사본)
g = GString()
g.set("First Message")
g.print()
