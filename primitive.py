# -*- encoding: utf8 -*-
import random
from tkinter import Button, Frame, Label


class Primitive(Frame):
    def __init__(self, parent=None, **kargs):
        Frame.__init__(self, parent, **kargs)
        self.pack()
        self.construccion()
        self.iteracion = 0  # estado

    def construccion(self):
        Label(self, text='Pulsa el botón para generar una combinación').pack()
        self.label = Label(self, text="Combinación", width=50)
        self.label.pack(side="left")
        Button(self, text="Nueva", command=self.sorteo).pack()

    def combinacion(self):
        numeros = random.sample(range(1, 99), 6)
        numeros.sort()
        complementarios = random.sample(range(1, 99), 1)
        joker = random.sample(range(1000000, 9999999), 1)
        reintegro = random.sample(range(1, 99), 1)

        return (
            str(numeros).strip('[]') + '  C: ' +
            str(complementarios).strip('[]') + '  Joker: ' +
            str(joker).strip('[]') + '  Reintegro: ' +
            str(reintegro).strip('[]')
        )

    def sorteo(self):
        self.iteracion += 1  # Actualiza n° de iteraciones
        self.label.configure(text=self.combinacion())


if __name__ == '__main__':
    Primitive().mainloop()
