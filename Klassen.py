# Aufgabe 1: Ersetzen von initialisiere() durch __init__() in Autoklasse
class Autoklasse:
    def __init__(self):
        self.geschwindigkeit = 150

print("--- Aufgabe 1 ---")
auto1 = Autoklasse()
print(f"Geschwindigkeit von auto1: {auto1.geschwindigkeit}")



# Aufgabe 2: Aufruf von __str__() der Basisklasse über super()
class ErstellteKlasse:
    def __str__(self):
        return "Dies ist die __str__-Methode der Erstellten Klasse."

class AbgeleiteteKlasse(ErstellteKlasse):
    def __str__(self):
        ausgabe = super().__str__()
        return f"{ausgabe} Und dies ist die __str__-Methode der abgeleiteten Klasse."

print("\n--- Aufgabe 2 ---")
instanz_aufgabe2 = AbgeleiteteKlasse()
print(instanz_aufgabe2)



# Aufgabe 3: Vererbung mit magischen Methoden für Bären
class Baer:
    def __init__(self, gewicht, alter):
        self.gewicht = gewicht
        self.alter = alter

    def __str__(self):
        return f"Das Gewicht beträgt {self.gewicht} kg und das Alter {self.alter} Jahre."

class ElternBaer(Baer):
    def __init__(self, gewicht, alter, anzahl_kinder):
        super().__init__(gewicht, alter)
        self.anzahl_kinder = anzahl_kinder

    def __str__(self):
        return f"{super().__str__()} Der Bär hat {self.anzahl_kinder} Kinder."

print("\n--- Aufgabe 3 ---")
baer = Baer(250, 6)
print(baer)

eltern_baer = ElternBaer(100, 3, 2)
print(eltern_baer)



# Aufgabe 4: Klassen Katze und ElternKatze mit Operator
class Katze:
    def __init__(self, groesse, gewicht):
        self.groesse = groesse
        self.gewicht = gewicht

    def __str__(self):
        return f"Die Größe der Katze ist {self.groesse} und das Gewicht ist {self.gewicht} kg."

    def __add__(self, gewichts_aenderung):
        self.gewicht += gewichts_aenderung
        return self

    def __sub__(self, gewichts_aenderung):
        self.gewicht -= gewichts_aenderung
        return self

class ElternKatze(Katze):
    def __init__(self, groesse, gewicht, anzahl_kinder):
        super().__init__(groesse, gewicht)
        self.anzahl_kinder = anzahl_kinder

    def __str__(self):
        return f"{super().__str__()} Die Anzahl der Kinder beträgt {self.anzahl_kinder}."

    def __add__(self, kinder_aenderung):
        if isinstance(kinder_aenderung, int):
            self.anzahl_kinder += kinder_aenderung
        return self

    def __sub__(self, kinder_aenderung):
        if isinstance(kinder_aenderung, int):
            self.anzahl_kinder -= kinder_aenderung
        return self

print("\n--- Aufgabe 4 ---")
katze = Katze("30 cm", 4)
print(katze)
katze = katze + 1
print(katze)
katze = katze - 0.5
print(katze)

eltern_katze = ElternKatze("40 cm", 6, 3)
print(eltern_katze)
eltern_katze = eltern_katze + 0.8 # Gewicht erhöhen (geerbt)
print(eltern_katze)
eltern_katze = eltern_katze + 1 # Anzahl Kinder erhöhen
print(eltern_katze)
eltern_katze = eltern_katze - 1 # Anzahl Kinder reduzieren
print(eltern_katze)
        

    


