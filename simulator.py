import matplotlib.pyplot as plt
import math
import simulator_gui
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def createInputVector(type, time, dt, period, amplitude):
    # tworzenie wektora sygnalu zadanego
    # type podany jako string: 'sinus' 'square' 'triangle'
    step_count = int(time/dt) + 1
    u = []
    k=0

    if (type=='sinus'):
        for i in range(step_count):
            u.append(amplitude*math.sin(2*math.pi/period*i*dt))
    elif (type=='square'):
        for i in range(step_count):
            if (math.sin(2*math.pi/period*i*dt) > 0):
                k = 1
            elif (math.sin(2*math.pi/period*i*dt) <= 0):
                k = -1
            u.append(amplitude * k)
    elif (type=='triangle'):
        for i in range(step_count):
            k=2*amplitude/math.pi*math.asin(math.sin(2*math.pi*i*dt/period))
            u.append(k)
    elif (type=='ramp'):
        for i in range(step_count):
            period1=period/math.pi
            k=2*amplitude/math.pi*math.atan(math.tan(i*dt/period1))
            u.append(k)
    elif (type=='step'):
        for i in range(step_count):
            u.append(amplitude)
            
    return u

def createTimeVector(time, dt):
    step_count = int(time/dt) + 1
    t = []
    for i in range(step_count):
        t.append(i*dt)
    return t

def createMatrixA(parameters, n):
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        A.append(row)
    a=0
    b=1
    m=n-1
    while m:
        A[a][b]=1
        b=b+1
        a=a+1
        m=m-1
    for i, param in enumerate(parameters):
        A[i][0] = -param
    return A

def createMatrixB(parameters, n):
    B = []
    for i in range(n):
        col = []
        col.append(0)
        B.append(col)
    for i, param in enumerate(parameters):
        B[i][0] = param
    return B




class Model():
    def __init__(self, A, B, n):
        self.A = A
        self.B = B
        self.n = n

    def simulation(self, u, t, dt):
        u_integral = 0  # zerowe warunki początkowe
        
        # wektor zmiennych stanu
        x = []
        for i in range(self.n):
            x.append(0)
        x_integral = x.copy()

        y = []

        for current_step in range(len(t)):
            # całka z u
            u_integral += u[current_step]*dt

            # całka wektora stanu x
            for row in range(self.n):
                x_integral[row] += x[row]*dt

            # tworzenie nowego wektora stanu
            # realizacja dzialania A*x+B*u
            for row in range(self.n):
                x[row] = 0
                for col in range(self.n):
                    x[row] += self.A[row][col] * x_integral[col]
                x[row] += self.B[row][0] * u_integral

            y.append(x[0])  # C = [1 0 0 0 ... ] wiec tylko zmienna stanu x0
        return y

class Simulator(QtWidgets.QMainWindow, simulator_gui.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # dodanie plot do QWidget plotArea
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        plot_box = QtWidgets.QVBoxLayout()
        plot_box.addWidget(self.canvas)
        self.plotArea.setLayout(plot_box)

        # wywolywanie funkcji po wcisnieciu przycisku
        self.runButton.clicked.connect(self.runSimulation)

    def readA_parameters(self, n):
        A_parameters = []
        parameters_string = self.textEdit_matrixA.toPlainText()
        parameters_list = parameters_string.split('\n')
        for param in parameters_list:
            if param == '':
                break
            A_parameters.append(float(param))
        assert len(A_parameters) == n
        return A_parameters

    def readB_parameters(self, n):
        B_parameters = []
        parameters_string = self.textEdit_matrixB.toPlainText()
        parameters_list = parameters_string.split('\n')
        for param in parameters_list:
            if param == '':
                break
            B_parameters.append(float(param))
        assert len(B_parameters) == n
        return B_parameters

    def printMessage(self, text):
        self.errorDisplay.setPlainText(text)
        self.repaint()

    def runSimulation(self):
        self.printMessage('symulacja w toku')
        n = self.parameter_n.value()  # wielkosc macierzy
        time = self.doubleSpinBox_stopTime.value()  # czas symulacji
        dt = self.doubleSpinBox_step.value()  # czas kroku
        period = self.doubleSpinBox_period.value() # okres sygnalu wejsciowego
        amplitude = self.doubleSpinBox_amplitude.value() # amplituda sygnalu wejsciowego
        
        signal_type = ''
        if self.radioButton_sinus.isChecked():
            signal_type = 'sinus'
        elif self.radioButton_square.isChecked():
            signal_type = 'square'
        elif self.radioButton_triangle.isChecked():
            signal_type = 'triangle'
        elif self.radioButton_ramp.isChecked():
            signal_type = 'ramp'
        elif self.radioButton_step.isChecked():
            signal_type = 'step'

        try:
            A_parameters = self.readA_parameters(n)
        except ValueError:
            self.printMessage('nie wlasciwy element w macierzy A')
            return
        except AssertionError:
            self.printMessage('nie wlasciwa ilosc parametrów macierzy A')
            return

        try:
            B_parameters = self.readB_parameters(n)
        except ValueError:
            self.printMessage('nie wlasciwy element w macierzy B')
            return
        except AssertionError:
            self.printMessage('nie wlasciwa ilosc parametrów macierzy B')
            return

        A = createMatrixA(A_parameters, n)
        B = createMatrixB(B_parameters, n)
        u = createInputVector(signal_type, time, dt, period, amplitude)
        t = createTimeVector(time, dt)
        model = Model(A, B, n)
        y = model.simulation(u, t, dt)
        self.printMessage('symulacja gotowa')

        print(u)
        print(y)
        print(t)

        # rysowanie wykresu
        self.figure.clear()
        self.ax = self.figure.add_subplot()
        self.ax.plot(t, u, 'g')
        self.ax.plot(t, y, 'r')
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Simulator()
    form.show()
    app.exec_()
