from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView
from gui.ui_scan_result_dialog import Ui_ScanResultDialog
from src.threat_index import ThreatIndex
from pathlib import Path
from typing import List, Tuple


class ScanResultDialog(QDialog):
    fix_button_clicked = Signal(list)

    def __init__(self, threat_index: ThreatIndex,
                 found_threats: List[Tuple[Path, int]], parent=None):
        super().__init__(parent)
        self.ui = Ui_ScanResultDialog()
        self.ui.setupUi(self)
        self.ui.threats_list.horizontalHeader() \
            .setSectionResizeMode(QHeaderView.ResizeToContents)
        self._threat_index = threat_index
        self._found_threats = found_threats
        self.fillTable()
        self.ui.fix_button.clicked.connect(
            lambda: self.fix_button_clicked.emit(self.filesToFix()))
        self.ui.fix_button.clicked.connect(self.close)
        self.ui.cancel_button.clicked.connect(self.close)

    def fillTable(self):
        """Fills the table with found threats list"""
        self.ui.threats_num.setText(str(len(self._found_threats)))
        for file, threat_id in self._found_threats:
            file_item = QTableWidgetItem()
            file_item.setCheckState(Qt.Checked)
            file_item.setText(str(file))
            file_item.file = file
            file_item.threat_id = threat_id
            descr_item = QTableWidgetItem()
            descr_item.setText(self._threat_index.description(threat_id))
            self.ui.threats_list.setRowCount(self.ui.threats_list.rowCount()+1)
            self.ui.threats_list.setItem(
                self.ui.threats_list.rowCount()-1, 0, file_item)
            self.ui.threats_list.setItem(
                self.ui.threats_list.rowCount()-1, 1, descr_item)

    def filesToFix(self) -> List[Tuple[Path, int]]:
        """Returns list ith files to fix,
           based on marked items in ui.threats_list"""
        files_to_fix = []
        for row in range(self.ui.threats_list.rowCount()):
            if self.ui.threats_list.item(row, 0).checkState() is Qt.Checked:
                files_to_fix.append(
                    (self.ui.threats_list.item(row, 0).file,
                     self.ui.threats_list.item(row, 0).threat_id))

        return files_to_fix
