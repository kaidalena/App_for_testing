from PyQt5 import QtWidgets, QtGui, QtCore
from models.expander_params import ExpanderParams
from models.grid_layout_params import GridLayoutParams
from models.errors import MyValueError
from models.my_query import MyQuery
import helper, json
from models.my_expander import QExpander


class HTTP_Tab(QtWidgets.QWidget):
    def __init__(self, method, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.parent = parent
        self.method = method
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout()

        # url
        self.url_label = QtWidgets.QLabel(self)
        self.horizontalLayout.addWidget(self.url_label)
        self.url_lineEdit = QtWidgets.QLineEdit(self)
        self.horizontalLayout.addWidget(self.url_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        # path params
        # self.path_params_groupBox = QtWidgets.QGroupBox(self)
        # self.gridLayout_path_params = GridLayoutParams(self.path_params_groupBox)
        # self.verticalLayout.addWidget(self.path_params_groupBox)

        # try:
            # grid = GridLayoutParams(self)
            # print(f'Self; {self}')
            # q_exp = QExpander(parent=self, grid=grid)

            # vbox = QtWidgets.QVBoxLayout()
            # vbox.addWidget(q_exp.expander)
            # vbox.setAlignment(QtCore.Qt.AlignTop)

            # self.path_params_groupBox = q_exp.params_groupBox
            # self.gridLayout_path_params = q_exp.gridLayout_path_params

            # self.verticalLayout.addWidget(q_exp.expander)
        # except Exception as ex:
        #     print(ex)

        # self.path_params_groupBox = QtWidgets.QGroupBox(self)
        self.gridLayout_path_params = ExpanderParams(title='Path params', parent=self)
        self.verticalLayout.addWidget(self.gridLayout_path_params.expander)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        # query params
        self.query_params_groupBox = QtWidgets.QGroupBox(self)
        self.query_params_groupBox.setObjectName("query_params_groupBox")
        self.gridLayout_query_params = GridLayoutParams(self.query_params_groupBox)
        self.verticalLayout.addWidget(self.query_params_groupBox)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        # headers
        self.headers_groupBox = QtWidgets.QGroupBox(self)
        self.gridLayout_headers = GridLayoutParams(self.headers_groupBox)
        self.verticalLayout.addWidget(self.headers_groupBox)


        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        # checks
        self.checks_label = QtWidgets.QLabel(self)
        self.verticalLayout.addWidget(self.checks_label)
        self.checks_tabWidget = QtWidgets.QTabWidget(self)
          # body tab
        self.checks_body_tab = QtWidgets.QWidget()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.checks_body_tab)
        self.check_body_textEdit = QtWidgets.QTextEdit(self.checks_body_tab)
        self.verticalLayout_2.addWidget(self.check_body_textEdit)
        self.checks_tabWidget.addTab(self.checks_body_tab, "")
          # code tab
        self.checks_code_tab = QtWidgets.QWidget()
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.checks_code_tab)
        self.check_code_textEdit = QtWidgets.QTextEdit(self.checks_code_tab)
        self.horizontalLayout_2.addWidget(self.check_code_textEdit)
        self.checks_tabWidget.addTab(self.checks_code_tab, "")
          # message tab
        self.checks_message_tab = QtWidgets.QWidget()
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.checks_message_tab)
        self.check_message_textEdit = QtWidgets.QTextEdit(self.checks_message_tab)
        self.horizontalLayout_3.addWidget(self.check_message_textEdit)
        self.checks_tabWidget.addTab(self.checks_message_tab, "")

        self.check_tabs = {
            'body': self.check_body_textEdit,
            'code': self.check_code_textEdit,
            'message': self.check_message_textEdit
        }

        self.verticalLayout.addWidget(self.checks_tabWidget)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)

        # save url btn
        self.save_url_pushButton = QtWidgets.QPushButton(self)
        self.horizontalLayout_5.addWidget(self.save_url_pushButton)

        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.set_name()

    def set_name(self):
        self.url_label.setText("URL:")
        # self.path_params_groupBox.setTitle("Path params")
        self.query_params_groupBox.setTitle("Query params")
        self.headers_groupBox.setTitle("Headers")
        self.checks_label.setText("Checks")
        self.checks_tabWidget.setTabText(self.checks_tabWidget.indexOf(self.checks_body_tab),"Body")
        self.checks_tabWidget.setTabText(self.checks_tabWidget.indexOf(self.checks_code_tab),"Code")
        self.checks_tabWidget.setTabText(self.checks_tabWidget.indexOf(self.checks_message_tab),"Message")
        self.save_url_pushButton.setText("Добавить урл в сценарий")

    def get_method(self):
        return self.method

    def get_url(self):
        url = self.url_lineEdit.text()
        if url is None or url == '':
            raise MyValueError("Поле 'URL' не должно быть пустым")
        return url

    def get_custom_params(self, param_obj):
        # print(param_obj)
        params = {}
        use_saved_param = []
        for key_line_edit in param_obj['keys']:
            if key_line_edit.text() != '':
                # if param_obj['ch_boxes'][param_obj['keys'].index(key_line_edit)].isChecked():
                #     use_saved_param.append(key_line_edit.text())
                # else:
                    params[key_line_edit.text()] = param_obj['values'][param_obj['keys'].index(key_line_edit)].text()
        return params, use_saved_param

    def get_path_params(self):
        return self.get_custom_params(self.gridLayout_path_params.get_params())

    def get_query_params(self):
        return self.get_custom_params(self.gridLayout_query_params.get_params())

    def get_headers(self):
        return self.get_custom_params(self.gridLayout_headers.get_params())

    def add_new_url_into_case(self):
        try:
            query = MyQuery()

            query.set_method(self.get_method())
            query.set_url(self.get_url())

            path_params, use_saved_path_params = self.get_path_params()
            query.add_path_params(path_params)
            query.add_path_params_saved_before(use_saved_path_params)

            query_params, use_saved_query_params = self.get_query_params()
            query.add_query_params(query_params)
            query.add_query_params_saved_before(use_saved_query_params)

            headers, use_saved_headers = self.get_headers()
            query.add_headers(headers)
            query.add_headers_saved_before(use_saved_headers)

            check_data = self.get_checks_data()
            for tab in check_data:
                query.set_checks(area=tab, json_data=check_data[tab])

            return query
        except Exception as ex:
            print(ex)
            helper.show_dialog(level='Error', msg=ex)

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