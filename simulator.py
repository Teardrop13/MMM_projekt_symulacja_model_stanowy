import matplotlib.pyplot as plt
import math
import simulator_gui
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

n = 3 # parametr zadany, wielkosc macierzy

t = 50 # czas symulacji
dt = 0.001 # czas kroku
step_count = int(t/dt) # liczba krokow

A = [[-5, 1, 0], [-2, 0, 1], [-1, 0, 0]]
B = [1, 1, 2] # czy jest jakas zaleznosc ze na ostatniej pozycji musi byc 1 ?

x = [0, 0, 0] # zmienne stanu
y = [] # wektor wyjściowy
t = [] # os czasu
u = [] # wektor wejsciowy

u_integral = 0 # zerowe warunki początkowe

# całka wektora zmiennych stanu
x_integral = x.copy()

# tworzenie wektora sygnalu zadanego
for i in range(step_count):

    # if i*dt > 3 and i*dt < 8:
    #     u.append(1)
    # else:
    #     u.append(0)

    # if i*dt > 3 and i*dt < 7:
    #     u.append(1)
    # elif i*dt > 8 and i*dt < 25:
    #     u.append(2)
    # else:
    #     u.append(0)

    u.append(1)

    # u.append(math.sin(i*dt))

    # u.append(5*i*dt)


for current_step in range(0, step_count):
    t.append(current_step*dt)

    # całka z u
    u_integral += u[current_step]*dt

    # całka wektora stanu x
    for row in range(n):
        x_integral[row] += x[row]*dt

    # tworzenie nowego wektora stanu
    # realizacja dzialania A*x+B*u
    for row in range(n):
        x[row] = 0
        for col in range(n):
            x[row] +=  A[row][col] * x_integral[col]
        x[row] += B[row] * u_integral

    y.append(x[0]) # C = [1 0 0 0 ... ] wiec tylko zmienna stanu x0


# plt.plot(t, u, 'g')
# plt.plot(t, y, 'r')
# plt.show()

class Simulator(QtWidgets.QMainWindow, simulator_gui.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Simulator()
    form.show()
    app.exec_()
