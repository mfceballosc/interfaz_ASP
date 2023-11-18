from .mainWindow import Ui_MainWindow
from PyQt5 import QtWidgets, uic, QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget




import numpy as np
import os
import pandas as pd
import comtrade
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.df = pd.DataFrame
        super(MainWindow, self).__init__()
        self.setupUi(self)
        img = os.path.abspath(os.path.join(os.getcwd(), "src", "assets", "unal.jpg"))
        self.label.setPixmap(QtGui.QPixmap(img))

        # pantalla de inicio
        lambda: self.menu.setCurrentIndex(0)

        # # grafica 
        self.graficaTempl = Canvas_grafica()

        # Botones 
        self.cargarArchivo.clicked.connect(self.abrirArchivo)
        self.b_graficar.clicked.connect(self.graficarSenal)
        self.b_comtrade.clicked.connect(self.graficarComtrade)
        self.Iniciar.clicked.connect(lambda: self.menu.setCurrentIndex(1))


    def graficarSenal(self):
        if not self.df.empty:
            self.graficaTempl.plot(self.df)
            self.grafica.addWidget(self.graficaTempl.getInstance())
        else: 
            print("Intentaa graficar un archivo vacio")

    def graficarComtrade(self):
        if not self.df_comtrade.empty:
            cols = self.df_comtrade.columns.tolist()
            self.graficaTempl.plotComtrade(self.df_comtrade[cols[:2]])
            self.grafica.addWidget(self.graficaTempl.getInstance())
        else: 
            print("Intentaa graficar un archivo vacio")

    def abrirArchivo(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccionar archivo", "", "Archivos de texto (*.csv);;Todos los archivos (*)")
        file_path_comtrade = file_path.replace('.csv', '.cfg')
        try:
            self.df = pd.read_csv(file_path)
            self.rec = comtrade.load(file_path_comtrade)
            self.df_comtrade = self.rec.to_dataframe()
        except:
            print("No selecciono un archivo")

        self.ResultadoAnalisis.setText("Hola mundo")



class Canvas_grafica(FigureCanvas):
    def __init__(self) -> None:
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        super().__init__(self.fig)


    def getInstance(self):
        return self


    def plot(self, df):
        cols = df.columns.tolist()
        time = df[cols[0]]
        desf = 0
        for i in range(1, len(cols)):
            df[cols[i]] = df[cols[i]] + desf
            signal = df[cols[i]].tolist()
            self.ax.step(time, signal, where='post')
            self.ax.text(time[0], signal[0], cols[i], fontsize=9)
            desf += 2
        self.ax.grid()
        self.ax.legend()

    def plotComtrade(self, df):
        df = df.head(50000)
        df.reset_index(inplace=True)
        cols = df.columns.tolist()
        time = df[cols[0]]
        desf = 0
        for i in range(1, len(cols)):
            df[cols[i]] = df[cols[i]] + desf
            signal = df[cols[i]].tolist()
            self.ax.plot(time, signal)
            self.ax.text(time[0], signal[0], cols[i], fontsize=9)
            desf += 2
        self.ax.grid()
        self.ax.legend()



