class viagem:
    def __init__(self):
        self.km = 0
        self.th = ""
        self.tm = ""
    def vm(self):
        tg = self.th + (self.tm/60)
        return self.km/tg
    
goncalo = viagem()
goncalo.km = int(input())
goncalo.th, goncalo.tm = map(int,input().split(":"))
# print (goncalo.th, goncalo.tm)
b = goncalo.vm()
print (b)