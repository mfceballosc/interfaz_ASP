# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 566)
        MainWindow.setMaximumSize(QtCore.QSize(10000, 10000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setStyleSheet("background-color: rgb(237, 241, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.menu = QtWidgets.QTabWidget(self.frame)
        self.menu.setEnabled(True)
        self.menu.setObjectName("menu")
        self.t1 = QtWidgets.QWidget()
        self.t1.setObjectName("t1")
        self.frame_4 = QtWidgets.QFrame(self.t1)
        self.frame_4.setGeometry(QtCore.QRect(40, 10, 721, 401))
        self.frame_4.setStyleSheet("background-color: rgb(254, 255, 237);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(20, 10, 691, 381))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../assets/unal.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.frame_5 = QtWidgets.QFrame(self.t1)
        self.frame_5.setGeometry(QtCore.QRect(40, 410, 721, 51))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.Iniciar = QtWidgets.QPushButton(self.frame_5)
        self.Iniciar.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.Iniciar.setObjectName("Iniciar")
        self.menu.addTab(self.t1, "")
        self.t2 = QtWidgets.QWidget()
        self.t2.setObjectName("t2")
        self.frame_2 = QtWidgets.QFrame(self.t2)
        self.frame_2.setGeometry(QtCore.QRect(20, 20, 741, 331))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 1px solid #000000")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setStyleSheet("QFrame{\n"
"border: none;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.grafica = QtWidgets.QVBoxLayout()
        self.grafica.setSpacing(0)
        self.grafica.setObjectName("grafica")
        self.verticalLayout_4.addLayout(self.grafica)
        self.verticalLayout_4.setStretch(1, 5)
        self.frame_3 = QtWidgets.QFrame(self.t2)
        self.frame_3.setGeometry(QtCore.QRect(20, 360, 741, 121))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 1px solid #000000")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.b_graficar = QtWidgets.QPushButton(self.frame_3)
        self.b_graficar.setObjectName("b_graficar")
        self.gridLayout.addWidget(self.b_graficar, 0, 0, 1, 1)
        self.ResultadoAnalisis = QtWidgets.QTextEdit(self.frame_3)
        self.ResultadoAnalisis.setStyleSheet("QFrame{\n"
"border-radius: 0px;\n"
"}")
        self.ResultadoAnalisis.setReadOnly(True)
        self.ResultadoAnalisis.setObjectName("ResultadoAnalisis")
        self.gridLayout.addWidget(self.ResultadoAnalisis, 0, 1, 2, 1)
        self.cargarArchivo = QtWidgets.QPushButton(self.frame_3)
        self.cargarArchivo.setObjectName("cargarArchivo")
        self.gridLayout.addWidget(self.cargarArchivo, 1, 0, 1, 1)
        self.menu.addTab(self.t2, "")
        self.verticalLayout_3.addWidget(self.menu)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Iniciar.setText(_translate("MainWindow", "Iniciar"))
        self.menu.setTabText(self.menu.indexOf(self.t1), _translate("MainWindow", "main"))
        self.label_2.setText(_translate("MainWindow", "señales"))
        self.b_graficar.setText(_translate("MainWindow", "graficar"))
        self.ResultadoAnalisis.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sdsdsdsd</p></body></html>"))
        self.cargarArchivo.setText(_translate("MainWindow", "cargar archivo"))
        self.menu.setTabText(self.menu.indexOf(self.t2), _translate("MainWindow", "analisis"))
