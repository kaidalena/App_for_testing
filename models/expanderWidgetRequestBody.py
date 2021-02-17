from PyQt5 import QtWidgets, QtGui, QtCore
from models.my_expander import QExpander


class RequestBody(QExpander):
    def __init__(self, title='Request Body', parent=None):
        self.parent = parent

        self.verticalLayout = QtWidgets.QVBoxLayout(parent)
        self.request_body_json = QtWidgets.QTextEdit()
        self.verticalLayout.addWidget(self.request_body_json)
        QExpander.__init__(self, parent=parent, contentLayout=self.verticalLayout, title=title)

    def get_request_body(self):
        return self.request_body_json.toPlainText()