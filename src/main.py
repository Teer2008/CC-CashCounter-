from time import sleep
import sys
import pickle, os
import glob

class Rechner:
    def __init__(self, ziel, ziel_float, DerzeitigerStand, DerzeitigerStand_float, Geld_Benötigt, Geld_Benötigt_str, Schell_Input, object_name, save_object, speicher_frage, datei_name, speicherungs_name, object_saves, save, cash_save, o_save):
        self.ziel = ziel
        self.ziel_float = ziel_float
        self.DerzeitigerStand = DerzeitigerStand
        self.DerzeitigerStand_float = DerzeitigerStand_float
        self.Geld_Benötigt = Geld_Benötigt
        self.Geld_Benötigt_str = Geld_Benötigt_str
        self.Schell_Input = Schell_Input
        self.object_name = object_name
        self.save_object = save_object
        self.speicher_frage = speicher_frage
        self.datei_name = datei_name
        self.speicherungs_name = speicherungs_name
        self.object_saves = object_saves
        self.save = save
        self.cash_save = cash_save
        self.o_save = o_save

    def Ziel_Input(self):
        self.ziel = input(str("Ziel eingeben(Bitte nur Zahlen): "))
        self.ziel_float = float(self.ziel)

    def DerzeitigerStand_Input(self):
        self.DerzeitigerStand = input(str("Jetzigen Geldstand eintragen(Bitte nur Zahlen): "))
        self.DerzeitigerStand_float = float(self.DerzeitigerStand)
        cash_counter.SpeicherungsfrageCash()

    def Benötigt_End(self):
        self.Geld_Benötigt = self.ziel_float - self.DerzeitigerStand_float
        self.Geld_Benötigt_str = str(self.Geld_Benötigt)
        print("Du benötigst noch " + self.Geld_Benötigt_str)

    def Bezeichnung_Object(self):
        self.object_name = input(str("Objekt Name eingeben: "))

    def SpeichernDesObjekts(self):
        self.save_object = [self.object_name, self.ziel, self.speicherungs_name]
        pickle.dump(self.save_object, open(self.speicherungs_name, "wb"))

    def SpeichernCashUpdate(self):
        self.save_object = [self.speicherungs_name]
        pickle.dump(self.save_object, open(self.speicherungs_name, "wb"))

    def Speicherungsfrage(self):
        self.speicher_frage = input(str("Speichern?(y/n)"))
        if self.speicher_frage == "y":
            self.speicherungs_name = (self.object_name + " " + self.ziel + ".ccs")
            cash_counter.SpeichernDesObjekts()
        if self.speicher_frage == "n":
            pass

    def SpeicherungsfrageCash(self):
        self.speicher_frage = input(str("Speichern?(y/n)"))
        if self.speicher_frage == "y":
            self.cash_save = glob.glob('*.ccca')
            for self.o_save in self.cash_save:
                self.datei_name = self.o_save
                os.remove(self.datei_name)
            self.speicherungs_name = (self.DerzeitigerStand + "€" + ".ccca")
            cash_counter.SpeichernCashUpdate()
        if self.speicher_frage == "n":
            pass

    def Main(self):
        while True:
            self.Schell_Input = input(str("Navigation(help für Befehlsliste: )"))

            if self.Schell_Input == "help":
                os.system("cls")
                print("\nB E F E H L S L I S T E:\n\nexit\nnew object\nclear\nlist all\ndelete object\ncash update\ncash list\n\n")

            if self.Schell_Input == "exit":
                os.system("cls")
                cash_counter.Schell_Func_Exit()

            if self.Schell_Input == "new object":
                os.system("cls")
                cash_counter.Schell_Func_new_object()

            if self.Schell_Input == "clear":
                os.system("cls")

            if self.Schell_Input == "list all":
                os.system("cls")
                cash_counter.program_boot()

            if self.Schell_Input == "delete object":
                os.system("cls")
                cash_counter.Shell_Func_Delete_Object()

            if self.Schell_Input == "cash update":
                os.system("cls")
                cash_counter.cash_update()

            if self.Schell_Input == "cash list":
                os.system("cls")
                cash_counter.Current_Cash_Boot()

    def Schell_Func_Exit(self):
            sys.exit()
    
    def Schell_Func_new_object(self):
        cash_counter.Ziel_Input()
        cash_counter.Bezeichnung_Object()
        cash_counter.Speicherungsfrage()

    def Shell_Func_Delete_Object(self):
        self.datei_name = input(str("Datei Name(Mit Endung)"))
        os.remove(self.datei_name)

    def cash_update(self):
        cash_counter.DerzeitigerStand_Input()

    def program_boot(self):
        self.object_saves = glob.glob('*.ccs')
        for self.save in self.object_saves:
            print(self.save)

    def Current_Cash_Boot(self):
        self.cash_save = glob.glob('*.ccca')
        for self.o_save in self.cash_save:
            print(self.o_save)

cash_counter = Rechner(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
cash_counter.Main()
