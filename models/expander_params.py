from PyQt5 import QtWidgets, QtGui, QtCore
from models.my_expander import QExpander


class ExpanderParams(QExpander):
    def __init__(self, title='', parent=None):
        try:
            # print(f'Parent for grid params: {parent}')
            self.grid = QtWidgets.QGridLayout(parent)
            self.grid.setRowMinimumHeight(1, 20)
            self.parent = parent
            self.params = {
                'keys': [],
                'values': [],
                # 'ch_boxes': [self.pp_1_checkBox]
            }

            self.label_key = QtWidgets.QLabel(self.parent)
            self.label_key.setText('Key')
            self.grid.addWidget(self.label_key, 0, 0, 1, 1)
            self.label_key = QtWidgets.QLabel(self.parent)
            self.label_key.setText('Value')
            self.grid.addWidget(self.label_key, 0, 1, 1, 1)

            self.add_btn = QtWidgets.QPushButton(self.parent)
            self.add_btn.setText('+')
            self.add_btn.clicked.connect(self.add_fields_params)
            self.grid.addWidget(self.add_btn, 0, 2, 1, 1)

            self.params['keys'].append(QtWidgets.QLineEdit(parent))
            self.params['values'].append(QtWidgets.QLineEdit(parent))
            hidden_field = QtWidgets.QLineEdit(parent)
            hidden_field.setVisible(False)
            self.grid.addWidget(self.params['keys'][0])
            self.grid.addWidget(self.params['values'][0])
            self.create_hidden_field()
            QExpander.__init__(self, parent=parent, grid=self.grid, title=title)

        except Exception as ex:
            print(f'From ExpanderParams __init__: {ex}')

    def add_fields_params(self):
        try:
            index = len(self.params['keys'])
            self.params['keys'].append(QtWidgets.QLineEdit(self.parent))
            self.params['values'].append(QtWidgets.QLineEdit(self.parent))
            hidden_field = QtWidgets.QLineEdit(self.parent)
            hidden_field.setVisible(False)
            # print(f'[add_fields_params] grid height before: {self.grid.sizeHint().height()}')
            self.grid.addWidget(self.params['keys'][index])
            self.grid.addWidget(self.params['values'][index])
            self.grid.addWidget(hidden_field)
            self.expander.change_anim()
        except Exception as ex:
            print(ex)

    def get_params(self):
        return self.params

    def create_hidden_field(self, row=None, column=None):
        hidden_field = QtWidgets.QLineEdit(self.parent)
        hidden_field.setVisible(False)
        self.grid.addWidget(hidden_field)