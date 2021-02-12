import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from design import ui_main, ui_query
from models.my_query import MyQuery
import json
from helper import decorator_function
from controllers.window_query import Window_query


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


@decorator_function
def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Window_main()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    main()