import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from design import ui_main, ui_query
from models.my_query import MyQuery
import json


class Window_main(QtWidgets.QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('PenoControl')
        self.create_new_pushButton.clicked.connect(self.open_query_window)

    def open_query_window(self):
        try:
            self.w_query = Window_query()
            self.w_query.show()
            self.close()
        except Exception as ex:
            print(ex)


class Window_query(QtWidgets.QMainWindow, ui_query.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('PenoControl query')
        self.querys = [MyQuery()]
        self.id_current_query = 0
        # self.url_lineEdit.focusOutEvent.connect(self.change_url)
        self.save_url_pushButton.clicked.connect(self.add_new_url_into_case)
        self.save_case_pushButton.clicked.connect(self.save_case)

    def save_case(self):
        data = []
        for query in self.querys:
            data.append(query.get_query())
        with open('out_data.json', 'w') as file:
            file.write(json.dumps(data))

    def change_url(self):
        print(f'url changes: {self.url_lineEdit.text()}')
        self.querys[self.id_current_query].set_url(self.url_lineEdit.text())

    def add_new_url_into_case(self):
        try:
            if self.tabWidget.currentIndex() == 0:
                self.querys[self.id_current_query].set_method('GET')
            else:
                self.querys[self.id_current_query].set_method('POST')
            print(f'url: {self.url_lineEdit.text()}')
            self.querys[self.id_current_query].set_url(self.url_lineEdit.text())
            print(f'path_params_groupBox: {self.path_params_groupBox.children()}')
            path_params, use_saved_path_params = self.get_path_params()
            self.querys[self.id_current_query].add_path_params(path_params)
            self.querys[self.id_current_query].add_path_params_saved_before(use_saved_path_params)
            print(f'query_params_groupBox: {self.query_params_groupBox.children()}')
            query_params, use_saved_query_params = self.get_query_params()
            self.querys[self.id_current_query].add_query_params(query_params)
            self.querys[self.id_current_query].add_query_params_saved_before(use_saved_query_params)

            headers, use_saved_headers = self.get_headers()
            self.querys[self.id_current_query].add_headers(headers)
            self.querys[self.id_current_query].add_headers_saved_before(use_saved_headers)
            print(f'check_body_textEdit: {self.check_body_textEdit.toPlainText()}')
            self.querys[self.id_current_query].set_request_body(self.check_body_textEdit.toPlainText())
        except Exception as e:
            print(e)

    def get_path_params(self):
        path_params = {}
        use_saved_param = []
        if self.pp_1_checkBox.isChecked():
            use_saved_param.append(self.pp_key_1_lineEdit.text())
        else:
            path_params[self.pp_key_1_lineEdit.text()] = self.pp_val_1_lineEdit.text()
        return path_params, use_saved_param

    def get_query_params(self):
        path_params = {}
        use_saved_param = []
        if self.qp_1_checkBox.isChecked():
            use_saved_param.append(self.qp_key_1_lineEdit.text())
        else:
            path_params[self.qp_key_1_lineEdit.text()] = self.qp_val_1_lineEdit.text()
        return path_params, use_saved_param

    def get_headers(self):
        path_params = {}
        use_saved_param = []
        if self.h_1_checkBox.isChecked():
            use_saved_param.append(self.h_key_1_lineEdit.text())
        else:
            path_params[self.h_key_1_lineEdit.text()] = self.h_val_1_lineEdit.text()
        return path_params, use_saved_param


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)  # Новый экземпляр QApplication
        window = Window_main()  # Создаём объект класса ExampleApp
        window.show()  # Показываем окно
        app.exec_()  # и запускаем приложение
    except Exception as ex:
        print(ex)