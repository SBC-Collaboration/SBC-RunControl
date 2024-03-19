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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QToolBar,
    QToolButton, QVBoxLayout, QWidget)
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
        self.action_settings = QAction(MainWindow)
        self.action_settings.setObjectName(u"action_settings")
        icon1 = QIcon()
        icon1.addFile(u":/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_settings.setIcon(icon1)
        self.action_settings.setMenuRole(QAction.PreferencesRole)
        self.action_log = QAction(MainWindow)
        self.action_log.setObjectName(u"action_log")
        icon2 = QIcon()
        icon2.addFile(u":/icons/log.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_log.setIcon(icon2)
        self.action_quit = QAction(MainWindow)
        self.action_quit.setObjectName(u"action_quit")
        icon3 = QIcon()
        icon3.addFile(u":/icons/quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_quit.setIcon(icon3)
        self.action_quit.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(50, 50))
        self.centralwidget.setBaseSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.start_run_but = QPushButton(self.centralwidget)
        self.start_run_but.setObjectName(u"start_run_but")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_run_but.sizePolicy().hasHeightForWidth())
        self.start_run_but.setSizePolicy(sizePolicy1)
        self.start_run_but.setMinimumSize(QSize(0, 50))
        self.start_run_but.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.start_run_but.setFont(font)
        self.start_run_but.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_run_but.setStyleSheet(u"QPushButton:enabled {color: rgb(0, 85, 0);}\n"
"QPushButton:disabled {color: rgb(120, 120, 120);}")

        self.gridLayout.addWidget(self.start_run_but, 0, 0, 1, 1)

        self.run_label = QLabel(self.centralwidget)
        self.run_label.setObjectName(u"run_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.run_label.sizePolicy().hasHeightForWidth())
        self.run_label.setSizePolicy(sizePolicy2)
        self.run_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.run_label, 3, 0, 1, 1)

        self.run_state_label = QLabel(self.centralwidget)
        self.run_state_label.setObjectName(u"run_state_label")
        self.run_state_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.run_state_label, 2, 0, 1, 1)

        self.event_num_label = QLabel(self.centralwidget)
        self.event_num_label.setObjectName(u"event_num_label")
        sizePolicy2.setHeightForWidth(self.event_num_label.sizePolicy().hasHeightForWidth())
        self.event_num_label.setSizePolicy(sizePolicy2)
        self.event_num_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.event_num_label, 5, 0, 1, 1)

        self.run_edit = QLineEdit(self.centralwidget)
        self.run_edit.setObjectName(u"run_edit")
        self.run_edit.setReadOnly(True)
        self.run_edit.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.run_edit, 4, 0, 1, 1)

        self.stop_run_but = QPushButton(self.centralwidget)
        self.stop_run_but.setObjectName(u"stop_run_but")
        self.stop_run_but.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.stop_run_but.sizePolicy().hasHeightForWidth())
        self.stop_run_but.setSizePolicy(sizePolicy1)
        self.stop_run_but.setMinimumSize(QSize(0, 50))
        self.stop_run_but.setFont(font)
        self.stop_run_but.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_run_but.setStyleSheet(u"QPushButton:enabled {color: rgb(170, 0, 0);}\n"
"QPushButton:disabled {color: rgb(120, 120, 120);}")
        self.stop_run_but.setCheckable(True)

        self.gridLayout.addWidget(self.stop_run_but, 1, 0, 1, 1)

        self.event_num_edit = QLineEdit(self.centralwidget)
        self.event_num_edit.setObjectName(u"event_num_edit")
        self.event_num_edit.setReadOnly(True)

        self.gridLayout.addWidget(self.event_num_edit, 6, 0, 1, 1)

        self.event_time_label = QLabel(self.centralwidget)
        self.event_time_label.setObjectName(u"event_time_label")
        sizePolicy2.setHeightForWidth(self.event_time_label.sizePolicy().hasHeightForWidth())
        self.event_time_label.setSizePolicy(sizePolicy2)
        self.event_time_label.setLineWidth(1)
        self.event_time_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.event_time_label, 7, 0, 1, 1)

        self.event_time_edit = QLineEdit(self.centralwidget)
        self.event_time_edit.setObjectName(u"event_time_edit")
        self.event_time_edit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.event_time_edit.setReadOnly(True)

        self.gridLayout.addWidget(self.event_time_edit, 8, 0, 1, 1)

        self.run_live_time_label = QLabel(self.centralwidget)
        self.run_live_time_label.setObjectName(u"run_live_time_label")
        sizePolicy2.setHeightForWidth(self.run_live_time_label.sizePolicy().hasHeightForWidth())
        self.run_live_time_label.setSizePolicy(sizePolicy2)
        self.run_live_time_label.setLineWidth(1)
        self.run_live_time_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.run_live_time_label, 9, 0, 1, 1)

        self.run_live_time_edit = QLineEdit(self.centralwidget)
        self.run_live_time_edit.setObjectName(u"run_live_time_edit")
        self.run_live_time_edit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.run_live_time_edit.setReadOnly(True)

        self.gridLayout.addWidget(self.run_live_time_edit, 10, 0, 1, 1)

        self.tabs_widget = QTabWidget(self.centralwidget)
        self.tabs_widget.setObjectName(u"tabs_widget")
        sizePolicy.setHeightForWidth(self.tabs_widget.sizePolicy().hasHeightForWidth())
        self.tabs_widget.setSizePolicy(sizePolicy)
        self.tabs_widget.setSizeIncrement(QSize(100, 0))
        self.tabs_widget.setTabShape(QTabWidget.Rounded)
        self.tabs_widget.setDocumentMode(False)
        self.tabs_widget.setTabsClosable(False)
        self.tabs_widget.setMovable(True)
        self.plc_tab = QWidget()
        self.plc_tab.setObjectName(u"plc_tab")
        self.tabs_widget.addTab(self.plc_tab, "")
        self.scint_tab = QWidget()
        self.scint_tab.setObjectName(u"scint_tab")
        self.tabs_widget.addTab(self.scint_tab, "")
        self.acoustics_tab = QWidget()
        self.acoustics_tab.setObjectName(u"acoustics_tab")
        self.tabs_widget.addTab(self.acoustics_tab, "")
        self.camera_tab = QWidget()
        self.camera_tab.setObjectName(u"camera_tab")
        self.verticalLayout = QVBoxLayout(self.camera_tab)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.camera_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 405, 331))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(1000, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.take_image_but = QPushButton(self.scrollAreaWidgetContents)
        self.take_image_but.setObjectName(u"take_image_but")
        self.take_image_but.setMinimumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.take_image_but)

        self.camera_status_label = QLabel(self.scrollAreaWidgetContents)
        self.camera_status_label.setObjectName(u"camera_status_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.camera_status_label.sizePolicy().hasHeightForWidth())
        self.camera_status_label.setSizePolicy(sizePolicy3)
        self.camera_status_label.setLayoutDirection(Qt.LeftToRight)
        self.camera_status_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.camera_status_label)

        self.cam1_status_light = QLabel(self.scrollAreaWidgetContents)
        self.cam1_status_light.setObjectName(u"cam1_status_light")
        self.cam1_status_light.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(150, 150, 150);")
        self.cam1_status_light.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.cam1_status_light)

        self.cam2_status_light = QLabel(self.scrollAreaWidgetContents)
        self.cam2_status_light.setObjectName(u"cam2_status_light")
        self.cam2_status_light.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(150, 150, 150);")
        self.cam2_status_light.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.cam2_status_light)

        self.cam3_status_light = QLabel(self.scrollAreaWidgetContents)
        self.cam3_status_light.setObjectName(u"cam3_status_light")
        self.cam3_status_light.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(150, 150, 150);")
        self.cam3_status_light.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.cam3_status_light)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cam1_image = QLabel(self.scrollAreaWidgetContents)
        self.cam1_image.setObjectName(u"cam1_image")
        self.cam1_image.setMaximumSize(QSize(500, 300))
        self.cam1_image.setScaledContents(False)

        self.verticalLayout_3.addWidget(self.cam1_image)

        self.cam1_image_check = QCheckBox(self.scrollAreaWidgetContents)
        self.cam1_image_check.setObjectName(u"cam1_image_check")
        self.cam1_image_check.setChecked(False)

        self.verticalLayout_3.addWidget(self.cam1_image_check)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cam2_image = QLabel(self.scrollAreaWidgetContents)
        self.cam2_image.setObjectName(u"cam2_image")
        self.cam2_image.setMaximumSize(QSize(500, 300))
        self.cam2_image.setScaledContents(False)

        self.verticalLayout_4.addWidget(self.cam2_image)

        self.cam2_image_check = QCheckBox(self.scrollAreaWidgetContents)
        self.cam2_image_check.setObjectName(u"cam2_image_check")
        self.cam2_image_check.setChecked(False)

        self.verticalLayout_4.addWidget(self.cam2_image_check)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.cam3_image = QLabel(self.scrollAreaWidgetContents)
        self.cam3_image.setObjectName(u"cam3_image")
        self.cam3_image.setMaximumSize(QSize(500, 300))
        self.cam3_image.setScaledContents(False)

        self.verticalLayout_5.addWidget(self.cam3_image)

        self.cam3_image_check = QCheckBox(self.scrollAreaWidgetContents)
        self.cam3_image_check.setObjectName(u"cam3_image_check")
        self.cam3_image_check.setChecked(False)

        self.verticalLayout_5.addWidget(self.cam3_image_check)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.image_num_label = QLabel(self.scrollAreaWidgetContents)
        self.image_num_label.setObjectName(u"image_num_label")

        self.horizontalLayout_3.addWidget(self.image_num_label)

        self.image_num_box = QSpinBox(self.scrollAreaWidgetContents)
        self.image_num_box.setObjectName(u"image_num_box")
        self.image_num_box.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_3.addWidget(self.image_num_box)

        self.prev_image_but = QPushButton(self.scrollAreaWidgetContents)
        self.prev_image_but.setObjectName(u"prev_image_but")

        self.horizontalLayout_3.addWidget(self.prev_image_but)

        self.next_imag_but = QToolButton(self.scrollAreaWidgetContents)
        self.next_imag_but.setObjectName(u"next_imag_but")
        sizePolicy1.setHeightForWidth(self.next_imag_but.sizePolicy().hasHeightForWidth())
        self.next_imag_but.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.next_imag_but)

        self.image_play_but = QToolButton(self.scrollAreaWidgetContents)
        self.image_play_but.setObjectName(u"image_play_but")

        self.horizontalLayout_3.addWidget(self.image_play_but)

        self.load_image_but = QToolButton(self.scrollAreaWidgetContents)
        self.load_image_but.setObjectName(u"load_image_but")

        self.horizontalLayout_3.addWidget(self.load_image_but)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.tabs_widget.addTab(self.camera_tab, "")

        self.gridLayout.addWidget(self.tabs_widget, 0, 1, 11, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 9)
        self.gridLayout.setColumnMinimumWidth(0, 80)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setAutoFillBackground(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.action_quit)
        self.toolBar.addAction(self.action_settings)
        self.toolBar.addAction(self.action_log)

        self.retranslateUi(MainWindow)
        self.action_settings.triggered.connect(MainWindow.open_settings_window)
        self.action_log.triggered.connect(MainWindow.open_log_window)
        self.action_quit.triggered.connect(MainWindow.close)
        self.start_run_but.clicked.connect(MainWindow.start_run)

        self.tabs_widget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SBC Run Control", None))
        self.action_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(shortcut)
        self.action_settings.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_log.setText(QCoreApplication.translate("MainWindow", u"Log", None))
