class Huzas:
    def __init__(self, huzas: int = 0, ev: int = 0, het: int = 0, szam: int = 0):
        self.huzas = int(huzas)
        self.ev = int(ev)
        self.het = int(het)
        self.szam = int(szam)

    def __str__(self):
        return f"Húzás: {self.huzas}, Év: {self.ev}, Hét: {self.het}, Szám: {self.szam}"

        