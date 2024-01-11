# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(500, 400))
        MainWindow.setBaseSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/icons/sbc_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionFiles = QAction(MainWindow)
        self.actionFiles.setObjectName(u"actionFiles")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(50, 50))
        self.centralwidget.setBaseSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.start_run_but = QPushButton(self.centralwidget)
        self.start_run_but.setObjectName(u"start_run_but")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_run_but.sizePolicy().hasHeightForWidth())
        self.start_run_but.setSizePolicy(sizePolicy1)
        self.start_run_but.setMinimumSize(QSize(0, 50))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(0, 85, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        self.start_run_but.setPalette(palette)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.start_run_but.setFont(font)
        self.start_run_but.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout_2.addWidget(self.start_run_but, 1, 0, 1, 1)

        self.quit_but = QPushButton(self.centralwidget)
        self.quit_but.setObjectName(u"quit_but")
        self.quit_but.setMinimumSize(QSize(80, 30))

        self.gridLayout_2.addWidget(self.quit_but, 0, 0, 1, 1)

        self.stop_run_but = QPushButton(self.centralwidget)
        self.stop_run_but.setObjectName(u"stop_run_but")
        self.stop_run_but.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.stop_run_but.sizePolicy().hasHeightForWidth())
        self.stop_run_but.setSizePolicy(sizePolicy1)
        self.stop_run_but.setMinimumSize(QSize(0, 50))
        palette1 = QPalette()
        brush2 = QBrush(QColor(170, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        self.stop_run_but.setPalette(palette1)
        self.stop_run_but.setFont(font)

        self.gridLayout_2.addWidget(self.stop_run_but, 2, 0, 1, 1)

        self.run_state_label = QLabel(self.centralwidget)
        self.run_state_label.setObjectName(u"run_state_label")
        self.run_state_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.run_state_label, 3, 0, 1, 1)

        self.tabs_widget = QTabWidget(self.centralwidget)
        self.tabs_widget.setObjectName(u"tabs_widget")
        sizePolicy.setHeightForWidth(self.tabs_widget.sizePolicy().hasHeightForWidth())
        self.tabs_widget.setSizePolicy(sizePolicy)
        self.plc_tab = QWidget()
        self.plc_tab.setObjectName(u"plc_tab")
        self.widget = QWidget(self.plc_tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 261, 181))
        self.tabs_widget.addTab(self.plc_tab, "")
        self.scint_tab = QWidget()
        self.scint_tab.setObjectName(u"scint_tab")
        self.tabs_widget.addTab(self.scint_tab, "")
        self.camera_tab = QWidget()
        self.camera_tab.setObjectName(u"camera_tab")
        self.verticalLayout_2 = QVBoxLayout(self.camera_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelsLayout = QHBoxLayout()
        self.labelsLayout.setObjectName(u"labelsLayout")
        self.TakeImageButton = QPushButton(self.camera_tab)
        self.TakeImageButton.setObjectName(u"TakeImageButton")
        self.TakeImageButton.setMinimumSize(QSize(80, 30))

        self.labelsLayout.addWidget(self.TakeImageButton)

        self.CameraStatusLabel = QLabel(self.camera_tab)
        self.CameraStatusLabel.setObjectName(u"CameraStatusLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.CameraStatusLabel.sizePolicy().hasHeightForWidth())
        self.CameraStatusLabel.setSizePolicy(sizePolicy2)
        self.CameraStatusLabel.setLayoutDirection(Qt.LeftToRight)
        self.CameraStatusLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.labelsLayout.addWidget(self.CameraStatusLabel)

        self.Cam1StatusLight = QLabel(self.camera_tab)
        self.Cam1StatusLight.setObjectName(u"Cam1StatusLight")
        self.Cam1StatusLight.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(150, 150, 150);")
        self.Cam1StatusLight.setAlignment(Qt.AlignCenter)

        self.labelsLayout.addWidget(self.Cam1StatusLight)

        self.Cam2StatusLight = QLabel(self.camera_tab)
        self.Cam2StatusLight.setObjectName(u"Cam2StatusLight")
        self.Cam2StatusLight.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(150, 150, 150);")
        self.Cam2StatusLight.setAlignment(Qt.AlignCenter)

        self.labelsLayout.addWidget(self.Cam2StatusLight)

        self.Cam3StatusLight = QLabel(self.camera_tab)
        self.Cam3StatusLight.setObjectName(u"Cam3StatusLight")
        self.Cam3StatusLight.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(150, 150, 150);")
        self.Cam3StatusLight.setAlignment(Qt.AlignCenter)

        self.labelsLayout.addWidget(self.Cam3StatusLight)


        self.verticalLayout_2.addLayout(self.labelsLayout)

        self.imagesLayout = QHBoxLayout()
        self.imagesLayout.setObjectName(u"imagesLayout")
        self.graphicsView = QGraphicsView(self.camera_tab)
        self.graphicsView.setObjectName(u"graphicsView")

        self.imagesLayout.addWidget(self.graphicsView)


        self.verticalLayout_2.addLayout(self.imagesLayout)

        self.tabs_widget.addTab(self.camera_tab, "")
        self.settings_tab = QWidget()
        self.settings_tab.setObjectName(u"settings_tab")
        self.tabs_widget.addTab(self.settings_tab, "")

        self.gridLayout_2.addWidget(self.tabs_widget, 0, 1, 4, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 500, 22))
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.menuBar.sizePolicy().hasHeightForWidth())
        self.menuBar.setSizePolicy(sizePolicy3)
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuLog = QMenu(self.menuBar)
        self.menuLog.setObjectName(u"menuLog")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuLog.menuAction())

        self.retranslateUi(MainWindow)
        self.start_run_but.clicked.connect(MainWindow.start_run)
        self.quit_but.clicked.connect(MainWindow.quit)
        self.stop_run_but.clicked.connect(MainWindow.stop_run)

        self.tabs_widget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SBC Run Control", None))
        self.actionFiles.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.start_run_but.setText(QCoreApplication.translate("MainWindow", u"Start Run", None))
        self.quit_but.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.stop_run_but.setText(QCoreApplication.translate("MainWindow", u"Stop Run", None))
        self.run_state_label.setText(QCoreApplication.translate("MainWindow", u"RunState", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.plc_tab), QCoreApplication.translate("MainWindow", u"PLC", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.scint_tab), QCoreApplication.translate("MainWindow", u"Scintillation", None))
        self.TakeImageButton.setText(QCoreApplication.translate("MainWindow", u"Take Image", None))
        self.CameraStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Camera Status:", None))
        self.Cam1StatusLight.setText(QCoreApplication.translate("MainWindow", u"Cam 1", None))
        self.Cam2StatusLight.setText(QCoreApplication.translate("MainWindow", u"Cam 2", None))
        self.Cam3StatusLight.setText(QCoreApplication.translate("MainWindow", u"Cam 3", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.camera_tab), QCoreApplication.translate("MainWindow", u"Camera", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.settings_tab), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuLog.setTitle(QCoreApplication.translate("MainWindow", u"Logs", None))
    # retranslateUi

