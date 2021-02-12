from PyQt5 import QtWidgets, QtGui


class GridLayoutParams(QtWidgets.QGridLayout):
    def __init__(self, parent=None):
        QtWidgets.QGridLayout.__init__(self, parent)
        self.params = {
            'keys': [],
            'values': [],
            # 'ch_boxes': [self.pp_1_checkBox]
        }
        self.parent = parent

        self.label_key = QtWidgets.QLabel(self.parent)
        self.label_key.setText('Key')
        self.addWidget(self.label_key, 0, 0, 1, 1)
        self.label_key = QtWidgets.QLabel(self.parent)
        self.label_key.setText('Value')
        self.addWidget(self.label_key, 0, 1, 1, 1)

        self.add_btn = QtWidgets.QPushButton(self.parent)
        self.add_btn.setText('+')
        self.add_btn.clicked.connect(self.add_fields_params)
        self.addWidget(self.add_btn, 0, 2, 1, 1)

        self.params['keys'].append(QtWidgets.QLineEdit(parent))
        self.params['values'].append(QtWidgets.QLineEdit(parent))
        hidden_field = QtWidgets.QLineEdit(parent)
        hidden_field.setVisible(False)
        self.addWidget(self.params['keys'][0])
        self.addWidget(self.params['values'][0])
        self.create_hidden_field()

    def add_fields_params(self):
        try:
            index = len(self.params['keys'])
            self.params['keys'].append(QtWidgets.QLineEdit(self.parent))
            self.params['values'].append(QtWidgets.QLineEdit(self.parent))
            hidden_field = QtWidgets.QLineEdit(self.parent)
            hidden_field.setVisible(False)
            self.addWidget(self.params['keys'][index])
            self.addWidget(self.params['values'][index])
            self.addWidget(hidden_field)
        except Exception as ex:
            print(ex)

    def get_params(self):
        return self.params

    def create_hidden_field(self, row=None, column=None):
        hidden_field = QtWidgets.QLineEdit(self.parent)
        hidden_field.setVisible(False)
        self.addWidget(hidden_field)