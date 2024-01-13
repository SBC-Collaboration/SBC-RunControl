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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QToolBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(400, 462)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsWindow.sizePolicy().hasHeightForWidth())
        SettingsWindow.setSizePolicy(sizePolicy)
        SettingsWindow.setMinimumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u":/icons/sbc_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        SettingsWindow.setWindowIcon(icon)
        self.actionReloadConfig = QAction(SettingsWindow)
        self.actionReloadConfig.setObjectName(u"actionReloadConfig")
        icon1 = QIcon()
        icon1.addFile(u":/icons/reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionReloadConfig.setIcon(icon1)
        self.actionReloadConfig.setMenuRole(QAction.NoRole)
        self.actionSaveConfig = QAction(SettingsWindow)
        self.actionSaveConfig.setObjectName(u"actionSaveConfig")
        icon2 = QIcon()
        icon2.addFile(u":/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSaveConfig.setIcon(icon2)
        self.actionSaveConfig.setMenuRole(QAction.NoRole)
        self.actionApply_config = QAction(SettingsWindow)
        self.actionApply_config.setObjectName(u"actionApply_config")
        icon3 = QIcon()
        icon3.addFile(u":/icons/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionApply_config.setIcon(icon3)
        self.actionApply_config.setMenuRole(QAction.NoRole)
        self.actionClose_Window = QAction(SettingsWindow)
        self.actionClose_Window.setObjectName(u"actionClose_Window")
        icon4 = QIcon()
        icon4.addFile(u":/icons/quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClose_Window.setIcon(icon4)
        self.actionClose_Window.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(SettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.files_tab = QWidget()
        self.files_tab.setObjectName(u"files_tab")
        self.verticalLayout_4 = QVBoxLayout(self.files_tab)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.files_scroll_area = QScrollArea(self.files_tab)
        self.files_scroll_area.setObjectName(u"files_scroll_area")
        self.files_scroll_area.setFrameShape(QFrame.NoFrame)
        self.files_scroll_area.setFrameShadow(QFrame.Plain)
        self.files_scroll_area.setLineWidth(0)
        self.files_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 388, 393))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 336, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 2, 1, 1)

        self.config_path_label = QLabel(self.scrollAreaWidgetContents_5)
        self.config_path_label.setObjectName(u"config_path_label")
        self.config_path_label.setMinimumSize(QSize(0, 0))
        self.config_path_label.setLineWidth(0)
        self.config_path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.config_path_label, 0, 0, 1, 1)

        self.data_path_label = QLabel(self.scrollAreaWidgetContents_5)
        self.data_path_label.setObjectName(u"data_path_label")
        self.data_path_label.setLineWidth(0)
        self.data_path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.data_path_label, 1, 0, 1, 1)

        self.data_path_edit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.data_path_edit.setObjectName(u"data_path_edit")

        self.gridLayout_3.addWidget(self.data_path_edit, 1, 2, 1, 1)

        self.config_path_edit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.config_path_edit.setObjectName(u"config_path_edit")

        self.gridLayout_3.addWidget(self.config_path_edit, 0, 2, 1, 1)

        self.files_scroll_area.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_4.addWidget(self.files_scroll_area)

        self.tabWidget.addTab(self.files_tab, "")
        self.run_tab = QWidget()
        self.run_tab.setObjectName(u"run_tab")
        self.verticalLayout_6 = QVBoxLayout(self.run_tab)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.run_scroll_area = QScrollArea(self.run_tab)
        self.run_scroll_area.setObjectName(u"run_scroll_area")
        self.run_scroll_area.setFrameShape(QFrame.NoFrame)
        self.run_scroll_area.setFrameShadow(QFrame.Plain)
        self.run_scroll_area.setLineWidth(0)
        self.run_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 388, 393))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinBox = QSpinBox(self.scrollAreaWidgetContents_4)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000)
        self.spinBox.setValue(100)

        self.gridLayout_2.addWidget(self.spinBox, 1, 1, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout_2.addWidget(self.doubleSpinBox, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.run_scroll_area.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_6.addWidget(self.run_scroll_area)

        self.tabWidget.addTab(self.run_tab, "")
        self.sipm_tab = QWidget()
        self.sipm_tab.setObjectName(u"sipm_tab")
        self.verticalLayout_5 = QVBoxLayout(self.sipm_tab)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.sipm_scroll_area = QScrollArea(self.sipm_tab)
        self.sipm_scroll_area.setObjectName(u"sipm_scroll_area")
        self.sipm_scroll_area.setFrameShape(QFrame.NoFrame)
        self.sipm_scroll_area.setFrameShadow(QFrame.Plain)
        self.sipm_scroll_area.setLineWidth(0)
        self.sipm_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 388, 393))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.setSpacing(3)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 368, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.label_31 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_7.addWidget(self.label_31, 0, 0, 1, 1)

        self.sipm_scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.sipm_scroll_area)

        self.tabWidget.addTab(self.sipm_tab, "")
        self.acoustics_tab = QWidget()
        self.acoustics_tab.setObjectName(u"acoustics_tab")
        self.verticalLayout_7 = QVBoxLayout(self.acoustics_tab)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.acoustics_scroll_area = QScrollArea(self.acoustics_tab)
        self.acoustics_scroll_area.setObjectName(u"acoustics_scroll_area")
        self.acoustics_scroll_area.setFrameShape(QFrame.NoFrame)
        self.acoustics_scroll_area.setFrameShadow(QFrame.Plain)
        self.acoustics_scroll_area.setLineWidth(0)
        self.acoustics_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 388, 393))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.acous_general_grid = QGridLayout()
        self.acous_general_grid.setSpacing(3)
        self.acous_general_grid.setObjectName(u"acous_general_grid")
        self.label_33 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_general_grid.addWidget(self.label_33, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.acous_general_grid.addWidget(self.comboBox, 0, 1, 1, 3)

        self.label_32 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_general_grid.addWidget(self.label_32, 0, 0, 1, 1)

        self.spinBox_25 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_25.setObjectName(u"spinBox_25")

        self.acous_general_grid.addWidget(self.spinBox_25, 1, 1, 1, 1)

        self.label_35 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_general_grid.addWidget(self.label_35, 1, 2, 1, 1)

        self.spinBox_43 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_43.setObjectName(u"spinBox_43")

        self.acous_general_grid.addWidget(self.spinBox_43, 1, 3, 1, 1)

        self.label_34 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_general_grid.addWidget(self.label_34, 2, 0, 1, 1)

        self.spinBox_26 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_26.setObjectName(u"spinBox_26")

        self.acous_general_grid.addWidget(self.spinBox_26, 2, 1, 1, 1)

        self.label_36 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_general_grid.addWidget(self.label_36, 2, 2, 1, 1)

        self.spinBox_44 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_44.setObjectName(u"spinBox_44")

        self.acous_general_grid.addWidget(self.spinBox_44, 2, 3, 1, 1)


        self.verticalLayout_8.addLayout(self.acous_general_grid)

        self.line_2 = QFrame(self.scrollAreaWidgetContents_6)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_2)

        self.acous_per_ch_grid = QGridLayout()
        self.acous_per_ch_grid.setSpacing(3)
        self.acous_per_ch_grid.setObjectName(u"acous_per_ch_grid")
        self.spinBox_84 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_84.setObjectName(u"spinBox_84")

        self.acous_per_ch_grid.addWidget(self.spinBox_84, 2, 3, 1, 1)

        self.label_37 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_37.setObjectName(u"label_37")

        self.acous_per_ch_grid.addWidget(self.label_37, 0, 3, 1, 1)

        self.spinBox_90 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_90.setObjectName(u"spinBox_90")

        self.acous_per_ch_grid.addWidget(self.spinBox_90, 5, 3, 1, 1)

        self.label_40 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.label_40, 1, 0, 1, 1)

        self.checkBox_19 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_19.setObjectName(u"checkBox_19")

        self.acous_per_ch_grid.addWidget(self.checkBox_19, 2, 5, 1, 1)

        self.comboBox_9 = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setIconSize(QSize(16, 16))
        self.comboBox_9.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.comboBox_9, 8, 6, 1, 1)

        self.spinBox_86 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_86.setObjectName(u"spinBox_86")

        self.acous_per_ch_grid.addWidget(self.spinBox_86, 3, 4, 1, 1)

        self.spinBox_92 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_92.setObjectName(u"spinBox_92")

        self.acous_per_ch_grid.addWidget(self.spinBox_92, 7, 3, 1, 1)

        self.label_62 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_62.setObjectName(u"label_62")

        self.acous_per_ch_grid.addWidget(self.label_62, 0, 5, 1, 1)

        self.checkBox_25 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_25.setObjectName(u"checkBox_25")

        self.acous_per_ch_grid.addWidget(self.checkBox_25, 8, 5, 1, 1)

        self.spinBox_97 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_97.setObjectName(u"spinBox_97")

        self.acous_per_ch_grid.addWidget(self.spinBox_97, 1, 7, 1, 1)

        self.label_56 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.label_56, 3, 0, 1, 1)

        self.spinBox_82 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_82.setObjectName(u"spinBox_82")
        self.spinBox_82.setStepType(QAbstractSpinBox.DefaultStepType)

        self.acous_per_ch_grid.addWidget(self.spinBox_82, 1, 3, 1, 1)

        self.checkBox_13 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.acous_per_ch_grid.addWidget(self.checkBox_13, 4, 2, 1, 1)

        self.spinBox_101 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_101.setObjectName(u"spinBox_101")

        self.acous_per_ch_grid.addWidget(self.spinBox_101, 5, 7, 1, 1)

        self.checkBox_22 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_22.setObjectName(u"checkBox_22")

        self.acous_per_ch_grid.addWidget(self.checkBox_22, 5, 5, 1, 1)

        self.comboBox_2 = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setIconSize(QSize(16, 16))
        self.comboBox_2.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.comboBox_2, 1, 6, 1, 1)

        self.comboBox_4 = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setIconSize(QSize(16, 16))
        self.comboBox_4.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.comboBox_4, 3, 6, 1, 1)

        self.label_58 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.label_58, 5, 0, 1, 1)

        self.label_39 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_39.setObjectName(u"label_39")

        self.acous_per_ch_grid.addWidget(self.label_39, 0, 2, 1, 1)

        self.checkBox_21 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_21.setObjectName(u"checkBox_21")

        self.acous_per_ch_grid.addWidget(self.checkBox_21, 4, 5, 1, 1)

        self.spinBox_95 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_95.setObjectName(u"spinBox_95")

        self.acous_per_ch_grid.addWidget(self.spinBox_95, 8, 4, 1, 1)

        self.checkBox_23 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.acous_per_ch_grid.addWidget(self.checkBox_23, 6, 5, 1, 1)

        self.checkBox_24 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_24.setObjectName(u"checkBox_24")

        self.acous_per_ch_grid.addWidget(self.checkBox_24, 7, 5, 1, 1)

        self.label_63 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_63.setObjectName(u"label_63")

        self.acous_per_ch_grid.addWidget(self.label_63, 0, 6, 1, 1)

        self.acous__ch1_enbl_ckbox = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous__ch1_enbl_ckbox.setObjectName(u"acous__ch1_enbl_ckbox")

        self.acous_per_ch_grid.addWidget(self.acous__ch1_enbl_ckbox, 1, 2, 1, 1)

        self.comboBox_7 = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setIconSize(QSize(16, 16))
        self.comboBox_7.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.comboBox_7, 6, 6, 1, 1)

        self.label_64 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_64.setObjectName(u"label_64")

        self.acous_per_ch_grid.addWidget(self.label_64, 0, 7, 1, 1)

        self.spinBox_91 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_91.setObjectName(u"spinBox_91")

        self.acous_per_ch_grid.addWidget(self.spinBox_91, 6, 4, 1, 1)

        self.label_38 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_38.setObjectName(u"label_38")

        self.acous_per_ch_grid.addWidget(self.label_38, 0, 4, 1, 1)

        self.spinBox_85 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_85.setObjectName(u"spinBox_85")

        self.acous_per_ch_grid.addWidget(self.spinBox_85, 3, 3, 1, 1)

        self.comboBox_6 = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setIconSize(QSize(16, 16))
        self.comboBox_6.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.comboBox_6, 5, 6, 1, 1)

        self.acous__ch3_enbl_ckbox = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous__ch3_enbl_ckbox.setObjectName(u"acous__ch3_enbl_ckbox")

        self.acous_per_ch_grid.addWidget(self.acous__ch3_enbl_ckbox, 3, 2, 1, 1)

        self.spinBox_88 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_88.setObjectName(u"spinBox_88")

        self.acous_per_ch_grid.addWidget(self.spinBox_88, 4, 4, 1, 1)

        self.checkBox_20 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_20.setObjectName(u"checkBox_20")

        self.acous_per_ch_grid.addWidget(self.checkBox_20, 3, 5, 1, 1)

        self.label_59 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.label_59, 6, 0, 1, 1)

        self.spinBox_98 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_98.setObjectName(u"spinBox_98")

        self.acous_per_ch_grid.addWidget(self.spinBox_98, 2, 7, 1, 1)

        self.spinBox_93 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_93.setObjectName(u"spinBox_93")

        self.acous_per_ch_grid.addWidget(self.spinBox_93, 6, 3, 1, 1)

        self.checkBox_14 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.acous_per_ch_grid.addWidget(self.checkBox_14, 5, 2, 1, 1)

        self.checkBox_15 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.acous_per_ch_grid.addWidget(self.checkBox_15, 6, 2, 1, 1)

        self.spinBox_99 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_99.setObjectName(u"spinBox_99")

        self.acous_per_ch_grid.addWidget(self.spinBox_99, 3, 7, 1, 1)

        self.spinBox_104 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_104.setObjectName(u"spinBox_104")

        self.acous_per_ch_grid.addWidget(self.spinBox_104, 8, 7, 1, 1)

        self.spinBox_87 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_87.setObjectName(u"spinBox_87")

        self.acous_per_ch_grid.addWidget(self.spinBox_87, 4, 3, 1, 1)

        self.spinBox_89 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_89.setObjectName(u"spinBox_89")

        self.acous_per_ch_grid.addWidget(self.spinBox_89, 5, 4, 1, 1)

        self.spinBox_100 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_100.setObjectName(u"spinBox_100")

        self.acous_per_ch_grid.addWidget(self.spinBox_100, 4, 7, 1, 1)

        self.spinBox_102 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_102.setObjectName(u"spinBox_102")

        self.acous_per_ch_grid.addWidget(self.spinBox_102, 6, 7, 1, 1)

        self.label_57 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.label_57, 4, 0, 1, 1)

        self.acous__ch2_enbl_ckbox = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous__ch2_enbl_ckbox.setObjectName(u"acous__ch2_enbl_ckbox")

        self.acous_per_ch_grid.addWidget(self.acous__ch2_enbl_ckbox, 2, 2, 1, 1)

        self.checkBox_18 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.acous_per_ch_grid.addWidget(self.checkBox_18, 1, 5, 1, 1)

        self.spinBox_96 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_96.setObjectName(u"spinBox_96")

        self.acous_per_ch_grid.addWidget(self.spinBox_96, 8, 3, 1, 1)

        self.label_61 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.label_61, 8, 0, 1, 1)

        self.spinBox_94 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_94.setObjectName(u"spinBox_94")

        self.acous_per_ch_grid.addWidget(self.spinBox_94, 7, 4, 1, 1)

        self.comboBox_5 = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setIconSize(QSize(16, 16))
        self.comboBox_5.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.comboBox_5, 4, 6, 1, 1)

        self.spinBox_103 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_103.setObjectName(u"spinBox_103")

        self.acous_per_ch_grid.addWidget(self.spinBox_103, 7, 7, 1, 1)

        self.label_52 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.label_52, 2, 0, 1, 1)

        self.spinBox_83 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_83.setObjectName(u"spinBox_83")

        self.acous_per_ch_grid.addWidget(self.spinBox_83, 2, 4, 1, 1)

        self.label_60 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.label_60, 7, 0, 1, 1)

        self.spinBox_81 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_81.setObjectName(u"spinBox_81")

        self.acous_per_ch_grid.addWidget(self.spinBox_81, 1, 4, 1, 1)

        self.checkBox_16 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.acous_per_ch_grid.addWidget(self.checkBox_16, 7, 2, 1, 1)

        self.checkBox_17 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_17.setObjectName(u"checkBox_17")

        self.acous_per_ch_grid.addWidget(self.checkBox_17, 8, 2, 1, 1)

        self.comboBox_8 = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setIconSize(QSize(16, 16))
        self.comboBox_8.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.comboBox_8, 7, 6, 1, 1)

        self.comboBox_3 = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setIconSize(QSize(16, 16))
        self.comboBox_3.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.comboBox_3, 2, 6, 1, 1)

        self.label_65 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.label_65, 9, 0, 1, 1)

        self.checkBox_26 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_26.setObjectName(u"checkBox_26")

        self.acous_per_ch_grid.addWidget(self.checkBox_26, 9, 5, 1, 1)

        self.comboBox_13 = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setIconSize(QSize(16, 16))
        self.comboBox_13.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.comboBox_13, 9, 6, 1, 1)

        self.spinBox_105 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox_105.setObjectName(u"spinBox_105")

        self.acous_per_ch_grid.addWidget(self.spinBox_105, 9, 7, 1, 1)


        self.verticalLayout_8.addLayout(self.acous_per_ch_grid)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_6)

        self.acoustics_scroll_area.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_7.addWidget(self.acoustics_scroll_area)

        self.tabWidget.addTab(self.acoustics_tab, "")
        self.cam_tab = QWidget()
        self.cam_tab.setObjectName(u"cam_tab")
        self.verticalLayout_3 = QVBoxLayout(self.cam_tab)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cam_scroll_area = QScrollArea(self.cam_tab)
        self.cam_scroll_area.setObjectName(u"cam_scroll_area")
        self.cam_scroll_area.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setKerning(True)
        self.cam_scroll_area.setFont(font)
        self.cam_scroll_area.setFrameShape(QFrame.NoFrame)
        self.cam_scroll_area.setFrameShadow(QFrame.Plain)
        self.cam_scroll_area.setLineWidth(0)
        self.cam_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 371, 427))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_17, 18, 0, 1, 1)

        self.spinBox_17 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_17.setObjectName(u"spinBox_17")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinBox_17.sizePolicy().hasHeightForWidth())
        self.spinBox_17.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_17, 4, 3, 1, 1)

        self.spinBox_40 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_40.setObjectName(u"spinBox_40")
        sizePolicy2.setHeightForWidth(self.spinBox_40.sizePolicy().hasHeightForWidth())
        self.spinBox_40.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_40, 23, 1, 1, 1)

        self.label_29 = QLabel(self.scrollAreaWidgetContents)
        self.label_29.setObjectName(u"label_29")
        sizePolicy1.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy1)
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_29, 1, 0, 1, 1)

        self.spinBox_5 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_5.setObjectName(u"spinBox_5")
        sizePolicy2.setHeightForWidth(self.spinBox_5.sizePolicy().hasHeightForWidth())
        self.spinBox_5.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_5, 11, 1, 1, 1)

        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_18, 21, 0, 1, 1)

        self.spinBox_42 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_42.setObjectName(u"spinBox_42")
        sizePolicy2.setHeightForWidth(self.spinBox_42.sizePolicy().hasHeightForWidth())
        self.spinBox_42.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_42, 23, 3, 1, 1)

        self.lineEdit_15 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_5.addWidget(self.lineEdit_15, 1, 1, 1, 1)

        self.lineEdit_12 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_5.addWidget(self.lineEdit_12, 3, 1, 1, 1)

        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_5.addWidget(self.lineEdit, 17, 3, 1, 1)

        self.spinBox_8 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_8.setObjectName(u"spinBox_8")
        sizePolicy2.setHeightForWidth(self.spinBox_8.sizePolicy().hasHeightForWidth())
        self.spinBox_8.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_8, 9, 3, 1, 1)

        self.lineEdit_7 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_5.addWidget(self.lineEdit_7, 2, 2, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_7, 11, 0, 1, 1)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_4.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_4.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.doubleSpinBox_4, 8, 3, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_11, 0, 3, 1, 1)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_3.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_3.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.doubleSpinBox_3, 8, 2, 1, 1)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_20, 23, 0, 1, 1)

        self.comboBox_10 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.gridLayout_5.addWidget(self.comboBox_10, 16, 1, 1, 1)

        self.spinBox_15 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_15.setObjectName(u"spinBox_15")
        sizePolicy2.setHeightForWidth(self.spinBox_15.sizePolicy().hasHeightForWidth())
        self.spinBox_15.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_15, 13, 2, 1, 1)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_19, 22, 0, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_9, 0, 1, 1, 1)

        self.spinBox_20 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_20.setObjectName(u"spinBox_20")
        sizePolicy2.setHeightForWidth(self.spinBox_20.sizePolicy().hasHeightForWidth())
        self.spinBox_20.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_20, 18, 3, 1, 1)

        self.lineEdit_16 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_5.addWidget(self.lineEdit_16, 1, 2, 1, 1)

        self.label_30 = QLabel(self.scrollAreaWidgetContents)
        self.label_30.setObjectName(u"label_30")
        sizePolicy1.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy1)
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_30, 2, 0, 1, 1)

        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")
        sizePolicy1.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy1)
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_21, 3, 0, 1, 1)

        self.lineEdit_14 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout_5.addWidget(self.lineEdit_14, 3, 3, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_10, 0, 2, 1, 1)

        self.spinBox_14 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_14.setObjectName(u"spinBox_14")
        sizePolicy2.setHeightForWidth(self.spinBox_14.sizePolicy().hasHeightForWidth())
        self.spinBox_14.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_14, 12, 3, 1, 1)

        self.spinBox_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_2.setObjectName(u"spinBox_2")
        sizePolicy2.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_2, 9, 1, 1, 1)

        self.lineEdit_9 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_5.addWidget(self.lineEdit_9, 2, 1, 1, 1)

        self.spinBox_38 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_38.setObjectName(u"spinBox_38")
        sizePolicy2.setHeightForWidth(self.spinBox_38.sizePolicy().hasHeightForWidth())
        self.spinBox_38.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_38, 22, 2, 1, 1)

        self.spinBox_3 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_3.setObjectName(u"spinBox_3")
        sizePolicy2.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_3, 10, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 24, 0, 1, 4)

        self.spinBox_4 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_4.setObjectName(u"spinBox_4")
        sizePolicy2.setHeightForWidth(self.spinBox_4.sizePolicy().hasHeightForWidth())
        self.spinBox_4.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_4, 12, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_6, 12, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_5.addWidget(self.lineEdit_3, 17, 1, 1, 1)

        self.spinBox_32 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_32.setObjectName(u"spinBox_32")
        sizePolicy2.setHeightForWidth(self.spinBox_32.sizePolicy().hasHeightForWidth())
        self.spinBox_32.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_32, 20, 2, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_14, 16, 0, 1, 1)

        self.spinBox_36 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_36.setObjectName(u"spinBox_36")
        sizePolicy2.setHeightForWidth(self.spinBox_36.sizePolicy().hasHeightForWidth())
        self.spinBox_36.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_36, 21, 3, 1, 1)

        self.spinBox_31 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_31.setObjectName(u"spinBox_31")
        sizePolicy2.setHeightForWidth(self.spinBox_31.sizePolicy().hasHeightForWidth())
        self.spinBox_31.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_31, 20, 1, 1, 1)

        self.spinBox_11 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_11.setObjectName(u"spinBox_11")
        sizePolicy2.setHeightForWidth(self.spinBox_11.sizePolicy().hasHeightForWidth())
        self.spinBox_11.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_11, 11, 2, 1, 1)

        self.spinBox_6 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_6.setObjectName(u"spinBox_6")
        sizePolicy2.setHeightForWidth(self.spinBox_6.sizePolicy().hasHeightForWidth())
        self.spinBox_6.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_6, 13, 1, 1, 1)

        self.spinBox_16 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_16.setObjectName(u"spinBox_16")
        sizePolicy2.setHeightForWidth(self.spinBox_16.sizePolicy().hasHeightForWidth())
        self.spinBox_16.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_16, 13, 3, 1, 1)

        self.spinBox_9 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_9.setObjectName(u"spinBox_9")
        sizePolicy2.setHeightForWidth(self.spinBox_9.sizePolicy().hasHeightForWidth())
        self.spinBox_9.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_9, 10, 2, 1, 1)

        self.spinBox_29 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_29.setObjectName(u"spinBox_29")
        sizePolicy2.setHeightForWidth(self.spinBox_29.sizePolicy().hasHeightForWidth())
        self.spinBox_29.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_29, 18, 1, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_3, 8, 0, 1, 1)

        self.spinBox_12 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_12.setObjectName(u"spinBox_12")
        sizePolicy2.setHeightForWidth(self.spinBox_12.sizePolicy().hasHeightForWidth())
        self.spinBox_12.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_12, 11, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_5.addWidget(self.lineEdit_2, 17, 2, 1, 1)

        self.lineEdit_8 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_5.addWidget(self.lineEdit_8, 2, 3, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_4, 9, 0, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_8, 13, 0, 1, 1)

        self.spinBox_19 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_19.setObjectName(u"spinBox_19")
        sizePolicy2.setHeightForWidth(self.spinBox_19.sizePolicy().hasHeightForWidth())
        self.spinBox_19.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_19, 4, 1, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_2.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_2.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.doubleSpinBox_2, 8, 1, 1, 1)

        self.spinBox_41 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_41.setObjectName(u"spinBox_41")
        sizePolicy2.setHeightForWidth(self.spinBox_41.sizePolicy().hasHeightForWidth())
        self.spinBox_41.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_41, 23, 2, 1, 1)

        self.spinBox_34 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_34.setObjectName(u"spinBox_34")
        sizePolicy2.setHeightForWidth(self.spinBox_34.sizePolicy().hasHeightForWidth())
        self.spinBox_34.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_34, 21, 1, 1, 1)

        self.spinBox_35 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_35.setObjectName(u"spinBox_35")
        sizePolicy2.setHeightForWidth(self.spinBox_35.sizePolicy().hasHeightForWidth())
        self.spinBox_35.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_35, 21, 2, 1, 1)

        self.spinBox_7 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_7.setObjectName(u"spinBox_7")
        sizePolicy2.setHeightForWidth(self.spinBox_7.sizePolicy().hasHeightForWidth())
        self.spinBox_7.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_7, 9, 2, 1, 1)

        self.spinBox_37 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_37.setObjectName(u"spinBox_37")
        sizePolicy2.setHeightForWidth(self.spinBox_37.sizePolicy().hasHeightForWidth())
        self.spinBox_37.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_37, 22, 1, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_13, 4, 0, 1, 1)

        self.spinBox_39 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_39.setObjectName(u"spinBox_39")
        sizePolicy2.setHeightForWidth(self.spinBox_39.sizePolicy().hasHeightForWidth())
        self.spinBox_39.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_39, 22, 3, 1, 1)

        self.lineEdit_17 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_5.addWidget(self.lineEdit_17, 1, 3, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_16, 20, 0, 1, 1)

        self.spinBox_33 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_33.setObjectName(u"spinBox_33")
        sizePolicy2.setHeightForWidth(self.spinBox_33.sizePolicy().hasHeightForWidth())
        self.spinBox_33.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_33, 20, 3, 1, 1)

        self.spinBox_10 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_10.setObjectName(u"spinBox_10")
        sizePolicy2.setHeightForWidth(self.spinBox_10.sizePolicy().hasHeightForWidth())
        self.spinBox_10.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_10, 10, 3, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_15, 17, 0, 1, 1)

        self.spinBox_13 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_13.setObjectName(u"spinBox_13")
        sizePolicy2.setHeightForWidth(self.spinBox_13.sizePolicy().hasHeightForWidth())
        self.spinBox_13.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_13, 12, 2, 1, 1)

        self.spinBox_30 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_30.setObjectName(u"spinBox_30")
        sizePolicy2.setHeightForWidth(self.spinBox_30.sizePolicy().hasHeightForWidth())
        self.spinBox_30.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_30, 18, 2, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_5, 10, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_5.addWidget(self.lineEdit_13, 3, 2, 1, 1)

        self.spinBox_18 = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_18.setObjectName(u"spinBox_18")
        sizePolicy2.setHeightForWidth(self.spinBox_18.sizePolicy().hasHeightForWidth())
        self.spinBox_18.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.spinBox_18, 4, 2, 1, 1)

        self.comboBox_11 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.gridLayout_5.addWidget(self.comboBox_11, 16, 2, 1, 1)

        self.comboBox_12 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")

        self.gridLayout_5.addWidget(self.comboBox_12, 16, 3, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_5.setColumnStretch(2, 1)
        self.gridLayout_5.setColumnStretch(3, 1)
        self.cam_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.cam_scroll_area)

        self.tabWidget.addTab(self.cam_tab, "")
        self.dio_tab = QWidget()
        self.dio_tab.setObjectName(u"dio_tab")
        self.verticalLayout = QVBoxLayout(self.dio_tab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dio_scroll_area = QScrollArea(self.dio_tab)
        self.dio_scroll_area.setObjectName(u"dio_scroll_area")
        self.dio_scroll_area.setFrameShape(QFrame.NoFrame)
        self.dio_scroll_area.setFrameShadow(QFrame.Plain)
        self.dio_scroll_area.setLineWidth(0)
        self.dio_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 388, 393))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setSpacing(3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(-1, 6, -1, 6)
        self.spinBox_22 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_22.setObjectName(u"spinBox_22")

        self.gridLayout_8.addWidget(self.spinBox_22, 3, 3, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_12, 0, 0, 1, 4)

        self.spinBox_21 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_21.setObjectName(u"spinBox_21")

        self.gridLayout_8.addWidget(self.spinBox_21, 3, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_8.addWidget(self.lineEdit_10, 1, 1, 1, 3)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_24, 3, 0, 1, 1)

        self.label_22 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_22, 1, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_8.addWidget(self.lineEdit_11, 2, 1, 1, 3)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_25, 3, 2, 1, 1)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_23, 2, 0, 1, 1)

        self.label_26 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_26, 4, 0, 1, 1)

        self.spinBox_23 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_23.setObjectName(u"spinBox_23")

        self.gridLayout_8.addWidget(self.spinBox_23, 4, 1, 1, 1)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_27, 4, 2, 1, 1)

        self.spinBox_24 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_24.setObjectName(u"spinBox_24")

        self.gridLayout_8.addWidget(self.spinBox_24, 4, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_8)

        self.line = QFrame(self.scrollAreaWidgetContents_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.label_28 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_28)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setSpacing(3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(6, 6, -1, -1)
        self.label_47 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_47, 2, 0, 1, 1)

        self.spinBox_53 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_53.setObjectName(u"spinBox_53")

        self.gridLayout_11.addWidget(self.spinBox_53, 4, 1, 1, 1)

        self.spinBox_47 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_47.setObjectName(u"spinBox_47")

        self.gridLayout_11.addWidget(self.spinBox_47, 2, 1, 1, 1)

        self.spinBox_46 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_46.setObjectName(u"spinBox_46")
        self.spinBox_46.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox_46.setKeyboardTracking(True)

        self.gridLayout_11.addWidget(self.spinBox_46, 2, 3, 1, 1)

        self.label_54 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_54, 9, 0, 1, 1)

        self.label_51 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_51, 7, 0, 1, 1)

        self.label_43 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_43, 0, 4, 1, 1)

        self.label_46 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_46, 0, 2, 1, 1)

        self.spinBox_54 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_54.setObjectName(u"spinBox_54")

        self.gridLayout_11.addWidget(self.spinBox_54, 4, 2, 1, 1)

        self.spinBox_50 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_50.setObjectName(u"spinBox_50")

        self.gridLayout_11.addWidget(self.spinBox_50, 3, 3, 1, 1)

        self.spinBox_56 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_56.setObjectName(u"spinBox_56")

        self.gridLayout_11.addWidget(self.spinBox_56, 4, 4, 1, 1)

        self.spinBox_48 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_48.setObjectName(u"spinBox_48")

        self.gridLayout_11.addWidget(self.spinBox_48, 2, 2, 1, 1)

        self.label_50 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_50, 6, 0, 1, 1)

        self.label_49 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_49, 5, 0, 1, 1)

        self.label_53 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_53, 8, 0, 1, 1)

        self.spinBox_55 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_55.setObjectName(u"spinBox_55")

        self.gridLayout_11.addWidget(self.spinBox_55, 4, 3, 1, 1)

        self.spinBox_49 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_49.setObjectName(u"spinBox_49")

        self.gridLayout_11.addWidget(self.spinBox_49, 3, 2, 1, 1)

        self.label_45 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_45, 0, 5, 1, 1)

        self.spinBox_52 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_52.setObjectName(u"spinBox_52")

        self.gridLayout_11.addWidget(self.spinBox_52, 3, 1, 1, 1)

        self.label_42 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_42, 0, 1, 1, 1)

        self.label_41 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_41, 3, 0, 1, 1)

        self.spinBox_45 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_45.setObjectName(u"spinBox_45")

        self.gridLayout_11.addWidget(self.spinBox_45, 2, 4, 1, 1)

        self.label_44 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_44, 0, 3, 1, 1)

        self.spinBox_51 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_51.setObjectName(u"spinBox_51")

        self.gridLayout_11.addWidget(self.spinBox_51, 3, 4, 1, 1)

        self.label_48 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_48, 4, 0, 1, 1)

        self.label_55 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_55, 10, 0, 1, 1)

        self.spinBox_57 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_57.setObjectName(u"spinBox_57")

        self.gridLayout_11.addWidget(self.spinBox_57, 5, 2, 1, 1)

        self.spinBox_58 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_58.setObjectName(u"spinBox_58")

        self.gridLayout_11.addWidget(self.spinBox_58, 5, 3, 1, 1)

        self.spinBox_59 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_59.setObjectName(u"spinBox_59")

        self.gridLayout_11.addWidget(self.spinBox_59, 5, 4, 1, 1)

        self.spinBox_60 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_60.setObjectName(u"spinBox_60")

        self.gridLayout_11.addWidget(self.spinBox_60, 5, 1, 1, 1)

        self.spinBox_61 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_61.setObjectName(u"spinBox_61")

        self.gridLayout_11.addWidget(self.spinBox_61, 6, 1, 1, 1)

        self.spinBox_62 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_62.setObjectName(u"spinBox_62")

        self.gridLayout_11.addWidget(self.spinBox_62, 6, 2, 1, 1)

        self.spinBox_63 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_63.setObjectName(u"spinBox_63")

        self.gridLayout_11.addWidget(self.spinBox_63, 6, 3, 1, 1)

        self.spinBox_64 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_64.setObjectName(u"spinBox_64")

        self.gridLayout_11.addWidget(self.spinBox_64, 6, 4, 1, 1)

        self.spinBox_65 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_65.setObjectName(u"spinBox_65")

        self.gridLayout_11.addWidget(self.spinBox_65, 7, 1, 1, 1)

        self.spinBox_66 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_66.setObjectName(u"spinBox_66")

        self.gridLayout_11.addWidget(self.spinBox_66, 7, 2, 1, 1)

        self.spinBox_67 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_67.setObjectName(u"spinBox_67")

        self.gridLayout_11.addWidget(self.spinBox_67, 7, 3, 1, 1)

        self.spinBox_68 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_68.setObjectName(u"spinBox_68")

        self.gridLayout_11.addWidget(self.spinBox_68, 7, 4, 1, 1)

        self.spinBox_69 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_69.setObjectName(u"spinBox_69")

        self.gridLayout_11.addWidget(self.spinBox_69, 8, 1, 1, 1)

        self.spinBox_70 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_70.setObjectName(u"spinBox_70")

        self.gridLayout_11.addWidget(self.spinBox_70, 8, 2, 1, 1)

        self.spinBox_71 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_71.setObjectName(u"spinBox_71")

        self.gridLayout_11.addWidget(self.spinBox_71, 8, 3, 1, 1)

        self.spinBox_72 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_72.setObjectName(u"spinBox_72")

        self.gridLayout_11.addWidget(self.spinBox_72, 8, 4, 1, 1)

        self.spinBox_73 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_73.setObjectName(u"spinBox_73")

        self.gridLayout_11.addWidget(self.spinBox_73, 9, 1, 1, 1)

        self.spinBox_74 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_74.setObjectName(u"spinBox_74")

        self.gridLayout_11.addWidget(self.spinBox_74, 9, 2, 1, 1)

        self.spinBox_75 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_75.setObjectName(u"spinBox_75")

        self.gridLayout_11.addWidget(self.spinBox_75, 9, 3, 1, 1)

        self.spinBox_76 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_76.setObjectName(u"spinBox_76")

        self.gridLayout_11.addWidget(self.spinBox_76, 9, 4, 1, 1)

        self.spinBox_77 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_77.setObjectName(u"spinBox_77")

        self.gridLayout_11.addWidget(self.spinBox_77, 10, 1, 1, 1)

        self.spinBox_78 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_78.setObjectName(u"spinBox_78")

        self.gridLayout_11.addWidget(self.spinBox_78, 10, 2, 1, 1)

        self.spinBox_79 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_79.setObjectName(u"spinBox_79")

        self.gridLayout_11.addWidget(self.spinBox_79, 10, 3, 1, 1)

        self.spinBox_80 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox_80.setObjectName(u"spinBox_80")

        self.gridLayout_11.addWidget(self.spinBox_80, 10, 4, 1, 1)

        self.comboBox_14 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.setObjectName(u"comboBox_14")

        self.gridLayout_11.addWidget(self.comboBox_14, 2, 5, 1, 1)

        self.comboBox_15 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.setObjectName(u"comboBox_15")

        self.gridLayout_11.addWidget(self.comboBox_15, 3, 5, 1, 1)

        self.comboBox_16 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.setObjectName(u"comboBox_16")

        self.gridLayout_11.addWidget(self.comboBox_16, 4, 5, 1, 1)

        self.comboBox_17 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.setObjectName(u"comboBox_17")

        self.gridLayout_11.addWidget(self.comboBox_17, 5, 5, 1, 1)

        self.comboBox_18 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.setObjectName(u"comboBox_18")

        self.gridLayout_11.addWidget(self.comboBox_18, 6, 5, 1, 1)

        self.comboBox_19 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.setObjectName(u"comboBox_19")

        self.gridLayout_11.addWidget(self.comboBox_19, 7, 5, 1, 1)

        self.comboBox_20 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.setObjectName(u"comboBox_20")

        self.gridLayout_11.addWidget(self.comboBox_20, 8, 5, 1, 1)

        self.comboBox_21 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.setObjectName(u"comboBox_21")

        self.gridLayout_11.addWidget(self.comboBox_21, 9, 5, 1, 1)

        self.comboBox_22 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.setObjectName(u"comboBox_22")

        self.gridLayout_11.addWidget(self.comboBox_22, 10, 5, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_11)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.dio_scroll_area.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.dio_scroll_area)

        self.tabWidget.addTab(self.dio_tab, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 1, 1, 1)

        SettingsWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(SettingsWindow)
        self.toolBar.setObjectName(u"toolBar")
        SettingsWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
