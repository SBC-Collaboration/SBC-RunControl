# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingswindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QToolBar, QWidget)
import resources_rc

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(498, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsWindow.sizePolicy().hasHeightForWidth())
        SettingsWindow.setSizePolicy(sizePolicy)
        SettingsWindow.setMinimumSize(QSize(300, 300))
        icon = QIcon()
        icon.addFile(u":/icons/sbc_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        SettingsWindow.setWindowIcon(icon)
        self.actionLoadConfig = QAction(SettingsWindow)
        self.actionLoadConfig.setObjectName(u"actionLoadConfig")
        icon1 = QIcon()
        icon1.addFile(u":/icons/reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLoadConfig.setIcon(icon1)
        self.actionLoadConfig.setMenuRole(QAction.NoRole)
        self.actionSaveConfig = QAction(SettingsWindow)
        self.actionSaveConfig.setObjectName(u"actionSaveConfig")
        icon2 = QIcon()
        icon2.addFile(u":/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSaveConfig.setIcon(icon2)
        self.actionSaveConfig.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(SettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.settings_files_tab = QWidget()
        self.settings_files_tab.setObjectName(u"settings_files_tab")
        self.gridLayout_3 = QGridLayout(self.settings_files_tab)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(3, 3, 3, 3)
        self.config_path_edit = QLineEdit(self.settings_files_tab)
        self.config_path_edit.setObjectName(u"config_path_edit")

        self.gridLayout_3.addWidget(self.config_path_edit, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(480, 174, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 3)

        self.data_path_label = QLabel(self.settings_files_tab)
        self.data_path_label.setObjectName(u"data_path_label")

        self.gridLayout_3.addWidget(self.data_path_label, 1, 0, 1, 1)

        self.config_path_label = QLabel(self.settings_files_tab)
        self.config_path_label.setObjectName(u"config_path_label")
        self.config_path_label.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.config_path_label, 0, 0, 1, 1)

        self.data_path_edit = QLineEdit(self.settings_files_tab)
        self.data_path_edit.setObjectName(u"data_path_edit")

        self.gridLayout_3.addWidget(self.data_path_edit, 1, 1, 1, 1)

        self.tabWidget.addTab(self.settings_files_tab, "")
        self.settings_run_tab = QWidget()
        self.settings_run_tab.setObjectName(u"settings_run_tab")
        self.gridLayout_2 = QGridLayout(self.settings_run_tab)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 2)

        self.label = QLabel(self.settings_run_tab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.settings_run_tab)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout_2.addWidget(self.doubleSpinBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.settings_run_tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinBox = QSpinBox(self.settings_run_tab)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_2.addWidget(self.spinBox, 1, 1, 1, 1)

        self.tabWidget.addTab(self.settings_run_tab, "")
        self.settings_sipm_tab = QWidget()
        self.settings_sipm_tab.setObjectName(u"settings_sipm_tab")
        self.tabWidget.addTab(self.settings_sipm_tab, "")
        self.settings_cam_tab = QWidget()
        self.settings_cam_tab.setObjectName(u"settings_cam_tab")
        self.tabWidget.addTab(self.settings_cam_tab, "")
        self.settings_dio_tab = QWidget()
        self.settings_dio_tab.setObjectName(u"settings_dio_tab")
        self.tabWidget.addTab(self.settings_dio_tab, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)

        SettingsWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(SettingsWindow)
        self.toolBar.setObjectName(u"toolBar")
        SettingsWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionLoadConfig)
        self.toolBar.addAction(self.actionSaveConfig)

        self.retranslateUi(SettingsWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"Settings", None))
        self.actionLoadConfig.setText(QCoreApplication.translate("SettingsWindow", u"LoadConfig", None))
        self.actionSaveConfig.setText(QCoreApplication.translate("SettingsWindow", u"SaveConfig", None))
        self.data_path_label.setText(QCoreApplication.translate("SettingsWindow", u"Data Path", None))
        self.config_path_label.setText(QCoreApplication.translate("SettingsWindow", u"Config Path", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_files_tab), QCoreApplication.translate("SettingsWindow", u"Files", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"Max Event Time (s)", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWindow", u"Max Number of Events", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_run_tab), QCoreApplication.translate("SettingsWindow", u"Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_sipm_tab), QCoreApplication.translate("SettingsWindow", u"SiPM", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_cam_tab), QCoreApplication.translate("SettingsWindow", u"Camera", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_dio_tab), QCoreApplication.translate("SettingsWindow", u"DIO", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"toolBar", None))
    # retranslateUi

