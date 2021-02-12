from PyQt5 import QtWidgets, QtGui
from design import ui_query
from models.my_query import MyQuery
from helper import decorator_function
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
            # self.pp_add_btn.clicked.connect(self.add_fields_path_params)
        except Exception as ex:
            print(f'ffff {ex}')

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
        with open('out_data.json', 'w') as file:
            file.write(json.dumps(data))

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
        except Exception as ex:
            self.show_error_dialog(str(ex))

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

    def show_error_dialog(self, msg='Error'):
        error_dialog = QtWidgets.QMessageBox()
        # error_dialog.setGeometry(aw=200)
        error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
        error_dialog.setText("Error")
        error_dialog.setInformativeText(msg)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec_()


class MyValueError(Exception):
    def __init__(self, msg):
        self.text = msg