import os
from pathlib import Path
from PySide6.QtCore import QThreadPool, QTimer, QTime
from PySide6.QtWidgets import QMainWindow, QFileDialog, QListWidgetItem, \
    QWidget
from PySide6.QtGui import QBrush, QColor, QCloseEvent
import src.file_interface as file_interface
from src.file_index import FileIndex
from src.threat_index import ThreatIndex
from src.cyclic_scan_config import CyclicScanConfig
from src.cyclic_scan import CyclicScan
from gui.scan_qt import ScanQt
from gui.scan_result_dialog import ScanResultDialog
from gui.ui_mainwindow import Ui_MainWindow
from gui.frequency_dialog import FrequencyDialog
from typing import List, Tuple, Callable

THREAT_INDEX_PATH = Path('threats.json')
FILE_INDEX_PATH = Path('scanned_files.json')
CYCLIC_SCAN_CONFIG_PATH = Path('cyclic_scan_config.json')


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setupWindow()
        self.initVirusScanner()
        self.cyclicScan()

    def closeEvent(self, event: QCloseEvent):
        self.disableVirusScanner()
        self.cyclic_scan_config.save(CYCLIC_SCAN_CONFIG_PATH)
        return super().closeEvent(event)

    def readFiles(self):
        """Reads all the files needed  to run the program"""
        try:
            self.file_index = FileIndex(FILE_INDEX_PATH)
        except Exception:
            self.file_index = FileIndex()

        if self.file_index.isEmpty():
            self.ui.no_file_index_notification.setVisible(True)

        try:
            self.threat_index = ThreatIndex(THREAT_INDEX_PATH)
        except Exception:
            self.threat_index = ThreatIndex()
        if self.threat_index.isEmpty():
            self.ui.no_threats_notification.setVisible(True)

        try:
            self.cyclic_scan_config = CyclicScanConfig(CYCLIC_SCAN_CONFIG_PATH)
        except Exception:
            self.cyclic_scan_config = CyclicScanConfig()
            self.ui.cyclic_scan_settings_notification.setVisible(True)

        if self.cyclic_scan_config.validateFile() is False:
            self.cyclic_scan_config = CyclicScanConfig()
            self.ui.cyclic_scan_settings_notification.setVisible(True)

    def setupWindow(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setupMenuButtons()

        self.setupHomePage()
        self.readFiles()
        self.setupScanPage()
        self.setupSettingsPage()

        self.ui.pages.setCurrentIndex(0)

    def setupMenuButtons(self):
        self.ui.home_menu_button.clicked.connect(
            lambda: self.ui.pages.setCurrentIndex(0))
        self.ui.scan_menu_button.clicked.connect(
            lambda: self.ui.pages.setCurrentIndex(2))
        self.ui.settings_menu_button.clicked.connect(
            lambda: self.ui.pages.setCurrentIndex(1))

    def setupHomePage(self):
        self.ui.cyclic_scan_notification.setVisible(False)
        self.ui.cyclic_scan_button.clicked.connect(self.startCyclicScan)
        self.ui.no_threats_notification.setVisible(False)
        self.ui.cyclic_scan_settings_notification.setVisible(False)
        self.ui.no_file_index_notification.setVisible(False)

    def setupScanPage(self):
        self.ui.incorrect_path_label.setVisible(False)
        self.ui.scanning_widget.setVisible(False)
        self.ui.path_button.clicked.connect(
            lambda: self.openFileDialog(
                lambda path: self.ui.path.setText(path)))
        self.ui.scan_button.clicked.connect(self.scanButtonClicked)

    def setupSettingsPage(self):
        # Cyclic scan
        self.ui.scan_frequency.textActivated.connect(self.scanFrequencyChanged)
        self.scan_frequency_dict = {}
        self.addFrequencyToDict(-1)  # "Wyłączone"
        self.addFrequencyToDict(1)
        self.addFrequencyToDict(2)
        self.addFrequencyToDict(5)
        self.addFrequencyToDict(7)
        self.addFrequencyToDict(14)
        self.addFrequencyToDict(31)
        self.restoreSettings()
        self.ui.save_settings_button.clicked.connect(self.saveSettings)
        self.ui.cancel_settings_button.clicked.connect(self.restoreSettings)
        self.ui.add_path_cyclic.clicked.connect(
            lambda: self.openFileDialog(
                lambda path: self.ui.cyclic_scan_paths.addItem(path)))
        self.ui.delete_path_cyclic.clicked.connect(
            lambda: self.ui.cyclic_scan_paths.takeItem(
                self.ui.cyclic_scan_paths.currentRow()))

        # Threat index
        self.ui.load_threat_index.clicked.connect(self.loadThreatIndex)
        self.ui.load_threats_failed.setVisible(False)
        self.ui.load_threats_succes.setVisible(False)

    def initVirusScanner(self):
        self.scanner = ScanQt(self.file_index, self.threat_index)
        self.scanner.fileError.connect(lambda path:
            self.addItemToLogList(f'Nie można otworzyć pliku: {str(path)}',  # noqa: E128, E501
                                  'darkgoldenrod'))
        self.scanner.dirError.connect(lambda path:
            self.addItemToLogList(f'Nie można otworzyć katalogu: {str(path)}',  # noqa: E128, E501
                                  'darkgoldenrod'))
        self.scanner.fileScanning.connect(self.fileScanning)
        self.scanner.threatFound.connect(self.threatFound)
        self.scanner.scanningComplete.connect(self.scanningComplete)
        self.scanner.scanningAborted.connect(self.scanningAborted)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timerTimeout)

    def disableVirusScanner(self):
        del self.scanner
        self.file_index.save(FILE_INDEX_PATH)
        del self.file_index
        del self.threat_index

    def cyclicScan(self):
        """Checks if a cyclic scan should be run"""
        self.cyclic_scan = CyclicScan(self.cyclic_scan_config)

        if self.cyclic_scan.isScanNeeded():
            self.ui.cyclic_scan_notification.setVisible(True)

    def validatePath(self, path: Path) -> bool:
        path_correct = path.exists()
        self.ui.incorrect_path_label.setVisible(not path_correct)
        return path_correct

    def scanButtonClicked(self):
        if self.ui.path.text() == '':
            self.ui.incorrect_path_label.setVisible(True)
            return
        path_to_scan = Path(self.ui.path.text()).absolute()
        if not self.validatePath(path_to_scan):
            return
        fast_scan = self.ui.fast_scan.isChecked()
        self.scan([path_to_scan], fast_scan)

    def scan(self, paths_to_scan: List[Path], fast_scan: bool):
        """Runs scanning"""
        self.ui.scan_button.setEnabled(False)
        self.ui.cancel_button.setEnabled(True)
        self.ui.scanning_widget.setVisible(True)
        self.ui.cancel_button.clicked.connect(self.scanner.stop)
        self.ui.log_list.clear()
        self.scanned_files = 0
        self.num_found_threats = 0
        self.scanning_time = QTime(0, 0)
        self.updateScanInfo()
        self.timer.start(1000)

        QThreadPool.globalInstance().start(
            lambda: self.startScanner(paths_to_scan, fast_scan))

    def startScanner(self, paths_to_scan: List[Path], fast_scan: bool):
        self.found_threats = self.scanner.scan(paths_to_scan, fast_scan)

    def addItemToLogList(self, text: str, color: str):
        item = QListWidgetItem()
        item.setText(text)
        item.setForeground(QBrush(QColor(color)))
        self.ui.log_list.addItem(item)

    def fileScanning(self, file: Path):
        """Updates information about currently scanned file"""
        self.scanned_files += 1
        self.ui.scanning_path.setText(str(file))
        self.updateScanInfo()

    def threatFound(self, file: Path, threat_id: int):
        """Updates information about founded threats"""
        self.num_found_threats += 1
        self.addItemToLogList(f'Znaleziono zagrożenie: {str(file)}', 'black')
        self.updateScanInfo()

    def scanningComplete(self):
        """Updates Ui when scan finished. Show dialog with found threats."""
        self.ui.scan_button.setEnabled(True)
        self.ui.cancel_button.setEnabled(False)
        self.ui.scanning_path.setText('')
        self.addItemToLogList('Pomyślnie zakończono skanowanie', 'green')
        self.timer.stop()

        if self.found_threats:  # show dialog, only if found any threat
            scan_result_dialog = ScanResultDialog(
                self.threat_index, self.found_threats, self)
            scan_result_dialog.fix_button_clicked.connect(self.fixFiles)
            scan_result_dialog.show()

    def scanningAborted(self):
        "Updates Ui when scan aborted"
        self.ui.scan_button.setEnabled(True)
        self.ui.cancel_button.setEnabled(False)
        self.ui.scanning_path.setText('')
        self.addItemToLogList('Anulowano skanowanie', 'red')
        self.timer.stop()

    def timerTimeout(self):
        """Slot executed by QTimer"""
        self.scanning_time = self.scanning_time.addSecs(1)
        self.updateScanInfo()

    def updateScanInfo(self):
        """Update information about scanning in Ui"""
        self.ui.duration.setText(self.scanning_time.toString('HH:mm:ss'))
        self.ui.threats_num.setText(str(self.num_found_threats))
        self.ui.scanned_num.setText(str(self.scanned_files))

    def fixFiles(self, files_to_fix: List[Tuple[Path, int]]):
        for file, threat_id in files_to_fix:
            self.scanner.fixFile(file, threat_id)
            self.addItemToLogList(f'Naprawionio: {str(file)}', 'black')
        self.addItemToLogList('Zakończono naprawianie plików', 'green')

    def addCustomFrequency(self):
        """Shows a dialog to select cyclic scan frequency"""
        self.dialog = FrequencyDialog()
        self.dialog.accepted.connect(self.addFrequencyToDict)
        self.dialog.show()

    def addFrequencyToDict(self, frequency: int):
        """Adds frequency to dict and QComboBox on settings page"""
        description = self.frequencyDescription(frequency)
        self.scan_frequency_dict[description] = frequency
        self.updateScanFrequency()
        self.ui.scan_frequency.setCurrentText(description)

    def updateScanFrequency(self):
        """Update items in QComboBox on setting page"""
        self.ui.scan_frequency.clear()
        self.ui.scan_frequency.addItems(self.scan_frequency_dict.keys())
        self.ui.scan_frequency.addItem("Niestandardowa...")

    def frequencyDescription(self, frequency: int) -> str:
        """Creates an appropriate description depending
           on the number of days"""
        if frequency == -1:
            description = 'Wyłączone'
        elif frequency % 7 == 0:
            description = f'Co {frequency // 7} tyg.'
        elif frequency % 31 == 0:
            description = f'Co {frequency // 31} mies.'
        else:
            description = f'Co {frequency} dni'
        return description

    def saveSettings(self):
        """Saves settings in config file"""
        # Cyclic scan
        frequency = self.scan_frequency_dict[
            self.ui.scan_frequency.currentText()]
        fast_scan = self.ui.cyclic_fast_scan.isChecked()
        paths = []
        for i in range(self.ui.cyclic_scan_paths.count()):
            paths.append(Path(self.ui.cyclic_scan_paths.item(i).text()))

        self.cyclic_scan.setConfig(frequency, fast_scan, paths)

        # Threat index
        self.threat_index.save(THREAT_INDEX_PATH)
        self.ui.load_threats_failed.setVisible(False)
        self.ui.load_threats_succes.setVisible(False)
        if not self.threat_index.isEmpty():
            self.ui.no_threats_notification.setVisible(False)

    def restoreSettings(self):
        """Restores settings from config file"""
        # Cyclic scan
        self.addFrequencyToDict(self.cyclic_scan_config.frequency())
        self.ui.cyclic_fast_scan.setChecked(self.cyclic_scan_config.fastScan())
        self.ui.cyclic_scan_paths.clear()
        for path in self.cyclic_scan_config.pathsToScan():
            self.ui.cyclic_scan_paths.addItem(str(path))
        self.scanFrequencyChanged(self.ui.scan_frequency.currentText())

        # Threat index
        self.threat_index.restoreBackup()
        self.ui.load_threats_failed.setVisible(False)
        self.ui.load_threats_succes.setVisible(False)

    def openFileDialog(self, slot: Callable[[str], None]):
        """Opend dialog where can be selected a file from the disk
           slot is a function to be called when a file is selected"""
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        file_dialog.show()
        file_dialog.currentChanged.connect(
            lambda path, dialog=file_dialog:
                dialog.setFileMode(QFileDialog.AnyFile)
                if os.path.isfile(path)
                else dialog.setFileMode(QFileDialog.Directory)
        )
        file_dialog.fileSelected.connect(slot)

    def scanFrequencyChanged(self, text: str):
        """Enable or diable cyclic scan settings,
           depending on cyclic scan in enabled"""
        if text == "Wyłączone":
            self.ui.cyclic_scan_settings.setEnabled(False)
        else:
            self.ui.cyclic_scan_settings.setEnabled(True)
            self.ui.cyclic_scan_settings_notification.setVisible(False)
            # Hides the notification about the need to reconfigure cyclic scanning # noqa: E501

        if text == 'Niestandardowa...':
            self.addCustomFrequency()

    def startCyclicScan(self):
        """Starts cyclic scan"""
        self.ui.cyclic_scan_notification.setVisible(False)
        paths_to_scan = self.cyclic_scan.pathsToScan()
        fast_scan = self.cyclic_scan.fastScan()
        self.cyclic_scan.scannedNow()
        self.ui.pages.setCurrentIndex(2)
        self.scan(paths_to_scan, fast_scan)

    def loadThreatIndex(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter('*.json')
        file_dialog.show()
        file_dialog.fileSelected.connect(self.openNewThreatIndex)

    def openNewThreatIndex(self, path):
        self.threat_index.backupIndex()
        path = Path(path)
        new_threat_index = file_interface.readJson(path)
        if not type(new_threat_index) == list \
           or len(new_threat_index) == 0 \
           or not type(new_threat_index[0]) == dict:
            self.ui.load_threats_failed.setVisible(True)
            self.ui.load_threats_succes.setVisible(False)
        else:
            for threat in new_threat_index:
                value = threat.get("value", None)
                description = threat.get("description", None)
                if type(value) == str and type(description) == str:
                    self.threat_index.addThreat(value, description)
            self.ui.load_threats_failed.setVisible(False)
            self.ui.load_threats_succes.setVisible(True)