#if QT_CONFIG(tooltip)
        self.action_log.setToolTip(QCoreApplication.translate("MainWindow", u"Log", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_log.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.action_quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(tooltip)
        self.action_quit.setToolTip(QCoreApplication.translate("MainWindow", u"quit", None))
#endif // QT_CONFIG(tooltip)
        self.start_run_but.setText(QCoreApplication.translate("MainWindow", u"Start Run", None))
        self.run_label.setText(QCoreApplication.translate("MainWindow", u"Run Num", None))
        self.run_state_label.setText(QCoreApplication.translate("MainWindow", u"RunState", None))
        self.event_num_label.setText(QCoreApplication.translate("MainWindow", u"Event Num", None))
        self.run_edit.setPlaceholderText("")
        self.stop_run_but.setText(QCoreApplication.translate("MainWindow", u"Stop Run", None))
        self.event_time_label.setText(QCoreApplication.translate("MainWindow", u"Event Time", None))
        self.run_live_time_label.setText(QCoreApplication.translate("MainWindow", u"Run Live Time", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.plc_tab), QCoreApplication.translate("MainWindow", u"PLC", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.scint_tab), QCoreApplication.translate("MainWindow", u"Scintillation", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.acoustics_tab), QCoreApplication.translate("MainWindow", u"Acoustics", None))
        self.take_image_but.setText(QCoreApplication.translate("MainWindow", u"Take Image", None))
        self.camera_status_label.setText(QCoreApplication.translate("MainWindow", u"Camera Status:", None))
        self.cam1_status_light.setText(QCoreApplication.translate("MainWindow", u"Cam 1", None))
        self.cam2_status_light.setText(QCoreApplication.translate("MainWindow", u"Cam 2", None))
        self.cam3_status_light.setText(QCoreApplication.translate("MainWindow", u"Cam 3", None))
        self.cam1_image.setText("")
        self.cam1_image_check.setText(QCoreApplication.translate("MainWindow", u"Cam1", None))
        self.cam2_image.setText("")
        self.cam2_image_check.setText(QCoreApplication.translate("MainWindow", u"Cam2", None))
        self.cam3_image.setText("")
        self.cam3_image_check.setText(QCoreApplication.translate("MainWindow", u"Cam3", None))
        self.image_num_label.setText(QCoreApplication.translate("MainWindow", u"Image #", None))
        self.prev_image_but.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.next_imag_but.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.image_play_but.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.load_image_but.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.camera_tab), QCoreApplication.translate("MainWindow", u"Camera", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

