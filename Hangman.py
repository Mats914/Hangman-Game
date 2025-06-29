import tkinter as tk
import random

# Lista med ord
ORDLISTA = ["äpple", "banan", "dator", "hund", "program", "skola", "kaffe", "fönster", "bil", "sommar"]

MAX_FEL = 6  # Max antal felgissningar

class HangmanSpel:
    def __init__(self, root):
        self.root = root
        self.root.title("Hänga Gubbe - På Svenska")
        self.ord = random.choice(ORDLISTA)
        self.gissade_bokstäver = []
        self.fel = 0

        # GUI-element
        self.ord_label = tk.Label(root, text=self.get_ord_visning(), font=("Helvetica", 24))
        self.ord_label.pack(pady=20)

        self.info_label = tk.Label(root, text="Gissa en bokstav:", font=("Helvetica", 14))
        self.info_label.pack()

        self.inmatning = tk.Entry(root, font=("Helvetica", 18), width=3, justify='center')
        self.inmatning.pack()
        self.inmatning.bind("<Return>", self.gissa_bokstav)

        self.meddelande = tk.Label(root, text="", font=("Helvetica", 14))
        self.meddelande.pack(pady=10)

        self.fel_label = tk.Label(root, text=f"Fel: {self.fel} av {MAX_FEL}", font=("Helvetica", 14))
        self.fel_label.pack()

    def get_ord_visning(self):
        return " ".join([bokstav if bokstav in self.gissade_bokstäver else "_" for bokstav in self.ord])

    def gissa_bokstav(self, event):
        bokstav = self.inmatning.get().lower()
        self.inmatning.delete(0, tk.END)

        if not bokstav.isalpha() or len(bokstav) != 1:
            self.meddelande.config(text="Ange en giltig bokstav!")
            return

        if bokstav in self.gissade_bokstäver:
            self.meddelande.config(text="Du har redan gissat den bokstaven.")
            return

        self.gissade_bokstäver.append(bokstav)

        if bokstav in self.ord:
            self.meddelande.config(text="Rätt gissat!")
        else:
            self.fel += 1
            self.meddelande.config(text="Fel bokstav.")
            self.fel_label.config(text=f"Fel: {self.fel} av {MAX_FEL}")

        self.ord_label.config(text=self.get_ord_visning())

        if all(bokstav in self.gissade_bokstäver for bokstav in self.ord):
            self.meddelande.config(text="Grattis! Du vann!")
            self.inmatning.config(state='disabled')
        elif self.fel >= MAX_FEL:
            self.meddelande.config(text=f"Du förlorade! Ordet var: {self.ord}")
            self.ord_label.config(text=self.ord)
            self.inmatning.config(state='disabled')

# Skapa fönster och kör spelet
root = tk.Tk()
app = HangmanSpel(root)
root.mainloop()
