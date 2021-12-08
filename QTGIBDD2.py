from pymysql import connections
from pymysql import cursors


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 675)
        MainWindow.setStyleSheet("background-image: url(gibdd.jpg)")
        self.label = QtWidgets.QLabel

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 120, 321, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.zapros_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 160, 321, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.zapros_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 280, 321, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.zapros_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 240, 321, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.zapros_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 200, 321, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.zapros_5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 0, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 130, 700, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 170, 800, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 210, 800, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 290, 800, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 250, 800, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(310, 600, 411, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.win2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Фильтры для отображения сотрудников отдельных должностей"))
        self.pushButton_2.setText(_translate("MainWindow", "Фильтры для отображения отдельных званий"))
        self.pushButton_3.setText(_translate("MainWindow", "Фильтры для отображения автомобилей одного владельца"))
        self.pushButton_4.setText(_translate("MainWindow", "Фильтры для отображения автомобилей прошедших и не прошедших технический осмотр"))
        self.pushButton_5.setText(_translate("MainWindow", "Фильтры для отображения найденных и не найденных угнанных автомобилей"))
        self.label.setText(_translate("MainWindow", "База данных ГИБДД"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))

    def zapros_1(self):
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT `Код должности`, `Код звания`, `ФИО` FROM `сотрудники`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.label_2.setText(str(g))


    def zapros_2(self):
        with connections.Connection(user='root',password='root',host='localhost',database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:

                sql = ('SELECT `Код звания`, `Наименование` FROM `звания`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.label_3.setText(str(g))

    def zapros_3(self):
        with connections.Connection(user='root',password='root',host='localhost',database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:

                sql = ('SELECT `Код автомобиля`,`Код водителя` FROM `автомобили`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.label_5.setText(str(g))

    def zapros_4(self):
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT `Технический осмотр` FROM `автомобили`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.label_6.setText(str(g))

    def zapros_5(self):
        with connections.Connection(user='root',password='root',host='localhost',database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:

                sql = ('SELECT `Отметка об нахождении` FROM `автомобили в угоне`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.label_4.setText(str(g))

    def win2(self):
        self.w2 = Window2()
        self.w2.show()

class Window2(QtWidgets.QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Window2')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
