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
    QToolBar, QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(400, 503)
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
        self.actionClose_Window.setMenuRole(QAction.QuitRole)
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
        self.general_tab = QWidget()
        self.general_tab.setObjectName(u"general_tab")
        self.verticalLayout_4 = QVBoxLayout(self.general_tab)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.files_scroll_area = QScrollArea(self.general_tab)
        self.files_scroll_area.setObjectName(u"files_scroll_area")
        self.files_scroll_area.setFrameShape(QFrame.NoFrame)
        self.files_scroll_area.setFrameShadow(QFrame.Plain)
        self.files_scroll_area.setLineWidth(0)
        self.files_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 388, 434))
        self.scrollAreaWidgetContents_5.setMaximumSize(QSize(1000, 16777215))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.config_path_edit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.config_path_edit.setObjectName(u"config_path_edit")

        self.gridLayout_3.addWidget(self.config_path_edit, 0, 2, 1, 1)

        self.config_path_label = QLabel(self.scrollAreaWidgetContents_5)
        self.config_path_label.setObjectName(u"config_path_label")
        self.config_path_label.setMinimumSize(QSize(0, 0))
        self.config_path_label.setLineWidth(0)
        self.config_path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.config_path_label, 0, 0, 1, 1)

        self.data_dir_label = QLabel(self.scrollAreaWidgetContents_5)
        self.data_dir_label.setObjectName(u"data_dir_label")
        self.data_dir_label.setLineWidth(0)
        self.data_dir_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.data_dir_label, 2, 0, 1, 1)

        self.data_dir_edit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.data_dir_edit.setObjectName(u"data_dir_edit")

        self.gridLayout_3.addWidget(self.data_dir_edit, 2, 2, 1, 1)

        self.config_path_but = QToolButton(self.scrollAreaWidgetContents_5)
        self.config_path_but.setObjectName(u"config_path_but")

        self.gridLayout_3.addWidget(self.config_path_but, 0, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 336, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 4, 2, 1, 1)

        self.data_dir_but = QToolButton(self.scrollAreaWidgetContents_5)
        self.data_dir_but.setObjectName(u"data_dir_but")

        self.gridLayout_3.addWidget(self.data_dir_but, 2, 3, 1, 1)

        self.log_path_label = QLabel(self.scrollAreaWidgetContents_5)
        self.log_path_label.setObjectName(u"log_path_label")
        self.log_path_label.setLineWidth(0)
        self.log_path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.log_path_label, 1, 0, 1, 1)

        self.log_path_edit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.log_path_edit.setObjectName(u"log_path_edit")

        self.gridLayout_3.addWidget(self.log_path_edit, 1, 2, 1, 1)

        self.log_path_but = QToolButton(self.scrollAreaWidgetContents_5)
        self.log_path_but.setObjectName(u"log_path_but")

        self.gridLayout_3.addWidget(self.log_path_but, 1, 3, 1, 1)

        self.files_scroll_area.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_4.addWidget(self.files_scroll_area)

        self.tabWidget.addTab(self.general_tab, "")
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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 388, 434))
        self.scrollAreaWidgetContents_4.setMaximumSize(QSize(1000, 16777215))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.max_num_ev_label = QLabel(self.scrollAreaWidgetContents_4)
        self.max_num_ev_label.setObjectName(u"max_num_ev_label")
        self.max_num_ev_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.max_num_ev_label, 1, 2, 1, 1)

        self.comboBox_23 = QComboBox(self.scrollAreaWidgetContents_4)
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.setObjectName(u"comboBox_23")
        self.comboBox_23.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBox_23, 0, 1, 1, 1)

        self.max_ev_time_box = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.max_ev_time_box.setObjectName(u"max_ev_time_box")

        self.gridLayout_2.addWidget(self.max_ev_time_box, 1, 1, 1, 1)

        self.max_ev_time_label = QLabel(self.scrollAreaWidgetContents_4)
        self.max_ev_time_label.setObjectName(u"max_ev_time_label")
        self.max_ev_time_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.max_ev_time_label, 1, 0, 1, 1)

        self.max_ev_time_label_2 = QLabel(self.scrollAreaWidgetContents_4)
        self.max_ev_time_label_2.setObjectName(u"max_ev_time_label_2")
        self.max_ev_time_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.max_ev_time_label_2, 0, 0, 1, 1)

        self.max_num_ev_box = QSpinBox(self.scrollAreaWidgetContents_4)
        self.max_num_ev_box.setObjectName(u"max_num_ev_box")
        self.max_num_ev_box.setMinimum(1)
        self.max_num_ev_box.setMaximum(1000)
        self.max_num_ev_box.setValue(100)

        self.gridLayout_2.addWidget(self.max_num_ev_box, 1, 3, 1, 1)

        self.max_ev_time_label_3 = QLabel(self.scrollAreaWidgetContents_4)
        self.max_ev_time_label_3.setObjectName(u"max_ev_time_label_3")
        self.max_ev_time_label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.max_ev_time_label_3, 0, 2, 1, 1)

        self.max_num_ev_box_2 = QSpinBox(self.scrollAreaWidgetContents_4)
        self.max_num_ev_box_2.setObjectName(u"max_num_ev_box_2")
        self.max_num_ev_box_2.setMinimum(1)
        self.max_num_ev_box_2.setMaximum(1000)
        self.max_num_ev_box_2.setValue(25)

        self.gridLayout_2.addWidget(self.max_num_ev_box_2, 0, 3, 1, 1)

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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 388, 434))
        self.scrollAreaWidgetContents_2.setMaximumSize(QSize(1000, 16777215))
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
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 388, 434))
        self.scrollAreaWidgetContents_6.setMaximumSize(QSize(1000, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.acous_general_grid = QGridLayout()
        self.acous_general_grid.setSpacing(3)
        self.acous_general_grid.setObjectName(u"acous_general_grid")
        self.acous_pre_trig_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_pre_trig_label.setObjectName(u"acous_pre_trig_label")
        self.acous_pre_trig_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_general_grid.addWidget(self.acous_pre_trig_label, 1, 0, 1, 1)

        self.acous_sample_rate_box = QComboBox(self.scrollAreaWidgetContents_6)
        self.acous_sample_rate_box.addItem("")
        self.acous_sample_rate_box.setObjectName(u"acous_sample_rate_box")

        self.acous_general_grid.addWidget(self.acous_sample_rate_box, 0, 1, 1, 3)

        self.acous_sample_rate_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_sample_rate_label.setObjectName(u"acous_sample_rate_label")
        self.acous_sample_rate_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_general_grid.addWidget(self.acous_sample_rate_label, 0, 0, 1, 1)

        self.acous_pre_trig_box = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_pre_trig_box.setObjectName(u"acous_pre_trig_box")

        self.acous_general_grid.addWidget(self.acous_pre_trig_box, 1, 1, 1, 1)

        self.acous_trig_timeout_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_trig_timeout_label.setObjectName(u"acous_trig_timeout_label")
        self.acous_trig_timeout_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_general_grid.addWidget(self.acous_trig_timeout_label, 1, 2, 1, 1)

        self.acous_trig_timeout_box = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_trig_timeout_box.setObjectName(u"acous_trig_timeout_box")

        self.acous_general_grid.addWidget(self.acous_trig_timeout_box, 1, 3, 1, 1)

        self.acous_post_trig_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_post_trig_label.setObjectName(u"acous_post_trig_label")
        self.acous_post_trig_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_general_grid.addWidget(self.acous_post_trig_label, 2, 0, 1, 1)

        self.acous_post_trig_box = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_post_trig_box.setObjectName(u"acous_post_trig_box")

        self.acous_general_grid.addWidget(self.acous_post_trig_box, 2, 1, 1, 1)

        self.acous_trig_delay_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_trig_delay_label.setObjectName(u"acous_trig_delay_label")
        self.acous_trig_delay_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_general_grid.addWidget(self.acous_trig_delay_label, 2, 2, 1, 1)

        self.acous_trig_delay_box = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_trig_delay_box.setObjectName(u"acous_trig_delay_box")

        self.acous_general_grid.addWidget(self.acous_trig_delay_box, 2, 3, 1, 1)


        self.verticalLayout_8.addLayout(self.acous_general_grid)

        self.acous_line = QFrame(self.scrollAreaWidgetContents_6)
        self.acous_line.setObjectName(u"acous_line")
        self.acous_line.setFrameShape(QFrame.HLine)
        self.acous_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.acous_line)

        self.acous_per_ch_grid = QGridLayout()
        self.acous_per_ch_grid.setSpacing(3)
        self.acous_per_ch_grid.setObjectName(u"acous_per_ch_grid")
        self.acous_enable_ch7 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_enable_ch7.setObjectName(u"acous_enable_ch7")

        self.acous_per_ch_grid.addWidget(self.acous_enable_ch7, 7, 1, 1, 1)

        self.acous_enable_ch3 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_enable_ch3.setObjectName(u"acous_enable_ch3")

        self.acous_per_ch_grid.addWidget(self.acous_enable_ch3, 3, 1, 1, 1)

        self.acous_trig_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_trig_label.setObjectName(u"acous_trig_label")
        self.acous_trig_label.setAlignment(Qt.AlignCenter)

        self.acous_per_ch_grid.addWidget(self.acous_trig_label, 0, 4, 1, 1)

        self.acous_threshold_ch4 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_threshold_ch4.setObjectName(u"acous_threshold_ch4")

        self.acous_per_ch_grid.addWidget(self.acous_threshold_ch4, 4, 6, 1, 1)

        self.acous_polarity_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_polarity_label.setObjectName(u"acous_polarity_label")
        self.acous_polarity_label.setAlignment(Qt.AlignCenter)

        self.acous_per_ch_grid.addWidget(self.acous_polarity_label, 0, 5, 1, 1)

        self.acous_ch5_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_ch5_label.setObjectName(u"acous_ch5_label")
        self.acous_ch5_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.acous_ch5_label, 5, 0, 1, 1)

        self.acous_polarity_ch4 = QComboBox(self.scrollAreaWidgetContents_6)
        self.acous_polarity_ch4.addItem("")
        self.acous_polarity_ch4.addItem("")
        self.acous_polarity_ch4.setObjectName(u"acous_polarity_ch4")
        self.acous_polarity_ch4.setIconSize(QSize(16, 16))
        self.acous_polarity_ch4.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.acous_polarity_ch4, 4, 5, 1, 1)

        self.acous_ch2_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_ch2_label.setObjectName(u"acous_ch2_label")
        self.acous_ch2_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.acous_ch2_label, 2, 0, 1, 1)

        self.acous_polarity_ch3 = QComboBox(self.scrollAreaWidgetContents_6)
        self.acous_polarity_ch3.addItem("")
        self.acous_polarity_ch3.addItem("")
        self.acous_polarity_ch3.setObjectName(u"acous_polarity_ch3")
        self.acous_polarity_ch3.setIconSize(QSize(16, 16))
        self.acous_polarity_ch3.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.acous_polarity_ch3, 3, 5, 1, 1)

        self.acous_polarity_ch5 = QComboBox(self.scrollAreaWidgetContents_6)
        self.acous_polarity_ch5.addItem("")
        self.acous_polarity_ch5.addItem("")
        self.acous_polarity_ch5.setObjectName(u"acous_polarity_ch5")
        self.acous_polarity_ch5.setIconSize(QSize(16, 16))
        self.acous_polarity_ch5.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.acous_polarity_ch5, 5, 5, 1, 1)

        self.acous_dc_offset_ch7 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_dc_offset_ch7.setObjectName(u"acous_dc_offset_ch7")

        self.acous_per_ch_grid.addWidget(self.acous_dc_offset_ch7, 7, 3, 1, 1)

        self.acous_range_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_range_label.setObjectName(u"acous_range_label")
        self.acous_range_label.setAlignment(Qt.AlignCenter)

        self.acous_per_ch_grid.addWidget(self.acous_range_label, 0, 2, 1, 1)

        self.acous_enable_ch4 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_enable_ch4.setObjectName(u"acous_enable_ch4")

        self.acous_per_ch_grid.addWidget(self.acous_enable_ch4, 4, 1, 1, 1)

        self.acous_trig_ch7 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_trig_ch7.setObjectName(u"acous_trig_ch7")

        self.acous_per_ch_grid.addWidget(self.acous_trig_ch7, 7, 4, 1, 1)

        self.acous_ch1_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_ch1_label.setObjectName(u"acous_ch1_label")
        self.acous_ch1_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.acous_ch1_label, 1, 0, 1, 1)

        self.acous_polarity_ext = QComboBox(self.scrollAreaWidgetContents_6)
        self.acous_polarity_ext.addItem("")
        self.acous_polarity_ext.addItem("")
        self.acous_polarity_ext.setObjectName(u"acous_polarity_ext")
        self.acous_polarity_ext.setIconSize(QSize(16, 16))
        self.acous_polarity_ext.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.acous_polarity_ext, 9, 5, 1, 1)

        self.acous_range_ch8 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_range_ch8.setObjectName(u"acous_range_ch8")

        self.acous_per_ch_grid.addWidget(self.acous_range_ch8, 8, 2, 1, 1)

        self.acous_ch6_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_ch6_label.setObjectName(u"acous_ch6_label")
        self.acous_ch6_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.acous_ch6_label, 6, 0, 1, 1)

        self.acous_polarity_ch8 = QComboBox(self.scrollAreaWidgetContents_6)
        self.acous_polarity_ch8.addItem("")
        self.acous_polarity_ch8.addItem("")
        self.acous_polarity_ch8.setObjectName(u"acous_polarity_ch8")
        self.acous_polarity_ch8.setIconSize(QSize(16, 16))
        self.acous_polarity_ch8.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.acous_polarity_ch8, 8, 5, 1, 1)

        self.acous_threshold_ch1 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_threshold_ch1.setObjectName(u"acous_threshold_ch1")

        self.acous_per_ch_grid.addWidget(self.acous_threshold_ch1, 1, 6, 1, 1)

        self.acous_dc_offset_ch4 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_dc_offset_ch4.setObjectName(u"acous_dc_offset_ch4")

        self.acous_per_ch_grid.addWidget(self.acous_dc_offset_ch4, 4, 3, 1, 1)

        self.acous_ch7_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_ch7_label.setObjectName(u"acous_ch7_label")
        self.acous_ch7_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.acous_ch7_label, 7, 0, 1, 1)

        self.acous_enable_ch2 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_enable_ch2.setObjectName(u"acous_enable_ch2")
        self.acous_enable_ch2.setStyleSheet(u"")

        self.acous_per_ch_grid.addWidget(self.acous_enable_ch2, 2, 1, 1, 1)

        self.acous_dc_offset_ch8 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_dc_offset_ch8.setObjectName(u"acous_dc_offset_ch8")

        self.acous_per_ch_grid.addWidget(self.acous_dc_offset_ch8, 8, 3, 1, 1)

        self.acous_threshold_ch3 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_threshold_ch3.setObjectName(u"acous_threshold_ch3")

        self.acous_per_ch_grid.addWidget(self.acous_threshold_ch3, 3, 6, 1, 1)

        self.acous_trig_ch6 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_trig_ch6.setObjectName(u"acous_trig_ch6")

        self.acous_per_ch_grid.addWidget(self.acous_trig_ch6, 6, 4, 1, 1)

        self.acous_trig_ext = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_trig_ext.setObjectName(u"acous_trig_ext")

        self.acous_per_ch_grid.addWidget(self.acous_trig_ext, 9, 4, 1, 1)

        self.acous_range_ch3 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_range_ch3.setObjectName(u"acous_range_ch3")

        self.acous_per_ch_grid.addWidget(self.acous_range_ch3, 3, 2, 1, 1)

        self.acous_polarity_ch6 = QComboBox(self.scrollAreaWidgetContents_6)
        self.acous_polarity_ch6.addItem("")
        self.acous_polarity_ch6.addItem("")
        self.acous_polarity_ch6.setObjectName(u"acous_polarity_ch6")
        self.acous_polarity_ch6.setIconSize(QSize(16, 16))
        self.acous_polarity_ch6.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.acous_polarity_ch6, 6, 5, 1, 1)

        self.acous_threshold_ch7 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_threshold_ch7.setObjectName(u"acous_threshold_ch7")

        self.acous_per_ch_grid.addWidget(self.acous_threshold_ch7, 7, 6, 1, 1)

        self.acous_ch3_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_ch3_label.setObjectName(u"acous_ch3_label")
        self.acous_ch3_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.acous_ch3_label, 3, 0, 1, 1)

        self.acous_threshold_ch8 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_threshold_ch8.setObjectName(u"acous_threshold_ch8")

        self.acous_per_ch_grid.addWidget(self.acous_threshold_ch8, 8, 6, 1, 1)

        self.acous_range_ch6 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_range_ch6.setObjectName(u"acous_range_ch6")

        self.acous_per_ch_grid.addWidget(self.acous_range_ch6, 6, 2, 1, 1)

        self.acous_threshold_ch2 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_threshold_ch2.setObjectName(u"acous_threshold_ch2")

        self.acous_per_ch_grid.addWidget(self.acous_threshold_ch2, 2, 6, 1, 1)

        self.acous_trig_ch4 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_trig_ch4.setObjectName(u"acous_trig_ch4")

        self.acous_per_ch_grid.addWidget(self.acous_trig_ch4, 4, 4, 1, 1)

        self.acous_dc_offset_ch1 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_dc_offset_ch1.setObjectName(u"acous_dc_offset_ch1")

        self.acous_per_ch_grid.addWidget(self.acous_dc_offset_ch1, 1, 3, 1, 1)

        self.acous_trig_ch2 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_trig_ch2.setObjectName(u"acous_trig_ch2")

        self.acous_per_ch_grid.addWidget(self.acous_trig_ch2, 2, 4, 1, 1)

        self.acous_ch8_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_ch8_label.setObjectName(u"acous_ch8_label")
        self.acous_ch8_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.acous_ch8_label, 8, 0, 1, 1)

        self.acous_threshold_ext = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_threshold_ext.setObjectName(u"acous_threshold_ext")

        self.acous_per_ch_grid.addWidget(self.acous_threshold_ext, 9, 6, 1, 1)

        self.acous_dc_offset_ch5 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_dc_offset_ch5.setObjectName(u"acous_dc_offset_ch5")

        self.acous_per_ch_grid.addWidget(self.acous_dc_offset_ch5, 5, 3, 1, 1)

        self.acous_dc_offset_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_dc_offset_label.setObjectName(u"acous_dc_offset_label")
        self.acous_dc_offset_label.setAlignment(Qt.AlignCenter)

        self.acous_per_ch_grid.addWidget(self.acous_dc_offset_label, 0, 3, 1, 1)

        self.acous_polarity_ch2 = QComboBox(self.scrollAreaWidgetContents_6)
        self.acous_polarity_ch2.addItem("")
        self.acous_polarity_ch2.addItem("")
        self.acous_polarity_ch2.setObjectName(u"acous_polarity_ch2")
        self.acous_polarity_ch2.setIconSize(QSize(16, 16))
        self.acous_polarity_ch2.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.acous_polarity_ch2, 2, 5, 1, 1)

        self.acous_trig_ch8 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_trig_ch8.setObjectName(u"acous_trig_ch8")

        self.acous_per_ch_grid.addWidget(self.acous_trig_ch8, 8, 4, 1, 1)

        self.acous_enabled_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_enabled_label.setObjectName(u"acous_enabled_label")
        self.acous_enabled_label.setAlignment(Qt.AlignCenter)

        self.acous_per_ch_grid.addWidget(self.acous_enabled_label, 0, 1, 1, 1)

        self.acous_enable_ch5 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_enable_ch5.setObjectName(u"acous_enable_ch5")

        self.acous_per_ch_grid.addWidget(self.acous_enable_ch5, 5, 1, 1, 1)

        self.acous_range_ch2 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_range_ch2.setObjectName(u"acous_range_ch2")

        self.acous_per_ch_grid.addWidget(self.acous_range_ch2, 2, 2, 1, 1)

        self.acous_ch4_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_ch4_label.setObjectName(u"acous_ch4_label")
        self.acous_ch4_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.acous_ch4_label, 4, 0, 1, 1)

        self.acous_range_ch7 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_range_ch7.setObjectName(u"acous_range_ch7")

        self.acous_per_ch_grid.addWidget(self.acous_range_ch7, 7, 2, 1, 1)

        self.acous_trig_ch5 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_trig_ch5.setObjectName(u"acous_trig_ch5")

        self.acous_per_ch_grid.addWidget(self.acous_trig_ch5, 5, 4, 1, 1)

        self.acous_trig_ch3 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_trig_ch3.setObjectName(u"acous_trig_ch3")

        self.acous_per_ch_grid.addWidget(self.acous_trig_ch3, 3, 4, 1, 1)

        self.acous_dc_offset_ch2 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_dc_offset_ch2.setObjectName(u"acous_dc_offset_ch2")

        self.acous_per_ch_grid.addWidget(self.acous_dc_offset_ch2, 2, 3, 1, 1)

        self.acous_range_ch5 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_range_ch5.setObjectName(u"acous_range_ch5")

        self.acous_per_ch_grid.addWidget(self.acous_range_ch5, 5, 2, 1, 1)

        self.acous_threshold_ch5 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_threshold_ch5.setObjectName(u"acous_threshold_ch5")

        self.acous_per_ch_grid.addWidget(self.acous_threshold_ch5, 5, 6, 1, 1)

        self.acous_threshold_ch6 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_threshold_ch6.setObjectName(u"acous_threshold_ch6")

        self.acous_per_ch_grid.addWidget(self.acous_threshold_ch6, 6, 6, 1, 1)

        self.acous_polarity_ch7 = QComboBox(self.scrollAreaWidgetContents_6)
        self.acous_polarity_ch7.addItem("")
        self.acous_polarity_ch7.addItem("")
        self.acous_polarity_ch7.setObjectName(u"acous_polarity_ch7")
        self.acous_polarity_ch7.setIconSize(QSize(16, 16))
        self.acous_polarity_ch7.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.acous_polarity_ch7, 7, 5, 1, 1)

        self.acous_enable_ch8 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_enable_ch8.setObjectName(u"acous_enable_ch8")

        self.acous_per_ch_grid.addWidget(self.acous_enable_ch8, 8, 1, 1, 1)

        self.acous_range_ch1 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_range_ch1.setObjectName(u"acous_range_ch1")
        self.acous_range_ch1.setStepType(QAbstractSpinBox.DefaultStepType)

        self.acous_per_ch_grid.addWidget(self.acous_range_ch1, 1, 2, 1, 1)

        self.acous_range_ch4 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_range_ch4.setObjectName(u"acous_range_ch4")

        self.acous_per_ch_grid.addWidget(self.acous_range_ch4, 4, 2, 1, 1)

        self.acous_enable_ch6 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_enable_ch6.setObjectName(u"acous_enable_ch6")

        self.acous_per_ch_grid.addWidget(self.acous_enable_ch6, 6, 1, 1, 1)

        self.acous_enable_ch1 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_enable_ch1.setObjectName(u"acous_enable_ch1")
        self.acous_enable_ch1.setStyleSheet(u"")

        self.acous_per_ch_grid.addWidget(self.acous_enable_ch1, 1, 1, 1, 1)

        self.acous_threshold_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_threshold_label.setObjectName(u"acous_threshold_label")
        self.acous_threshold_label.setAlignment(Qt.AlignCenter)

        self.acous_per_ch_grid.addWidget(self.acous_threshold_label, 0, 6, 1, 1)

        self.acous_polarity_ch1 = QComboBox(self.scrollAreaWidgetContents_6)
        self.acous_polarity_ch1.addItem("")
        self.acous_polarity_ch1.addItem("")
        self.acous_polarity_ch1.setObjectName(u"acous_polarity_ch1")
        sizePolicy.setHeightForWidth(self.acous_polarity_ch1.sizePolicy().hasHeightForWidth())
        self.acous_polarity_ch1.setSizePolicy(sizePolicy)
        self.acous_polarity_ch1.setIconSize(QSize(16, 16))
        self.acous_polarity_ch1.setFrame(True)

        self.acous_per_ch_grid.addWidget(self.acous_polarity_ch1, 1, 5, 1, 1)

        self.acous_ext_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_ext_label.setObjectName(u"acous_ext_label")
        self.acous_ext_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.acous_ext_label, 9, 0, 1, 1)

        self.acous_trig_ch1 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.acous_trig_ch1.setObjectName(u"acous_trig_ch1")

        self.acous_per_ch_grid.addWidget(self.acous_trig_ch1, 1, 4, 1, 1)

        self.acous_dc_offset_ch3 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_dc_offset_ch3.setObjectName(u"acous_dc_offset_ch3")

        self.acous_per_ch_grid.addWidget(self.acous_dc_offset_ch3, 3, 3, 1, 1)

        self.acous_dc_offset_ch6 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_dc_offset_ch6.setObjectName(u"acous_dc_offset_ch6")

        self.acous_per_ch_grid.addWidget(self.acous_dc_offset_ch6, 6, 3, 1, 1)

        self.acous_per_ch_grid.setColumnStretch(0, 1)
        self.acous_per_ch_grid.setColumnStretch(1, 1)
        self.acous_per_ch_grid.setColumnStretch(2, 1)
        self.acous_per_ch_grid.setColumnStretch(3, 1)
        self.acous_per_ch_grid.setColumnStretch(4, 1)
        self.acous_per_ch_grid.setColumnStretch(5, 1)
        self.acous_per_ch_grid.setColumnStretch(6, 1)

        self.verticalLayout_8.addLayout(self.acous_per_ch_grid)

        self.acous_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.acous_spacer)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 388, 434))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(1000, 16777215))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.state_comm_pin_label = QLabel(self.scrollAreaWidgetContents)
        self.state_comm_pin_label.setObjectName(u"state_comm_pin_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.state_comm_pin_label.sizePolicy().hasHeightForWidth())
        self.state_comm_pin_label.setSizePolicy(sizePolicy1)
        self.state_comm_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.state_comm_pin_label, 18, 0, 1, 1)

        self.mode_cam3 = QSpinBox(self.scrollAreaWidgetContents)
        self.mode_cam3.setObjectName(u"mode_cam3")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mode_cam3.sizePolicy().hasHeightForWidth())
        self.mode_cam3.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.mode_cam3, 4, 3, 1, 1)

        self.trig_pin_cam_1 = QSpinBox(self.scrollAreaWidgetContents)
        self.trig_pin_cam_1.setObjectName(u"trig_pin_cam_1")
        sizePolicy2.setHeightForWidth(self.trig_pin_cam_1.sizePolicy().hasHeightForWidth())
        self.trig_pin_cam_1.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.trig_pin_cam_1, 23, 1, 1, 1)

        self.config_path_label_2 = QLabel(self.scrollAreaWidgetContents)
        self.config_path_label_2.setObjectName(u"config_path_label_2")
        sizePolicy1.setHeightForWidth(self.config_path_label_2.sizePolicy().hasHeightForWidth())
        self.config_path_label_2.setSizePolicy(sizePolicy1)
        self.config_path_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.config_path_label_2, 1, 0, 1, 1)

        self.post_trig_len_cam1 = QSpinBox(self.scrollAreaWidgetContents)
        self.post_trig_len_cam1.setObjectName(u"post_trig_len_cam1")
        sizePolicy2.setHeightForWidth(self.post_trig_len_cam1.sizePolicy().hasHeightForWidth())
        self.post_trig_len_cam1.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.post_trig_len_cam1, 11, 1, 1, 1)

        self.trig_latch_pin_label = QLabel(self.scrollAreaWidgetContents)
        self.trig_latch_pin_label.setObjectName(u"trig_latch_pin_label")
        sizePolicy1.setHeightForWidth(self.trig_latch_pin_label.sizePolicy().hasHeightForWidth())
        self.trig_latch_pin_label.setSizePolicy(sizePolicy1)
        self.trig_latch_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.trig_latch_pin_label, 21, 0, 1, 1)

        self.trig_pin_cam3 = QSpinBox(self.scrollAreaWidgetContents)
        self.trig_pin_cam3.setObjectName(u"trig_pin_cam3")
        sizePolicy2.setHeightForWidth(self.trig_pin_cam3.sizePolicy().hasHeightForWidth())
        self.trig_pin_cam3.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.trig_pin_cam3, 23, 3, 1, 1)

        self.config_path_cam1 = QLineEdit(self.scrollAreaWidgetContents)
        self.config_path_cam1.setObjectName(u"config_path_cam1")

        self.gridLayout_5.addWidget(self.config_path_cam1, 1, 1, 1, 1)

        self.ip_addr_cam1 = QLineEdit(self.scrollAreaWidgetContents)
        self.ip_addr_cam1.setObjectName(u"ip_addr_cam1")

        self.gridLayout_5.addWidget(self.ip_addr_cam1, 3, 1, 1, 1)

        self.date_format_cam3 = QLineEdit(self.scrollAreaWidgetContents)
        self.date_format_cam3.setObjectName(u"date_format_cam3")

        self.gridLayout_5.addWidget(self.date_format_cam3, 17, 3, 1, 1)

        self.exposure_cam3 = QSpinBox(self.scrollAreaWidgetContents)
        self.exposure_cam3.setObjectName(u"exposure_cam3")
        sizePolicy2.setHeightForWidth(self.exposure_cam3.sizePolicy().hasHeightForWidth())
        self.exposure_cam3.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.exposure_cam3, 9, 3, 1, 1)

        self.data_path_cam2 = QLineEdit(self.scrollAreaWidgetContents)
        self.data_path_cam2.setObjectName(u"data_path_cam2")

        self.gridLayout_5.addWidget(self.data_path_cam2, 2, 2, 1, 1)

        self.post_trig_len_label = QLabel(self.scrollAreaWidgetContents)
        self.post_trig_len_label.setObjectName(u"post_trig_len_label")
        sizePolicy1.setHeightForWidth(self.post_trig_len_label.sizePolicy().hasHeightForWidth())
        self.post_trig_len_label.setSizePolicy(sizePolicy1)
        self.post_trig_len_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.post_trig_len_label, 11, 0, 1, 1)

        self.trig_wait_cam3 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.trig_wait_cam3.setObjectName(u"trig_wait_cam3")
        sizePolicy2.setHeightForWidth(self.trig_wait_cam3.sizePolicy().hasHeightForWidth())
        self.trig_wait_cam3.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.trig_wait_cam3, 8, 3, 1, 1)

        self.cam3_label = QLabel(self.scrollAreaWidgetContents)
        self.cam3_label.setObjectName(u"cam3_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cam3_label.sizePolicy().hasHeightForWidth())
        self.cam3_label.setSizePolicy(sizePolicy3)
        self.cam3_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.cam3_label, 0, 3, 1, 1)

        self.trig_wait_cam2 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.trig_wait_cam2.setObjectName(u"trig_wait_cam2")
        sizePolicy2.setHeightForWidth(self.trig_wait_cam2.sizePolicy().hasHeightForWidth())
        self.trig_wait_cam2.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.trig_wait_cam2, 8, 2, 1, 1)

        self.trig_pin_label = QLabel(self.scrollAreaWidgetContents)
        self.trig_pin_label.setObjectName(u"trig_pin_label")
        sizePolicy1.setHeightForWidth(self.trig_pin_label.sizePolicy().hasHeightForWidth())
        self.trig_pin_label.setSizePolicy(sizePolicy1)
        self.trig_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.trig_pin_label, 23, 0, 1, 1)

        self.image_format_cam1 = QComboBox(self.scrollAreaWidgetContents)
        self.image_format_cam1.addItem("")
        self.image_format_cam1.addItem("")
        self.image_format_cam1.setObjectName(u"image_format_cam1")

        self.gridLayout_5.addWidget(self.image_format_cam1, 16, 1, 1, 1)

        self.pix_threshold_cam2 = QSpinBox(self.scrollAreaWidgetContents)
        self.pix_threshold_cam2.setObjectName(u"pix_threshold_cam2")
        sizePolicy2.setHeightForWidth(self.pix_threshold_cam2.sizePolicy().hasHeightForWidth())
        self.pix_threshold_cam2.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.pix_threshold_cam2, 13, 2, 1, 1)

        self.state_pin_label = QLabel(self.scrollAreaWidgetContents)
        self.state_pin_label.setObjectName(u"state_pin_label")
        sizePolicy1.setHeightForWidth(self.state_pin_label.sizePolicy().hasHeightForWidth())
        self.state_pin_label.setSizePolicy(sizePolicy1)
        self.state_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.state_pin_label, 22, 0, 1, 1)

        self.cam1_label = QLabel(self.scrollAreaWidgetContents)
        self.cam1_label.setObjectName(u"cam1_label")
        sizePolicy3.setHeightForWidth(self.cam1_label.sizePolicy().hasHeightForWidth())
        self.cam1_label.setSizePolicy(sizePolicy3)
        self.cam1_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.cam1_label, 0, 1, 1, 1)

        self.state_comm_pin_cam3 = QSpinBox(self.scrollAreaWidgetContents)
        self.state_comm_pin_cam3.setObjectName(u"state_comm_pin_cam3")
        sizePolicy2.setHeightForWidth(self.state_comm_pin_cam3.sizePolicy().hasHeightForWidth())
        self.state_comm_pin_cam3.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.state_comm_pin_cam3, 18, 3, 1, 1)

        self.config_path_cam2 = QLineEdit(self.scrollAreaWidgetContents)
        self.config_path_cam2.setObjectName(u"config_path_cam2")

        self.gridLayout_5.addWidget(self.config_path_cam2, 1, 2, 1, 1)

        self.data_path_label = QLabel(self.scrollAreaWidgetContents)
        self.data_path_label.setObjectName(u"data_path_label")
        sizePolicy1.setHeightForWidth(self.data_path_label.sizePolicy().hasHeightForWidth())
        self.data_path_label.setSizePolicy(sizePolicy1)
        self.data_path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.data_path_label, 2, 0, 1, 1)

        self.ip_addr_label = QLabel(self.scrollAreaWidgetContents)
        self.ip_addr_label.setObjectName(u"ip_addr_label")
        sizePolicy1.setHeightForWidth(self.ip_addr_label.sizePolicy().hasHeightForWidth())
        self.ip_addr_label.setSizePolicy(sizePolicy1)
        self.ip_addr_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.ip_addr_label, 3, 0, 1, 1)

        self.ip_addr_cam3 = QLineEdit(self.scrollAreaWidgetContents)
        self.ip_addr_cam3.setObjectName(u"ip_addr_cam3")

        self.gridLayout_5.addWidget(self.ip_addr_cam3, 3, 3, 1, 1)

        self.cam2_label = QLabel(self.scrollAreaWidgetContents)
        self.cam2_label.setObjectName(u"cam2_label")
        sizePolicy3.setHeightForWidth(self.cam2_label.sizePolicy().hasHeightForWidth())
        self.cam2_label.setSizePolicy(sizePolicy3)
        self.cam2_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.cam2_label, 0, 2, 1, 1)

        self.adc_threshold_cam3 = QSpinBox(self.scrollAreaWidgetContents)
        self.adc_threshold_cam3.setObjectName(u"adc_threshold_cam3")
        sizePolicy2.setHeightForWidth(self.adc_threshold_cam3.sizePolicy().hasHeightForWidth())
        self.adc_threshold_cam3.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.adc_threshold_cam3, 12, 3, 1, 1)

        self.exposure_cam1 = QSpinBox(self.scrollAreaWidgetContents)
        self.exposure_cam1.setObjectName(u"exposure_cam1")
        sizePolicy2.setHeightForWidth(self.exposure_cam1.sizePolicy().hasHeightForWidth())
        self.exposure_cam1.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.exposure_cam1, 9, 1, 1, 1)

        self.data_path_cam1 = QLineEdit(self.scrollAreaWidgetContents)
        self.data_path_cam1.setObjectName(u"data_path_cam1")

        self.gridLayout_5.addWidget(self.data_path_cam1, 2, 1, 1, 1)

        self.state_pin_cam2 = QSpinBox(self.scrollAreaWidgetContents)
        self.state_pin_cam2.setObjectName(u"state_pin_cam2")
        sizePolicy2.setHeightForWidth(self.state_pin_cam2.sizePolicy().hasHeightForWidth())
        self.state_pin_cam2.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.state_pin_cam2, 22, 2, 1, 1)

        self.buffer_len_cam1 = QSpinBox(self.scrollAreaWidgetContents)
        self.buffer_len_cam1.setObjectName(u"buffer_len_cam1")
        sizePolicy2.setHeightForWidth(self.buffer_len_cam1.sizePolicy().hasHeightForWidth())
        self.buffer_len_cam1.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.buffer_len_cam1, 10, 1, 1, 1)

        self.cam_spacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.cam_spacer, 24, 0, 1, 4)

        self.adc_threshold_cam1 = QSpinBox(self.scrollAreaWidgetContents)
        self.adc_threshold_cam1.setObjectName(u"adc_threshold_cam1")
        sizePolicy2.setHeightForWidth(self.adc_threshold_cam1.sizePolicy().hasHeightForWidth())
        self.adc_threshold_cam1.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.adc_threshold_cam1, 12, 1, 1, 1)

        self.adc_threshold_label = QLabel(self.scrollAreaWidgetContents)
        self.adc_threshold_label.setObjectName(u"adc_threshold_label")
        sizePolicy1.setHeightForWidth(self.adc_threshold_label.sizePolicy().hasHeightForWidth())
        self.adc_threshold_label.setSizePolicy(sizePolicy1)
        self.adc_threshold_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.adc_threshold_label, 12, 0, 1, 1)

        self.date_format_cam1 = QLineEdit(self.scrollAreaWidgetContents)
        self.date_format_cam1.setObjectName(u"date_format_cam1")

        self.gridLayout_5.addWidget(self.date_format_cam1, 17, 1, 1, 1)

        self.trig_enbl_pin_cam2 = QSpinBox(self.scrollAreaWidgetContents)
        self.trig_enbl_pin_cam2.setObjectName(u"trig_enbl_pin_cam2")
        sizePolicy2.setHeightForWidth(self.trig_enbl_pin_cam2.sizePolicy().hasHeightForWidth())
        self.trig_enbl_pin_cam2.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.trig_enbl_pin_cam2, 20, 2, 1, 1)

        self.image_format_label = QLabel(self.scrollAreaWidgetContents)
        self.image_format_label.setObjectName(u"image_format_label")
        sizePolicy1.setHeightForWidth(self.image_format_label.sizePolicy().hasHeightForWidth())
        self.image_format_label.setSizePolicy(sizePolicy1)
        self.image_format_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.image_format_label, 16, 0, 1, 1)

        self.trig_latch_pin_cam3 = QSpinBox(self.scrollAreaWidgetContents)
        self.trig_latch_pin_cam3.setObjectName(u"trig_latch_pin_cam3")
        sizePolicy2.setHeightForWidth(self.trig_latch_pin_cam3.sizePolicy().hasHeightForWidth())
        self.trig_latch_pin_cam3.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.trig_latch_pin_cam3, 21, 3, 1, 1)

        self.trig_enbl_pin_cam1 = QSpinBox(self.scrollAreaWidgetContents)
        self.trig_enbl_pin_cam1.setObjectName(u"trig_enbl_pin_cam1")
        sizePolicy2.setHeightForWidth(self.trig_enbl_pin_cam1.sizePolicy().hasHeightForWidth())
        self.trig_enbl_pin_cam1.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.trig_enbl_pin_cam1, 20, 1, 1, 1)

        self.post_trig_len_cam2 = QSpinBox(self.scrollAreaWidgetContents)
        self.post_trig_len_cam2.setObjectName(u"post_trig_len_cam2")
        sizePolicy2.setHeightForWidth(self.post_trig_len_cam2.sizePolicy().hasHeightForWidth())
        self.post_trig_len_cam2.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.post_trig_len_cam2, 11, 2, 1, 1)

        self.pix_threshold_cam1 = QSpinBox(self.scrollAreaWidgetContents)
        self.pix_threshold_cam1.setObjectName(u"pix_threshold_cam1")
        sizePolicy2.setHeightForWidth(self.pix_threshold_cam1.sizePolicy().hasHeightForWidth())
        self.pix_threshold_cam1.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.pix_threshold_cam1, 13, 1, 1, 1)

        self.pix_threshold_cam3 = QSpinBox(self.scrollAreaWidgetContents)
        self.pix_threshold_cam3.setObjectName(u"pix_threshold_cam3")
        sizePolicy2.setHeightForWidth(self.pix_threshold_cam3.sizePolicy().hasHeightForWidth())
        self.pix_threshold_cam3.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.pix_threshold_cam3, 13, 3, 1, 1)

        self.buffer_len_cam2 = QSpinBox(self.scrollAreaWidgetContents)
        self.buffer_len_cam2.setObjectName(u"buffer_len_cam2")
        sizePolicy2.setHeightForWidth(self.buffer_len_cam2.sizePolicy().hasHeightForWidth())
        self.buffer_len_cam2.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.buffer_len_cam2, 10, 2, 1, 1)

        self.state_comm_pin_cam1 = QSpinBox(self.scrollAreaWidgetContents)
        self.state_comm_pin_cam1.setObjectName(u"state_comm_pin_cam1")
        sizePolicy2.setHeightForWidth(self.state_comm_pin_cam1.sizePolicy().hasHeightForWidth())
        self.state_comm_pin_cam1.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.state_comm_pin_cam1, 18, 1, 1, 1)

        self.trig_wait_label = QLabel(self.scrollAreaWidgetContents)
        self.trig_wait_label.setObjectName(u"trig_wait_label")
        sizePolicy1.setHeightForWidth(self.trig_wait_label.sizePolicy().hasHeightForWidth())
        self.trig_wait_label.setSizePolicy(sizePolicy1)
        self.trig_wait_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.trig_wait_label, 8, 0, 1, 1)

        self.post_trig_len_cam3 = QSpinBox(self.scrollAreaWidgetContents)
        self.post_trig_len_cam3.setObjectName(u"post_trig_len_cam3")
        sizePolicy2.setHeightForWidth(self.post_trig_len_cam3.sizePolicy().hasHeightForWidth())
        self.post_trig_len_cam3.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.post_trig_len_cam3, 11, 3, 1, 1)

        self.date_format_cam2 = QLineEdit(self.scrollAreaWidgetContents)
        self.date_format_cam2.setObjectName(u"date_format_cam2")

        self.gridLayout_5.addWidget(self.date_format_cam2, 17, 2, 1, 1)

        self.data_path_cam3 = QLineEdit(self.scrollAreaWidgetContents)
        self.data_path_cam3.setObjectName(u"data_path_cam3")

        self.gridLayout_5.addWidget(self.data_path_cam3, 2, 3, 1, 1)

        self.exposure_label = QLabel(self.scrollAreaWidgetContents)
        self.exposure_label.setObjectName(u"exposure_label")
        sizePolicy1.setHeightForWidth(self.exposure_label.sizePolicy().hasHeightForWidth())
        self.exposure_label.setSizePolicy(sizePolicy1)
        self.exposure_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.exposure_label, 9, 0, 1, 1)

        self.pix_threshold_label = QLabel(self.scrollAreaWidgetContents)
        self.pix_threshold_label.setObjectName(u"pix_threshold_label")
        sizePolicy1.setHeightForWidth(self.pix_threshold_label.sizePolicy().hasHeightForWidth())
        self.pix_threshold_label.setSizePolicy(sizePolicy1)
        self.pix_threshold_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.pix_threshold_label, 13, 0, 1, 1)

        self.mode_cam1 = QSpinBox(self.scrollAreaWidgetContents)
        self.mode_cam1.setObjectName(u"mode_cam1")
        sizePolicy2.setHeightForWidth(self.mode_cam1.sizePolicy().hasHeightForWidth())
        self.mode_cam1.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.mode_cam1, 4, 1, 1, 1)

        self.trig_wait_cam1 = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.trig_wait_cam1.setObjectName(u"trig_wait_cam1")
        sizePolicy2.setHeightForWidth(self.trig_wait_cam1.sizePolicy().hasHeightForWidth())
        self.trig_wait_cam1.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.trig_wait_cam1, 8, 1, 1, 1)

        self.trig_pin_cam2 = QSpinBox(self.scrollAreaWidgetContents)
        self.trig_pin_cam2.setObjectName(u"trig_pin_cam2")
        sizePolicy2.setHeightForWidth(self.trig_pin_cam2.sizePolicy().hasHeightForWidth())
        self.trig_pin_cam2.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.trig_pin_cam2, 23, 2, 1, 1)

        self.trig_latch_pin_cam1 = QSpinBox(self.scrollAreaWidgetContents)
        self.trig_latch_pin_cam1.setObjectName(u"trig_latch_pin_cam1")
        sizePolicy2.setHeightForWidth(self.trig_latch_pin_cam1.sizePolicy().hasHeightForWidth())
        self.trig_latch_pin_cam1.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.trig_latch_pin_cam1, 21, 1, 1, 1)

        self.trig_latch_pin_cam2 = QSpinBox(self.scrollAreaWidgetContents)
        self.trig_latch_pin_cam2.setObjectName(u"trig_latch_pin_cam2")
        sizePolicy2.setHeightForWidth(self.trig_latch_pin_cam2.sizePolicy().hasHeightForWidth())
        self.trig_latch_pin_cam2.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.trig_latch_pin_cam2, 21, 2, 1, 1)

        self.exposure_cam2 = QSpinBox(self.scrollAreaWidgetContents)
        self.exposure_cam2.setObjectName(u"exposure_cam2")
        sizePolicy2.setHeightForWidth(self.exposure_cam2.sizePolicy().hasHeightForWidth())
        self.exposure_cam2.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.exposure_cam2, 9, 2, 1, 1)

        self.state_pin_cam1 = QSpinBox(self.scrollAreaWidgetContents)
        self.state_pin_cam1.setObjectName(u"state_pin_cam1")
        sizePolicy2.setHeightForWidth(self.state_pin_cam1.sizePolicy().hasHeightForWidth())
        self.state_pin_cam1.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.state_pin_cam1, 22, 1, 1, 1)

        self.mode_label = QLabel(self.scrollAreaWidgetContents)
        self.mode_label.setObjectName(u"mode_label")
        sizePolicy1.setHeightForWidth(self.mode_label.sizePolicy().hasHeightForWidth())
        self.mode_label.setSizePolicy(sizePolicy1)
        self.mode_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.mode_label, 4, 0, 1, 1)

        self.state_pin_cam3 = QSpinBox(self.scrollAreaWidgetContents)
        self.state_pin_cam3.setObjectName(u"state_pin_cam3")
        sizePolicy2.setHeightForWidth(self.state_pin_cam3.sizePolicy().hasHeightForWidth())
        self.state_pin_cam3.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.state_pin_cam3, 22, 3, 1, 1)

        self.config_path_cam3 = QLineEdit(self.scrollAreaWidgetContents)
        self.config_path_cam3.setObjectName(u"config_path_cam3")

        self.gridLayout_5.addWidget(self.config_path_cam3, 1, 3, 1, 1)

        self.trig_enbl_pin_label = QLabel(self.scrollAreaWidgetContents)
        self.trig_enbl_pin_label.setObjectName(u"trig_enbl_pin_label")
        sizePolicy1.setHeightForWidth(self.trig_enbl_pin_label.sizePolicy().hasHeightForWidth())
        self.trig_enbl_pin_label.setSizePolicy(sizePolicy1)
        self.trig_enbl_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.trig_enbl_pin_label, 20, 0, 1, 1)

        self.trig_enbl_pin_cam3 = QSpinBox(self.scrollAreaWidgetContents)
        self.trig_enbl_pin_cam3.setObjectName(u"trig_enbl_pin_cam3")
        sizePolicy2.setHeightForWidth(self.trig_enbl_pin_cam3.sizePolicy().hasHeightForWidth())
        self.trig_enbl_pin_cam3.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.trig_enbl_pin_cam3, 20, 3, 1, 1)

        self.buffer_len_cam3 = QSpinBox(self.scrollAreaWidgetContents)
        self.buffer_len_cam3.setObjectName(u"buffer_len_cam3")
        sizePolicy2.setHeightForWidth(self.buffer_len_cam3.sizePolicy().hasHeightForWidth())
        self.buffer_len_cam3.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.buffer_len_cam3, 10, 3, 1, 1)

        self.date_format_label = QLabel(self.scrollAreaWidgetContents)
        self.date_format_label.setObjectName(u"date_format_label")
        sizePolicy1.setHeightForWidth(self.date_format_label.sizePolicy().hasHeightForWidth())
        self.date_format_label.setSizePolicy(sizePolicy1)
        self.date_format_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.date_format_label, 17, 0, 1, 1)

        self.adc_threshold_cam2 = QSpinBox(self.scrollAreaWidgetContents)
        self.adc_threshold_cam2.setObjectName(u"adc_threshold_cam2")
        sizePolicy2.setHeightForWidth(self.adc_threshold_cam2.sizePolicy().hasHeightForWidth())
        self.adc_threshold_cam2.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.adc_threshold_cam2, 12, 2, 1, 1)

        self.state_comm_pin_cam2 = QSpinBox(self.scrollAreaWidgetContents)
        self.state_comm_pin_cam2.setObjectName(u"state_comm_pin_cam2")
        sizePolicy2.setHeightForWidth(self.state_comm_pin_cam2.sizePolicy().hasHeightForWidth())
        self.state_comm_pin_cam2.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.state_comm_pin_cam2, 18, 2, 1, 1)

        self.buffer_len_label = QLabel(self.scrollAreaWidgetContents)
        self.buffer_len_label.setObjectName(u"buffer_len_label")
        sizePolicy1.setHeightForWidth(self.buffer_len_label.sizePolicy().hasHeightForWidth())
        self.buffer_len_label.setSizePolicy(sizePolicy1)
        self.buffer_len_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.buffer_len_label, 10, 0, 1, 1)

        self.ip_addr_cam2 = QLineEdit(self.scrollAreaWidgetContents)
        self.ip_addr_cam2.setObjectName(u"ip_addr_cam2")

        self.gridLayout_5.addWidget(self.ip_addr_cam2, 3, 2, 1, 1)

        self.mode_cam2 = QSpinBox(self.scrollAreaWidgetContents)
        self.mode_cam2.setObjectName(u"mode_cam2")
        sizePolicy2.setHeightForWidth(self.mode_cam2.sizePolicy().hasHeightForWidth())
        self.mode_cam2.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.mode_cam2, 4, 2, 1, 1)

        self.image_format_cam2 = QComboBox(self.scrollAreaWidgetContents)
        self.image_format_cam2.addItem("")
        self.image_format_cam2.addItem("")
        self.image_format_cam2.setObjectName(u"image_format_cam2")

        self.gridLayout_5.addWidget(self.image_format_cam2, 16, 2, 1, 1)

        self.iamge_format_cam3 = QComboBox(self.scrollAreaWidgetContents)
        self.iamge_format_cam3.addItem("")
        self.iamge_format_cam3.addItem("")
        self.iamge_format_cam3.setObjectName(u"iamge_format_cam3")

        self.gridLayout_5.addWidget(self.iamge_format_cam3, 16, 3, 1, 1)

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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 388, 434))
        self.scrollAreaWidgetContents_3.setMaximumSize(QSize(1000, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fifo_grid_layout = QGridLayout()
        self.fifo_grid_layout.setSpacing(3)
        self.fifo_grid_layout.setObjectName(u"fifo_grid_layout")
        self.fifo_grid_layout.setContentsMargins(-1, 6, -1, 6)
        self.trig_or_pin_edit = QSpinBox(self.scrollAreaWidgetContents_3)
        self.trig_or_pin_edit.setObjectName(u"trig_or_pin_edit")

        self.fifo_grid_layout.addWidget(self.trig_or_pin_edit, 3, 3, 1, 1)

        self.fifo_layout = QLabel(self.scrollAreaWidgetContents_3)
        self.fifo_layout.setObjectName(u"fifo_layout")
        self.fifo_layout.setAlignment(Qt.AlignCenter)

        self.fifo_grid_layout.addWidget(self.fifo_layout, 0, 0, 1, 4)

        self.trig_reset_pin_edit = QSpinBox(self.scrollAreaWidgetContents_3)
        self.trig_reset_pin_edit.setObjectName(u"trig_reset_pin_edit")

        self.fifo_grid_layout.addWidget(self.trig_reset_pin_edit, 3, 1, 1, 1)

        self.trig_in_pins_edit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.trig_in_pins_edit.setObjectName(u"trig_in_pins_edit")

        self.fifo_grid_layout.addWidget(self.trig_in_pins_edit, 1, 1, 1, 3)

        self.trig_reset_pin_label = QLabel(self.scrollAreaWidgetContents_3)
        self.trig_reset_pin_label.setObjectName(u"trig_reset_pin_label")
        self.trig_reset_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.fifo_grid_layout.addWidget(self.trig_reset_pin_label, 3, 0, 1, 1)

        self.trig_in_pins_label = QLabel(self.scrollAreaWidgetContents_3)
        self.trig_in_pins_label.setObjectName(u"trig_in_pins_label")
        self.trig_in_pins_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.fifo_grid_layout.addWidget(self.trig_in_pins_label, 1, 0, 1, 1)

        self.trig_latch_pins_edit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.trig_latch_pins_edit.setObjectName(u"trig_latch_pins_edit")

        self.fifo_grid_layout.addWidget(self.trig_latch_pins_edit, 2, 1, 1, 3)

        self.trig_or_pin_label = QLabel(self.scrollAreaWidgetContents_3)
        self.trig_or_pin_label.setObjectName(u"trig_or_pin_label")
        self.trig_or_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.fifo_grid_layout.addWidget(self.trig_or_pin_label, 3, 2, 1, 1)

        self.trig_latch_pins_label = QLabel(self.scrollAreaWidgetContents_3)
        self.trig_latch_pins_label.setObjectName(u"trig_latch_pins_label")
        self.trig_latch_pins_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.fifo_grid_layout.addWidget(self.trig_latch_pins_label, 2, 0, 1, 1)

        self.on_time_pin_label = QLabel(self.scrollAreaWidgetContents_3)
        self.on_time_pin_label.setObjectName(u"on_time_pin_label")
        self.on_time_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.fifo_grid_layout.addWidget(self.on_time_pin_label, 4, 0, 1, 1)

        self.on_time_pin_edit = QSpinBox(self.scrollAreaWidgetContents_3)
        self.on_time_pin_edit.setObjectName(u"on_time_pin_edit")

        self.fifo_grid_layout.addWidget(self.on_time_pin_edit, 4, 1, 1, 1)

        self.heartbeat_pin_label = QLabel(self.scrollAreaWidgetContents_3)
        self.heartbeat_pin_label.setObjectName(u"heartbeat_pin_label")
        self.heartbeat_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.fifo_grid_layout.addWidget(self.heartbeat_pin_label, 4, 2, 1, 1)

        self.heartbeat_pin_edit = QSpinBox(self.scrollAreaWidgetContents_3)
        self.heartbeat_pin_edit.setObjectName(u"heartbeat_pin_edit")

        self.fifo_grid_layout.addWidget(self.heartbeat_pin_edit, 4, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.fifo_grid_layout)

        self.dio_line = QFrame(self.scrollAreaWidgetContents_3)
        self.dio_line.setObjectName(u"dio_line")
        self.dio_line.setFrameShape(QFrame.HLine)
        self.dio_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.dio_line)

        self.gate_label = QLabel(self.scrollAreaWidgetContents_3)
        self.gate_label.setObjectName(u"gate_label")
        self.gate_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.gate_label)

        self.gate_grid_layout = QGridLayout()
        self.gate_grid_layout.setSpacing(3)
        self.gate_grid_layout.setObjectName(u"gate_grid_layout")
        self.gate_grid_layout.setContentsMargins(6, 6, -1, -1)
        self.wave1_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave1_label.setObjectName(u"wave1_label")
        self.wave1_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave1_label, 2, 0, 1, 1)

        self.gate_pin_wave3 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave3.setObjectName(u"gate_pin_wave3")

        self.gate_grid_layout.addWidget(self.gate_pin_wave3, 4, 1, 1, 1)

        self.gate_pin_wave1 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave1.setObjectName(u"gate_pin_wave1")

        self.gate_grid_layout.addWidget(self.gate_pin_wave1, 2, 1, 1, 1)

        self.gate_phase_wave1 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave1.setObjectName(u"gate_phase_wave1")
        self.gate_phase_wave1.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.gate_phase_wave1.setKeyboardTracking(True)

        self.gate_grid_layout.addWidget(self.gate_phase_wave1, 2, 3, 1, 1)

        self.wave8_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave8_label.setObjectName(u"wave8_label")
        self.wave8_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave8_label, 9, 0, 1, 1)

        self.wave6_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave6_label.setObjectName(u"wave6_label")
        self.wave6_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave6_label, 7, 0, 1, 1)

        self.duty_label = QLabel(self.scrollAreaWidgetContents_3)
        self.duty_label.setObjectName(u"duty_label")
        self.duty_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.duty_label, 0, 4, 1, 1)

        self.gate_period_label = QLabel(self.scrollAreaWidgetContents_3)
        self.gate_period_label.setObjectName(u"gate_period_label")
        self.gate_period_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.gate_period_label, 0, 2, 1, 1)

        self.gate_period_wave3 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave3.setObjectName(u"gate_period_wave3")

        self.gate_grid_layout.addWidget(self.gate_period_wave3, 4, 2, 1, 1)

        self.gate_phase_wave2 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave2.setObjectName(u"gate_phase_wave2")

        self.gate_grid_layout.addWidget(self.gate_phase_wave2, 3, 3, 1, 1)

        self.duty_wave3 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave3.setObjectName(u"duty_wave3")

        self.gate_grid_layout.addWidget(self.duty_wave3, 4, 4, 1, 1)

        self.gate_period_wave1 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave1.setObjectName(u"gate_period_wave1")

        self.gate_grid_layout.addWidget(self.gate_period_wave1, 2, 2, 1, 1)

        self.wave5_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave5_label.setObjectName(u"wave5_label")
        self.wave5_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave5_label, 6, 0, 1, 1)

        self.wave4_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave4_label.setObjectName(u"wave4_label")
        self.wave4_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave4_label, 5, 0, 1, 1)

        self.wave7_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave7_label.setObjectName(u"wave7_label")
        self.wave7_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave7_label, 8, 0, 1, 1)

        self.gate_phase_wave3 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave3.setObjectName(u"gate_phase_wave3")

        self.gate_grid_layout.addWidget(self.gate_phase_wave3, 4, 3, 1, 1)

        self.gate_period_wave2 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave2.setObjectName(u"gate_period_wave2")

        self.gate_grid_layout.addWidget(self.gate_period_wave2, 3, 2, 1, 1)

        self.gate_polarity_label = QLabel(self.scrollAreaWidgetContents_3)
        self.gate_polarity_label.setObjectName(u"gate_polarity_label")
        self.gate_polarity_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.gate_polarity_label, 0, 5, 1, 1)

        self.gate_pin_wave2 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave2.setObjectName(u"gate_pin_wave2")

        self.gate_grid_layout.addWidget(self.gate_pin_wave2, 3, 1, 1, 1)

        self.gate_pin_label = QLabel(self.scrollAreaWidgetContents_3)
        self.gate_pin_label.setObjectName(u"gate_pin_label")
        self.gate_pin_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.gate_pin_label, 0, 1, 1, 1)

        self.wave2_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave2_label.setObjectName(u"wave2_label")
        self.wave2_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave2_label, 3, 0, 1, 1)

        self.duty_wave1 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave1.setObjectName(u"duty_wave1")

        self.gate_grid_layout.addWidget(self.duty_wave1, 2, 4, 1, 1)

        self.gate_phase_label = QLabel(self.scrollAreaWidgetContents_3)
        self.gate_phase_label.setObjectName(u"gate_phase_label")
        self.gate_phase_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.gate_phase_label, 0, 3, 1, 1)

        self.duty_wave2 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave2.setObjectName(u"duty_wave2")

        self.gate_grid_layout.addWidget(self.duty_wave2, 3, 4, 1, 1)

        self.wave3_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave3_label.setObjectName(u"wave3_label")
        self.wave3_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave3_label, 4, 0, 1, 1)

        self.wave9_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave9_label.setObjectName(u"wave9_label")
        self.wave9_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave9_label, 10, 0, 1, 1)

        self.gate_period_wave4 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave4.setObjectName(u"gate_period_wave4")

        self.gate_grid_layout.addWidget(self.gate_period_wave4, 5, 2, 1, 1)

        self.gate_phase_wave4 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave4.setObjectName(u"gate_phase_wave4")

        self.gate_grid_layout.addWidget(self.gate_phase_wave4, 5, 3, 1, 1)

        self.duty_wave4 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave4.setObjectName(u"duty_wave4")

        self.gate_grid_layout.addWidget(self.duty_wave4, 5, 4, 1, 1)

        self.gate_pin_wave4 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave4.setObjectName(u"gate_pin_wave4")

        self.gate_grid_layout.addWidget(self.gate_pin_wave4, 5, 1, 1, 1)

        self.gate_pin_wave5 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave5.setObjectName(u"gate_pin_wave5")

        self.gate_grid_layout.addWidget(self.gate_pin_wave5, 6, 1, 1, 1)

        self.gate_period_wave5 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave5.setObjectName(u"gate_period_wave5")

        self.gate_grid_layout.addWidget(self.gate_period_wave5, 6, 2, 1, 1)

        self.gate_phase_wave5 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave5.setObjectName(u"gate_phase_wave5")

        self.gate_grid_layout.addWidget(self.gate_phase_wave5, 6, 3, 1, 1)

        self.duty_wave5 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave5.setObjectName(u"duty_wave5")

        self.gate_grid_layout.addWidget(self.duty_wave5, 6, 4, 1, 1)

        self.gate_pin_wave6 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave6.setObjectName(u"gate_pin_wave6")

        self.gate_grid_layout.addWidget(self.gate_pin_wave6, 7, 1, 1, 1)

        self.gate_period_wave6 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave6.setObjectName(u"gate_period_wave6")

        self.gate_grid_layout.addWidget(self.gate_period_wave6, 7, 2, 1, 1)

        self.gate_phase_wave6 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave6.setObjectName(u"gate_phase_wave6")

        self.gate_grid_layout.addWidget(self.gate_phase_wave6, 7, 3, 1, 1)

        self.duty_wave6 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave6.setObjectName(u"duty_wave6")

        self.gate_grid_layout.addWidget(self.duty_wave6, 7, 4, 1, 1)

        self.gate_pin_wave7 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave7.setObjectName(u"gate_pin_wave7")

        self.gate_grid_layout.addWidget(self.gate_pin_wave7, 8, 1, 1, 1)

        self.gate_period_wave7 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave7.setObjectName(u"gate_period_wave7")

        self.gate_grid_layout.addWidget(self.gate_period_wave7, 8, 2, 1, 1)

        self.gate_phase_wave7 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave7.setObjectName(u"gate_phase_wave7")

        self.gate_grid_layout.addWidget(self.gate_phase_wave7, 8, 3, 1, 1)

        self.duty_wave7 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave7.setObjectName(u"duty_wave7")

        self.gate_grid_layout.addWidget(self.duty_wave7, 8, 4, 1, 1)

        self.gate_pin_wave8 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave8.setObjectName(u"gate_pin_wave8")

        self.gate_grid_layout.addWidget(self.gate_pin_wave8, 9, 1, 1, 1)

        self.gate_period_wave8 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave8.setObjectName(u"gate_period_wave8")

        self.gate_grid_layout.addWidget(self.gate_period_wave8, 9, 2, 1, 1)

        self.gate_phase_wave8 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave8.setObjectName(u"gate_phase_wave8")

        self.gate_grid_layout.addWidget(self.gate_phase_wave8, 9, 3, 1, 1)

        self.duty_wave8 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave8.setObjectName(u"duty_wave8")

        self.gate_grid_layout.addWidget(self.duty_wave8, 9, 4, 1, 1)

        self.gate_pin_wave9 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave9.setObjectName(u"gate_pin_wave9")

        self.gate_grid_layout.addWidget(self.gate_pin_wave9, 10, 1, 1, 1)

        self.gate_period_wave9 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave9.setObjectName(u"gate_period_wave9")

        self.gate_grid_layout.addWidget(self.gate_period_wave9, 10, 2, 1, 1)

        self.gate_phase_wave9 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave9.setObjectName(u"gate_phase_wave9")

        self.gate_grid_layout.addWidget(self.gate_phase_wave9, 10, 3, 1, 1)

        self.duty_wave9 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave9.setObjectName(u"duty_wave9")

        self.gate_grid_layout.addWidget(self.duty_wave9, 10, 4, 1, 1)

        self.gate_polarity_wave1 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave1.addItem("")
        self.gate_polarity_wave1.addItem("")
        self.gate_polarity_wave1.setObjectName(u"gate_polarity_wave1")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave1, 2, 5, 1, 1)

        self.gate_polarity_wave2 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave2.addItem("")
        self.gate_polarity_wave2.addItem("")
        self.gate_polarity_wave2.setObjectName(u"gate_polarity_wave2")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave2, 3, 5, 1, 1)

        self.gate_polarity_wave3 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave3.addItem("")
        self.gate_polarity_wave3.addItem("")
        self.gate_polarity_wave3.setObjectName(u"gate_polarity_wave3")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave3, 4, 5, 1, 1)

        self.gate_polarity_wave4 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave4.addItem("")
        self.gate_polarity_wave4.addItem("")
        self.gate_polarity_wave4.setObjectName(u"gate_polarity_wave4")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave4, 5, 5, 1, 1)

        self.gate_polarity_wave5 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave5.addItem("")
        self.gate_polarity_wave5.addItem("")
        self.gate_polarity_wave5.setObjectName(u"gate_polarity_wave5")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave5, 6, 5, 1, 1)

        self.gate_polarity_wave6 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave6.addItem("")
        self.gate_polarity_wave6.addItem("")
        self.gate_polarity_wave6.setObjectName(u"gate_polarity_wave6")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave6, 7, 5, 1, 1)

        self.gate_polarity_wave7 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave7.addItem("")
        self.gate_polarity_wave7.addItem("")
        self.gate_polarity_wave7.setObjectName(u"gate_polarity_wave7")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave7, 8, 5, 1, 1)

        self.gate_polarity_wave8 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave8.addItem("")
        self.gate_polarity_wave8.addItem("")
        self.gate_polarity_wave8.setObjectName(u"gate_polarity_wave8")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave8, 9, 5, 1, 1)

        self.gate_polarity_wave9 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave9.addItem("")
        self.gate_polarity_wave9.addItem("")
        self.gate_polarity_wave9.setObjectName(u"gate_polarity_wave9")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave9, 10, 5, 1, 1)


        self.verticalLayout_2.addLayout(self.gate_grid_layout)

        self.dio_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.dio_spacer)

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
        self.data_dir_label.setBuddy(self.data_dir_edit)
        self.log_path_label.setBuddy(self.data_dir_edit)
        self.max_num_ev_label.setBuddy(self.max_num_ev_box)
        self.max_ev_time_label.setBuddy(self.max_ev_time_box)
        self.max_ev_time_label_2.setBuddy(self.max_ev_time_box)
        self.max_ev_time_label_3.setBuddy(self.max_ev_time_box)
        self.acous_pre_trig_label.setBuddy(self.acous_pre_trig_box)
        self.acous_sample_rate_label.setBuddy(self.acous_sample_rate_box)
        self.acous_trig_timeout_label.setBuddy(self.acous_trig_timeout_box)
        self.acous_post_trig_label.setBuddy(self.acous_post_trig_box)
        self.acous_trig_delay_label.setBuddy(self.acous_trig_delay_box)
        self.acous_ch5_label.setBuddy(self.acous_enable_ch5)
        self.acous_ch2_label.setBuddy(self.acous_enable_ch2)
        self.acous_ch1_label.setBuddy(self.acous_enable_ch1)
        self.acous_ch6_label.setBuddy(self.acous_enable_ch6)
        self.acous_ch7_label.setBuddy(self.acous_enable_ch7)
        self.acous_ch3_label.setBuddy(self.acous_enable_ch3)
        self.acous_ch8_label.setBuddy(self.acous_enable_ch8)
        self.acous_ch4_label.setBuddy(self.acous_enable_ch4)
        self.trig_reset_pin_label.setBuddy(self.trig_reset_pin_edit)
        self.trig_in_pins_label.setBuddy(self.trig_in_pins_edit)
        self.trig_or_pin_label.setBuddy(self.trig_or_pin_edit)
        self.trig_latch_pins_label.setBuddy(self.trig_latch_pins_edit)
        self.on_time_pin_label.setBuddy(self.on_time_pin_edit)
        self.heartbeat_pin_label.setBuddy(self.heartbeat_pin_edit)
