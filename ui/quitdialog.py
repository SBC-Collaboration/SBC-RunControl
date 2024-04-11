# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quitdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QSizePolicy, QWidget)

class Ui_QuitDialog(object):
    def setupUi(self, QuitDialog):
        if not QuitDialog.objectName():
            QuitDialog.setObjectName(u"QuitDialog")
        QuitDialog.resize(247, 90)
        self.gridLayout = QGridLayout(QuitDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(QuitDialog)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(QuitDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(QuitDialog)
        self.buttonBox.accepted.connect(QuitDialog.accept)
        self.buttonBox.rejected.connect(QuitDialog.reject)

        QMetaObject.connectSlotsByName(QuitDialog)
    # setupUi

    def retranslateUi(self, QuitDialog):
        QuitDialog.setWindowTitle(QCoreApplication.translate("QuitDialog", u"Quit Confirmation", None))
        self.label.setText(QCoreApplication.translate("QuitDialog", u"Run currently active. Quitting now will end current run immediately. Are you sure?", None))
    # retranslateUi

