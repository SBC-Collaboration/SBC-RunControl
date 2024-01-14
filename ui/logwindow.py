# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QMainWindow,
    QPlainTextEdit, QSizePolicy, QToolBar, QWidget)
import resources_rc

class Ui_LogWindow(object):
    def setupUi(self, LogWindow):
        if not LogWindow.objectName():
            LogWindow.setObjectName(u"LogWindow")
        LogWindow.resize(350, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LogWindow.sizePolicy().hasHeightForWidth())
        LogWindow.setSizePolicy(sizePolicy)
        LogWindow.setMinimumSize(QSize(300, 150))
        icon = QIcon()
        icon.addFile(u":/icons/sbc_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        LogWindow.setWindowIcon(icon)
        self.actionClose_Window = QAction(LogWindow)
        self.actionClose_Window.setObjectName(u"actionClose_Window")
        icon1 = QIcon()
        icon1.addFile(u":/icons/quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClose_Window.setIcon(icon1)
        self.actionClose_Window.setMenuRole(QAction.NoRole)
        self.actionReload_Log = QAction(LogWindow)
        self.actionReload_Log.setObjectName(u"actionReload_Log")
        icon2 = QIcon()
        icon2.addFile(u":/icons/reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionReload_Log.setIcon(icon2)
        self.actionReload_Log.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(LogWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.auto_update_box = QCheckBox(self.centralwidget)
        self.auto_update_box.setObjectName(u"auto_update_box")
        self.auto_update_box.setChecked(True)

        self.gridLayout.addWidget(self.auto_update_box, 0, 1, 1, 1)

        self.hold_end_box = QCheckBox(self.centralwidget)
        self.hold_end_box.setObjectName(u"hold_end_box")
        self.hold_end_box.setChecked(True)

        self.gridLayout.addWidget(self.hold_end_box, 0, 2, 1, 1)

        self.log_box = QPlainTextEdit(self.centralwidget)
        self.log_box.setObjectName(u"log_box")

        self.gridLayout.addWidget(self.log_box, 3, 1, 1, 2)

        LogWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(LogWindow)
        self.toolBar.setObjectName(u"toolBar")
        LogWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionClose_Window)
        self.toolBar.addAction(self.actionReload_Log)

        self.retranslateUi(LogWindow)
        self.actionClose_Window.triggered.connect(LogWindow.close)
        self.actionReload_Log.triggered.connect(LogWindow.load_log)

        QMetaObject.connectSlotsByName(LogWindow)
    # setupUi

    def retranslateUi(self, LogWindow):
        LogWindow.setWindowTitle(QCoreApplication.translate("LogWindow", u"Log", None))
        self.actionClose_Window.setText(QCoreApplication.translate("LogWindow", u"Close Window", None))
#if QT_CONFIG(tooltip)
        self.actionClose_Window.setToolTip(QCoreApplication.translate("LogWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionClose_Window.setShortcut(QCoreApplication.translate("LogWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionReload_Log.setText(QCoreApplication.translate("LogWindow", u"Reload Log", None))
#if QT_CONFIG(tooltip)
        self.actionReload_Log.setToolTip(QCoreApplication.translate("LogWindow", u"Reload Log", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionReload_Log.setShortcut(QCoreApplication.translate("LogWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.auto_update_box.setText(QCoreApplication.translate("LogWindow", u"Auto Update", None))
        self.hold_end_box.setText(QCoreApplication.translate("LogWindow", u"Hold At End", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("LogWindow", u"toolBar", None))
    # retranslateUi

