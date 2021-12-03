from pymysql import connections
from pymysql import cursors

from PyQt5 import QtWidgets, QtCore, QtGui

class Main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget = QtWidgets.QWidget()
        self.lay1 = QtWidgets.QVBoxLayout(self.widget)

        self.push_but_1 = QtWidgets.QPushButton('Фильтры для отображения сотрудников отдельных должностей')
        self.push_but_1.clicked.connect(self.zapros_1)
        self.info_1 = QtWidgets.QLabel('info 1')

        self.push_but_2 = QtWidgets.QPushButton('Фильтры для отображения отдельных званий')
        self.push_but_2.clicked.connect(self.zapros_2)
        self.info_2 = QtWidgets.QLabel('info 2')

        self.push_but_3 = QtWidgets.QPushButton('Фильтры для отображения автомобилей одного владельца ')
        self.push_but_3.clicked.connect(self.zapros_3)
        self.info_3 = QtWidgets.QLabel('info 3')

        self.push_but_4 = QtWidgets.QPushButton('Фильтры для отображения автомобилей прошедших и не прошедших технический осмотр')
        self.push_but_4.clicked.connect(self.zapros_4)
        self.info_4 = QtWidgets.QLabel('info 4')

        self.push_but_5 = QtWidgets.QPushButton('Фильтры для отображения найденных и не найденных угнанных автомобилей')
        self.push_but_5.clicked.connect(self.zapros_5)
        self.info_5 = QtWidgets.QLabel('info 5')

        self.lay1.addWidget(self.push_but_1)
        self.lay1.addWidget(self.info_1)

        self.lay1.addWidget(self.push_but_2)
        self.lay1.addWidget(self.info_2)

        self.lay1.addWidget(self.push_but_3)
        self.lay1.addWidget(self.info_3)

        self.lay1.addWidget(self.push_but_4)
        self.lay1.addWidget(self.info_4)

        self.lay1.addWidget(self.push_but_5)
        self.lay1.addWidget(self.info_5)

        scrol = QtWidgets.QScrollArea()
        scrol.setWidget(self.widget)
        scrol.setWidgetResizable(True)
        self.setCentralWidget(scrol)

        self.resize(800,600)
        self.show()

    def zapros_1(self):
        with connections.Connection(user='root',password='root',host='localhost',database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:

                sql = ('SELECT `Код сотрудника`, `Код звания`, `ФИО` FROM `сотрудники`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.info_1.setText(str(g))

    def zapros_2(self):
        with connections.Connection(user='root',password='root',host='localhost',database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:

                sql = ('SELECT `Код звания`, `Наименование` FROM `звания`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.info_2.setText(str(g))

    def zapros_3(self):
        with connections.Connection(user='root',password='root',host='localhost',database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:

                sql = ('SELECT `Код автомобиля`,`Код водителя` FROM `автомобили`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.info_3.setText(str(g))

    def zapros_4(self):
        with connections.Connection(user='root',password='root',host='localhost',database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:

                sql = ('SELECT `Технический осмотр` FROM `автомобили`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.info_4.setText(str(g))

    def zapros_5(self):
        with connections.Connection(user='root',password='root',host='localhost',database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:

                sql = ('SELECT `Отметка об нахождении` FROM `автомобили в угоне`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.info_5.setText(str(g))

class App(QtWidgets.QApplication):
    def __init__(self,argv):
        super().__init__(argv)

        self.setStyle('Fusion')

app = App([])
win = Main_window()
app.exec()