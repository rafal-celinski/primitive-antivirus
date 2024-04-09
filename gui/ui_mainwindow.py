# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(830, 420)
        MainWindow.setMinimumSize(QSize(830, 420))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_13 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.home_menu_button = QPushButton(self.centralwidget)
        self.home_menu_button.setObjectName(u"home_menu_button")
        self.home_menu_button.setMinimumSize(QSize(200, 60))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.home_menu_button.setFont(font)

        self.verticalLayout_5.addWidget(self.home_menu_button)

        self.scan_menu_button = QPushButton(self.centralwidget)
        self.scan_menu_button.setObjectName(u"scan_menu_button")
        self.scan_menu_button.setMinimumSize(QSize(0, 60))
        self.scan_menu_button.setFont(font)

        self.verticalLayout_5.addWidget(self.scan_menu_button)

        self.settings_menu_button = QPushButton(self.centralwidget)
        self.settings_menu_button.setObjectName(u"settings_menu_button")
        self.settings_menu_button.setMinimumSize(QSize(0, 60))
        self.settings_menu_button.setFont(font)
        self.settings_menu_button.setMouseTracking(False)

        self.verticalLayout_5.addWidget(self.settings_menu_button)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_13.addLayout(self.verticalLayout_5)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setMinimumSize(QSize(0, 400))
        self.pages.setCursor(QCursor(Qt.ArrowCursor))
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_7 = QVBoxLayout(self.home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.home_title = QLabel(self.home)
        self.home_title.setObjectName(u"home_title")
        self.home_title.setFont(font)

        self.verticalLayout_7.addWidget(self.home_title)

        self.line_4 = QFrame(self.home)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_4)

        self.label_4 = QLabel(self.home)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_4)

        self.cyclic_scan_notification = QWidget(self.home)
        self.cyclic_scan_notification.setObjectName(u"cyclic_scan_notification")
        self.verticalLayout_8 = QVBoxLayout(self.cyclic_scan_notification)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_12)

        self.label_5 = QLabel(self.cyclic_scan_notification)
        self.label_5.setObjectName(u"label_5")
        palette = QPalette()
        brush = QBrush(QColor(184, 134, 11, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.label_5.setPalette(palette)

        self.horizontalLayout_11.addWidget(self.label_5)

        self.cyclic_scan_button = QPushButton(self.cyclic_scan_notification)
        self.cyclic_scan_button.setObjectName(u"cyclic_scan_button")
        self.cyclic_scan_button.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_11.addWidget(self.cyclic_scan_button)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)


        self.verticalLayout_7.addWidget(self.cyclic_scan_notification)

        self.no_threats_notification = QLabel(self.home)
        self.no_threats_notification.setObjectName(u"no_threats_notification")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no_threats_notification.sizePolicy().hasHeightForWidth())
        self.no_threats_notification.setSizePolicy(sizePolicy)
        self.no_threats_notification.setMinimumSize(QSize(0, 24))
        palette1 = QPalette()
        brush3 = QBrush(QColor(255, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.no_threats_notification.setPalette(palette1)
        font2 = QFont()
        font2.setBold(True)
        self.no_threats_notification.setFont(font2)
        self.no_threats_notification.setScaledContents(True)
        self.no_threats_notification.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.no_threats_notification)

        self.cyclic_scan_settings_notification = QLabel(self.home)
        self.cyclic_scan_settings_notification.setObjectName(u"cyclic_scan_settings_notification")
        sizePolicy.setHeightForWidth(self.cyclic_scan_settings_notification.sizePolicy().hasHeightForWidth())
        self.cyclic_scan_settings_notification.setSizePolicy(sizePolicy)
        self.cyclic_scan_settings_notification.setMinimumSize(QSize(0, 24))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.cyclic_scan_settings_notification.setPalette(palette2)
        self.cyclic_scan_settings_notification.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.cyclic_scan_settings_notification)

        self.no_file_index_notification = QLabel(self.home)
        self.no_file_index_notification.setObjectName(u"no_file_index_notification")
        sizePolicy.setHeightForWidth(self.no_file_index_notification.sizePolicy().hasHeightForWidth())
        self.no_file_index_notification.setSizePolicy(sizePolicy)
        self.no_file_index_notification.setMinimumSize(QSize(0, 24))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.no_file_index_notification.setPalette(palette3)
        self.no_file_index_notification.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.no_file_index_notification)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.pages.addWidget(self.home)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout = QVBoxLayout(self.settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_title_2 = QLabel(self.settings)
        self.home_title_2.setObjectName(u"home_title_2")
        self.home_title_2.setFont(font)

        self.verticalLayout.addWidget(self.home_title_2)

        self.line_3 = QFrame(self.settings)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.scrollArea = QScrollArea(self.settings)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 464, 413))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 6, 0)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(12)
        self.label.setFont(font3)

        self.verticalLayout_4.addWidget(self.label)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_10.addWidget(self.label_2)

        self.scan_frequency = QComboBox(self.scrollAreaWidgetContents)
        self.scan_frequency.setObjectName(u"scan_frequency")
        self.scan_frequency.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_10.addWidget(self.scan_frequency)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.cyclic_scan_settings = QWidget(self.scrollAreaWidgetContents)
        self.cyclic_scan_settings.setObjectName(u"cyclic_scan_settings")
        self.verticalLayout_6 = QVBoxLayout(self.cyclic_scan_settings)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cyclic_fast_scan = QCheckBox(self.cyclic_scan_settings)
        self.cyclic_fast_scan.setObjectName(u"cyclic_fast_scan")

        self.verticalLayout_6.addWidget(self.cyclic_fast_scan)

        self.label_3 = QLabel(self.cyclic_scan_settings)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.cyclic_scan_paths = QListWidget(self.cyclic_scan_settings)
        self.cyclic_scan_paths.setObjectName(u"cyclic_scan_paths")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cyclic_scan_paths.sizePolicy().hasHeightForWidth())
        self.cyclic_scan_paths.setSizePolicy(sizePolicy1)
        self.cyclic_scan_paths.setFrameShape(QFrame.NoFrame)
        self.cyclic_scan_paths.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_6.addWidget(self.cyclic_scan_paths)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.add_path_cyclic = QPushButton(self.cyclic_scan_settings)
        self.add_path_cyclic.setObjectName(u"add_path_cyclic")

        self.horizontalLayout_5.addWidget(self.add_path_cyclic)

        self.delete_path_cyclic = QPushButton(self.cyclic_scan_settings)
        self.delete_path_cyclic.setObjectName(u"delete_path_cyclic")

        self.horizontalLayout_5.addWidget(self.delete_path_cyclic)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addWidget(self.cyclic_scan_settings)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 40))
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_4.addWidget(self.label_6)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.load_threat_index = QPushButton(self.scrollAreaWidgetContents)
        self.load_threat_index.setObjectName(u"load_threat_index")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.load_threat_index.sizePolicy().hasHeightForWidth())
        self.load_threat_index.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.load_threat_index)

        self.load_threats_succes = QLabel(self.scrollAreaWidgetContents)
        self.load_threats_succes.setObjectName(u"load_threats_succes")
        palette4 = QPalette()
        brush4 = QBrush(QColor(0, 100, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.load_threats_succes.setPalette(palette4)

        self.horizontalLayout_12.addWidget(self.load_threats_succes)

        self.load_threats_failed = QLabel(self.scrollAreaWidgetContents)
        self.load_threats_failed.setObjectName(u"load_threats_failed")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.load_threats_failed.setPalette(palette5)

        self.horizontalLayout_12.addWidget(self.load_threats_failed)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.cancel_settings_button = QPushButton(self.settings)
        self.cancel_settings_button.setObjectName(u"cancel_settings_button")

        self.horizontalLayout.addWidget(self.cancel_settings_button)

        self.save_settings_button = QPushButton(self.settings)
        self.save_settings_button.setObjectName(u"save_settings_button")

        self.horizontalLayout.addWidget(self.save_settings_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pages.addWidget(self.settings)
        self.scan = QWidget()
        self.scan.setObjectName(u"scan")
        self.scan.setToolTipDuration(-2)
        self.verticalLayout_3 = QVBoxLayout(self.scan)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scan_title = QLabel(self.scan)
        self.scan_title.setObjectName(u"scan_title")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scan_title.sizePolicy().hasHeightForWidth())
        self.scan_title.setSizePolicy(sizePolicy3)
        self.scan_title.setFont(font)

        self.verticalLayout_3.addWidget(self.scan_title)

        self.line_2 = QFrame(self.scan)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.path = QLineEdit(self.scan)
        self.path.setObjectName(u"path")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.path.sizePolicy().hasHeightForWidth())
        self.path.setSizePolicy(sizePolicy4)
        self.path.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_7.addWidget(self.path)

        self.path_button = QToolButton(self.scan)
        self.path_button.setObjectName(u"path_button")

        self.horizontalLayout_7.addWidget(self.path_button)

        self.horizontalSpacer_5 = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.scan_button = QPushButton(self.scan)
        self.scan_button.setObjectName(u"scan_button")
        sizePolicy2.setHeightForWidth(self.scan_button.sizePolicy().hasHeightForWidth())
        self.scan_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.scan_button)

        self.horizontalSpacer_8 = QSpacerItem(3, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.incorrect_path_label = QLabel(self.scan)
        self.incorrect_path_label.setObjectName(u"incorrect_path_label")
        self.incorrect_path_label.setEnabled(True)
        self.incorrect_path_label.setStyleSheet(u"QLabel {color : red; }")

        self.horizontalLayout_8.addWidget(self.incorrect_path_label)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.fast_scan = QCheckBox(self.scan)
        self.fast_scan.setObjectName(u"fast_scan")

        self.horizontalLayout_8.addWidget(self.fast_scan)

        self.horizontalSpacer_7 = QSpacerItem(3, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.scanning_widget = QWidget(self.scan)
        self.scanning_widget.setObjectName(u"scanning_widget")
        self.scanning_widget.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scanning_widget.sizePolicy().hasHeightForWidth())
        self.scanning_widget.setSizePolicy(sizePolicy5)
        self.scanning_widget.setAcceptDrops(False)
        self.verticalLayout_2 = QVBoxLayout(self.scanning_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.title_scanning = QLabel(self.scanning_widget)
        self.title_scanning.setObjectName(u"title_scanning")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        self.title_scanning.setFont(font4)

        self.horizontalLayout_6.addWidget(self.title_scanning)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.cancel_button = QPushButton(self.scanning_widget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_6.addWidget(self.cancel_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scanned_title = QLabel(self.scanning_widget)
        self.scanned_title.setObjectName(u"scanned_title")

        self.horizontalLayout_2.addWidget(self.scanned_title)

        self.scanned_num = QLabel(self.scanning_widget)
        self.scanned_num.setObjectName(u"scanned_num")

        self.horizontalLayout_2.addWidget(self.scanned_num)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.duration_title = QLabel(self.scanning_widget)
        self.duration_title.setObjectName(u"duration_title")

        self.horizontalLayout_3.addWidget(self.duration_title)

        self.duration = QLabel(self.scanning_widget)
        self.duration.setObjectName(u"duration")

        self.horizontalLayout_3.addWidget(self.duration)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.threats_title = QLabel(self.scanning_widget)
        self.threats_title.setObjectName(u"threats_title")

        self.horizontalLayout_4.addWidget(self.threats_title)

        self.threats_num = QLabel(self.scanning_widget)
        self.threats_num.setObjectName(u"threats_num")

        self.horizontalLayout_4.addWidget(self.threats_num)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.scanning_path = QLabel(self.scanning_widget)
        self.scanning_path.setObjectName(u"scanning_path")
        sizePolicy1.setHeightForWidth(self.scanning_path.sizePolicy().hasHeightForWidth())
        self.scanning_path.setSizePolicy(sizePolicy1)
        self.scanning_path.setMinimumSize(QSize(0, 60))
        self.scanning_path.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.scanning_path)

        self.log_title = QLabel(self.scanning_widget)
        self.log_title.setObjectName(u"log_title")
        sizePolicy1.setHeightForWidth(self.log_title.sizePolicy().hasHeightForWidth())
        self.log_title.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.log_title)

        self.log_list = QListWidget(self.scanning_widget)
        self.log_list.setObjectName(u"log_list")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.log_list.sizePolicy().hasHeightForWidth())
        self.log_list.setSizePolicy(sizePolicy6)
        font5 = QFont()
        font5.setKerning(True)
        self.log_list.setFont(font5)
        self.log_list.setFrameShape(QFrame.NoFrame)
        self.log_list.setFrameShadow(QFrame.Sunken)
        self.log_list.setMidLineWidth(0)
        self.log_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.log_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.log_list.setAutoScroll(True)
        self.log_list.setProperty("showDropIndicator", True)
        self.log_list.setProperty("isWrapping", False)
        self.log_list.setLayoutMode(QListView.SinglePass)

        self.verticalLayout_2.addWidget(self.log_list)


        self.horizontalLayout_9.addWidget(self.scanning_widget)

        self.verticalSpacer_3 = QSpacerItem(3, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_9.addItem(self.verticalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.pages.addWidget(self.scan)

        self.horizontalLayout_13.addWidget(self.pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Antywirus", None))
        self.home_menu_button.setText(QCoreApplication.translate("MainWindow", u"Menu g\u0142\u00f3wne", None))
        self.scan_menu_button.setText(QCoreApplication.translate("MainWindow", u"Skanowanie", None))
        self.settings_menu_button.setText(QCoreApplication.translate("MainWindow", u"Ustawienia", None))
        self.home_title.setText(QCoreApplication.translate("MainWindow", u"Menu g\u0142\u00f3wne", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Antywirus jest aktywny!", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Wymagane cykliczne skanowanie:", None))
        self.cyclic_scan_button.setText(QCoreApplication.translate("MainWindow", u"Wykonaj teraz", None))
        self.no_threats_notification.setText(QCoreApplication.translate("MainWindow", u"Plik z baz\u0105 wirus\u00f3w jest pusty, zaimportuj baz\u0119 wirusu\u00f3w w ustawieniach!", None))
        self.cyclic_scan_settings_notification.setText(QCoreApplication.translate("MainWindow", u"Plik z konfiguracj\u0105 cyklicznego skanowania uszkodzony, skonfiguruj ponownie w ustawieniach", None))
        self.no_file_index_notification.setText(QCoreApplication.translate("MainWindow", u"Brak historii skanowanych plik\u00f3w, szybkie skanowanie mo\u017ce by\u0107 niedostepne", None))
        self.home_title_2.setText(QCoreApplication.translate("MainWindow", u"Ustawienia", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cykliczne skanowanie:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cz\u0119stotliwo\u015b\u0107 skanowania:", None))
        self.cyclic_fast_scan.setText(QCoreApplication.translate("MainWindow", u"Szybkie skanowanie", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Katalogi i pliki, kt\u00f3re maj\u0105 by\u0107 skanowane:", None))
        self.add_path_cyclic.setText(QCoreApplication.translate("MainWindow", u"Dodaj katalog/plik", None))
        self.delete_path_cyclic.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144 katalog/plik", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Baza wirus\u00f3w:", None))
        self.load_threat_index.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj baz\u0119 wirus\u00f3w", None))
        self.load_threats_succes.setText(QCoreApplication.translate("MainWindow", u"Pomy\u015blnie za\u0142adowano baz\u0119 wirus\u00f3w", None))
        self.load_threats_failed.setText(QCoreApplication.translate("MainWindow", u"Plik jest nieprawid\u0142owy", None))
        self.cancel_settings_button.setText(QCoreApplication.translate("MainWindow", u"Anuluj", None))
        self.save_settings_button.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.scan_title.setText(QCoreApplication.translate("MainWindow", u"Skanowanie", None))
        self.path.setInputMask("")
        self.path.setText("")
        self.path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Podaj scie\u017ck\u0119 pliku/katalogu do przeskanowania", None))
        self.path_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.scan_button.setText(QCoreApplication.translate("MainWindow", u"Skanuj", None))
        self.incorrect_path_label.setText(QCoreApplication.translate("MainWindow", u"\u015acie\u017cka jest nieprawid\u0142owa, spr\u00f3buj ponownie", None))
        self.fast_scan.setText(QCoreApplication.translate("MainWindow", u"Szybki skan", None))
        self.title_scanning.setText(QCoreApplication.translate("MainWindow", u"Trwa skanowanie", None))
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"Anuluj", None))
        self.scanned_title.setText(QCoreApplication.translate("MainWindow", u"Przeskanowane obiekty:", None))
        self.scanned_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.duration_title.setText(QCoreApplication.translate("MainWindow", u"Czas trwania:", None))
        self.duration.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.threats_title.setText(QCoreApplication.translate("MainWindow", u"Wykrytych zagro\u017ce\u0144:", None))
        self.threats_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.scanning_path.setText("")
        self.log_title.setText(QCoreApplication.translate("MainWindow", u"Dziennik skanowania:", None))
    # retranslateUi

