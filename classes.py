class Galds:
    krasa = ""
    def __init__(self):
        self.krasa="sarkana"
    def iegutKrasu(self):
        return self.krasa
class StiklaGalds(Galds):
    mainigais = 0
    def __init__(self):
        self.krasa="zala"
    def funkc():
        return 0
class KokaGalds(Galds):
    mainigais2 = 0
    def funkc2():
        return 0

galds = StiklaGalds()
galds.krasa
galds2 = Galds()
galds3 = StiklaGalds()

class Ekrans:
    izkirtspejaX = 1080
    izpirtspejaY = 1920
    def IegutPikseluSkaitu(self):
        return self.izkirtspejaX * self.izpirtspejaY
class Viedtalrunis:
    ekrans: Ekrans
    def __init__(self) -> None:
        self.ekrans = Ekrans()

viedtalr = Viedtalrunis()
viedtalr.ekrans.izkirtspejaX = 1000
print(viedtalr.ekrans.IegutPikseluSkaitu())