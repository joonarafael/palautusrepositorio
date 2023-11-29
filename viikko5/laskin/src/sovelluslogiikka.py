class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self.vanha_arvo = None

    def miinus(self, operandi):
        self.vanha_arvo = self._arvo
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self.vanha_arvo = self._arvo
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self.vanha_arvo = self._arvo
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def kumoa(self):
        self._arvo = self.vanha_arvo

    def arvo(self):
        return self._arvo
