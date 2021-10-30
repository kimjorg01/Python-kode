import tkinter
from tkinter import messagebox
import random

# Kode for å lage et spill hvor spilleren skal gjette hvilket tall datamaskinen har valgt (tilfeldig)

class GjettTalletSpill:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.hovedvindu.title("Gjett tallet spill")
        self.forklaring = tkinter.Label(self.hovedvindu, text="Gjett et tall fra 1 til 1000:")
        self.forklaring.grid(column=0, row=0)
        self.tallfelt = tkinter.Entry(self.hovedvindu, width=6)
        self.tallfelt.grid(column=1, row=0)
        self.beskjed = tkinter.StringVar()
        self.beskjed.set("Dette er ditt første forsøk")
        self.beskjed_felt = tkinter.Label(self.hovedvindu, textvariable=self.beskjed)
        self.beskjed_felt.grid(column=0, row=1, columnspan=2)
        self.knapp = tkinter.Button(self.hovedvindu, text="Gjett tall", command=self.knapp_callback)
        self.knapp.grid(column=0, row=2, columnspan=2)

        self.mitt_Tall = random.randint(1, 1000)
        self.forrige_gjett = -5000
        self.antall_forsok = 0
        print(self.mitt_Tall)

        tkinter.mainloop()

    def les_tall(self):
        teksten = self.tallfelt.get()
        tallet = -1
        try:
            tallet = int(teksten)
        except ValueError:
            messagebox.showerror("Ulovlig verdi", "Du må skrive et lovlig tall")
        return tallet

    def knapp_callback(self):
        tallet = self.les_tall()
        if tallet >= 0:
            self.antall_forsok += 1
            resultat = ""
            if tallet == self.mitt_Tall:
                messagebox.showinfo("Seier!", f"Gratulerer! Du gjettet riktig! Du brukte {self.antall_forsok} forsøk")
                self.hovedvindu.destroy()
            if tallet < self.mitt_Tall:
                resultat += "Du gjettet lavere enn mitt tall"
            else:
                resultat += "Du gjettet høyere enn mitt tall"
            if abs(tallet-self.mitt_Tall) < abs(self.forrige_gjett-self.mitt_Tall):
                resultat += " og du er nærmere enn sist gang"
            else:
                resultat += " og du er lengre unna enn sist gang"
            self.forrige_gjett = tallet
            resultat += f". Du har brukt {self.antall_forsok} forsøk."
            self.beskjed.set(resultat)


if __name__ == "__main__":
    gui = GjettTalletSpill()