class viagem:
    def __init__(self):
        self.km = 0
        self.tg = "hh/mm"
    def vm(self):
        return self.km/self.tg
    
goncalo = viagem()
goncalo.km = int(input())
goncalo.tg = int(input().split("/"))
b = goncalo.vm()
print (b)