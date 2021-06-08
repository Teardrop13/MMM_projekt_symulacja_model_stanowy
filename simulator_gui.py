# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulator_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1300, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(1300, 800))
        Dialog.setMaximumSize(QtCore.QSize(1300, 800))
        self.textEdit_matrixA = QtWidgets.QTextEdit(Dialog)
        self.textEdit_matrixA.setGeometry(QtCore.QRect(20, 100, 100, 231))
        self.textEdit_matrixA.setTabChangesFocus(False)
        self.textEdit_matrixA.setObjectName("textEdit_matrixA")
        self.textEdit_matrixB = QtWidgets.QTextEdit(Dialog)
        self.textEdit_matrixB.setGeometry(QtCore.QRect(170, 100, 100, 231))
        self.textEdit_matrixB.setObjectName("textEdit_matrixB")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 370, 201, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_sinus = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_sinus.setEnabled(True)
        self.radioButton_sinus.setChecked(True)
        self.radioButton_sinus.setObjectName("radioButton_sinus")
        self.verticalLayout.addWidget(self.radioButton_sinus)
        self.radioButton_square = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_square.setObjectName("radioButton_square")
        self.verticalLayout.addWidget(self.radioButton_square)
        self.radioButton_triangle = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_triangle.setObjectName("radioButton_triangle")
        self.verticalLayout.addWidget(self.radioButton_triangle)
        self.radioButton_ramp = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_ramp.setObjectName("radioButton_ramp")
        self.verticalLayout.addWidget(self.radioButton_ramp)
        self.radioButton_step = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_step.setObjectName("radioButton_step")
        self.verticalLayout.addWidget(self.radioButton_step)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 70, 100, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 70, 100, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 30, 30))
        self.label_3.setObjectName("label_3")
        self.parameter_n = QtWidgets.QSpinBox(Dialog)
        self.parameter_n.setGeometry(QtCore.QRect(50, 20, 51, 31))
        self.parameter_n.setFrame(True)
        self.parameter_n.setMinimum(3)
        self.parameter_n.setMaximum(10)
        self.parameter_n.setObjectName("parameter_n")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(330, 470, 151, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(330, 420, 151, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(330, 370, 141, 41))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(330, 520, 141, 41))
        self.label_8.setObjectName("label_8")
        self.runButton = QtWidgets.QPushButton(Dialog)
        self.runButton.setGeometry(QtCore.QRect(1170, 750, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy)
        self.runButton.setMaximumSize(QtCore.QSize(800, 1300))
        self.runButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.runButton.setObjectName("runButton")
        self.errorDisplay = QtWidgets.QPlainTextEdit(Dialog)
        self.errorDisplay.setEnabled(True)
        self.errorDisplay.setGeometry(QtCore.QRect(10, 690, 471, 91))
        self.errorDisplay.setReadOnly(True)
        self.errorDisplay.setPlainText("")
        self.errorDisplay.setObjectName("errorDisplay")
        self.doubleSpinBox_step = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_step.setGeometry(QtCore.QRect(230, 520, 91, 41))
        self.doubleSpinBox_step.setDecimals(5)
        self.doubleSpinBox_step.setMinimum(1e-05)
        self.doubleSpinBox_step.setMaximum(1.0)
        self.doubleSpinBox_step.setSingleStep(0.001)
        self.doubleSpinBox_step.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_step.setProperty("value", 0.001)
        self.doubleSpinBox_step.setObjectName("doubleSpinBox_step")
        self.doubleSpinBox_period = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_period.setGeometry(QtCore.QRect(230, 370, 91, 41))
        self.doubleSpinBox_period.setDecimals(4)
        self.doubleSpinBox_period.setMinimum(0.0001)
        self.doubleSpinBox_period.setMaximum(100.0)
        self.doubleSpinBox_period.setSingleStep(0.1)
        self.doubleSpinBox_period.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_period.setObjectName("doubleSpinBox_period")
        self.doubleSpinBox_amplitude = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_amplitude.setGeometry(QtCore.QRect(230, 420, 91, 41))
        self.doubleSpinBox_amplitude.setDecimals(4)
        self.doubleSpinBox_amplitude.setMaximum(20.0)
        self.doubleSpinBox_amplitude.setSingleStep(0.1)
        self.doubleSpinBox_amplitude.setProperty("value", 1.0)
        self.doubleSpinBox_amplitude.setObjectName("doubleSpinBox_amplitude")
        self.doubleSpinBox_stopTime = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_stopTime.setGeometry(QtCore.QRect(230, 470, 91, 41))
        self.doubleSpinBox_stopTime.setDecimals(4)
        self.doubleSpinBox_stopTime.setMinimum(0.0001)
        self.doubleSpinBox_stopTime.setMaximum(100.0)
        self.doubleSpinBox_stopTime.setSingleStep(1.0)
        self.doubleSpinBox_stopTime.setProperty("value", 10.0)
        self.doubleSpinBox_stopTime.setObjectName("doubleSpinBox_stopTime")
        self.plotArea = QtWidgets.QWidget(Dialog)
        self.plotArea.setGeometry(QtCore.QRect(550, 30, 721, 431))
        self.plotArea.setObjectName("plotArea")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Symulator"))
        self.radioButton_sinus.setText(_translate("Dialog", "Sinus"))
        self.radioButton_square.setText(_translate("Dialog", "Sygnał prostokątny"))
        self.radioButton_triangle.setText(_translate("Dialog", "Trójkąt"))
        self.radioButton_ramp.setText(_translate("Dialog", "Rampa"))
        self.radioButton_step.setText(_translate("Dialog", "Skok"))
        self.label.setText(_translate("Dialog", "Macierz A"))
        self.label_2.setText(_translate("Dialog", "Macierz B"))
        self.label_3.setText(_translate("Dialog", "n:"))
        self.label_4.setText(_translate("Dialog", "Czas symulacji"))
        self.label_5.setText(_translate("Dialog", "Amplituda"))
        self.label_6.setText(_translate("Dialog", "Okres"))
        self.label_8.setText(_translate("Dialog", "Krok"))
        self.runButton.setText(_translate("Dialog", "Uruchom"))
