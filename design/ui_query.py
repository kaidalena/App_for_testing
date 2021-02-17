from PyQt5 import QtCore, QtGui, QtWidgets
from models.http_tab import HTTP_Tab


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 840)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.get_tab = HTTP_Tab(method='GET')
        self.tabWidget.addTab(self.get_tab, "")

        self.post_tab = HTTP_Tab(method='POST')
        self.tabWidget.addTab(self.post_tab, "")

        self.put_tab = HTTP_Tab(method='PUT')
        self.tabWidget.addTab(self.put_tab, "")


        self.horizontalLayout_4.addWidget(self.tabWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.urls_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.urls_listWidget.setObjectName("urls_listWidget")
        self.verticalLayout_3.addWidget(self.urls_listWidget)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.saved_params_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.saved_params_tableWidget.setObjectName("saved_params_tableWidget")
        self.saved_params_tableWidget.setColumnCount(0)
        self.saved_params_tableWidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.saved_params_tableWidget)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.save_case_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.save_case_pushButton.setObjectName("save_case_pushButton")
        self.horizontalLayout_6.addWidget(self.save_case_pushButton)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.start_test_case_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.start_test_case_pushButton.setObjectName("start_test_case_pushButton")
        self.horizontalLayout_7.addWidget(self.start_test_case_pushButton)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        #####################################################################

        # try:
        #     q_exp = QExpander(self)
        #
        #     vbox = QtWidgets.QVBoxLayout()
        #     vbox.addWidget(q_exp.expander)
        #     vbox.setAlignment(QtCore.Qt.AlignTop)
        #
        #     # self.verticalLayout_3.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        #     self.verticalLayout_3.addLayout(vbox)
        # except Exception as ex:
        #     print(ex)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.get_tab), _translate("MainWindow", "GET"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.post_tab), _translate("MainWindow", "POST"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.put_tab), _translate("MainWindow", "PUT"))
        self.label_11.setText(_translate("MainWindow", "URLs"))
        self.label_12.setText(_translate("MainWindow", "Saved parameters"))
        self.save_case_pushButton.setText(_translate("MainWindow", "Сохранить сценарий"))
        self.start_test_case_pushButton.setText(_translate("MainWindow", "Запустить тестирование"))

    def _button_clicked(self, button):
        """
        For the toggle behavior of a QButtonGroup to work you must
        connect the clicked signal!
        """
        print('button-active', self.button_group.id(button))