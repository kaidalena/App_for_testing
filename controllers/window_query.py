from PyQt5 import QtWidgets
from design import ui_query
from models.my_query import MyQuery
from utils import helper
from tests.test_first_case import test_second
import json



class Window_query(QtWidgets.QMainWindow, ui_query.Ui_MainWindow):
    def __init__(self):
        try:
            super().__init__()
            self.setupUi(self)
            self.setWindowTitle('PenoControl query')
            self.querys = []

            self.get_tab.save_url_pushButton.clicked.connect(self.save_url)
            self.post_tab.save_url_pushButton.clicked.connect(self.save_url)
            self.put_tab.save_url_pushButton.clicked.connect(self.save_url)

            self.save_case_pushButton.clicked.connect(self.save_case)
            self.start_test_case_pushButton.clicked.connect(self.start_test)

        except Exception as ex:
            print(ex)
            helper.show_dialog(level='Error', msg=ex)

    def save_case(self):
        data = []
        for query in self.querys:
            data.append(query.get_query())
        with open('tests/tests_descriptions.json', 'w') as file:
            file.write(json.dumps(data))

    def save_url(self):
        try:
            self.querys.append(self.tabWidget.currentWidget().add_new_url_into_case())
            self.urls_listWidget.addItem(self.tabWidget.currentWidget().get_url())
        except Exception as ex:
            print(ex)
            helper.show_dialog(level='Error', msg=ex)

    # @helper.decorator_function
    def start_test(self):
        try:
            if test_second():
                helper.show_dialog(level='Info', msg='Тест пройден успешно')
        except Exception as ex:
            print(ex)
            helper.show_dialog(level='Error', msg=str(ex))