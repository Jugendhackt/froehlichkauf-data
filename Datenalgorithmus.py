class Produkt():
    def __init__(self, Name, Inhaltsstoffe, Nährwerte, Verpackung, Herkunftsort, Herstellungsbedingungen, reusable = False):
        self.Inhaltsstoffe = Inhaltsstoffe #Liste
        self.Nährwerte = Nährwerte #Liste, pro 100 Gramm, [Brennwert in kj, Fett g, Kohlenhydrate g, Zucker g, Eiweiß g, Salz g]
        self.Verpackung = Verpackung # Plastik oder Papier
        self.Herkunftsort = Herkunftsort #nach Entfernung
        self.Herstellungsbedingungen = Herstellungsbedingungen #Info über Firma insgesamt, 0 (schlecht) bis 5 (gut)

#Bio und Fairtrade

Land_des_Einkäufers = "DE"

Produkt("nippon", [], [2229, 30.1, 58.9, 40.2, 5.6, 0.22], 0, "DE", 0)

Gefährliche_Inhaltsstoffe: {}

def Gesundheit(Produkt):

def Umwelt(Produkt):
    #Herkunftsort, selbes Land ist gut
    if Land_des_Einkäufers == Produkt.Herkunftsort:


def Ethik(Produkt):
    return Produkt.Herstellungsbedingungen #