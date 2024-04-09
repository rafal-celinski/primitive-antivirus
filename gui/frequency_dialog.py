from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog
from gui.ui_frequency_dialog import Ui_FrequencyDialog


class FrequencyDialog(QDialog):
    accepted = Signal(int)

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_FrequencyDialog()
        self.ui.setupUi(self)
        self.ui.ok_button.clicked.connect(self.okButtonClicked)

    def okButtonClicked(self):
        value = self.ui.value.value()
        if self.ui.unit.currentText() == 'dni':
            pass
        elif self.ui.unit.currentText() == 'tyg.':
            value = value*7
        elif self.ui.unit.currentText() == 'mies.':
            value = value*31

        self.accepted.emit(value)

        self.close()
