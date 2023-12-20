from tekoaly import Tekoaly
from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu

class KiviPaperiSakset:
    def __init__(self):
        self.tuomari = Tuomari()
        self.tekoaly = Tekoaly()
        self.parempi_tekoaly = TekoalyParannettu(10)
        self.pelimuoto = -1

    def pelaa(self, pelimuoto):
        self.pelimuoto = pelimuoto
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self.tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(self.tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        if self.pelimuoto == 0:
            return input("Toisen pelaajan siirto: ")

        elif self.pelimuoto == 1:
            tekoalyn_siirto = self.tekoaly.anna_siirto()

            print(f"Tietokone valitsi: {tekoalyn_siirto}")
            return tekoalyn_siirto

        else:
            tekoalyn_siirto = self.parempi_tekoaly.anna_siirto()

            print(f"Tietokone valitsi: {tekoalyn_siirto}")
            self.parempi_tekoaly.aseta_siirto(ensimmaisen_siirto)
            return tekoalyn_siirto

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
