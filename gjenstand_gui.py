import tkinter
from tkinter import messagebox

# Gjenstand klassen består av 4 inputs/verdier:

# navn: hva heter gjenstander/ hva er gjenstanden

# fra_aar og til_aar: hvilken tid er gjenstanden fra? Hvis vi ikke vet eksakt,
#  hvilke årstall befinner gjenstanden seg mellom?

# sted: hvor er gjenstanden fra? F.eks: Rogaland, Sandnes...

#GUI til gjenstand lager et vindu hvor man kan skrive inn for de 4 inputtene/verdiene
# i klassen Gjenstand

# Det lages en liste som lagrer gjenstandene, og disse printes når vinduet lukkes.

class Gjenstand:
    def __init__(self, navn, fra_aar, til_aar, sted):
        self.navn = navn
        self.fra_aar = fra_aar
        self.til_aar = til_aar
        self.sted = sted

    def __str__(self):
        if self.fra_aar == self.til_aar:
            return f"{self.navn} fra år {self.fra_aar} fra {self.sted}"
        return f"{self.navn} fra tidsperiode (år {self.fra_aar}-{self.til_aar}) fra {self.sted}"

class GjenstandGUI:
    def __init__(self):
        self.gjenstander = []

        self.hovedvindu = tkinter.Tk()

        self.navn = tkinter.Label(self.hovedvindu, text="Navn på gjenstanden:")
        self.navn.grid(column=0, row=0)
        self.navn_felt = tkinter.Entry(self.hovedvindu, width=10)
        self.navn_felt.grid(column=1, row=0)

        self.tidligste_aar = tkinter.Label(self.hovedvindu, text="Tidligste år:")
        self.tidligste_aar.grid(column=0, row=1)
        self.tidlig_aar_felt = tkinter.Entry(self.hovedvindu, width=10)
        self.tidlig_aar_felt.grid(column=1, row=1)

        self.seneste_aar = tkinter.Label(self.hovedvindu, text="Seneste år:")
        self.seneste_aar.grid(column=0, row=2)
        self.senest_aar_felt = tkinter.Entry(self.hovedvindu, width=10)
        self.senest_aar_felt.grid(column=1, row=2)

        self.gjenstand_fra = tkinter.Label(self.hovedvindu, text="Hvor er gjenstanden fra:")
        self.gjenstand_fra.grid(column=0, row=3)
        self.gjenstand_fra_felt = tkinter.Entry(self.hovedvindu, width=10)
        self.gjenstand_fra_felt.grid(column=1, row=3)

        self.fjern_knapp = tkinter.Button(self.hovedvindu, text="Fjern innhold", command=self.fjern_innhold_metode)
        self.fjern_knapp.grid(column=0, row=4)
        self.lagre_knapp = tkinter.Button(self.hovedvindu, text="Lagre gjenstand", command=self.registrer_gjenstand)
        self.lagre_knapp.grid(column=1, row=4)

        tkinter.mainloop()

    def fjern_innhold_metode(self):
        self.navn_felt.delete(0, tkinter.END)
        self.tidlig_aar_felt.delete(0, tkinter.END)
        self.senest_aar_felt.delete(0, tkinter.END)
        self.gjenstand_fra_felt.delete(0, tkinter.END)

    def registrer_gjenstand(self):
        try:
            tidlig_aar = int(self.tidlig_aar_felt.get())
        except ValueError:
            messagebox.showerror("Må være et tall!")
            return
        try:
            senest_aar = int(self.senest_aar_felt.get())
        except ValueError:
            messagebox.showerror("Må være et tall!")
            return
        gjenstander = Gjenstand(self.navn_felt.get(), tidlig_aar, senest_aar, self.gjenstand_fra_felt.get())
        self.gjenstander.append(gjenstander)
        self.fjern_innhold_metode()




if __name__ == "__main__":
    gui = GjenstandGUI()
    for gjenstand in gui.gjenstander:
        print(gjenstand)