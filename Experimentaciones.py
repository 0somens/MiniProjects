import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

class VANCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora de VAN")
        self.root.geometry("400x500")

        self.descInicial_var = tk.DoubleVar()
        self.tasaDesc_var = tk.DoubleVar()
        self.n_var = tk.IntVar()

        tk.Label(self.root, text="Desembolso Inicial:").pack()
        tk.Entry(self.root, textvariable=self.descInicial_var).pack()
        tk.Label(self.root, text="Tasa de Descuento (%):").pack()
        tk.Entry(self.root, textvariable=self.tasaDesc_var).pack()
        tk.Label(self.root, text="Número de ciclos:").pack()
        tk.Entry(self.root, textvariable=self.n_var).pack()

        # Botón para calcular
        tk.Button(self.root, text="Ingresar Flujos de Caja", command=self.ingresar_flujos).pack()
        
        #flujos de caja
        self.flujos = []
        
        self.root.mainloop()
# Segunda ventana
    def ingresar_flujos(self):
        self.n = self.n_var.get()
        self.flujos = []

        self.flujo_window = tk.Toplevel(self.root)
        self.flujo_window.title("Ingresar Flujos de Caja")
        
        self.flujo_entries = []
        for i in range(1, self.n + 1):
            tk.Label(self.flujo_window, text=f"Año {i}:").grid(row=i, column=0)
            entry = tk.Entry(self.flujo_window)
            entry.grid(row=i, column=1)
            self.flujo_entries.append(entry)
        
        tk.Button(self.flujo_window, text="Calcular VAN", command=self.calcular_van).grid(row=self.n + 1, columnspan=2)

    def calcular_van(self):
        try:
            descInicial = self.descInicial_var.get()
            tasaDesc = self.tasaDesc_var.get() / 100
            self.flujos = [float(entry.get()) for entry in self.flujo_entries]

            # Calcular VAN
            van = -descInicial + np.sum(np.array(self.flujos) / ((1 + tasaDesc) ** np.arange(1, len(self.flujos) + 1))) # self flujos para que coincida con la cantidad de flujos ingresados
            # van = -descInicial + np.sum(np.array(self.flujos) / (1 + tasaDesc) ** np.arange(1, self.n + 1))
            
            
            # Mostrar resultado
            resultado = f"El VAN es: {van:.2f}\n"
            resultado += "Rentable" if van > 0 else "No rentable"

            messagebox.showinfo("Resultado", resultado)

            # Mostrar gráfica
            self.mostrar_grafico()

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
# Resultado
    def mostrar_grafico(self):
        años = np.arange(1, self.n + 1)
        plt.figure(figsize=(6, 4))
        plt.bar(años, self.flujos, color='green')
        plt.axhline(0, color='black', linewidth=1)
        plt.xlabel("Año")
        plt.ylabel("Flujo de Caja")
        plt.title("Evolución de los Flujos de Caja")
        plt.show()


# Ejecutar la aplicación
# if __name__ == "__main__":
#     VANCalculator()

import unittest
import numpy as np

def calcular_van(descInicial, tasaDesc, flujos):
    n = len(flujos)
    van = -descInicial + np.sum(np.array(flujos) / (1 + tasaDesc) ** np.arange(1, n + 1))
    return van

class TestVANCalculator(unittest.TestCase):

    def test_proyecto_rentable(self):
        van = calcular_van(10000, 0.10, [3000, 3500, 4000, 4500, 5000])
        self.assertGreater(van, 0, "El VAN debería ser positivo (Rentable).")

    def test_proyecto_no_rentable(self):
        van = calcular_van(15000, 0.12, [2000, 2500, 3000, 3500])
        self.assertLess(van, 0, "El VAN debería ser negativo (No Rentable).")

    def test_proyecto_indiferente(self):
        van = calcular_van(8500, 0.08, [2500, 3000, 3600])
        self.assertAlmostEqual(van, 0, delta=0.1, msg="El VAN debería ser cercano a 0 (Indiferente).")

if __name__ == "__main__":
    unittest.main()
