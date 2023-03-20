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
            return Pasutijums(klients, ediens, viesmilis, self._virtuve)
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
    _nosaukums: str
class Recepte:
    _sastavdalas: 'list[Sastavdala]'
    _instrukcijas: 'list[str]'
    def __init__(self) -> None:
        self._sastavdalas = []
        self._instrukcijas = []
    def AprekinamIzmaksas(self) -> float:
        kopIzmaksas = 0.0
        for sastavdala in self._sastavdalas:
            kopIzmaksas += sastavdala._izmaksas
        return kopIzmaksas

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
    _virtuve: 'Virtuve'
    def __init__(self, klients: Klients, receptes: 'list[Recepte]', viesmilis: Viesmilis, virtuve: 'Virtuve') -> None:
        self._klients = klients
        self._receptes = receptes
        self._viesmilis = viesmilis
        self._virtuve = virtuve
    def AprekinamIzmaksas(self) -> float:
        kopIzmaksas = 0.0
        for recepte in self._receptes:
            kopIzmaksas += recepte.AprekinamIzmaksas()
        return kopIzmaksas
    def Izpildam(self):
        izmaksas = self.AprekinamIzmaksas()
        if self._klients._pieejamaNauda < izmaksas:
            print("Klientam nepietiek naudas!")
            return
        else:
            self._klients._pieejamaNauda -= izmaksas
            return self._virtuve.Gatavot(self._receptes)

class Virtuve:
    _sastavdalas: 'dict[Sastavdala, int]'
    def __init__(self) -> None:
        self._sastavdalas = {}
    def Gatavot(self, ediens: 'list[Recepte]') -> 'list[Ediens]':
        # Te vajadzētu piesaistīt pavāru. Mēs to šajā versijā nedarīsim.
        pagatavotaisEdiens = []
        for recepte in ediens:
            # Pārbaudam vai vispār pietiek sastāvdaļas
            for sastavdala in recepte._sastavdalas:
                if self._sastavdalas[sastavdala] < 1:
                    print("Nepietiek sastāvdaļas!")
            # Izmantojam sastāvdaļas
            for sastavdala in recepte._sastavdalas:
                self._sastavdalas[sastavdala] -= 1

            pagEdiens = Ediens()
            pagEdiens._sastavdalas = recepte._sastavdalas
            pagatavotaisEdiens.append(pagEdiens)
        return pagatavotaisEdiens

udens = Sastavdala()
udens._izmaksas = 0.2
udens._nosaukums = "Ūdens"
kartupeli = Sastavdala()
kartupeli._izmaksas = 0.6
kartupeli._nosaukums = "Kartupeļi"
virtuve = Virtuve()
virtuve._sastavdalas[udens] = 2
virtuve._sastavdalas[kartupeli] = 3

Janis = Pavars()
Mikelis = Viesmilis()
restorans = Restorans(virtuve)
restorans._darbinieki.append(Janis)
restorans._darbinieki.append(Mikelis)
Mikelis._dzeramnauda = 200

recepte = Recepte()
recepte._sastavdalas.append(udens)
recepte._sastavdalas.append(kartupeli)
recepte._instrukcijas.append("Vārīt ūdeni")
recepte._instrukcijas.append("...")

klients = Klients()
klients._pieejamaNauda = 200.0

pasutijums = restorans.PirktEdienu(klients, [recepte])
ediens = pasutijums.Izpildam()
print(f"Klients nopirka {len(ediens)} ēdienus. Klientam palika {klients._pieejamaNauda} naudiņas!")
for sastavdala in restorans._virtuve._sastavdalas:
    print(f"Palika sastavdala {sastavdala._nosaukums}: {restorans._virtuve._sastavdalas[sastavdala]}")
