from PyQt5 import QtWidgets, QtGui


def decorator_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            print(ex)
            show_dialog(level='Error', msg=str(ex))
    wrapper.__name__ = func.__name__
    return wrapper


def show_dialog(level='Error', msg='Error'):
    dialog = QtWidgets.QMessageBox()
    # error_dialog.setGeometry(aw=200)
    levels = {
        'Error': QtWidgets.QMessageBox.Critical,
        'Info': QtWidgets.QMessageBox.Information
    }
    dialog.setIcon(levels[level])
    dialog.setText(level)
    dialog.setInformativeText(msg)
    dialog.setWindowTitle(level)
    dialog.exec_()