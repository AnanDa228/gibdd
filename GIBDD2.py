from pymysql import connections
from pymysql import cursors

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 524)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 110, 161, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.othet)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 140, 161, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.forms)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(634, 110, 161, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.zastavka)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 0, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)


        self.zastavka()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Фильтры поиска"))
        self.pushButton_2.setText(_translate("MainWindow", "Формы"))
        self.pushButton_3.setText(_translate("MainWindow", "Заставка"))
        self.label.setText(_translate("MainWindow", "БАЗА ДАННЫХ ГИБДД"))

    def othet(self):
            self.othet = QtWidgets.QMainWindow()
            self.othet.setWindowTitle('База данных ГИБДД')
            self.othet.setWindowIcon(QtGui.QIcon('1.jpg'))
            self.widget = QtWidgets.QWidget()
            self.lay1 = QtWidgets.QVBoxLayout(self.widget)

            self.push_but_1 = QtWidgets.QPushButton('Фильтры для отображения сотрудников отдельных должностей')
            self.push_but_1.clicked.connect(self.zapros_1)
            self.push_but_1.setFixedSize(500, 30)
            self.push_but_1.setStyleSheet('font: bold 14px;')
            self.info_1 = QtWidgets.QLabel('сотрудники')

            self.push_but_2 = QtWidgets.QPushButton('Фильтры для отображения отдельных званий')
            self.push_but_2.clicked.connect(self.zapros_2)
            self.push_but_2.setFixedSize(500, 30)
            self.push_but_2.setStyleSheet('font: bold 14px;')
            self.info_2 = QtWidgets.QLabel('звания')

            self.push_but_3 = QtWidgets.QPushButton('Фильтры для отображения автомобилей одного владельца')
            self.push_but_3.clicked.connect(self.zapros_3)
            self.push_but_3.setFixedSize(500, 30)
            self.push_but_3.setStyleSheet('font: bold 14px;')
            self.info_3 = QtWidgets.QLabel('автомобили')

            self.push_but_4 = QtWidgets.QPushButton(
                'Фильтры для отображения автомобилей прошедших и не прошедших технический осмотр')
            self.push_but_4.clicked.connect(self.zapros_4)
            self.push_but_4.setFixedSize(500, 30)
            self.push_but_4.setStyleSheet('font: bold 14px;')
            self.info_4 = QtWidgets.QLabel('тех осмотр')

            self.push_but_5 = QtWidgets.QPushButton(
                'Фильтры для отображения найденных и не найденных угнанных автомобилей')
            self.push_but_5.clicked.connect(self.zapros_5)
            self.push_but_5.setFixedSize(500, 30)
            self.push_but_5.setStyleSheet('font: bold 14px;')
            self.info_5 = QtWidgets.QLabel('угнанные автомобили')

            self.but_all = QtWidgets.QPushButton('Подробная информация')
            self.but_all.clicked.connect(self.all_information_bd)

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

            self.lay1.addWidget(self.but_all)

            scrol = QtWidgets.QScrollArea()
            scrol.setWidget(self.widget)
            scrol.setWidgetResizable(True)
            self.othet.setCentralWidget(scrol)

            self.othet.resize(800, 600)
            self.othet.show()

    def all_information_bd(self):
            self.all_info = QtWidgets.QMainWindow()
            self.all_info.setWindowTitle('Информация из БД')
            self.all_info.setWindowIcon(QtGui.QIcon('1.jpg'))
            self.widget_info = QtWidgets.QWidget()
            self.lay_info = QtWidgets.QVBoxLayout(self.widget_info)


            self.table_1 = QtWidgets.QTableWidget()
            self.table_1.setColumnCount(9)
            self.table_1.setRowCount(len(self.get_info_brigades()))
            self.table_1.setHorizontalHeaderLabels(['Код сотрудника', 'ФИО', 'Возраст', 'Пол', 'Адрес', 'Телефон', 'Паспортные данные', 'Код должности','Код звания'])
            self.but_update_table_1 = QtWidgets.QPushButton('Обновить сотрудники')
            self.but_update_table_1.clicked.connect(self.update_brigades)

            self.lay_info.addWidget(self.table_1)
            self.lay_info.addWidget(self.but_update_table_1)

            self.table_2 = QtWidgets.QTableWidget()
            self.table_2.setColumnCount(5)
            self.table_2.setRowCount(len(self.get_info_customers()))
            self.table_2.setHorizontalHeaderLabels(['Код звания', 'Наименование', '	Надбавка', 'Обязанности', 'Требования'])
            self.but_update_table_2 = QtWidgets.QPushButton('Обновить Звания')
            self.but_update_table_2.clicked.connect(self.update_customers)

            self.lay_info.addWidget(self.table_2)
            self.lay_info.addWidget(self.but_update_table_2)

            self.table_3 = QtWidgets.QTableWidget()
            self.table_3.setColumnCount(5)
            self.table_3.setRowCount(len(self.get_info_materials()))
            self.table_3.setHorizontalHeaderLabels(['Код должности', 'Наименование Должности', 'Оклад', 'Обязанности', 'Требования'])
            self.but_update_table_3 = QtWidgets.QPushButton('Обновить Должности')
            self.but_update_table_3.clicked.connect(self.update_materials)

            self.lay_info.addWidget(self.table_3)
            self.lay_info.addWidget(self.but_update_table_3)

            self.table_4 = QtWidgets.QTableWidget()
            self.table_4.setColumnCount(11)
            self.table_4.setRowCount(len(self.get_info_orders()))
            self.table_4.setHorizontalHeaderLabels(['Код водителя', 'ФИО', 'Дата рождения', 'Адрес', 'Паспортные данные', 'Номер водительского удостоверения', 'Дата выдачи удостоверения','Дата окончания удостоверения', 'Категория удостоверения', 'Описание','Код сотрудника'])
            self.but_update_table_4 = QtWidgets.QPushButton('Обновить Водители')
            self.but_update_table_4.clicked.connect(self.update_orders)

            self.lay_info.addWidget(self.table_4)
            self.lay_info.addWidget(self.but_update_table_4)

            self.table_5 = QtWidgets.QTableWidget()
            self.table_5.setColumnCount(9)
            self.table_5.setRowCount(len(self.get_info_positions()))
            self.table_5.setHorizontalHeaderLabels(['Код марки', 'Наименование', 'Фирма производитель', 'Страна производитель', 'Дата начала производства', 'Дата окончания производства','Характеристики','Категория','Описание'])
            self.but_update_table_5 = QtWidgets.QPushButton('Обновить Марки автомобилей')
            self.but_update_table_5.clicked.connect(self.update_positions)

            self.lay_info.addWidget(self.table_5)
            self.lay_info.addWidget(self.but_update_table_5)

            self.table_6 = QtWidgets.QTableWidget()
            self.table_6.setColumnCount(14)
            self.table_6.setRowCount(len(self.get_info_staff()))
            self.table_6.setHorizontalHeaderLabels(['Код автомобиля', 'Код водителя', 'Код марки', 'Регистрационный номер', 'Номер кузова', 'Номер двигателя', 'Номер техпаспорта', 'Дата выпуска','Дата регистрации','Цвет','Технический осмотр','Дата технического осмотра','Описание','Код сотрудника'])
            self.but_update_table_6 = QtWidgets.QPushButton('Обновить Автомобили')
            self.but_update_table_6.clicked.connect(self.update_staff)

            self.lay_info.addWidget(self.table_6)
            self.lay_info.addWidget(self.but_update_table_6)

            self.table_7 = QtWidgets.QTableWidget()
            self.table_7.setColumnCount(7)
            self.table_7.setRowCount(len(self.get_info_types_of_works()))
            self.table_7.setHorizontalHeaderLabels(['Дата угона', 'Дата обращения', 'Код автомобиля', 'Код водителя', 'Обстоятельства угона', 'Отметка о находжении','Дата нахождения','Код сотрудника'])
            self.but_update_table_7 = QtWidgets.QPushButton('Обновить Автомобили в угоне')
            self.but_update_table_7.clicked.connect(self.update_types_of_works)

            self.lay_info.addWidget(self.table_7)
            self.lay_info.addWidget(self.but_update_table_7)

            self.new_scrol = QtWidgets.QScrollArea()
            self.new_scrol.setWidget(self.widget_info)
            self.new_scrol.setWidgetResizable(True)

            self.all_info.setCentralWidget(self.new_scrol)
            self.all_info.resize(800, 600)

            self.all_info.show()

        ##brigadees
    def get_info_brigades(self):
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ('SELECT * FROM `сотрудники`')
                    cursor.execute(sql)
                    g = cursor.fetchall()

                return g

    def update_brigades(self):
            for i in range(0, len(self.get_info_brigades())):
                for g in range(0, 9):
                    f = str(self.get_info_brigades()[i][g])

                    self.table_1.setItem(i, g, QtWidgets.QTableWidgetItem(f))

        ###customers
    def get_info_customers(self):
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ('SELECT * FROM `звания`')
                    cursor.execute(sql)
                    g = cursor.fetchall()

                return g

    def update_customers(self):
            for i in range(0, len(self.get_info_customers())):
                for g in range(0, 5):
                    f = str(self.get_info_customers()[i][g])

                    self.table_2.setItem(i, g, QtWidgets.QTableWidgetItem(f))

        ###materials
    def get_info_materials(self):
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ('SELECT * FROM `должности`')
                    cursor.execute(sql)
                    g = cursor.fetchall()

                return g

    def update_materials(self):
            for i in range(0, len(self.get_info_materials())):
                for g in range(0, 5):
                    f = str(self.get_info_materials()[i][g])

                    self.table_3.setItem(i, g, QtWidgets.QTableWidgetItem(f))

        ###orders
    def get_info_orders(self):
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ('SELECT * FROM `водители`')
                    cursor.execute(sql)
                    g = cursor.fetchall()

                return g

    def update_orders(self):
            for i in range(0, len(self.get_info_orders())):
                for g in range(0, 11):
                    f = str(self.get_info_orders()[i][g])

                    self.table_4.setItem(i, g, QtWidgets.QTableWidgetItem(f))

        ###  positions
    def get_info_positions(self):
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ('SELECT * FROM `марки автомобилей`')
                    cursor.execute(sql)
                    g = cursor.fetchall()

                return g

    def update_positions(self):
            for i in range(0, len(self.get_info_positions())):
                for g in range(0, 9):
                    f = str(self.get_info_positions()[i][g])

                    self.table_5.setItem(i, g, QtWidgets.QTableWidgetItem(f))

        ###staff
    def get_info_staff(self):
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ('SELECT * FROM `автомобили`')
                    cursor.execute(sql)
                    g = cursor.fetchall()

                return g

    def update_staff(self):
            for i in range(0, len(self.get_info_staff())):
                for g in range(0, 14):
                    f = str(self.get_info_staff()[i][g])

                    self.table_6.setItem(i, g, QtWidgets.QTableWidgetItem(f))

        ###types_of_works
    def get_info_types_of_works(self):
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ('SELECT * FROM `автомобили в угоне`')
                    cursor.execute(sql)
                    g = cursor.fetchall()

                return g

    def update_types_of_works(self):
            for i in range(0, len(self.get_info_types_of_works())):
                for g in range(0, 8):
                    f = str(self.get_info_types_of_works()[i][g])

                    self.table_7.setItem(i, g, QtWidgets.QTableWidgetItem(f))

    def forms(self):
            self.form = QtWidgets.QMainWindow()
            self.form.setWindowTitle('База данных ГИБДД')
            self.form.setWindowIcon(QtGui.QIcon('1.jpg'))
            self.widget3 = QtWidgets.QWidget()

            self.lay3 = QtWidgets.QVBoxLayout(self.widget3)

            self.but_about_program = QtWidgets.QPushButton('О программе')
            self.but_about_program.clicked.connect(self.info_a)

            self.but_zastavka = QtWidgets.QPushButton('Заставка')
            self.but_zastavka.clicked.connect(self.zastavka)

            self.info_aboyt_programm = QtWidgets.QLabel('')

            self.lay3.addWidget(self.but_about_program)
            self.lay3.addWidget(self.info_aboyt_programm)
            self.lay3.addWidget(self.but_zastavka)

            self.form.setCentralWidget(self.widget3)

            self.form.resize(800, 600)
            self.form.show()

    def zastavka(self):
            self.zastavka_new = QtWidgets.QMainWindow()
            self.zastavka_new.setWindowTitle('База данных ГИБДД')
            self.zastavka_new.setWindowIcon(QtGui.QIcon('1.jpg'))
            self.widget_zastavka = QtWidgets.QWidget()

            self.lay4 = QtWidgets.QVBoxLayout(self.widget_zastavka)
            self.zastavka_info = QtWidgets.QLabel('Это заставка')

            self.lay4.addWidget(self.zastavka_info)

            self.zastavka_new.setCentralWidget(self.widget_zastavka)
            self.zastavka_new.resize(800, 600)
            self.zastavka_new.show()

    def info_a(self):
            self.info_aboyt_programm.setText('Это информация о программе')

    def zapros_1(self):
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ('SELECT `Код должности`, `Код звания`, `ФИО` FROM `сотрудники`')
                    cursor.execute(sql)
                    g = cursor.fetchall()
                    print(g)
                    self.info_1.setText(str(g))

    def zapros_2(self):
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ('SELECT `Код звания`, `Наименование` FROM `звания`')
                    cursor.execute(sql)
                    g = cursor.fetchall()
                    print(g)
                    self.info_2.setText(str(g))

    def zapros_3(self):
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ('SELECT `Код автомобиля`,`Код водителя` FROM `автомобили`')
                    cursor.execute(sql)
                    g = cursor.fetchall()
                    print(g)
                    self.info_3.setText(str(g))

    def zapros_4(self):
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ('SELECT `Технический осмотр` FROM `автомобили`')
                    cursor.execute(sql)
                    g = cursor.fetchall()
                    print(g)
                    self.info_4.setText(str(g))

    def zapros_5(self):
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ('SELECT `Отметка об нахождении` FROM `автомобили в угоне`')
                    cursor.execute(sql)
                    g = cursor.fetchall()
                    print(g)
                    self.info_5.setText(str(g))

class App(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        self.setStyle('Fusion')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
