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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QSizePolicy,
    QTextEdit, QToolBar, QWidget)
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
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.log_box = QTextEdit(self.centralwidget)
        self.log_box.setObjectName(u"log_box")

        self.horizontalLayout.addWidget(self.log_box)

        LogWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(LogWindow)
        self.toolBar.setObjectName(u"toolBar")
        LogWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionClose_Window)
        self.toolBar.addAction(self.actionReload_Log)

        self.retranslateUi(LogWindow)

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
        self.log_box.setHtml(QCoreApplication.translate("LogWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Log is loaded here</p></body></html>", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("LogWindow", u"toolBar", None))
    # retranslateUi

