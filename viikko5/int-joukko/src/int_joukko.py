class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("kapasiteetti2")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, target):
        """check if target exists in sequence"""
        if target in self.lukujono:
            return True
        else:
            return False

    def lisaa(self, target):
        """add new item if it does not exist already"""
        if self.kuuluu(target):
            return False

        self.lukujono[self.alkioiden_lkm] = target
        self.alkioiden_lkm += 1

        if self.alkioiden_lkm == len(self.lukujono):
            taulukko_old = self.lukujono
            self.kopioi_lista(self.lukujono, taulukko_old)
            self.lukujono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_lista(taulukko_old, self.lukujono)

        return True

    def poista(self, target):
        """remove item"""
        try:
            kohta = self.lukujono.index(target)
        except ValueError:
            return False

        self.lukujono[kohta] = 0

        for j in range(kohta, self.alkioiden_lkm - 1):
            apu = self.lukujono[j]
            self.lukujono[j] = self.lukujono[j + 1]
            self.lukujono[j + 1] = apu

        self.alkioiden_lkm -= 1

        return True

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdiste_joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdiste_joukko.lisaa(b_taulu[i])

        return yhdiste_joukko

    @staticmethod
    def leikkaus(a, b):
        leikkaus_juokko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus_juokko.lisaa(b_taulu[j])

        return leikkaus_juokko

    @staticmethod
    def erotus(a, b):
        erotus_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            erotus_joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotus_joukko.poista(b_taulu[i])

        return erotus_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
