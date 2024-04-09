# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scan_result_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDialog,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ScanResultDialog(object):
    def setupUi(self, ScanResultDialog):
        if not ScanResultDialog.objectName():
            ScanResultDialog.setObjectName(u"ScanResultDialog")
        ScanResultDialog.resize(600, 300)
        ScanResultDialog.setMinimumSize(QSize(600, 300))
        self.verticalLayout = QVBoxLayout(ScanResultDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.threats_label = QLabel(ScanResultDialog)
        self.threats_label.setObjectName(u"threats_label")

        self.horizontalLayout.addWidget(self.threats_label)

        self.threats_num = QLabel(ScanResultDialog)
        self.threats_num.setObjectName(u"threats_num")
        self.threats_num.setMinimumSize(QSize(50, 0))

        self.horizontalLayout.addWidget(self.threats_num)

        self.label = QLabel(ScanResultDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.threats_list = QTableWidget(ScanResultDialog)
        if (self.threats_list.columnCount() < 2):
            self.threats_list.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.threats_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.threats_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.threats_list.setObjectName(u"threats_list")
        self.threats_list.setFrameShape(QFrame.StyledPanel)
        self.threats_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.threats_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.threats_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.threats_list.setTabKeyNavigation(False)
        self.threats_list.setProperty("showDropIndicator", False)
        self.threats_list.setDragDropOverwriteMode(False)
        self.threats_list.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.threats_list.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.threats_list.setShowGrid(False)
        self.threats_list.setWordWrap(False)
        self.threats_list.setCornerButtonEnabled(False)
        self.threats_list.horizontalHeader().setVisible(True)
        self.threats_list.horizontalHeader().setCascadingSectionResizes(False)
        self.threats_list.horizontalHeader().setDefaultSectionSize(290)
        self.threats_list.horizontalHeader().setHighlightSections(False)
        self.threats_list.horizontalHeader().setProperty("showSortIndicator", False)
        self.threats_list.horizontalHeader().setStretchLastSection(True)
        self.threats_list.verticalHeader().setVisible(False)
        self.threats_list.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.threats_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.fix_button = QPushButton(ScanResultDialog)
        self.fix_button.setObjectName(u"fix_button")

        self.horizontalLayout_2.addWidget(self.fix_button)

        self.cancel_button = QPushButton(ScanResultDialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_2.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(ScanResultDialog)

        QMetaObject.connectSlotsByName(ScanResultDialog)
    # setupUi

    def retranslateUi(self, ScanResultDialog):
        ScanResultDialog.setWindowTitle(QCoreApplication.translate("ScanResultDialog", u"Dialog", None))
        self.threats_label.setText(QCoreApplication.translate("ScanResultDialog", u"Znalezionych zagro\u017ce\u0144:", None))
        self.threats_num.setText(QCoreApplication.translate("ScanResultDialog", u"0", None))
        self.label.setText(QCoreApplication.translate("ScanResultDialog", u"Zaznacz, kt\u00f3re pliki chcesz naprawi\u0107:", None))
        ___qtablewidgetitem = self.threats_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ScanResultDialog", u"Plik", None));
        ___qtablewidgetitem1 = self.threats_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ScanResultDialog", u"Wykryte zagro\u017cenie", None));
        self.fix_button.setText(QCoreApplication.translate("ScanResultDialog", u"Napraw", None))
        self.cancel_button.setText(QCoreApplication.translate("ScanResultDialog", u"Anuluj", None))
    # retranslateUi