#if QT_CONFIG(shortcut)
        self.config_path_label.setBuddy(self.config_path_edit)
        self.data_path_label.setBuddy(self.data_path_edit)
        self.label_2.setBuddy(self.spinBox)
        self.label.setBuddy(self.doubleSpinBox)
        self.label_33.setBuddy(self.spinBox_25)
        self.label_32.setBuddy(self.comboBox)
        self.label_35.setBuddy(self.spinBox_43)
        self.label_34.setBuddy(self.spinBox_26)
        self.label_36.setBuddy(self.spinBox_44)
        self.label_40.setBuddy(self.acous__ch1_enbl_ckbox)
        self.label_56.setBuddy(self.acous__ch3_enbl_ckbox)
        self.label_58.setBuddy(self.checkBox_14)
        self.label_59.setBuddy(self.checkBox_15)
        self.label_57.setBuddy(self.checkBox_13)
        self.label_61.setBuddy(self.checkBox_17)
        self.label_52.setBuddy(self.acous__ch2_enbl_ckbox)
        self.label_60.setBuddy(self.checkBox_16)
        self.label_24.setBuddy(self.spinBox_21)
        self.label_22.setBuddy(self.lineEdit_10)
        self.label_25.setBuddy(self.spinBox_22)
        self.label_23.setBuddy(self.lineEdit_11)
        self.label_26.setBuddy(self.spinBox_23)
        self.label_27.setBuddy(self.spinBox_24)
