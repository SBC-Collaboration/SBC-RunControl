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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QToolBar, QWidget)
import resources_rc

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(495, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsWindow.sizePolicy().hasHeightForWidth())
        SettingsWindow.setSizePolicy(sizePolicy)
        SettingsWindow.setMinimumSize(QSize(400, 300))
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
        self.gridLayout_6 = QGridLayout(self.settings_sipm_tab)
        self.gridLayout_6.setSpacing(3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(3, 3, 3, 3)
        self.scrollArea_2 = QScrollArea(self.settings_sipm_tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 412, 225))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalSpacer_4 = QSpacerItem(20, 204, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_6.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.settings_sipm_tab, "")
        self.settings_cam_tab = QWidget()
        self.settings_cam_tab.setObjectName(u"settings_cam_tab")
        self.gridLayout_4 = QGridLayout(self.settings_cam_tab)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.scrollArea = QScrollArea(self.settings_cam_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setKerning(True)
        self.scrollArea.setFont(font)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 460, 379))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_17, 16, 0, 1, 1)

        self.spinBox_17 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_17.setObjectName(u"spinBox_17")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spinBox_17.sizePolicy().hasHeightForWidth())
        self.spinBox_17.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_17, 2, 3, 1, 1)

        self.spinBox_40 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_40.setObjectName(u"spinBox_40")
        sizePolicy1.setHeightForWidth(self.spinBox_40.sizePolicy().hasHeightForWidth())
        self.spinBox_40.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_40, 21, 1, 1, 1)

        self.spinBox_32 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_32.setObjectName(u"spinBox_32")
        sizePolicy1.setHeightForWidth(self.spinBox_32.sizePolicy().hasHeightForWidth())
        self.spinBox_32.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_32, 18, 2, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_14, 14, 0, 1, 1)

        self.spinBox_5 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_5.setObjectName(u"spinBox_5")
        sizePolicy1.setHeightForWidth(self.spinBox_5.sizePolicy().hasHeightForWidth())
        self.spinBox_5.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_5, 9, 1, 1, 1)

        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_18, 19, 0, 1, 1)

        self.spinBox_36 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_36.setObjectName(u"spinBox_36")
        sizePolicy1.setHeightForWidth(self.spinBox_36.sizePolicy().hasHeightForWidth())
        self.spinBox_36.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_36, 19, 3, 1, 1)

        self.spinBox_42 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_42.setObjectName(u"spinBox_42")
        sizePolicy1.setHeightForWidth(self.spinBox_42.sizePolicy().hasHeightForWidth())
        self.spinBox_42.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_42, 21, 3, 1, 1)

        self.lineEdit_8 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_5.addWidget(self.lineEdit_8, 1, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_5.addWidget(self.lineEdit_3, 15, 1, 1, 1)

        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_5.addWidget(self.lineEdit, 15, 3, 1, 1)

        self.spinBox_31 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_31.setObjectName(u"spinBox_31")
        sizePolicy1.setHeightForWidth(self.spinBox_31.sizePolicy().hasHeightForWidth())
        self.spinBox_31.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_31, 18, 1, 1, 1)

        self.spinBox_11 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_11.setObjectName(u"spinBox_11")
        sizePolicy1.setHeightForWidth(self.spinBox_11.sizePolicy().hasHeightForWidth())
        self.spinBox_11.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_11, 9, 2, 1, 1)

        self.spinBox_6 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_6.setObjectName(u"spinBox_6")
        sizePolicy1.setHeightForWidth(self.spinBox_6.sizePolicy().hasHeightForWidth())
        self.spinBox_6.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_6, 11, 1, 1, 1)

        self.spinBox_8 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_8.setObjectName(u"spinBox_8")
        sizePolicy1.setHeightForWidth(self.spinBox_8.sizePolicy().hasHeightForWidth())
        self.spinBox_8.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_8, 7, 3, 1, 1)

        self.spinBox_16 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_16.setObjectName(u"spinBox_16")
        sizePolicy1.setHeightForWidth(self.spinBox_16.sizePolicy().hasHeightForWidth())
        self.spinBox_16.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_16, 11, 3, 1, 1)

        self.spinBox_9 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_9.setObjectName(u"spinBox_9")
        sizePolicy1.setHeightForWidth(self.spinBox_9.sizePolicy().hasHeightForWidth())
        self.spinBox_9.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_9, 8, 2, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_7, 9, 0, 1, 1)

        self.spinBox_29 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_29.setObjectName(u"spinBox_29")
        sizePolicy1.setHeightForWidth(self.spinBox_29.sizePolicy().hasHeightForWidth())
        self.spinBox_29.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_29, 16, 1, 1, 1)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_4.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_4.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.doubleSpinBox_4, 6, 3, 1, 1)

        self.lineEdit_9 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_5.addWidget(self.lineEdit_9, 1, 3, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_11, 0, 3, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_3, 6, 0, 1, 1)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_3.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_3.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.doubleSpinBox_3, 6, 2, 1, 1)

        self.spinBox_12 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_12.setObjectName(u"spinBox_12")
        sizePolicy1.setHeightForWidth(self.spinBox_12.sizePolicy().hasHeightForWidth())
        self.spinBox_12.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_12, 9, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_5.addWidget(self.lineEdit_2, 15, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_5.addWidget(self.lineEdit_4, 14, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_5.addWidget(self.lineEdit_6, 14, 3, 1, 1)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_20, 21, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_5.addWidget(self.lineEdit_7, 1, 1, 1, 1)

        self.spinBox_15 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_15.setObjectName(u"spinBox_15")
        sizePolicy1.setHeightForWidth(self.spinBox_15.sizePolicy().hasHeightForWidth())
        self.spinBox_15.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_15, 11, 2, 1, 1)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_19, 20, 0, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_4, 7, 0, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_8, 11, 0, 1, 1)

        self.spinBox_19 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_19.setObjectName(u"spinBox_19")
        sizePolicy1.setHeightForWidth(self.spinBox_19.sizePolicy().hasHeightForWidth())
        self.spinBox_19.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_19, 2, 1, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_9, 0, 1, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_2.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_2.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.doubleSpinBox_2, 6, 1, 1, 1)

        self.spinBox_41 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_41.setObjectName(u"spinBox_41")
        sizePolicy1.setHeightForWidth(self.spinBox_41.sizePolicy().hasHeightForWidth())
        self.spinBox_41.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_41, 21, 2, 1, 1)

        self.spinBox_20 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_20.setObjectName(u"spinBox_20")
        sizePolicy1.setHeightForWidth(self.spinBox_20.sizePolicy().hasHeightForWidth())
        self.spinBox_20.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_20, 16, 3, 1, 1)

        self.spinBox_34 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_34.setObjectName(u"spinBox_34")
        sizePolicy1.setHeightForWidth(self.spinBox_34.sizePolicy().hasHeightForWidth())
        self.spinBox_34.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_34, 19, 1, 1, 1)

        self.spinBox_35 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_35.setObjectName(u"spinBox_35")
        sizePolicy1.setHeightForWidth(self.spinBox_35.sizePolicy().hasHeightForWidth())
        self.spinBox_35.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_35, 19, 2, 1, 1)

        self.spinBox_7 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_7.setObjectName(u"spinBox_7")
        sizePolicy1.setHeightForWidth(self.spinBox_7.sizePolicy().hasHeightForWidth())
        self.spinBox_7.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_7, 7, 2, 1, 1)

        self.spinBox_37 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_37.setObjectName(u"spinBox_37")
        sizePolicy1.setHeightForWidth(self.spinBox_37.sizePolicy().hasHeightForWidth())
        self.spinBox_37.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_37, 20, 1, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_21, 1, 0, 1, 1)

        self.spinBox_39 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_39.setObjectName(u"spinBox_39")
        sizePolicy1.setHeightForWidth(self.spinBox_39.sizePolicy().hasHeightForWidth())
        self.spinBox_39.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_39, 20, 3, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_16, 18, 0, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_10, 0, 2, 1, 1)

        self.spinBox_14 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_14.setObjectName(u"spinBox_14")
        sizePolicy1.setHeightForWidth(self.spinBox_14.sizePolicy().hasHeightForWidth())
        self.spinBox_14.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_14, 10, 3, 1, 1)

        self.spinBox_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_2.setObjectName(u"spinBox_2")
        sizePolicy1.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_2, 7, 1, 1, 1)

        self.spinBox_33 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_33.setObjectName(u"spinBox_33")
        sizePolicy1.setHeightForWidth(self.spinBox_33.sizePolicy().hasHeightForWidth())
        self.spinBox_33.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_33, 18, 3, 1, 1)

        self.spinBox_10 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_10.setObjectName(u"spinBox_10")
        sizePolicy1.setHeightForWidth(self.spinBox_10.sizePolicy().hasHeightForWidth())
        self.spinBox_10.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_10, 8, 3, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_15, 15, 0, 1, 1)

        self.spinBox_13 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_13.setObjectName(u"spinBox_13")
        sizePolicy1.setHeightForWidth(self.spinBox_13.sizePolicy().hasHeightForWidth())
        self.spinBox_13.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_13, 10, 2, 1, 1)

        self.spinBox_3 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_3.setObjectName(u"spinBox_3")
        sizePolicy1.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_3, 8, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_5.addWidget(self.lineEdit_5, 14, 2, 1, 1)

        self.spinBox_38 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_38.setObjectName(u"spinBox_38")
        sizePolicy1.setHeightForWidth(self.spinBox_38.sizePolicy().hasHeightForWidth())
        self.spinBox_38.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_38, 20, 2, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_5, 8, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 22, 0, 1, 4)

        self.spinBox_4 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_4.setObjectName(u"spinBox_4")
        sizePolicy1.setHeightForWidth(self.spinBox_4.sizePolicy().hasHeightForWidth())
        self.spinBox_4.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_4, 10, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_6, 10, 0, 1, 1)

        self.spinBox_18 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_18.setObjectName(u"spinBox_18")
        sizePolicy1.setHeightForWidth(self.spinBox_18.sizePolicy().hasHeightForWidth())
        self.spinBox_18.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_18, 2, 2, 1, 1)

        self.spinBox_30 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_30.setObjectName(u"spinBox_30")
        sizePolicy1.setHeightForWidth(self.spinBox_30.sizePolicy().hasHeightForWidth())
        self.spinBox_30.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.spinBox_30, 16, 2, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

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

        self.tabWidget.setCurrentIndex(3)


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
        self.label_17.setText(QCoreApplication.translate("SettingsWindow", u"State Comm Pin (IN)", None))
        self.label_14.setText(QCoreApplication.translate("SettingsWindow", u"Image Format", None))
        self.label_18.setText(QCoreApplication.translate("SettingsWindow", u"Trig Latch Pin (IN)", None))
        self.label_7.setText(QCoreApplication.translate("SettingsWindow", u"Frames After", None))
        self.label_11.setText(QCoreApplication.translate("SettingsWindow", u"Cam 3", None))
        self.label_3.setText(QCoreApplication.translate("SettingsWindow", u"Trig Enable Time", None))
        self.label_20.setText(QCoreApplication.translate("SettingsWindow", u"Trigger Pin (OUT)", None))
        self.lineEdit_7.setText("")
        self.label_19.setText(QCoreApplication.translate("SettingsWindow", u"State Pin (OUT)", None))
        self.label_4.setText(QCoreApplication.translate("SettingsWindow", u"Exposure", None))
        self.label_8.setText(QCoreApplication.translate("SettingsWindow", u"Pixel Treshold", None))
        self.label_9.setText(QCoreApplication.translate("SettingsWindow", u"Cam 1", None))
        self.label_13.setText(QCoreApplication.translate("SettingsWindow", u"Mode", None))
        self.label_21.setText(QCoreApplication.translate("SettingsWindow", u"IP Address", None))
        self.label_16.setText(QCoreApplication.translate("SettingsWindow", u"Trig Enbl Pin (IN)", None))
        self.label_10.setText(QCoreApplication.translate("SettingsWindow", u"Cam 2", None))
        self.label_15.setText(QCoreApplication.translate("SettingsWindow", u"Date Format", None))
        self.label_5.setText(QCoreApplication.translate("SettingsWindow", u"Buffer Length", None))
        self.label_6.setText(QCoreApplication.translate("SettingsWindow", u"ADC Threshold", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_cam_tab), QCoreApplication.translate("SettingsWindow", u"Camera", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_dio_tab), QCoreApplication.translate("SettingsWindow", u"DIO", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"toolBar", None))
    # retranslateUi