#endif // QT_CONFIG(shortcut)

        self.toolBar.addAction(self.actionClose_Window)
        self.toolBar.addAction(self.actionReloadConfig)
        self.toolBar.addAction(self.actionApply_config)
        self.toolBar.addAction(self.actionSaveConfig)

        self.retranslateUi(SettingsWindow)
        self.actionClose_Window.triggered.connect(SettingsWindow.close)
        self.config_path_but.clicked.connect(SettingsWindow.select_config_path)
        self.data_dir_but.clicked.connect(SettingsWindow.select_data_dir)
        self.actionApply_config.triggered.connect(SettingsWindow.apply_config)
        self.actionSaveConfig.triggered.connect(SettingsWindow.save_config)
        self.actionReloadConfig.triggered.connect(SettingsWindow.load_config)
        self.log_path_but.clicked.connect(SettingsWindow.select_log_path)

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
        self.data_dir_label.setText(QCoreApplication.translate("SettingsWindow", u"Data Dir", None))
        self.config_path_but.setText(QCoreApplication.translate("SettingsWindow", u"...", None))
        self.data_dir_but.setText(QCoreApplication.translate("SettingsWindow", u"...", None))
        self.log_path_label.setText(QCoreApplication.translate("SettingsWindow", u"Log Path", None))
        self.log_path_but.setText(QCoreApplication.translate("SettingsWindow", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.general_tab), QCoreApplication.translate("SettingsWindow", u"General", None))
        self.max_num_ev_label.setText(QCoreApplication.translate("SettingsWindow", u"Max Num of Events", None))
        self.comboBox_23.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Cf-252", None))
        self.comboBox_23.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Co-57", None))
        self.comboBox_23.setItemText(2, QCoreApplication.translate("SettingsWindow", u"Cs-137", None))

        self.max_ev_time_box.setSuffix(QCoreApplication.translate("SettingsWindow", u"s", None))
        self.max_ev_time_label.setText(QCoreApplication.translate("SettingsWindow", u"Max Event Time", None))
        self.max_ev_time_label_2.setText(QCoreApplication.translate("SettingsWindow", u"Source", None))
        self.max_ev_time_label_3.setText(QCoreApplication.translate("SettingsWindow", u"Pressure Setpoint", None))
        self.max_num_ev_box_2.setSuffix(QCoreApplication.translate("SettingsWindow", u"psia", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.run_tab), QCoreApplication.translate("SettingsWindow", u"Run", None))
        self.label_31.setText(QCoreApplication.translate("SettingsWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sipm_tab), QCoreApplication.translate("SettingsWindow", u"SiPM", None))
        self.acous_pre_trig_label.setText(QCoreApplication.translate("SettingsWindow", u"Pre Trig Length", None))
        self.acous_sample_rate_box.setItemText(0, QCoreApplication.translate("SettingsWindow", u"100 MS/s", None))

        self.acous_sample_rate_label.setText(QCoreApplication.translate("SettingsWindow", u"Sample Rate", None))
        self.acous_trig_timeout_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig Timeout", None))
        self.acous_post_trig_label.setText(QCoreApplication.translate("SettingsWindow", u"Post Trig Length", None))
        self.acous_trig_delay_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig Delay", None))
        self.acous_enable_ch7.setText("")
        self.acous_enable_ch3.setText("")
        self.acous_trig_label.setText(QCoreApplication.translate("SettingsWindow", u"Trigger", None))
        self.acous_polarity_label.setText(QCoreApplication.translate("SettingsWindow", u"Polarity", None))
        self.acous_ch5_label.setText(QCoreApplication.translate("SettingsWindow", u"Ch 5", None))
        self.acous_polarity_ch4.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.acous_polarity_ch4.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.acous_ch2_label.setText(QCoreApplication.translate("SettingsWindow", u"Ch 2", None))
        self.acous_polarity_ch3.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.acous_polarity_ch3.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.acous_polarity_ch5.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.acous_polarity_ch5.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.acous_dc_offset_ch7.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.acous_range_label.setText(QCoreApplication.translate("SettingsWindow", u"Range", None))
        self.acous_enable_ch4.setText("")
        self.acous_trig_ch7.setText("")
        self.acous_ch1_label.setText(QCoreApplication.translate("SettingsWindow", u"Ch 1", None))
        self.acous_polarity_ext.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.acous_polarity_ext.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.acous_range_ch8.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.acous_ch6_label.setText(QCoreApplication.translate("SettingsWindow", u"Ch 6", None))
        self.acous_polarity_ch8.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.acous_polarity_ch8.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.acous_dc_offset_ch4.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.acous_ch7_label.setText(QCoreApplication.translate("SettingsWindow", u"Ch 7", None))
        self.acous_enable_ch2.setText("")
        self.acous_dc_offset_ch8.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.acous_trig_ch6.setText("")
        self.acous_trig_ext.setText("")
        self.acous_range_ch3.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.acous_polarity_ch6.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.acous_polarity_ch6.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.acous_ch3_label.setText(QCoreApplication.translate("SettingsWindow", u"Ch 3", None))
        self.acous_range_ch6.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.acous_trig_ch4.setText("")
        self.acous_dc_offset_ch1.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.acous_trig_ch2.setText("")
        self.acous_ch8_label.setText(QCoreApplication.translate("SettingsWindow", u"Ch 8", None))
        self.acous_dc_offset_ch5.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.acous_dc_offset_label.setText(QCoreApplication.translate("SettingsWindow", u"DC Offset", None))
        self.acous_polarity_ch2.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.acous_polarity_ch2.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.acous_trig_ch8.setText("")
        self.acous_enabled_label.setText(QCoreApplication.translate("SettingsWindow", u"Enabled", None))
        self.acous_enable_ch5.setText("")
        self.acous_range_ch2.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.acous_ch4_label.setText(QCoreApplication.translate("SettingsWindow", u"Ch 4", None))
        self.acous_range_ch7.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.acous_trig_ch5.setText("")
        self.acous_trig_ch3.setText("")
        self.acous_dc_offset_ch2.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.acous_range_ch5.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.acous_polarity_ch7.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.acous_polarity_ch7.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.acous_enable_ch8.setText("")
        self.acous_range_ch1.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.acous_range_ch4.setSuffix(QCoreApplication.translate("SettingsWindow", u"mV", None))
        self.acous_enable_ch6.setText("")
        self.acous_enable_ch1.setText("")
        self.acous_threshold_label.setText(QCoreApplication.translate("SettingsWindow", u"Threshold", None))
        self.acous_polarity_ch1.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Rising", None))
        self.acous_polarity_ch1.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Falling", None))

        self.acous_ext_label.setText(QCoreApplication.translate("SettingsWindow", u"Ext", None))
        self.acous_trig_ch1.setText("")
        self.acous_dc_offset_ch3.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.acous_dc_offset_ch6.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.acoustics_tab), QCoreApplication.translate("SettingsWindow", u"Acoustics", None))
        self.state_comm_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"State Comm Pin", None))
        self.config_path_label_2.setText(QCoreApplication.translate("SettingsWindow", u"Config Path", None))
        self.trig_latch_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig Latch Pin", None))
        self.config_path_cam1.setText("")
        self.data_path_cam2.setText("")
        self.post_trig_len_label.setText(QCoreApplication.translate("SettingsWindow", u"Post-Trig Length", None))
        self.trig_wait_cam3.setSuffix(QCoreApplication.translate("SettingsWindow", u"s", None))
        self.cam3_label.setText(QCoreApplication.translate("SettingsWindow", u"Cam 3", None))
        self.trig_wait_cam2.setSuffix(QCoreApplication.translate("SettingsWindow", u"s", None))
        self.trig_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"Trigger Pin", None))
        self.image_format_cam1.setItemText(0, QCoreApplication.translate("SettingsWindow", u"png", None))
        self.image_format_cam1.setItemText(1, QCoreApplication.translate("SettingsWindow", u"jpg", None))

        self.state_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"State Pin", None))
        self.cam1_label.setText(QCoreApplication.translate("SettingsWindow", u"Cam 1", None))
        self.data_path_label.setText(QCoreApplication.translate("SettingsWindow", u"Data Path", None))
        self.ip_addr_label.setText(QCoreApplication.translate("SettingsWindow", u"IP Address", None))
        self.ip_addr_cam3.setText("")
        self.cam2_label.setText(QCoreApplication.translate("SettingsWindow", u"Cam 2", None))
        self.adc_threshold_label.setText(QCoreApplication.translate("SettingsWindow", u"ADC Threshold", None))
        self.image_format_label.setText(QCoreApplication.translate("SettingsWindow", u"Image Format", None))
        self.trig_wait_label.setText(QCoreApplication.translate("SettingsWindow", u"Trigger Wait", None))
        self.exposure_label.setText(QCoreApplication.translate("SettingsWindow", u"Exposure", None))
        self.pix_threshold_label.setText(QCoreApplication.translate("SettingsWindow", u"Pixel Treshold", None))
        self.trig_wait_cam1.setSuffix(QCoreApplication.translate("SettingsWindow", u"s", None))
        self.mode_label.setText(QCoreApplication.translate("SettingsWindow", u"Mode", None))
        self.trig_enbl_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig Enable Pin", None))
        self.date_format_label.setText(QCoreApplication.translate("SettingsWindow", u"Date Format", None))
        self.buffer_len_label.setText(QCoreApplication.translate("SettingsWindow", u"Buffer Length", None))
        self.image_format_cam2.setItemText(0, QCoreApplication.translate("SettingsWindow", u"png", None))
        self.image_format_cam2.setItemText(1, QCoreApplication.translate("SettingsWindow", u"jpg", None))

        self.iamge_format_cam3.setItemText(0, QCoreApplication.translate("SettingsWindow", u"png", None))
        self.iamge_format_cam3.setItemText(1, QCoreApplication.translate("SettingsWindow", u"jpg", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cam_tab), QCoreApplication.translate("SettingsWindow", u"Camera", None))
        self.fifo_layout.setText(QCoreApplication.translate("SettingsWindow", u"Trig FIFO Arduino", None))
        self.trig_reset_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig Reset Pin", None))
        self.trig_in_pins_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig In Pins", None))
        self.trig_or_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig Or Pin", None))
        self.trig_latch_pins_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig Latch Pins", None))
        self.on_time_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"On-Time Pin", None))
        self.heartbeat_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"Heartbeat Pin", None))
        self.gate_label.setText(QCoreApplication.translate("SettingsWindow", u"Gate Generator Arduino", None))
        self.wave1_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 1", None))
        self.wave8_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 8", None))
        self.wave6_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 6", None))
        self.duty_label.setText(QCoreApplication.translate("SettingsWindow", u"Duty", None))
        self.gate_period_label.setText(QCoreApplication.translate("SettingsWindow", u"Period", None))
        self.duty_wave3.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.wave5_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 5", None))
        self.wave4_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 4", None))
        self.wave7_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 7", None))
        self.gate_polarity_label.setText(QCoreApplication.translate("SettingsWindow", u"Polarity", None))
        self.gate_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"Pin", None))
        self.wave2_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 2", None))
        self.duty_wave1.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.gate_phase_label.setText(QCoreApplication.translate("SettingsWindow", u"Phase", None))
        self.duty_wave2.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.wave3_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 3", None))
        self.wave9_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 9", None))
        self.duty_wave4.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.duty_wave5.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.duty_wave6.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.duty_wave7.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.duty_wave8.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.duty_wave9.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.gate_polarity_wave1.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave1.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.gate_polarity_wave2.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave2.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.gate_polarity_wave3.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave3.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.gate_polarity_wave4.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave4.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.gate_polarity_wave5.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave5.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.gate_polarity_wave6.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave6.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.gate_polarity_wave7.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave7.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.gate_polarity_wave8.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave8.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.gate_polarity_wave9.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave9.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dio_tab), QCoreApplication.translate("SettingsWindow", u"DIO", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"toolBar", None))
    # retranslateUi

