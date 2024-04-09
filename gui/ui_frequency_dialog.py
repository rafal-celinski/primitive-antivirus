# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frequency_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_FrequencyDialog(object):
    def setupUi(self, FrequencyDialog):
        if not FrequencyDialog.objectName():
            FrequencyDialog.setObjectName(u"FrequencyDialog")
        FrequencyDialog.resize(220, 130)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FrequencyDialog.sizePolicy().hasHeightForWidth())
        FrequencyDialog.setSizePolicy(sizePolicy)
        FrequencyDialog.setMinimumSize(QSize(220, 130))
        FrequencyDialog.setMaximumSize(QSize(220, 130))
        self.verticalLayout = QVBoxLayout(FrequencyDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(FrequencyDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.value = QSpinBox(FrequencyDialog)
        self.value.setObjectName(u"value")
        self.value.setMinimum(1)

        self.horizontalLayout.addWidget(self.value)

        self.unit = QComboBox(FrequencyDialog)
        self.unit.addItem("")
        self.unit.addItem("")
        self.unit.addItem("")
        self.unit.setObjectName(u"unit")

        self.horizontalLayout.addWidget(self.unit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.ok_button = QPushButton(FrequencyDialog)
        self.ok_button.setObjectName(u"ok_button")

        self.verticalLayout.addWidget(self.ok_button)


        self.retranslateUi(FrequencyDialog)

        QMetaObject.connectSlotsByName(FrequencyDialog)
    # setupUi

    def retranslateUi(self, FrequencyDialog):
        FrequencyDialog.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("FrequencyDialog", u"Cz\u0119stotliow\u015b\u0107 skanowania:", None))
        self.unit.setItemText(0, QCoreApplication.translate("FrequencyDialog", u"dni", None))
        self.unit.setItemText(1, QCoreApplication.translate("FrequencyDialog", u"tyg.", None))
        self.unit.setItemText(2, QCoreApplication.translate("FrequencyDialog", u"mies.", None))

        self.ok_button.setText(QCoreApplication.translate("FrequencyDialog", u"OK", None))
    # retranslateUi

