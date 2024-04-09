from PySide6.QtCore import QTranslator, QLibraryInfo
from PySide6.QtWidgets import QApplication
from gui.mainwindow import MainWindow
import sys


def main(args):
    app = QApplication(args)

    translator = QTranslator()
    translator.load('qt_pl_PL', QLibraryInfo.path(
        QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main(sys.argv)
