class Restorans:
    _darbinieki: 'list[Darbinieks]'
    _virtuve: 'Virtuve'
    def __init__(self, virtuve: 'Virtuve') -> None:
        self._darbinieki = []
        self._virtuve = virtuve
    def AprekinamAlgas(self) -> float:
        kopAlga = 0.0
        for darbinieks in self._darbinieki:
            kopAlga += darbinieks.IzvadamAlgu()
        return kopAlga
    def PirktEdienu(self, klients: 'Klients', ediens: 'list[Recepte]') -> 'Pasutijums':
        for darbinieks in self._darbinieki:
            if type(darbinieks) is Viesmilis:
                if not darbinieks._kaduApkalpo:
                    viesmilis = darbinieks
                    break
        if 'viesmilis' not in locals():
            print("Kluda: nav pieejami viesmili")
        else:
            viesmilis._kaduApkalpo = True
            return Pasutijums(klients, ediens, viesmilis)
class Darbinieks:
    _alga: float = 100.0
    def __init__(self) -> None:
        pass
    def IzvadamAlgu(self) -> float:
        return self._alga
class Pavars(Darbinieks):
    _alga: float = 200.0
    def __init__(self) -> None:
        pass
class Viesmilis(Darbinieks):
    _dzeramnauda: float = 0.0
    _alga: float = 150.0
    _kaduApkalpo: bool = False
    def __init__(self) -> None:
        super().__init__()
    def IzvadamAlgu(self) -> float:
        return super().IzvadamAlgu() + self._dzeramnauda
class Sastavdala:
    _izmaksas: float = 0.0
class Recepte:
    _sastavdalas: 'list[Sastavdala]'
    _instrukcijas: 'list[str]'
    def __init__(self) -> None:
        self._sastavdalas = []
        self._instrukcijas = []
class Ediens:
    _sastavdalas: 'list[Sastavdala]'
    def __init__(self) -> None:
        self._sastavdalas = []
    def AprekinamIzmaksas(self) -> float:
        kopIzmaksas = 0.0
        for sastavdala in self._sastavdalas:
            kopIzmaksas += sastavdala._izmaksas
        return kopIzmaksas
class Klients:
    _pieejamaNauda: float = 0.0
class Pasutijums:
    _klients: Klients
    _receptes: 'list[Recepte]'
    _viesmilis: Viesmilis
    def __init__(self, klients: Klients, receptes: 'list[Recepte]', viesmilis: Viesmilis) -> None:
        self._klients = klients
        self._receptes = receptes
        self._viesmilis = viesmilis
    def AprekinamIzmaksas(self) -> float:
        kopIzmaksas = 0.0
        for recepte in self._receptes:
            kopIzmaksas += recepte._izmaksas
        return kopIzmaksas
class Virtuve:
    _sastavdalas: 'list[Sastavdala]'
    def Gatavot(pavars: Pavars, ediens: Ediens) -> None:
        pass

Janis = Pavars()
Mikelis = Viesmilis()
virtuve = Virtuve()
restorans = Restorans(virtuve)
restorans._darbinieki.append(Janis)
restorans._darbinieki.append(Mikelis)
Mikelis._dzeramnauda = 200

udens = Sastavdala()
udens._izmaksas = 0.2
kartupeli = Sastavdala()
kartupeli._izmaksas = 0.6
recepte = Recepte()
recepte._sastavdalas.append(udens)
recepte._sastavdalas.append(kartupeli)
recepte._instrukcijas.append("Vārīt ūdeni")
recepte._instrukcijas.append("...")

klients = Klients()
klients._pieejamaNauda = 200.0

pasutijums = restorans.PirktEdienu(klients, [recepte])
print(Mikelis._kaduApkalpo)

# TODO: Pabeigt pirkuma secību
# Virtuvē jāpabeidz gatavot, jānomaina _kaduApkalpo uz False
# Jāatgriež list[Ēdiens]