#endif // QT_CONFIG(shortcut)

        self.toolBar.addAction(self.actionClose_Window)
        self.toolBar.addAction(self.actionReloadConfig)
        self.toolBar.addAction(self.actionApply_config)
        self.toolBar.addAction(self.actionSaveConfig)

        self.retranslateUi(SettingsWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"Settings", None))
        self.actionReloadConfig.setText(QCoreApplication.translate("SettingsWindow", u"Reload config", None))
#if QT_CONFIG(tooltip)
        self.actionReloadConfig.setToolTip(QCoreApplication.translate("SettingsWindow", u"Reload config", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionReloadConfig.setShortcut(QCoreApplication.translate("SettingsWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionSaveConfig.setText(QCoreApplication.translate("SettingsWindow", u"Save config", None))
#if QT_CONFIG(tooltip)
        self.actionSaveConfig.setToolTip(QCoreApplication.translate("SettingsWindow", u"Save config to file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSaveConfig.setShortcut(QCoreApplication.translate("SettingsWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionApply_config.setText(QCoreApplication.translate("SettingsWindow", u"Apply config", None))
#if QT_CONFIG(tooltip)
        self.actionApply_config.setToolTip(QCoreApplication.translate("SettingsWindow", u"Apply config", None))
#endif // QT_CONFIG(tooltip)
        self.actionClose_Window.setText(QCoreApplication.translate("SettingsWindow", u"Close Window", None))
#if QT_CONFIG(tooltip)
        self.actionClose_Window.setToolTip(QCoreApplication.translate("SettingsWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionClose_Window.setShortcut(QCoreApplication.translate("SettingsWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.config_path_label.setText(QCoreApplication.translate("SettingsWindow", u"Config Path", None))
        self.data_path_label.setText(QCoreApplication.translate("SettingsWindow", u"Data Path", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.files_tab), QCoreApplication.translate("SettingsWindow", u"Files", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWindow", u"Max Number of Events", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"Max Event Time", None))
        self.doubleSpinBox.setSuffix(QCoreApplication.translate("SettingsWindow", u"s", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.run_tab), QCoreApplication.translate("SettingsWindow", u"Run", None))
        self.label_31.setText(QCoreApplication.translate("SettingsWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sipm_tab), QCoreApplication.translate("SettingsWindow", u"SiPM", None))
        self.label_33.setText(QCoreApplication.translate("SettingsWindow", u"Pre Trig Length", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("SettingsWindow", u"100 MS/s", None))

        self.label_32.setText(QCoreApplication.translate("SettingsWindow", u"Sample Rate", None))
        self.label_35.setText(QCoreApplication.translate("SettingsWindow", u"Trig Timeout", None))
        self.label_34.setText(QCoreApplication.translate("SettingsWindow", u"Post Trig Length", None))
        self.label_36.setText(QCoreApplication.translate("SettingsWindow", u"Trig Delay", None))
        self.spinBox_84.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.label_37.setText(QCoreApplication.translate("SettingsWindow", u"Range", None))
        self.spinBox_90.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.label_40.setText(QCoreApplication.translate("SettingsWindow", u"Ch 1", None))
        self.checkBox_19.setText("")
        self.comboBox_9.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.spinBox_86.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.spinBox_92.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.label_62.setText(QCoreApplication.translate("SettingsWindow", u"Trigger", None))
        self.checkBox_25.setText("")
        self.label_56.setText(QCoreApplication.translate("SettingsWindow", u"Ch 3", None))
        self.spinBox_82.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.checkBox_13.setText("")
        self.checkBox_22.setText("")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.comboBox_4.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.label_58.setText(QCoreApplication.translate("SettingsWindow", u"Ch 5", None))
        self.label_39.setText(QCoreApplication.translate("SettingsWindow", u"Enabled", None))
        self.checkBox_21.setText("")
        self.spinBox_95.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.checkBox_23.setText("")
        self.checkBox_24.setText("")
        self.label_63.setText(QCoreApplication.translate("SettingsWindow", u"Polarity", None))
        self.acous__ch1_enbl_ckbox.setText("")
        self.comboBox_7.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.label_64.setText(QCoreApplication.translate("SettingsWindow", u"Threshold", None))
        self.spinBox_91.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.label_38.setText(QCoreApplication.translate("SettingsWindow", u"DC Offset", None))
        self.spinBox_85.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.acous__ch3_enbl_ckbox.setText("")
        self.spinBox_88.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.checkBox_20.setText("")
        self.label_59.setText(QCoreApplication.translate("SettingsWindow", u"Ch 6", None))
        self.spinBox_93.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.checkBox_14.setText("")
        self.checkBox_15.setText("")
        self.spinBox_87.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.spinBox_89.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.label_57.setText(QCoreApplication.translate("SettingsWindow", u"Ch 4", None))
        self.acous__ch2_enbl_ckbox.setText("")
        self.checkBox_18.setText("")
        self.spinBox_96.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.label_61.setText(QCoreApplication.translate("SettingsWindow", u"Ch 8", None))
        self.spinBox_94.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.label_52.setText(QCoreApplication.translate("SettingsWindow", u"Ch 2", None))
        self.spinBox_83.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.label_60.setText(QCoreApplication.translate("SettingsWindow", u"Ch 7", None))
        self.spinBox_81.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.checkBox_16.setText("")
        self.checkBox_17.setText("")
        self.comboBox_8.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.label_65.setText(QCoreApplication.translate("SettingsWindow", u"Ext", None))
        self.checkBox_26.setText("")
        self.comboBox_13.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.comboBox_13.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.acoustics_tab), QCoreApplication.translate("SettingsWindow", u"Acoustics", None))
        self.label_17.setText(QCoreApplication.translate("SettingsWindow", u"State Comm Pin", None))
        self.label_29.setText(QCoreApplication.translate("SettingsWindow", u"Config Path", None))
        self.label_18.setText(QCoreApplication.translate("SettingsWindow", u"Trig Latch Pin", None))
        self.lineEdit_15.setText("")
        self.lineEdit_7.setText("")
        self.label_7.setText(QCoreApplication.translate("SettingsWindow", u"Post-Trig Length", None))
        self.doubleSpinBox_4.setSuffix(QCoreApplication.translate("SettingsWindow", u"s", None))
        self.label_11.setText(QCoreApplication.translate("SettingsWindow", u"Cam 3", None))
        self.doubleSpinBox_3.setSuffix(QCoreApplication.translate("SettingsWindow", u"s", None))
        self.label_20.setText(QCoreApplication.translate("SettingsWindow", u"Trigger Pin", None))
        self.comboBox_10.setItemText(0, QCoreApplication.translate("SettingsWindow", u"png", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("SettingsWindow", u"jpg", None))

        self.label_19.setText(QCoreApplication.translate("SettingsWindow", u"State Pin", None))
        self.label_9.setText(QCoreApplication.translate("SettingsWindow", u"Cam 1", None))
        self.label_30.setText(QCoreApplication.translate("SettingsWindow", u"Data Path", None))
        self.label_21.setText(QCoreApplication.translate("SettingsWindow", u"IP Address", None))
        self.lineEdit_14.setText("")
        self.label_10.setText(QCoreApplication.translate("SettingsWindow", u"Cam 2", None))
        self.label_6.setText(QCoreApplication.translate("SettingsWindow", u"ADC Threshold", None))
        self.label_14.setText(QCoreApplication.translate("SettingsWindow", u"Image Format", None))
        self.label_3.setText(QCoreApplication.translate("SettingsWindow", u"Trig Enable Time", None))
        self.label_4.setText(QCoreApplication.translate("SettingsWindow", u"Exposure", None))
        self.label_8.setText(QCoreApplication.translate("SettingsWindow", u"Pixel Treshold", None))
        self.doubleSpinBox_2.setSuffix(QCoreApplication.translate("SettingsWindow", u"s", None))
        self.label_13.setText(QCoreApplication.translate("SettingsWindow", u"Mode", None))
        self.label_16.setText(QCoreApplication.translate("SettingsWindow", u"Trig Enable Pin", None))
        self.label_15.setText(QCoreApplication.translate("SettingsWindow", u"Date Format", None))
        self.label_5.setText(QCoreApplication.translate("SettingsWindow", u"Buffer Length", None))
        self.comboBox_11.setItemText(0, QCoreApplication.translate("SettingsWindow", u"png", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("SettingsWindow", u"jpg", None))

        self.comboBox_12.setItemText(0, QCoreApplication.translate("SettingsWindow", u"png", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("SettingsWindow", u"jpg", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cam_tab), QCoreApplication.translate("SettingsWindow", u"Camera", None))
        self.label_12.setText(QCoreApplication.translate("SettingsWindow", u"Trig FIFO Arduino", None))
        self.label_24.setText(QCoreApplication.translate("SettingsWindow", u"Trig Reset Pin", None))
        self.label_22.setText(QCoreApplication.translate("SettingsWindow", u"Trig In Pins", None))
        self.label_25.setText(QCoreApplication.translate("SettingsWindow", u"Trig Or Pin", None))
        self.label_23.setText(QCoreApplication.translate("SettingsWindow", u"Trig Latch Pins", None))
        self.label_26.setText(QCoreApplication.translate("SettingsWindow", u"On-Time Pin", None))
        self.label_27.setText(QCoreApplication.translate("SettingsWindow", u"Heartbeat Pin", None))
        self.label_28.setText(QCoreApplication.translate("SettingsWindow", u"Gate Generator Arduino", None))
        self.label_47.setText(QCoreApplication.translate("SettingsWindow", u"Wave 1", None))
        self.label_54.setText(QCoreApplication.translate("SettingsWindow", u"Wave 8", None))
        self.label_51.setText(QCoreApplication.translate("SettingsWindow", u"Wave 6", None))
        self.label_43.setText(QCoreApplication.translate("SettingsWindow", u"Duty", None))
        self.label_46.setText(QCoreApplication.translate("SettingsWindow", u"Period", None))
        self.spinBox_56.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.label_50.setText(QCoreApplication.translate("SettingsWindow", u"Wave 5", None))
        self.label_49.setText(QCoreApplication.translate("SettingsWindow", u"Wave 4", None))
        self.label_53.setText(QCoreApplication.translate("SettingsWindow", u"Wave 7", None))
        self.label_45.setText(QCoreApplication.translate("SettingsWindow", u"Polarity", None))
        self.label_42.setText(QCoreApplication.translate("SettingsWindow", u"Pin", None))
        self.label_41.setText(QCoreApplication.translate("SettingsWindow", u"Wave 2", None))
        self.spinBox_45.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.label_44.setText(QCoreApplication.translate("SettingsWindow", u"Phase", None))
        self.spinBox_51.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.label_48.setText(QCoreApplication.translate("SettingsWindow", u"Wave 3", None))
        self.label_55.setText(QCoreApplication.translate("SettingsWindow", u"Wave 9", None))
        self.spinBox_59.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.spinBox_64.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.spinBox_68.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.spinBox_72.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.spinBox_76.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.spinBox_80.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.comboBox_14.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.comboBox_14.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.comboBox_15.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.comboBox_15.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.comboBox_16.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.comboBox_16.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.comboBox_17.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.comboBox_17.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.comboBox_18.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.comboBox_18.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.comboBox_19.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.comboBox_19.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.comboBox_20.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.comboBox_20.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.comboBox_21.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.comboBox_21.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.comboBox_22.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.comboBox_22.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dio_tab), QCoreApplication.translate("SettingsWindow", u"DIO", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"toolBar", None))
    # retranslateUi

