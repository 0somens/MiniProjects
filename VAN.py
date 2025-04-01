import pandas as pd
import numpy as np
import matplotlib as plt
import tkinter as tk


descInicial = float(input('Desembolso inicial: '))
tasaDesc = float(input('Tasa de descuento (porcentaje): '))/100
n = int(input('Cantidad de ciclos: '))
van = -descInicial




for i in range(1,n+1):
    flujoCaja = float(input('Flujo de caja N°' ))
    van += flujoCaja/(1+tasaDesc)**i

if van < 0:
    print('No rentable' , van)
elif van > 0:
    print('Rentable' , van)
    
    
# Atributos que se le podrian agregar:
    # Herramientas visuales (gráficas para ver la evolución del flujo o cualquier comoponente el cual no sea solo por consola)
    # Interfaz gráfica para que sea más sencillo entender qué se esta insertando
    # Orden, posibilidad de poder agregar más o menos flujos de caja o cambiar en desemlboso inciail sin tener que arrancar el programa nuevamente
    # Optmizacion de la formula mediante el uso de librerias
    