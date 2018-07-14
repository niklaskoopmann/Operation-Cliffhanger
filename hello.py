# -*- coding: utf-8 -*-

# class for places
class Ort:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung
        self.nach = {}

richtungen = ("norden", "süden", "osten", "westen", "oben", "unten")

bar = Ort(
	"Die Bar",
	"Du nichtnütziges Stück Schafscheiße sitzt mal wieder seit Stunden in der Bar und kippst dir billigen Fusel hinter die Binde. Du kannst hier entweder weiter rumsitzen und saufen oder du verlässt die Bar nach Süden und erlebst vielleicht noch mal irgendwas.")

strasse = Ort(
	"Die Straße vor der Bar",
	"Du stehst (wankst) auf dem Bürgersteig vor der Bar.")

bar.nach["süden"] = strasse
strasse.nach["norden"] = bar

aktuellerOrt = bar

# geklaute druck-Funktion, die print ersetzt
def druck(s="", width=80):
    column = 0
    for word in str(s).split():
        column += len(word) + 1
        if column > width:
            column = len(word) + 1
            print()
        print (word, end=" ")
    print()

def ortBeschreiben(ort):
	druck()
	druck(ort.name)
	druck()
	druck(ort.beschreibung)
	druck()

def ortBetreten(ort):
	global aktuellerOrt
	aktuellerOrt = ort
	ortBeschreiben(ort)

# geklaute Eingabe-Funktion
def anweisung():
    return [word.lower() for word in input("? ").rstrip(".?!").split()]

# SPIELEN!
def spiel():
	ortBetreten(bar)
	# todo

spiel()