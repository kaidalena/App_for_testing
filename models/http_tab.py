from PyQt5 import QtWidgets
from models.expanderWidgetParams import RequestParams
from models.errors import MyValueError
from models.my_query import MyQuery
import json
from utils import helper
from models.expanderWidgetRequestBody import RequestBody
from models.tab_widget_checks import TabWidgetChecks


class HTTP_Tab(QtWidgets.QWidget):
    def __init__(self, method, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.parent = parent
        self.method = method
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout()

        # url
        self._add_url_field()

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        # path params
        self.expander_path_params = RequestParams(title='Path params', parent=self)
        self.verticalLayout.addWidget(self.expander_path_params.expander)
        self.expander_path_params.expander.setDisabled(True)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        # query params
        self.expander_query_params = RequestParams(title='Query params', parent=self)
        self.verticalLayout.addWidget(self.expander_query_params.expander)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        # headers
        self.expander_headers = RequestParams(title='Headers', parent=self)
        self.verticalLayout.addWidget(self.expander_headers.expander)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)


        # checks
        self.checks_label = QtWidgets.QLabel(self)
        self.verticalLayout.addWidget(self.checks_label)
        self.checks_tabWidget = TabWidgetChecks(parent=self)
        self.verticalLayout.addWidget(self.checks_tabWidget)

        # self.expander_request_body = RequestBody(parent=self)
        # self.verticalLayout.addWidget(self.expander_request_body.expander)

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
        self.checks_label.setText("Checks")
        self.save_url_pushButton.setText("Добавить урл в сценарий")

    def get_method(self):
        return self.method

    def _add_url_field(self):
        self.url_label = QtWidgets.QLabel(self)
        self.url_label.setText("URL:")
        self.horizontalLayout.addWidget(self.url_label)

        self.url_lineEdit = QtWidgets.QLineEdit(self)
        self.horizontalLayout.addWidget(self.url_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        def validate_url():
            try:
                if self.url_lineEdit.text()[0] != '/':
                    print(f"The URL must start with '/'")
            except IndexError as er:
                print('Empty url')
            except Exception as ex:
                print(ex)
                print(f"type ex: {type(ex)} \nex: {ex}")

        # self.url_lineEdit.textChanged.connect(validate_url/)
        # self.url_lineEdit.focus.connect(validate_url)

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
        return self.get_custom_params(self.expander_path_params.get_params())

    def get_query_params(self):
        return self.get_custom_params(self.expander_query_params.get_params())

    def get_headers(self):
        return self.get_custom_params(self.expander_headers.get_params())

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

            check_data = self.checks_tabWidget.get_checks_data()
            for tab in check_data:
                query.set_checks(area=tab, json_data=check_data[tab])

            return query
        except Exception as ex:
            print(ex)
            helper.show_dialog(level='Error', msg=ex)
