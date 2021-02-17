from PyQt5 import QtWidgets, QtGui
import json


class TabWidgetChecks(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        QtWidgets.QTabWidget.__init__(self, parent=parent)
        self.parent = parent

        # body tab
        self.checks_body_tab = QtWidgets.QWidget()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.checks_body_tab)
        self.check_body_textEdit = QtWidgets.QTextEdit(self.checks_body_tab)
        self.verticalLayout_2.addWidget(self.check_body_textEdit)
        self.addTab(self.checks_body_tab, "")

        # code tab
        self.checks_code_tab = QtWidgets.QWidget()
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.checks_code_tab)
        self.check_code_textEdit = QtWidgets.QTextEdit(self.checks_code_tab)
        self.horizontalLayout_2.addWidget(self.check_code_textEdit)
        self.addTab(self.checks_code_tab, "")

        # message tab
        self.checks_message_tab = QtWidgets.QWidget()
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.checks_message_tab)
        self.check_message_textEdit = QtWidgets.QTextEdit(self.checks_message_tab)
        self.horizontalLayout_3.addWidget(self.check_message_textEdit)
        self.addTab(self.checks_message_tab, "")

        self.check_tabs = {
            'body': self.check_body_textEdit,
            'code': self.check_code_textEdit,
            'message': self.check_message_textEdit
        }

        self.set_name()

    def set_name(self):
        self.setTabText(self.indexOf(self.checks_body_tab), "Body")
        self.setTabText(self.indexOf(self.checks_code_tab), "Code")
        self.setTabText(self.indexOf(self.checks_message_tab), "Message")

    def get_checks_data(self):
        try:
            check_data = {
                'body': {},
                'code': {},
                'message': {}
            }
            for tab in self.check_tabs:
                data = self.check_tabs[tab].toPlainText()
                if data is not None and data != '':
                    check_data[tab] = json.loads(data)
            return check_data
        except Exception as ex:
            print(f'f4rom get_checks_data {ex}')