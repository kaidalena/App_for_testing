from PyQt5 import QtWidgets, QtGui


class TabWidgetChecks(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        QtWidgets.QTabWidget.__init__(self, parent)
        self.parent = parent
        # self.get_tab = QtWidgets.QWidget()
        # self.checks_body_tab = QtWidgets.QWidget()
        # # self.checks_body_tab.setObjectName("checks_body_tab")
        # self.check_body_textEdit = QtWidgets.QTextEdit(self.checks_body_tab)
        # self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.checks_body_tab)
        # self.verticalLayout_2.addWidget(self.check_body_textEdit)
        # self.checks_tabWidget.addTab(self.checks_body_tab, "")
        #
        # self.checks_code_tab = QtWidgets.QWidget()
        # # self.checks_code_tab.setObjectName("checks_code_tab")
        # self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.checks_code_tab)
        # # self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.check_code_textEdit = QtWidgets.QTextEdit(self.checks_code_tab)
        # # self.check_code_textEdit.setObjectName("check_code_textEdit")
        # self.horizontalLayout_2.addWidget(self.check_code_textEdit)
        # self.checks_tabWidget.addTab(self.checks_code_tab, "")
        #
        # self.checks_message_tab = QtWidgets.QWidget()
        # # self.checks_message_tab.setObjectName("checks_message_tab")
        # self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.checks_message_tab)
        # # self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # self.check_message_textEdit = QtWidgets.QTextEdit(self.checks_message_tab)
        # # self.check_message_textEdit.setObjectName("check_message_textEdit")
        # self.horizontalLayout_3.addWidget(self.check_message_textEdit)
        # self.checks_tabWidget.addTab(self.checks_message_tab, "")
