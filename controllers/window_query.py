from PyQt5 import QtWidgets, QtGui
from design import ui_query
from models.my_query import MyQuery
from models.errors import MyValueError
import helper
from tests.test_first_case import test_second
import json



class Window_query(QtWidgets.QMainWindow, ui_query.Ui_MainWindow):
    def __init__(self):
        try:
            super().__init__()
            self.setupUi(self)
            self.setWindowTitle('PenoControl query')
            self.querys = [MyQuery()]
            self.id_current_query = 0
            self.init_arrays()
            self.save_url_pushButton.clicked.connect(self.add_new_url_into_case)
            self.save_case_pushButton.clicked.connect(self.save_case)
            self.start_test_case_pushButton.clicked.connect(self.start_test)
            self.post_tab.save_url_pushButton.clicked.connect(self.post_save_url)
        except Exception as ex:
            print(ex)
            helper.show_dialog(level='Error', msg=ex)

    def init_arrays(self):
        self.check_tabs = {
            'body': self.check_body_textEdit,
            'code': self.check_code_textEdit,
            'message': self.check_message_textEdit
        }
        self.methods = {
            'get_tab': 'GET',
            'post_tab': 'POST',
            'put_tab': 'PUT'
        }

    def save_case(self):
        data = []
        for query in self.querys:
            data.append(query.get_query())
        with open('tests_descriptions.json', 'w') as file:
            file.write(json.dumps(data))

    def post_save_url(self):
        try:
            self.querys[self.id_current_query] = self.post_tab.add_new_url_into_case()
            self.urls_listWidget.addItem(self.post_tab.get_url())
            self.id_current_query += 1
        except Exception as ex:
            print(ex)
            helper.show_dialog(level='Error', msg=ex)

    def add_new_url_into_case(self):
        try:
            self.querys[self.id_current_query].set_method(self.methods[self.tabWidget.currentWidget().objectName()])

            self.querys[self.id_current_query].set_url(self.get_url())

            path_params, use_saved_path_params = self.get_custom_params(self.gridLayout_path_params.get_params())
            self.querys[self.id_current_query].add_path_params(path_params)
            self.querys[self.id_current_query].add_path_params_saved_before(use_saved_path_params)

            query_params, use_saved_query_params = self.get_custom_params(self.gridLayout_query_params.get_params())
            self.querys[self.id_current_query].add_query_params(query_params)
            self.querys[self.id_current_query].add_query_params_saved_before(use_saved_query_params)

            headers, use_saved_headers = self.get_custom_params(self.gridLayout_headers.get_params())
            self.querys[self.id_current_query].add_headers(headers)
            self.querys[self.id_current_query].add_headers_saved_before(use_saved_headers)

            check_data = self.get_checks_data()
            for tab in check_data:
                self.querys[self.id_current_query].set_checks(area=tab, json_data=check_data[tab])

            item = QtGui.QStandardItem(self.get_url())
            self.urls_listWidget.addItem(self.get_url())
            self.id_current_query += 1
        except Exception as ex:
            print(ex)
            helper.show_dialog(level='Error', msg=ex)

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

    def get_url(self):
        url = self.url_lineEdit.text()
        if url is None or url == '':
            raise MyValueError("Поле 'URL' не должно быть пустым")
        return url

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

    # @helper.decorator_function
    def start_test(self):
        try:
            if test_second():
                helper.show_dialog(level='Info', msg='Тест пройден успешно')
        except Exception as ex:
            print(ex)
            helper.show_dialog(level='Error', msg=str(ex))