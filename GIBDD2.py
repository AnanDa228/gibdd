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
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(634, 140, 161, 23))
        self.pushButton_4.clicked.connect(self.add)
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
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_4)

        self.zastavka()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Фильтры поиска"))
        self.pushButton_2.setText(_translate("MainWindow", "Формы"))
        self.pushButton_3.setText(_translate("MainWindow", "Заставка"))
        self.pushButton_4.setText(_translate("MainWindow", "Добавление данных"))
        self.label.setText(_translate("MainWindow", "БАЗА ДАННЫХ ГИБДД"))

    def add(self):
        self.add_info = QtWidgets.QMainWindow()
        self.add_info.setWindowTitle('Добавление данных')
        self.widget_into = QtWidgets.QWidget()
        self.lay2 = QtWidgets.QVBoxLayout(self.widget_into)

        self.add_table_1 = QtWidgets.QPushButton('Добавить новые звания')
        self.add_table_1.clicked.connect(self.add_zva)

        self.add_table_2 = QtWidgets.QPushButton('Добавить новые должности')
        self.add_table_2.clicked.connect(self.add_dol)

        self.add_table_3 = QtWidgets.QPushButton('Добавить новых сотрудников')
        self.add_table_3.clicked.connect(self.add_sot)

        self.add_table_4 = QtWidgets.QPushButton('Добавить новые марки автомобилей')
        self.add_table_4.clicked.connect(self.add_mark)

        self.add_table_5 = QtWidgets.QPushButton('Добавить новые автомобили')
        self.add_table_5.clicked.connect(self.add_avto)

        self.add_table_6 = QtWidgets.QPushButton('Добавить новых водителей')
        self.add_table_6.clicked.connect(self.add_vod)

        self.add_table_7 = QtWidgets.QPushButton('Добавить новые автомибили в угоне')
        self.add_table_7.clicked.connect(self.add_avtoug)

        self.lay2.addWidget(self.add_table_1)
        self.lay2.addWidget(self.add_table_2)
        self.lay2.addWidget(self.add_table_3)
        self.lay2.addWidget(self.add_table_4)
        self.lay2.addWidget(self.add_table_5)
        self.lay2.addWidget(self.add_table_6)
        self.lay2.addWidget(self.add_table_7)

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidget(self.widget_into)
        self.scroll.setWidgetResizable(True)

        self.add_info.setCentralWidget(self.scroll)
        self.add_info.resize(800, 600)

        self.add_info.show()

    def add_zva(self):
        self.add_zva1 = QtWidgets.QMainWindow()
        self.add_zva1.setWindowTitle('Добавление данных о званиях')
        self.widget_zva = QtWidgets.QWidget()
        self.zva2 = QtWidgets.QVBoxLayout(self.widget_zva)

        self.add_table_zva = QtWidgets.QPushButton('Добавить данные')
        self.add_table_zva.clicked.connect(self.add_table_1_2)

        self.idzva4 = QtWidgets.QLineEdit('Код звания')
        self.namezva = QtWidgets.QLineEdit('Наименование')
        self.nadzva = QtWidgets.QLineEdit('Надбавка')
        self.obyazzva = QtWidgets.QLineEdit('Обязанности')
        self.trebzva = QtWidgets.QLineEdit('Требования')

        self.zva2.addWidget(self.idzva4)
        self.zva2.addWidget(self.namezva)
        self.zva2.addWidget(self.nadzva)
        self.zva2.addWidget(self.obyazzva)
        self.zva2.addWidget(self.trebzva)
        self.zva2.addWidget(self.add_table_zva)

        self.new_scrol_zva = QtWidgets.QScrollArea()
        self.new_scrol_zva.setWidget(self.widget_zva)
        self.new_scrol_zva.setWidgetResizable(True)

        self.add_zva1.setCentralWidget(self.new_scrol_zva)
        self.add_zva1.resize(800, 600)

        self.add_zva1.show()

    def add_dol(self):
        self.add_dol1 = QtWidgets.QMainWindow()
        self.add_dol1.setWindowTitle('Добавление данных о должностях')
        self.widget_dol = QtWidgets.QWidget()
        self.dol2 = QtWidgets.QVBoxLayout(self.widget_dol)

        self.add_table_dol = QtWidgets.QPushButton('Добавить данные')
        self.add_table_dol.clicked.connect(self.add_table_1_3)

        self.iddol4 = QtWidgets.QLineEdit('Код должности')
        self.namedolzh = QtWidgets.QLineEdit('Наименование')
        self.naddol = QtWidgets.QLineEdit('Надбавка')
        self.obyazdol = QtWidgets.QLineEdit('Обязанности')
        self.trebdol = QtWidgets.QLineEdit('Требования')

        self.dol2.addWidget(self.iddol4)
        self.dol2.addWidget(self.namedolzh)
        self.dol2.addWidget(self.naddol)
        self.dol2.addWidget(self.obyazdol)
        self.dol2.addWidget(self.trebdol)
        self.dol2.addWidget(self.add_table_dol)

        self.new_scrol_dol = QtWidgets.QScrollArea()
        self.new_scrol_dol.setWidget(self.widget_dol)
        self.new_scrol_dol.setWidgetResizable(True)

        self.add_dol1.setCentralWidget(self.new_scrol_dol)
        self.add_dol1.resize(800, 600)

        self.add_dol1.show()

    def add_sot(self):
        self.add_sot1 = QtWidgets.QMainWindow()
        self.add_sot1.setWindowTitle('Добавление данных о сотрудниках')
        self.widget_sot = QtWidgets.QWidget()
        self.sot2 = QtWidgets.QVBoxLayout(self.widget_sot)

        self.add_table_sot = QtWidgets.QPushButton('Добавить данные')
        self.add_table_sot.clicked.connect(self.add_table_1_1)

        self.name = QtWidgets.QLineEdit('ФИО')
        self.age = QtWidgets.QLineEdit('Возраст')
        self.gender = QtWidgets.QLineEdit('Пол')
        self.adress = QtWidgets.QLineEdit('Адрес')
        self.phone = QtWidgets.QLineEdit('Телефон')
        self.passport = QtWidgets.QLineEdit('Номер паспорта')
        self.iddol = QtWidgets.QLineEdit('Код звания(существующий)')
        self.idzva = QtWidgets.QLineEdit('Код должности(существующий)')

        self.sot2.addWidget(self.name)
        self.sot2.addWidget(self.age)
        self.sot2.addWidget(self.gender)
        self.sot2.addWidget(self.adress)
        self.sot2.addWidget(self.phone)
        self.sot2.addWidget(self.passport)
        self.sot2.addWidget(self.iddol)
        self.sot2.addWidget(self.idzva)
        self.sot2.addWidget(self.add_table_sot)

        self.new_scrol_sot = QtWidgets.QScrollArea()
        self.new_scrol_sot.setWidget(self.widget_sot)
        self.new_scrol_sot.setWidgetResizable(True)

        self.add_sot1.setCentralWidget(self.new_scrol_sot)
        self.add_sot1.resize(800, 600)

        self.add_sot1.show()

    def add_mark(self): #table5
        self.add_mark1 = QtWidgets.QMainWindow()
        self.add_mark1.setWindowTitle('Добавление данных о марках')
        self.widget_mark = QtWidgets.QWidget()
        self.mark2 = QtWidgets.QVBoxLayout(self.widget_mark)

        self.add_table_mark = QtWidgets.QPushButton('Добавить данные')
        self.add_table_mark.clicked.connect(self.add_table_1_5)

        self.idmark4 = QtWidgets.QLineEdit('Код марки')
        self.namemark = QtWidgets.QLineEdit('Наименнование')
        self.firma = QtWidgets.QLineEdit('Фирма проивзодитель')
        self.country = QtWidgets.QLineEdit('Страна производитель')
        self.datestart = QtWidgets.QLineEdit('Дата начала производства, пример как писать(2019-06-21)')
        self.dateend = QtWidgets.QLineEdit('Дата окончания производства, пример как писать(2019-06-21)')
        self.character = QtWidgets.QLineEdit('Харатеристики')
        self.category = QtWidgets.QLineEdit('Категория')
        self.opisanie = QtWidgets.QLineEdit('Описание')


        self.mark2.addWidget(self.idmark4)
        self.mark2.addWidget(self.namemark)
        self.mark2.addWidget(self.firma)
        self.mark2.addWidget(self.country)
        self.mark2.addWidget(self.datestart)
        self.mark2.addWidget(self.dateend)
        self.mark2.addWidget(self.character)
        self.mark2.addWidget(self.category)
        self.mark2.addWidget(self.opisanie)
        self.mark2.addWidget(self.add_table_mark)

        self.new_scrol_mark = QtWidgets.QScrollArea()
        self.new_scrol_mark.setWidget(self.widget_mark)
        self.new_scrol_mark.setWidgetResizable(True)

        self.add_mark1.setCentralWidget(self.new_scrol_mark)
        self.add_mark1.resize(800, 600)

        self.add_mark1.show()

    def add_avto(self):
        self.add_avto1 = QtWidgets.QMainWindow()
        self.add_avto1.setWindowTitle('Добавление данных о марках')
        self.widget_avto = QtWidgets.QWidget()
        self.avto2 = QtWidgets.QVBoxLayout(self.widget_avto)

        self.add_table_avto = QtWidgets.QPushButton('Добавить данные')
        self.add_table_avto.clicked.connect(self.add_table_1_6)

        self.idavto4 = QtWidgets.QLineEdit('Код автомобиля')
        self.idvod2 = QtWidgets.QLineEdit('Код водителя(существующий)')
        self.idmark2 = QtWidgets.QLineEdit('Код марки(существующий)')
        self.regnumber = QtWidgets.QLineEdit('Регистрационный номер')
        self.kuznumber = QtWidgets.QLineEdit('Номер кузова')
        self.dvignumber = QtWidgets.QLineEdit('Номер двигателя')
        self.technumber = QtWidgets.QLineEdit('Номер техпаспорта')
        self.daterealese = QtWidgets.QLineEdit('Дата выпуска')
        self.datereg = QtWidgets.QLineEdit('Дата регистрации')
        self.coloravto = QtWidgets.QLineEdit('Цвет')
        self.techosmotr = QtWidgets.QLineEdit('Технический осмотр')
        self.datetechosmotr = QtWidgets.QLineEdit('Дата технического осмотра,пример как писать(2019-06-21)')
        self.opisanieavto = QtWidgets.QLineEdit('Описание')
        self.idsot2 = QtWidgets.QLineEdit('Код сотрудника(существующий)')

        self.avto2.addWidget(self.idavto4)
        self.avto2.addWidget(self.idvod2)
        self.avto2.addWidget(self.idmark2)
        self.avto2.addWidget(self.regnumber)
        self.avto2.addWidget(self.kuznumber)
        self.avto2.addWidget(self.dvignumber)
        self.avto2.addWidget(self.technumber)
        self.avto2.addWidget(self.daterealese)
        self.avto2.addWidget(self.datereg)
        self.avto2.addWidget(self.coloravto)
        self.avto2.addWidget(self.techosmotr)
        self.avto2.addWidget(self.datetechosmotr)
        self.avto2.addWidget(self.opisanieavto)
        self.avto2.addWidget(self.idsot2)
        self.avto2.addWidget(self.add_table_avto)

        self.new_scrol_avto = QtWidgets.QScrollArea()
        self.new_scrol_avto.setWidget(self.widget_avto)
        self.new_scrol_avto.setWidgetResizable(True)

        self.add_avto1.setCentralWidget(self.new_scrol_avto)
        self.add_avto1.resize(800, 600)

        self.add_avto1.show()

    def add_vod(self):
        self.add_vod1 = QtWidgets.QMainWindow()
        self.add_vod1.setWindowTitle('Добавление данных о водителях')
        self.widget_vod = QtWidgets.QWidget()
        self.vod2 = QtWidgets.QVBoxLayout(self.widget_vod)

        self.add_table_vod = QtWidgets.QPushButton('Добавить данные')
        self.add_table_vod.clicked.connect(self.add_table_1_4)

        self.idvod4 = QtWidgets.QLineEdit('Код водителя')
        self.fio = QtWidgets.QLineEdit('ФИО')
        self.datebirth = QtWidgets.QLineEdit('Дата рождения,пример как писать(2002-06-21)')
        self.adressvod = QtWidgets.QLineEdit('Адрес водителя')
        self.passdata = QtWidgets.QLineEdit('Паспортные данные')
        self.idvodud = QtWidgets.QLineEdit('Номер водительского удостоверения')
        self.datevyd = QtWidgets.QLineEdit('Дата выдачи удостоверения,пример как писать(2018-06-21)')
        self.dateoko = QtWidgets.QLineEdit('Дата окончания, пример как писать(2019-06-21)')
        self.categoryud = QtWidgets.QLineEdit('Категория удостоверения')
        self.opisanievod = QtWidgets.QLineEdit('Описание')
        self.idsot3 = QtWidgets.QLineEdit('Код сотрудника(существующий)')

        self.vod2.addWidget(self.idvod4)
        self.vod2.addWidget(self.fio)
        self.vod2.addWidget(self.datebirth)
        self.vod2.addWidget(self.adressvod)
        self.vod2.addWidget(self.passdata)
        self.vod2.addWidget(self.idvodud)
        self.vod2.addWidget(self.datevyd)
        self.vod2.addWidget(self.dateoko)
        self.vod2.addWidget(self.categoryud)
        self.vod2.addWidget(self.opisanievod)
        self.vod2.addWidget(self.idsot3)
        self.vod2.addWidget(self.add_table_vod)

        self.new_scrol_vod = QtWidgets.QScrollArea()
        self.new_scrol_vod.setWidget(self.widget_vod)
        self.new_scrol_vod.setWidgetResizable(True)

        self.add_vod1.setCentralWidget(self.new_scrol_vod)
        self.add_vod1.resize(800, 600)

        self.add_vod1.show()

    def add_avtoug(self):
        self.add_ugo1 = QtWidgets.QMainWindow()
        self.add_ugo1.setWindowTitle('Добавление данных о сотрудниках')
        self.widget_ugo = QtWidgets.QWidget()
        self.ugo2 = QtWidgets.QVBoxLayout(self.widget_ugo)

        self.add_table_ugo = QtWidgets.QPushButton('Добавить данные')
        self.add_table_ugo.clicked.connect(self.add_table_1_7)

        self.dateugo = QtWidgets.QLineEdit('Дата угона, пример как писать(2019-06-21)')
        self.dateobr = QtWidgets.QLineEdit('Дата обращения, пример как писать(2019-06-21)')
        self.kodavto = QtWidgets.QLineEdit('Код автомобиля(существующий)')
        self.kodvodi = QtWidgets.QLineEdit('Код водителя(существующий)')
        self.obstoatel = QtWidgets.QLineEdit('Обстоятельства угона')
        self.checkugo = QtWidgets.QLineEdit('Отметка об нахождении')
        self.datanahod = QtWidgets.QLineEdit('Дата нахождения, пример как писать(2019-06-21)')
        self.kodsotr = QtWidgets.QLineEdit('Код сотрудника(существующий)')

        self.ugo2.addWidget(self.dateugo)
        self.ugo2.addWidget(self.dateobr)
        self.ugo2.addWidget(self.kodavto)
        self.ugo2.addWidget(self.kodvodi)
        self.ugo2.addWidget(self.obstoatel)
        self.ugo2.addWidget(self.checkugo)
        self.ugo2.addWidget(self.datanahod)
        self.ugo2.addWidget(self.kodsotr)
        self.ugo2.addWidget(self.add_table_ugo)

        self.new_scrol_ugo = QtWidgets.QScrollArea()
        self.new_scrol_ugo.setWidget(self.widget_ugo)
        self.new_scrol_ugo.setWidgetResizable(True)

        self.add_ugo1.setCentralWidget(self.new_scrol_ugo)
        self.add_ugo1.resize(800, 600)

        self.add_ugo1.show()

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
        self.table_1.setHorizontalHeaderLabels(
            ['Код сотрудника', 'ФИО', 'Возраст', 'Пол', 'Адрес', 'Телефон', 'Паспортные данные', 'Код должности',
             'Код звания'])
        self.but_update_table_1 = QtWidgets.QPushButton('Обновить сотрудники')
        self.but_update_table_1.clicked.connect(self.sync_brigades)

        self.lay_info.addWidget(self.table_1)
        self.lay_info.addWidget(self.but_update_table_1)

        self.table_2 = QtWidgets.QTableWidget()
        self.table_2.setColumnCount(5)
        self.table_2.setRowCount(len(self.get_info_customers()))
        self.table_2.setHorizontalHeaderLabels(
            ['Код звания', 'Наименование', '	Надбавка', 'Обязанности', 'Требования'])
        self.but_update_table_2 = QtWidgets.QPushButton('Обновить Звания')
        self.but_update_table_2.clicked.connect(self.sync_customers)

        self.lay_info.addWidget(self.table_2)
        self.lay_info.addWidget(self.but_update_table_2)

        self.table_3 = QtWidgets.QTableWidget()
        self.table_3.setColumnCount(5)
        self.table_3.setRowCount(len(self.get_info_materials()))
        self.table_3.setHorizontalHeaderLabels(
            ['Код должности', 'Наименование Должности', 'Оклад', 'Обязанности', 'Требования'])
        self.but_update_table_3 = QtWidgets.QPushButton('Обновить Должности')
        self.but_update_table_3.clicked.connect(self.sync_materials)

        self.lay_info.addWidget(self.table_3)
        self.lay_info.addWidget(self.but_update_table_3)

        self.table_4 = QtWidgets.QTableWidget()
        self.table_4.setColumnCount(11)
        self.table_4.setRowCount(len(self.get_info_orders()))
        self.table_4.setHorizontalHeaderLabels(
            ['Код водителя', 'ФИО', 'Дата рождения', 'Адрес', 'Паспортные данные', 'Номер водительского удостоверения',
             'Дата выдачи удостоверения', 'Дата окончания удостоверения', 'Категория удостоверения', 'Описание',
             'Код сотрудника'])
        self.but_update_table_4 = QtWidgets.QPushButton('Обновить Водители')
        self.but_update_table_4.clicked.connect(self.sync_orders)

        self.lay_info.addWidget(self.table_4)
        self.lay_info.addWidget(self.but_update_table_4)

        self.table_5 = QtWidgets.QTableWidget()
        self.table_5.setColumnCount(9)
        self.table_5.setRowCount(len(self.get_info_positions()))
        self.table_5.setHorizontalHeaderLabels(
            ['Код марки', 'Наименование', 'Фирма производитель', 'Страна производитель', 'Дата начала производства',
             'Дата окончания производства', 'Характеристики', 'Категория', 'Описание'])
        self.but_update_table_5 = QtWidgets.QPushButton('Обновить Марки автомобилей')
        self.but_update_table_5.clicked.connect(self.sync_positions)

        self.lay_info.addWidget(self.table_5)
        self.lay_info.addWidget(self.but_update_table_5)

        self.table_6 = QtWidgets.QTableWidget()
        self.table_6.setColumnCount(14)
        self.table_6.setRowCount(len(self.get_info_staff()))
        self.table_6.setHorizontalHeaderLabels(
            ['Код автомобиля', 'Код водителя', 'Код марки', 'Регистрационный номер', 'Номер кузова', 'Номер двигателя',
             'Номер техпаспорта', 'Дата выпуска', 'Дата регистрации', 'Цвет', 'Технический осмотр',
             'Дата технического осмотра', 'Описание', 'Код сотрудника'])
        self.but_update_table_6 = QtWidgets.QPushButton('Обновить Автомобили')
        self.but_update_table_6.clicked.connect(self.sync_staff)

        self.lay_info.addWidget(self.table_6)
        self.lay_info.addWidget(self.but_update_table_6)

        self.table_7 = QtWidgets.QTableWidget()
        self.table_7.setColumnCount(7)
        self.table_7.setRowCount(len(self.get_info_types_of_works()))
        self.table_7.setHorizontalHeaderLabels(
            ['Дата угона', 'Дата обращения', 'Код автомобиля', 'Код водителя', 'Обстоятельства угона',
             'Отметка о находжении', 'Дата нахождения', 'Код сотрудника'])
        self.but_update_table_7 = QtWidgets.QPushButton('Обновить Автомобили в угоне')
        self.but_update_table_7.clicked.connect(self.sync_types_of_works)

        self.new_scrol = QtWidgets.QScrollArea()
        self.new_scrol.setWidget(self.widget_info)
        self.new_scrol.setWidgetResizable(True)

        self.all_info.setCentralWidget(self.new_scrol)
        self.all_info.resize(800, 600)

        self.all_info.show()

        self.getDeleteSingleBrigadesUi()
        self.getDeleteSingleZvaUi()
        self.getDeleteSingleDolzhUi()
        self.getDeleteSingleMarkUi()
        self.getDeleteSingleAvtoUi()
        self.getDeleteSingleVodUi()
        self.getDeleteSingleAvtoUi()

        # Настройка UI для удаления 1 сотрудника по его идентификатору
    def getDeleteSingleBrigadesUi(self):
            self.deleteBrigadesQButton = QtWidgets.QPushButton('Удалить запись в сотрудниках')
            self.deleteBrigadesQButton.clicked.connect(self.deleteOneBrigades)
            self.deleteBrigadesPrimaryValue = QtWidgets.QLineEdit('код сотрудника')
            self.lay_info.addWidget(self.deleteBrigadesPrimaryValue)
            self.lay_info.addWidget(self.deleteBrigadesQButton)

        # Удаление 1 сотрудника по идентификатору
    def deleteOneBrigades(self):
            print(self.deleteBrigadesPrimaryValue.text())
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = "DELETE FROM `сотрудники` WHERE `Код сотрудника` = %s"
                    cursor.execute(sql, (self.deleteBrigadesPrimaryValue.text()))
                    bd.commit()

    def getDeleteSingleZvaUi(self):
            self.deleteZvaQButton = QtWidgets.QPushButton('Удалить запись в званиях')
            self.deleteZvaQButton.clicked.connect(self.deleteOneZva)
            self.deleteZvanyePrimaryValue = QtWidgets.QLineEdit('код звания')
            self.lay_info.addWidget(self.deleteZvanyePrimaryValue)
            self.lay_info.addWidget(self.deleteZvaQButton)

        # Удаление 1 сотрудника по идентификатору
    def deleteOneZva(self):
            print(self.deleteZvanyePrimaryValue.text())
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = "DELETE FROM `звания` WHERE `Код звания` = %s"
                    cursor.execute(sql, (self.deleteZvanyePrimaryValue.text()))
                    bd.commit()

    def getDeleteSingleDolzhUi(self):
            self.deleteDolzhQButton = QtWidgets.QPushButton('Удалить запись в должностях')
            self.deleteDolzhQButton.clicked.connect(self.deleteOneDolzhUi)
            self.deleteDolzhPrimaryValue = QtWidgets.QLineEdit('код должности')
            self.lay_info.addWidget(self.deleteDolzhPrimaryValue)
            self.lay_info.addWidget(self.deleteDolzhQButton)

        # Удаление 1 сотрудника по идентификатору
    def deleteOneDolzhUi(self):
            print(self.deleteDolzhPrimaryValue.text())
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = "DELETE FROM `должности` WHERE `Код должности` = %s"
                    cursor.execute(sql, (self.deleteDolzhPrimaryValue.text()))
                    bd.commit()

    def getDeleteSingleVodUi(self):
            self.deleteVodQButton = QtWidgets.QPushButton('Удалить запись в водителях')
            self.deleteVodQButton.clicked.connect(self.deleteOneVodUi)
            self.deleteVodPrimaryValue = QtWidgets.QLineEdit('код водителя')
            self.lay_info.addWidget(self.deleteVodPrimaryValue)
            self.lay_info.addWidget(self.deleteVodQButton)

        # Удаление 1 сотрудника по идентификатору
    def deleteOneVodUi(self):
            print(self.deleteVodPrimaryValue.text())
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = "DELETE FROM `водители` WHERE `Код водителя` = %s"
                    cursor.execute(sql, (self.deleteVodPrimaryValue.text()))
                    bd.commit()

    def getDeleteSingleMarkUi(self):
            self.deleteMarkQButton = QtWidgets.QPushButton('Удалить запись в марках автомобиля')
            self.deleteMarkQButton.clicked.connect(self.deleteOneMarkUi)
            self.deleteMarkPrimaryValue = QtWidgets.QLineEdit('код марки')
            self.lay_info.addWidget(self.deleteMarkPrimaryValue)
            self.lay_info.addWidget(self.deleteMarkQButton)

        # Удаление 1 сотрудника по идентификатору
    def deleteOneMarkUi(self):
            print(self.deleteMarkPrimaryValue.text())
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = "DELETE FROM `марки автомобилей` WHERE `Код марки` = %s"
                    cursor.execute(sql, (self.deleteMarkPrimaryValue.text()))
                    bd.commit()

    def getDeleteSingleAvtoUi(self):
            self.deleteAvtoQButton = QtWidgets.QPushButton('Удалить запись в автомобилях')
            self.deleteAvtoQButton.clicked.connect(self.deleteOneAvtoUi)
            self.deleteAvtoPrimaryValue = QtWidgets.QLineEdit('код автомобиля')
            self.lay_info.addWidget(self.deleteAvtoPrimaryValue)
            self.lay_info.addWidget(self.deleteAvtoQButton)

        # Удаление 1 сотрудника по идентификатору
    def deleteOneAvtoUi(self):
            print(self.deleteAvtoPrimaryValue.text())
            with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = "DELETE FROM `автомобили` WHERE `Код автомобиля` = %s"
                    cursor.execute(sql, (self.deleteAvtoPrimaryValue.text()))
                    bd.commit()

    ##brigadees
    def get_info_brigades(self):
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `сотрудники`')
                cursor.execute(sql)
                g = cursor.fetchall()
            print(g)
            return g

        # Синхронизация свежего списка сотрудников

    def sync_brigades(self):
        row = 0

        # Получим всех сотрудников из базы
        brigades = self.get_info_brigades()
        # После получения сотрудников обновляем таблицу равную с количеством из бд
        self.table_1.setRowCount(len(brigades))

        for singleSotrud in brigades:
            column = 0

            for attribute in singleSotrud:
                attributeStr = str(attribute)
                print(attributeStr)
                self.table_1.setItem(row, column, QtWidgets.QTableWidgetItem(attributeStr))
                column += 1

            row += 1



        ###customers

    def get_info_customers(self):
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `звания`')
                cursor.execute(sql)
                g = cursor.fetchall()

            return g

        # Синхронизация свежего списка сотрудников

    def sync_customers(self):
        row = 0

        # Получим всех сотрудников из базы
        brigades = self.get_info_customers()
        # После получения сотрудников обновляем таблицу равную с количеством из бд
        self.table_1.setRowCount(len(brigades))

        for singleSotrud in brigades:
            column = 0

            for attribute in singleSotrud:
                attributeStr = str(attribute)
                print(attributeStr)
                self.table_2.setItem(row, column, QtWidgets.QTableWidgetItem(attributeStr))
                column += 1

            row += 1

    ###materials
    def get_info_materials(self):
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `должности`')
                cursor.execute(sql)
                g = cursor.fetchall()

            return g

        # Синхронизация свежего списка сотрудников

    def sync_materials(self):
        row = 0

        # Получим всех сотрудников из базы
        brigades = self.get_info_materials()
        # После получения сотрудников обновляем таблицу равную с количеством из бд
        self.table_1.setRowCount(len(brigades))

        for singleSotrud in brigades:
            column = 0

            for attribute in singleSotrud:
                attributeStr = str(attribute)
                print(attributeStr)
                self.table_3.setItem(row, column, QtWidgets.QTableWidgetItem(attributeStr))
                column += 1

            row += 1

    ###orders
    def get_info_orders(self):
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `водители`')
                cursor.execute(sql)
                g = cursor.fetchall()

            return g

        # Синхронизация свежего списка сотрудников

    def sync_orders(self):
        row = 0

        # Получим всех сотрудников из базы
        brigades = self.get_info_orders()
        # После получения сотрудников обновляем таблицу равную с количеством из бд
        self.table_1.setRowCount(len(brigades))

        for singleSotrud in brigades:
            column = 0

            for attribute in singleSotrud:
                attributeStr = str(attribute)
                print(attributeStr)
                self.table_4.setItem(row, column, QtWidgets.QTableWidgetItem(attributeStr))
                column += 1

            row += 1

    ###  positions
    def get_info_positions(self):
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `марки автомобилей`')
                cursor.execute(sql)
                g = cursor.fetchall()

            return g

        # Синхронизация свежего списка сотрудников

    def sync_positions(self):
        row = 0

        # Получим всех сотрудников из базы
        brigades = self.get_info_positions()
        # После получения сотрудников обновляем таблицу равную с количеством из бд
        self.table_1.setRowCount(len(brigades))

        for singleSotrud in brigades:
            column = 0

            for attribute in singleSotrud:
                attributeStr = str(attribute)
                print(attributeStr)
                self.table_5.setItem(row, column, QtWidgets.QTableWidgetItem(attributeStr))
                column += 1

            row += 1

    ###staff
    def get_info_staff(self):
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `автомобили`')
                cursor.execute(sql)
                g = cursor.fetchall()

            return g

        # Синхронизация свежего списка сотрудников

    def sync_staff(self):
        row = 0

        # Получим всех сотрудников из базы
        brigades = self.get_info_staff()
        # После получения сотрудников обновляем таблицу равную с количеством из бд
        self.table_1.setRowCount(len(brigades))

        for singleSotrud in brigades:
            column = 0

            for attribute in singleSotrud:
                attributeStr = str(attribute)
                print(attributeStr)
                self.table_6.setItem(row, column, QtWidgets.QTableWidgetItem(attributeStr))
                column += 1

            row += 1

    ###types_of_works
    def get_info_types_of_works(self):
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `автомобили в угоне`')
                cursor.execute(sql)
                g = cursor.fetchall()

            return g

        # Синхронизация свежего списка сотрудников

    def sync_types_of_works(self):
        row = 0

        # Получим всех сотрудников из базы
        brigades = self.get_info_types_of_works()
        # После получения сотрудников обновляем таблицу равную с количеством из бд
        self.table_1.setRowCount(len(brigades))

        for singleSotrud in brigades:
            column = 0

            for attribute in singleSotrud:
                attributeStr = str(attribute)
                print(attributeStr)
                self.table_7.setItem(row, column, QtWidgets.QTableWidgetItem(attributeStr))
                column += 1

            row += 1

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

    def add_table_1_1(self):
        print(self.name.text())
        print(self.age.text())
        print(self.gender.text())
        print(self.adress.text())
        print(self.phone.text())
        print(self.passport.text())
        print(self.iddol.text())
        print(self.idzva.text())
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = (
                    "INSERT INTO `сотрудники` (`ФИО`, `Возраст`, `Пол`, `Адрес`, `Телефон`, `Паспортные данные`, `Код должности`, `Код звания`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
                cursor.execute(sql, (
                self.name.text(), self.age.text(), self.gender.text(), self.adress.text(),
                self.phone.text(), self.passport.text(), self.iddol.text(), self.idzva.text()))
                bd.commit()

        # Синхронизация свежего списка сотрудников
    def sync_brigades(self):
            row = 0

            # Получим всех сотрудников из базы
            brigades = self.get_info_brigades()
            # После получения сотрудников обновляем таблицу равную с количеством из бд
            self.table_1.setRowCount(len(brigades))

            for singleSotrud in brigades:
                column = 0

                for attribute in singleSotrud:
                    attributeStr = str(attribute)
                    print(attributeStr)
                    self.table_1.setItem(row, column, QtWidgets.QTableWidgetItem(attributeStr))
                    column += 1

                row += 1

    def add_table_1_2(self):
        print(self.idzva4.text())
        print(self.namezva.text())
        print(self.nadzva.text())
        print(self.obyazzva.text())
        print(self.trebzva.text())
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = (
                    "INSERT INTO `звания` (`Код звания`,`Наименование`, `Надбавка`, `Обязанности`, `Требования`) VALUES (%s, %s, %s, %s, %s)")
                cursor.execute(sql, (
                self.idzva4.text(),self.namezva.text(), self.nadzva.text(), self.obyazzva.text(),self.trebzva.text()))
                bd.commit()

    def add_table_1_3(self):
        print(self.iddol4.text())
        print(self.namedolzh.text())
        print(self.naddol.text())
        print(self.obyazdol.text())
        print(self.trebdol.text())
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = (
                    "INSERT INTO `должности` (`Код должности`,`Наименование должности`, `Оклад`, `Обязанности`, `Требования`) VALUES (%s, %s, %s, %s, %s)")
                cursor.execute(sql, (
                    self.iddol4.text() ,self.namedolzh.text(), self.naddol.text(), self.obyazdol.text(), self.trebdol.text()))
                bd.commit()

    def add_table_1_4(self):
        print(self.idvod4.text())
        print(self.fio.text())
        print(self.datebirth.text())
        print(self.adressvod.text())
        print(self.passdata.text())
        print(self.idvodud.text())
        print(self.datevyd.text())
        print(self.dateoko.text())
        print(self.categoryud.text())
        print(self.opisanievod.text())
        print(self.idsot3.text())
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = (
                    "INSERT INTO `водители` (`Код водителя`,`ФИО`, `Дата рождения`, `Адрес`, `Паспортные данные`, `Номер водительского удостоверения`, `Дата выдачи удостоверения`, `Дата окончания удостоверения`, `Категория удостоверения`,`Описание`,`Код сотрудника`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                cursor.execute(sql, (
                self.idvod4.text(),self.fio.text(), self.datebirth.text(), self.adressvod.text(), self.passdata.text(),
                self.idvodud.text(), self.datevyd.text(), self.dateoko.text(), self.categoryud.text(), self.opisanievod.text(), self.idsot3.text()))
                bd.commit()

    def add_table_1_5(self):
        print(self.idmark4.text())
        print(self.namemark.text())
        print(self.firma.text())
        print(self.country.text())
        print(self.datestart.text())
        print(self.dateend.text())
        print(self.character.text())
        print(self.category.text())
        print(self.opisanie.text())
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = (
                    "INSERT INTO `марки автомобилей` (`Код марки`,`Наименование`, `Фирма производитель`, `Страна производитель`, `Дата начала производства`, `Дата окончания производства`, `Характеристики`, `Категория`, `Описание`) VALUES (%s ,%s, %s, %s, %s, %s, %s, %s, %s)")
                cursor.execute(sql, (
                self.idmark4.text(), self.namemark.text(), self.firma.text(), self.country.text(), self.datestart.text(),
                self.dateend.text(), self.character.text(), self.category.text(), self.opisanie.text()))
                bd.commit()

    def add_table_1_6(self):
        print(self.idavto4.text())
        print(self.idvod2.text())
        print(self.idmark2.text())
        print(self.regnumber.text())
        print(self.kuznumber.text())
        print(self.dvignumber.text())
        print(self.technumber.text())
        print(self.daterealese.text())
        print(self.datereg.text())
        print(self.coloravto.text())
        print(self.techosmotr.text())
        print(self.datetechosmotr.text())
        print(self.opisanieavto.text())
        print(self.idsot2.text())
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = (
                    "INSERT INTO `автомобили` (`Код автомобиля`,`Код водителя`, `Код марки`, `Регистрационный номер`, `Номер кузова`, `Номер двигателя`,`Номер техпаспорта`,`Дата выпуска`, `Дата регистрации`,`Цвет`,`Технический осмотр`,`Дата технического осмотра`,`Описание`,`Код сотрудника`) VALUES (%s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                cursor.execute(sql, (
                self.idavto4.text(),self.idvod2.text(), self.idmark2.text(), self.regnumber.text(), self.kuznumber.text(),
                self.dvignumber.text(), self.technumber.text(), self.daterealese.text(), self.datereg.text(), self.coloravto.text(),self.techosmotr.text(),self.datetechosmotr.text(),self.opisanieavto.text(),self.idsot2.text()))
                bd.commit()

    def add_table_1_7(self):
        print(self.dateugo.text())
        print(self.dateobr.text())
        print(self.kodavto.text())
        print(self.kodvodi.text())
        print(self.obstoatel.text())
        print(self.checkugo.text())
        print(self.datanahod.text())
        print(self.kodsotr.text())
        with connections.Connection(user='root', password='root', host='localhost', database='gibdd') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = (
                    "INSERT INTO `водители` (`Дата угона`, `Дата обращения`, `Код автомобиля`, `Код водителя`, `Обстоятельства угона`, `Отметка об нахождении`, `Дата нахождения `,`Код сотрудника`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
                cursor.execute(sql, (
                self.dateugo.text(), self.dateobr.text(), self.kodavto.text(), self.kodvodi.text(),
                self.obstoatel.text(), self.checkugo.text(), self.datanahod.text(), self.kodsotr.text()))
                bd.commit()

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
