# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingswindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
        SettingsWindow.resize(400, 511)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
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
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 390, 438))
        self.scrollAreaWidgetContents_5.setMaximumSize(QSize(1000, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.log_path_edit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.log_path_edit.setObjectName(u"log_path_edit")

        self.gridLayout_3.addWidget(self.log_path_edit, 1, 1, 1, 1)

        self.config_path_label = QLabel(self.scrollAreaWidgetContents_5)
        self.config_path_label.setObjectName(u"config_path_label")
        self.config_path_label.setMinimumSize(QSize(0, 0))
        self.config_path_label.setLineWidth(0)
        self.config_path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.config_path_label, 0, 0, 1, 1)

        self.log_path_label = QLabel(self.scrollAreaWidgetContents_5)
        self.log_path_label.setObjectName(u"log_path_label")
        self.log_path_label.setLineWidth(0)
        self.log_path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.log_path_label, 1, 0, 1, 1)

        self.log_path_but = QToolButton(self.scrollAreaWidgetContents_5)
        self.log_path_but.setObjectName(u"log_path_but")

        self.gridLayout_3.addWidget(self.log_path_but, 1, 2, 1, 1)

        self.config_path_but = QToolButton(self.scrollAreaWidgetContents_5)
        self.config_path_but.setObjectName(u"config_path_but")

        self.gridLayout_3.addWidget(self.config_path_but, 0, 2, 1, 1)

        self.config_path_edit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.config_path_edit.setObjectName(u"config_path_edit")

        self.gridLayout_3.addWidget(self.config_path_edit, 0, 1, 1, 1)

        self.data_dir_label = QLabel(self.scrollAreaWidgetContents_5)
        self.data_dir_label.setObjectName(u"data_dir_label")
        self.data_dir_label.setLineWidth(0)
        self.data_dir_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.data_dir_label, 2, 0, 1, 1)

        self.data_dir_edit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.data_dir_edit.setObjectName(u"data_dir_edit")

        self.gridLayout_3.addWidget(self.data_dir_edit, 2, 1, 1, 1)

        self.data_dir_but = QToolButton(self.scrollAreaWidgetContents_5)
        self.data_dir_but.setObjectName(u"data_dir_but")

        self.gridLayout_3.addWidget(self.data_dir_but, 2, 2, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_3)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setSpacing(3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.max_num_ev_label = QLabel(self.scrollAreaWidgetContents_5)
        self.max_num_ev_label.setObjectName(u"max_num_ev_label")
        self.max_num_ev_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.max_num_ev_label, 0, 0, 1, 1)

        self.max_ev_time_label = QLabel(self.scrollAreaWidgetContents_5)
        self.max_ev_time_label.setObjectName(u"max_ev_time_label")
        self.max_ev_time_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.max_ev_time_label, 0, 2, 1, 1)

        self.max_ev_time_box = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.max_ev_time_box.setObjectName(u"max_ev_time_box")
        self.max_ev_time_box.setMaximum(100000.000000000000000)

        self.gridLayout_9.addWidget(self.max_ev_time_box, 0, 3, 1, 1)

        self.max_num_ev_box = QSpinBox(self.scrollAreaWidgetContents_5)
        self.max_num_ev_box.setObjectName(u"max_num_ev_box")
        self.max_num_ev_box.setMinimum(1)
        self.max_num_ev_box.setMaximum(1000)
        self.max_num_ev_box.setValue(100)

        self.gridLayout_9.addWidget(self.max_num_ev_box, 0, 1, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_9)

        self.verticalSpacer = QSpacerItem(20, 336, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.files_scroll_area.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_4.addWidget(self.files_scroll_area)

        self.tabWidget.addTab(self.general_tab, "")
        self.scint_tab = QWidget()
        self.scint_tab.setObjectName(u"scint_tab")
        self.verticalLayout_5 = QVBoxLayout(self.scint_tab)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.sipm_scroll_area = QScrollArea(self.scint_tab)
        self.sipm_scroll_area.setObjectName(u"sipm_scroll_area")
        self.sipm_scroll_area.setFrameShape(QFrame.NoFrame)
        self.sipm_scroll_area.setFrameShadow(QFrame.Plain)
        self.sipm_scroll_area.setLineWidth(0)
        self.sipm_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 390, 438))
        self.scrollAreaWidgetContents_2.setMaximumSize(QSize(1000, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(3)
        self.sipm_ip_addr_label = QLabel(self.scrollAreaWidgetContents_2)
        self.sipm_ip_addr_label.setObjectName(u"sipm_ip_addr_label")
        self.sipm_ip_addr_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.sipm_ip_addr_label, 1, 0, 1, 1)

        self.sipm_bias_box = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.sipm_bias_box.setObjectName(u"sipm_bias_box")
        self.sipm_bias_box.setDecimals(1)

        self.gridLayout_4.addWidget(self.sipm_bias_box, 2, 1, 1, 1)

        self.sipm_qp_box = QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.sipm_qp_box.setObjectName(u"sipm_qp_box")
        self.sipm_qp_box.setDecimals(1)

        self.gridLayout_4.addWidget(self.sipm_qp_box, 2, 3, 1, 1)

        self.sipm_ip_addr_edit = QLineEdit(self.scrollAreaWidgetContents_2)
        self.sipm_ip_addr_edit.setObjectName(u"sipm_ip_addr_edit")

        self.gridLayout_4.addWidget(self.sipm_ip_addr_edit, 1, 1, 1, 3)

        self.sipm_qp_label = QLabel(self.scrollAreaWidgetContents_2)
        self.sipm_qp_label.setObjectName(u"sipm_qp_label")
        self.sipm_qp_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.sipm_qp_label, 2, 2, 1, 1)

        self.sipm_bias_label = QLabel(self.scrollAreaWidgetContents_2)
        self.sipm_bias_label.setObjectName(u"sipm_bias_label")
        self.sipm_bias_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.sipm_bias_label, 2, 0, 1, 1)

        self.sipm_amp_label = QLabel(self.scrollAreaWidgetContents_2)
        self.sipm_amp_label.setObjectName(u"sipm_amp_label")
        self.sipm_amp_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.sipm_amp_label, 0, 0, 1, 4)


        self.verticalLayout_9.addLayout(self.gridLayout_4)

        self.line = QFrame(self.scrollAreaWidgetContents_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setSpacing(3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.caen_polarity_box = QComboBox(self.scrollAreaWidgetContents_2)
        self.caen_polarity_box.addItem("")
        self.caen_polarity_box.addItem("")
        self.caen_polarity_box.setObjectName(u"caen_polarity_box")

        self.gridLayout_6.addWidget(self.caen_polarity_box, 6, 1, 1, 1)

        self.caen_polarity_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_polarity_label.setObjectName(u"caen_polarity_label")
        self.caen_polarity_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.caen_polarity_label, 6, 0, 1, 1)

        self.caen_port_box = QSpinBox(self.scrollAreaWidgetContents_2)
        self.caen_port_box.setObjectName(u"caen_port_box")
        self.caen_port_box.setMinimumSize(QSize(50, 0))

        self.gridLayout_6.addWidget(self.caen_port_box, 1, 3, 1, 1)

        self.caen_io_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_io_label.setObjectName(u"caen_io_label")
        self.caen_io_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.caen_io_label, 6, 2, 1, 1)

        self.caen_post_trig_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_post_trig_label.setObjectName(u"caen_post_trig_label")
        self.caen_post_trig_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.caen_post_trig_label, 3, 2, 1, 1)

        self.caen_ext_trig_box = QComboBox(self.scrollAreaWidgetContents_2)
        self.caen_ext_trig_box.addItem("")
        self.caen_ext_trig_box.addItem("")
        self.caen_ext_trig_box.addItem("")
        self.caen_ext_trig_box.addItem("")
        self.caen_ext_trig_box.setObjectName(u"caen_ext_trig_box")

        self.gridLayout_6.addWidget(self.caen_ext_trig_box, 7, 1, 1, 1)

        self.caen_model_box = QComboBox(self.scrollAreaWidgetContents_2)
        self.caen_model_box.addItem("")
        self.caen_model_box.addItem("")
        self.caen_model_box.addItem("")
        self.caen_model_box.setObjectName(u"caen_model_box")

        self.gridLayout_6.addWidget(self.caen_model_box, 1, 1, 1, 1)

        self.caen_conn_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_conn_label.setObjectName(u"caen_conn_label")
        self.caen_conn_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.caen_conn_label, 2, 0, 1, 1)

        self.caen_ext_trig_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_ext_trig_label.setObjectName(u"caen_ext_trig_label")
        self.caen_ext_trig_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.caen_ext_trig_label, 7, 0, 1, 1)

        self.caen_sw_trig_box = QComboBox(self.scrollAreaWidgetContents_2)
        self.caen_sw_trig_box.addItem("")
        self.caen_sw_trig_box.addItem("")
        self.caen_sw_trig_box.addItem("")
        self.caen_sw_trig_box.addItem("")
        self.caen_sw_trig_box.setObjectName(u"caen_sw_trig_box")

        self.gridLayout_6.addWidget(self.caen_sw_trig_box, 7, 3, 1, 1)

        self.caen_evs_box = QSpinBox(self.scrollAreaWidgetContents_2)
        self.caen_evs_box.setObjectName(u"caen_evs_box")
        self.caen_evs_box.setMaximum(10000)

        self.gridLayout_6.addWidget(self.caen_evs_box, 2, 3, 1, 1)

        self.caen_overlap_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_overlap_label.setObjectName(u"caen_overlap_label")
        self.caen_overlap_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.caen_overlap_label, 5, 0, 1, 1)

        self.caen_overlap_box = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_overlap_box.setObjectName(u"caen_overlap_box")

        self.gridLayout_6.addWidget(self.caen_overlap_box, 5, 1, 1, 1)

        self.caen_length_box = QSpinBox(self.scrollAreaWidgetContents_2)
        self.caen_length_box.setObjectName(u"caen_length_box")
        self.caen_length_box.setMaximum(10000)

        self.gridLayout_6.addWidget(self.caen_length_box, 3, 1, 1, 1)

        self.caen_evs_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_evs_label.setObjectName(u"caen_evs_label")
        self.caen_evs_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.caen_evs_label, 2, 2, 1, 1)

        self.caen_io_box = QComboBox(self.scrollAreaWidgetContents_2)
        self.caen_io_box.addItem("")
        self.caen_io_box.addItem("")
        self.caen_io_box.setObjectName(u"caen_io_box")

        self.gridLayout_6.addWidget(self.caen_io_box, 6, 3, 1, 1)

        self.caen_conn_box = QComboBox(self.scrollAreaWidgetContents_2)
        self.caen_conn_box.addItem("")
        self.caen_conn_box.addItem("")
        self.caen_conn_box.setObjectName(u"caen_conn_box")

        self.gridLayout_6.addWidget(self.caen_conn_box, 2, 1, 1, 1)

        self.caen_general_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_general_label.setObjectName(u"caen_general_label")
        self.caen_general_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.caen_general_label, 0, 0, 1, 4)

        self.caen_model_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_model_label.setObjectName(u"caen_model_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.caen_model_label.sizePolicy().hasHeightForWidth())
        self.caen_model_label.setSizePolicy(sizePolicy1)
        self.caen_model_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.caen_model_label, 1, 0, 1, 1)

        self.caen_port_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_port_label.setObjectName(u"caen_port_label")
        self.caen_port_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.caen_port_label, 1, 2, 1, 1)

        self.caen_sw_trig_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_sw_trig_label.setObjectName(u"caen_sw_trig_label")
        self.caen_sw_trig_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.caen_sw_trig_label, 7, 2, 1, 1)

        self.caen_length_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_length_label.setObjectName(u"caen_length_label")
        self.caen_length_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.caen_length_label, 3, 0, 1, 1)

        self.caen_post_trig_box = QSpinBox(self.scrollAreaWidgetContents_2)
        self.caen_post_trig_box.setObjectName(u"caen_post_trig_box")
        self.caen_post_trig_box.setMaximum(100)

        self.gridLayout_6.addWidget(self.caen_post_trig_box, 3, 3, 1, 1)

        self.caen_decimation_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_decimation_label.setObjectName(u"caen_decimation_label")
        self.caen_decimation_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.caen_decimation_label, 4, 2, 1, 1)

        self.caen_trigin_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_trigin_label.setObjectName(u"caen_trigin_label")
        self.caen_trigin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.caen_trigin_label, 4, 0, 1, 1)

        self.caen_trigin_box = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_trigin_box.setObjectName(u"caen_trigin_box")

        self.gridLayout_6.addWidget(self.caen_trigin_box, 4, 1, 1, 1)

        self.caen_decimation_box = QSpinBox(self.scrollAreaWidgetContents_2)
        self.caen_decimation_box.setObjectName(u"caen_decimation_box")
        self.caen_decimation_box.setMinimum(1)
        self.caen_decimation_box.setMaximum(7)

        self.gridLayout_6.addWidget(self.caen_decimation_box, 4, 3, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_6)

        self.line_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_2)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setSpacing(3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.caen_g0_thres_box = QSpinBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_thres_box.setObjectName(u"caen_g0_thres_box")
        self.caen_g0_thres_box.setMaximum(65536)

        self.gridLayout_7.addWidget(self.caen_g0_thres_box, 1, 3, 1, 1)

        self.caen_g0_enable_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_g0_enable_label.setObjectName(u"caen_g0_enable_label")
        self.caen_g0_enable_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.caen_g0_enable_label, 1, 0, 1, 1)

        self.caen_g0_enable_box = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_enable_box.setObjectName(u"caen_g0_enable_box")

        self.gridLayout_7.addWidget(self.caen_g0_enable_box, 1, 1, 1, 1)

        self.caen_g0_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_g0_label.setObjectName(u"caen_g0_label")
        self.caen_g0_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.caen_g0_label, 0, 0, 1, 4)

        self.caen_g0_thres_label = QLabel(self.scrollAreaWidgetContents_2)
        self.caen_g0_thres_label.setObjectName(u"caen_g0_thres_label")
        self.caen_g0_thres_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.caen_g0_thres_label, 1, 2, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_7)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setSpacing(3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.caen_g0_acq_mask_6 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_acq_mask_6.setObjectName(u"caen_g0_acq_mask_6")

        self.gridLayout_8.addWidget(self.caen_g0_acq_mask_6, 2, 7, 1, 1)

        self.label_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_21, 1, 0, 1, 1)

        self.caen_g0_trig_mask_4 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_trig_mask_4.setObjectName(u"caen_g0_trig_mask_4")

        self.gridLayout_8.addWidget(self.caen_g0_trig_mask_4, 1, 5, 1, 1)

        self.caen_g0_trig_mask_1 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_trig_mask_1.setObjectName(u"caen_g0_trig_mask_1")

        self.gridLayout_8.addWidget(self.caen_g0_trig_mask_1, 1, 2, 1, 1)

        self.caen_g0_acq_mask_7 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_acq_mask_7.setObjectName(u"caen_g0_acq_mask_7")

        self.gridLayout_8.addWidget(self.caen_g0_acq_mask_7, 2, 8, 1, 1)

        self.caen_g0_trig_mask_0 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_trig_mask_0.setObjectName(u"caen_g0_trig_mask_0")

        self.gridLayout_8.addWidget(self.caen_g0_trig_mask_0, 1, 1, 1, 1)

        self.caen_g0_acq_mask_4 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_acq_mask_4.setObjectName(u"caen_g0_acq_mask_4")

        self.gridLayout_8.addWidget(self.caen_g0_acq_mask_4, 2, 5, 1, 1)

        self.label_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_22, 2, 0, 1, 1)

        self.caen_g0_trig_mask_5 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_trig_mask_5.setObjectName(u"caen_g0_trig_mask_5")

        self.gridLayout_8.addWidget(self.caen_g0_trig_mask_5, 1, 6, 1, 1)

        self.caen_g0_acq_mask_5 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_acq_mask_5.setObjectName(u"caen_g0_acq_mask_5")

        self.gridLayout_8.addWidget(self.caen_g0_acq_mask_5, 2, 6, 1, 1)

        self.caen_g0_trig_mask_3 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_trig_mask_3.setObjectName(u"caen_g0_trig_mask_3")

        self.gridLayout_8.addWidget(self.caen_g0_trig_mask_3, 1, 4, 1, 1)

        self.caen_g0_trig_mask_7 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_trig_mask_7.setObjectName(u"caen_g0_trig_mask_7")

        self.gridLayout_8.addWidget(self.caen_g0_trig_mask_7, 1, 8, 1, 1)

        self.caen_g0_trig_mask_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_trig_mask_2.setObjectName(u"caen_g0_trig_mask_2")

        self.gridLayout_8.addWidget(self.caen_g0_trig_mask_2, 1, 3, 1, 1)

        self.caen_g0_trig_mask_6 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_trig_mask_6.setObjectName(u"caen_g0_trig_mask_6")

        self.gridLayout_8.addWidget(self.caen_g0_trig_mask_6, 1, 7, 1, 1)

        self.caen_g0_acq_mask_3 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_acq_mask_3.setObjectName(u"caen_g0_acq_mask_3")

        self.gridLayout_8.addWidget(self.caen_g0_acq_mask_3, 2, 4, 1, 1)

        self.caen_g0_acq_mask_0 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_acq_mask_0.setObjectName(u"caen_g0_acq_mask_0")

        self.gridLayout_8.addWidget(self.caen_g0_acq_mask_0, 2, 1, 1, 1)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_23, 3, 0, 1, 1)

        self.caen_g0_acq_mask_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_acq_mask_2.setObjectName(u"caen_g0_acq_mask_2")

        self.gridLayout_8.addWidget(self.caen_g0_acq_mask_2, 2, 3, 1, 1)

        self.caen_g0_acq_mask_1 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_acq_mask_1.setObjectName(u"caen_g0_acq_mask_1")

        self.gridLayout_8.addWidget(self.caen_g0_acq_mask_1, 2, 2, 1, 1)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_8.addWidget(self.label_30, 0, 8, 1, 1)

        self.label_29 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_8.addWidget(self.label_29, 0, 7, 1, 1)

        self.label_28 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_8.addWidget(self.label_28, 0, 6, 1, 1)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_8.addWidget(self.label_27, 0, 5, 1, 1)

        self.label_26 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_8.addWidget(self.label_26, 0, 4, 1, 1)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_8.addWidget(self.label_25, 0, 3, 1, 1)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_8.addWidget(self.label_24, 0, 2, 1, 1)

        self.label_32 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_8.addWidget(self.label_32, 0, 1, 1, 1)

        self.caen_g0_offset_0 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_offset_0.setObjectName(u"caen_g0_offset_0")
        font = QFont()
        font.setKerning(True)
        self.caen_g0_offset_0.setFont(font)
        self.caen_g0_offset_0.setWrapping(False)
        self.caen_g0_offset_0.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.caen_g0_offset_0.setProperty("showGroupSeparator", False)
        self.caen_g0_offset_0.setMaximum(255)
        self.caen_g0_offset_0.setValue(0)

        self.gridLayout_8.addWidget(self.caen_g0_offset_0, 3, 1, 1, 1)

        self.caen_g0_offset_1 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_offset_1.setObjectName(u"caen_g0_offset_1")
        self.caen_g0_offset_1.setFont(font)
        self.caen_g0_offset_1.setWrapping(False)
        self.caen_g0_offset_1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.caen_g0_offset_1.setProperty("showGroupSeparator", False)
        self.caen_g0_offset_1.setMaximum(255)
        self.caen_g0_offset_1.setValue(0)

        self.gridLayout_8.addWidget(self.caen_g0_offset_1, 3, 2, 1, 1)

        self.caen_g0_offset_2 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_offset_2.setObjectName(u"caen_g0_offset_2")
        self.caen_g0_offset_2.setFont(font)
        self.caen_g0_offset_2.setWrapping(False)
        self.caen_g0_offset_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.caen_g0_offset_2.setProperty("showGroupSeparator", False)
        self.caen_g0_offset_2.setMaximum(255)
        self.caen_g0_offset_2.setValue(0)

        self.gridLayout_8.addWidget(self.caen_g0_offset_2, 3, 3, 1, 1)

        self.caen_g0_offset_3 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_offset_3.setObjectName(u"caen_g0_offset_3")
        self.caen_g0_offset_3.setFont(font)
        self.caen_g0_offset_3.setWrapping(False)
        self.caen_g0_offset_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.caen_g0_offset_3.setProperty("showGroupSeparator", False)
        self.caen_g0_offset_3.setMaximum(255)
        self.caen_g0_offset_3.setValue(0)

        self.gridLayout_8.addWidget(self.caen_g0_offset_3, 3, 4, 1, 1)

        self.caen_g0_offset_4 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_offset_4.setObjectName(u"caen_g0_offset_4")
        self.caen_g0_offset_4.setFont(font)
        self.caen_g0_offset_4.setWrapping(False)
        self.caen_g0_offset_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.caen_g0_offset_4.setProperty("showGroupSeparator", False)
        self.caen_g0_offset_4.setMaximum(255)
        self.caen_g0_offset_4.setValue(0)

        self.gridLayout_8.addWidget(self.caen_g0_offset_4, 3, 5, 1, 1)

        self.caen_g0_offset_5 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_offset_5.setObjectName(u"caen_g0_offset_5")
        self.caen_g0_offset_5.setFont(font)
        self.caen_g0_offset_5.setWrapping(False)
        self.caen_g0_offset_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.caen_g0_offset_5.setProperty("showGroupSeparator", False)
        self.caen_g0_offset_5.setMaximum(255)
        self.caen_g0_offset_5.setValue(0)

        self.gridLayout_8.addWidget(self.caen_g0_offset_5, 3, 6, 1, 1)

        self.caen_g0_offset_6 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_offset_6.setObjectName(u"caen_g0_offset_6")
        self.caen_g0_offset_6.setFont(font)
        self.caen_g0_offset_6.setWrapping(False)
        self.caen_g0_offset_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.caen_g0_offset_6.setProperty("showGroupSeparator", False)
        self.caen_g0_offset_6.setMaximum(255)
        self.caen_g0_offset_6.setValue(0)

        self.gridLayout_8.addWidget(self.caen_g0_offset_6, 3, 7, 1, 1)

        self.caen_g0_offset_7 = QSpinBox(self.scrollAreaWidgetContents_2)
        self.caen_g0_offset_7.setObjectName(u"caen_g0_offset_7")
        self.caen_g0_offset_7.setFont(font)
        self.caen_g0_offset_7.setWrapping(False)
        self.caen_g0_offset_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.caen_g0_offset_7.setProperty("showGroupSeparator", False)
        self.caen_g0_offset_7.setMaximum(255)
        self.caen_g0_offset_7.setValue(0)

        self.gridLayout_8.addWidget(self.caen_g0_offset_7, 3, 8, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_8)

        self.verticalSpacer_4 = QSpacerItem(20, 368, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)

        self.sipm_scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.sipm_scroll_area)

        self.tabWidget.addTab(self.scint_tab, "")
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
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 390, 438))
        self.scrollAreaWidgetContents_6.setMaximumSize(QSize(1000, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.acous_general_grid = QGridLayout()
        self.acous_general_grid.setSpacing(3)
        self.acous_general_grid.setObjectName(u"acous_general_grid")
        self.acous_trig_delay_box = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_trig_delay_box.setObjectName(u"acous_trig_delay_box")

        self.acous_general_grid.addWidget(self.acous_trig_delay_box, 3, 3, 1, 1)

        self.acous_post_trig_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_post_trig_label.setObjectName(u"acous_post_trig_label")
        self.acous_post_trig_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_general_grid.addWidget(self.acous_post_trig_label, 3, 0, 1, 1)

        self.acous_trig_delay_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_trig_delay_label.setObjectName(u"acous_trig_delay_label")
        self.acous_trig_delay_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_general_grid.addWidget(self.acous_trig_delay_label, 3, 2, 1, 1)

        self.acous_trig_timeout_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_trig_timeout_label.setObjectName(u"acous_trig_timeout_label")
        self.acous_trig_timeout_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_general_grid.addWidget(self.acous_trig_timeout_label, 2, 2, 1, 1)

        self.acous_post_trig_box = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_post_trig_box.setObjectName(u"acous_post_trig_box")

        self.acous_general_grid.addWidget(self.acous_post_trig_box, 3, 1, 1, 1)

        self.acous_pre_trig_box = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_pre_trig_box.setObjectName(u"acous_pre_trig_box")

        self.acous_general_grid.addWidget(self.acous_pre_trig_box, 2, 1, 1, 1)

        self.acous_sample_rate_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_sample_rate_label.setObjectName(u"acous_sample_rate_label")
        self.acous_sample_rate_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_general_grid.addWidget(self.acous_sample_rate_label, 1, 0, 1, 1)

        self.acous_trig_timeout_box = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_trig_timeout_box.setObjectName(u"acous_trig_timeout_box")

        self.acous_general_grid.addWidget(self.acous_trig_timeout_box, 2, 3, 1, 1)

        self.acous_sample_rate_box = QComboBox(self.scrollAreaWidgetContents_6)
        self.acous_sample_rate_box.addItem("")
        self.acous_sample_rate_box.setObjectName(u"acous_sample_rate_box")

        self.acous_general_grid.addWidget(self.acous_sample_rate_box, 1, 1, 1, 3)

        self.acous_pre_trig_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_pre_trig_label.setObjectName(u"acous_pre_trig_label")
        self.acous_pre_trig_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_general_grid.addWidget(self.acous_pre_trig_label, 2, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents_6)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.acous_general_grid.addWidget(self.label, 0, 0, 1, 4)


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
        font2 = QFont()
        font2.setKerning(False)
        self.acous_range_ch8.setFont(font2)
        self.acous_range_ch8.setButtonSymbols(QAbstractSpinBox.NoButtons)

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
        self.acous_range_ch3.setFont(font2)
        self.acous_range_ch3.setButtonSymbols(QAbstractSpinBox.NoButtons)

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
        self.acous_range_ch6.setFont(font2)
        self.acous_range_ch6.setButtonSymbols(QAbstractSpinBox.NoButtons)

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
        self.acous_range_ch2.setFont(font2)
        self.acous_range_ch2.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.acous_per_ch_grid.addWidget(self.acous_range_ch2, 2, 2, 1, 1)

        self.acous_ch4_label = QLabel(self.scrollAreaWidgetContents_6)
        self.acous_ch4_label.setObjectName(u"acous_ch4_label")
        self.acous_ch4_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acous_per_ch_grid.addWidget(self.acous_ch4_label, 4, 0, 1, 1)

        self.acous_range_ch7 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_range_ch7.setObjectName(u"acous_range_ch7")
        self.acous_range_ch7.setFont(font2)
        self.acous_range_ch7.setButtonSymbols(QAbstractSpinBox.NoButtons)

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
        self.acous_range_ch5.setFont(font2)
        self.acous_range_ch5.setButtonSymbols(QAbstractSpinBox.NoButtons)

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
        self.acous_range_ch1.setFont(font2)
        self.acous_range_ch1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.acous_range_ch1.setStepType(QAbstractSpinBox.DefaultStepType)

        self.acous_per_ch_grid.addWidget(self.acous_range_ch1, 1, 2, 1, 1)

        self.acous_range_ch4 = QSpinBox(self.scrollAreaWidgetContents_6)
        self.acous_range_ch4.setObjectName(u"acous_range_ch4")
        self.acous_range_ch4.setFont(font2)
        self.acous_range_ch4.setButtonSymbols(QAbstractSpinBox.NoButtons)

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

        self.acous_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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
        self.cam_scroll_area.setFont(font)
        self.cam_scroll_area.setFrameShape(QFrame.NoFrame)
        self.cam_scroll_area.setFrameShadow(QFrame.Plain)
        self.cam_scroll_area.setLineWidth(0)
        self.cam_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 376, 481))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(1000, 16777215))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.cam3_buffer_len = QSpinBox(self.scrollAreaWidgetContents)
        self.cam3_buffer_len.setObjectName(u"cam3_buffer_len")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cam3_buffer_len.sizePolicy().hasHeightForWidth())
        self.cam3_buffer_len.setSizePolicy(sizePolicy2)
        self.cam3_buffer_len.setMinimum(1)
        self.cam3_buffer_len.setMaximum(1000)

        self.gridLayout_5.addWidget(self.cam3_buffer_len, 11, 3, 1, 1)

        self.cam2_data_path = QLineEdit(self.scrollAreaWidgetContents)
        self.cam2_data_path.setObjectName(u"cam2_data_path")

        self.gridLayout_5.addWidget(self.cam2_data_path, 3, 2, 1, 1)

        self.mode_label = QLabel(self.scrollAreaWidgetContents)
        self.mode_label.setObjectName(u"mode_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mode_label.sizePolicy().hasHeightForWidth())
        self.mode_label.setSizePolicy(sizePolicy3)
        self.mode_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.mode_label, 5, 0, 1, 1)

        self.cam2_adc_threshold = QSpinBox(self.scrollAreaWidgetContents)
        self.cam2_adc_threshold.setObjectName(u"cam2_adc_threshold")
        sizePolicy2.setHeightForWidth(self.cam2_adc_threshold.sizePolicy().hasHeightForWidth())
        self.cam2_adc_threshold.setSizePolicy(sizePolicy2)
        self.cam2_adc_threshold.setMaximum(10000)

        self.gridLayout_5.addWidget(self.cam2_adc_threshold, 13, 2, 1, 1)

        self.cam3_config_path = QLineEdit(self.scrollAreaWidgetContents)
        self.cam3_config_path.setObjectName(u"cam3_config_path")

        self.gridLayout_5.addWidget(self.cam3_config_path, 2, 3, 1, 1)

        self.cam2_label = QLabel(self.scrollAreaWidgetContents)
        self.cam2_label.setObjectName(u"cam2_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cam2_label.sizePolicy().hasHeightForWidth())
        self.cam2_label.setSizePolicy(sizePolicy4)
        self.cam2_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.cam2_label, 0, 2, 1, 1)

        self.cam1_trig_wait = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cam1_trig_wait.setObjectName(u"cam1_trig_wait")
        sizePolicy2.setHeightForWidth(self.cam1_trig_wait.sizePolicy().hasHeightForWidth())
        self.cam1_trig_wait.setSizePolicy(sizePolicy2)
        self.cam1_trig_wait.setMaximum(1000.000000000000000)

        self.gridLayout_5.addWidget(self.cam1_trig_wait, 9, 1, 1, 1)

        self.cam2_trig_pin = QSpinBox(self.scrollAreaWidgetContents)
        self.cam2_trig_pin.setObjectName(u"cam2_trig_pin")
        sizePolicy2.setHeightForWidth(self.cam2_trig_pin.sizePolicy().hasHeightForWidth())
        self.cam2_trig_pin.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam2_trig_pin, 24, 2, 1, 1)

        self.cam2_buffer_len = QSpinBox(self.scrollAreaWidgetContents)
        self.cam2_buffer_len.setObjectName(u"cam2_buffer_len")
        sizePolicy2.setHeightForWidth(self.cam2_buffer_len.sizePolicy().hasHeightForWidth())
        self.cam2_buffer_len.setSizePolicy(sizePolicy2)
        self.cam2_buffer_len.setMinimum(1)
        self.cam2_buffer_len.setMaximum(1000)

        self.gridLayout_5.addWidget(self.cam2_buffer_len, 11, 2, 1, 1)

        self.ip_addr_label = QLabel(self.scrollAreaWidgetContents)
        self.ip_addr_label.setObjectName(u"ip_addr_label")
        sizePolicy3.setHeightForWidth(self.ip_addr_label.sizePolicy().hasHeightForWidth())
        self.ip_addr_label.setSizePolicy(sizePolicy3)
        self.ip_addr_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.ip_addr_label, 4, 0, 1, 1)

        self.post_trig_len_label = QLabel(self.scrollAreaWidgetContents)
        self.post_trig_len_label.setObjectName(u"post_trig_len_label")
        sizePolicy3.setHeightForWidth(self.post_trig_len_label.sizePolicy().hasHeightForWidth())
        self.post_trig_len_label.setSizePolicy(sizePolicy3)
        self.post_trig_len_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.post_trig_len_label, 12, 0, 1, 1)

        self.cam2_trig_wait = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cam2_trig_wait.setObjectName(u"cam2_trig_wait")
        sizePolicy2.setHeightForWidth(self.cam2_trig_wait.sizePolicy().hasHeightForWidth())
        self.cam2_trig_wait.setSizePolicy(sizePolicy2)
        self.cam2_trig_wait.setMaximum(1000.000000000000000)

        self.gridLayout_5.addWidget(self.cam2_trig_wait, 9, 2, 1, 1)

        self.cam2_image_format = QComboBox(self.scrollAreaWidgetContents)
        self.cam2_image_format.addItem("")
        self.cam2_image_format.addItem("")
        self.cam2_image_format.addItem("")
        self.cam2_image_format.setObjectName(u"cam2_image_format")

        self.gridLayout_5.addWidget(self.cam2_image_format, 17, 2, 1, 1)

        self.cam3_image_format = QComboBox(self.scrollAreaWidgetContents)
        self.cam3_image_format.addItem("")
        self.cam3_image_format.addItem("")
        self.cam3_image_format.addItem("")
        self.cam3_image_format.setObjectName(u"cam3_image_format")

        self.gridLayout_5.addWidget(self.cam3_image_format, 17, 3, 1, 1)

        self.adc_threshold_label = QLabel(self.scrollAreaWidgetContents)
        self.adc_threshold_label.setObjectName(u"adc_threshold_label")
        sizePolicy3.setHeightForWidth(self.adc_threshold_label.sizePolicy().hasHeightForWidth())
        self.adc_threshold_label.setSizePolicy(sizePolicy3)
        self.adc_threshold_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.adc_threshold_label, 13, 0, 1, 1)

        self.date_format_label = QLabel(self.scrollAreaWidgetContents)
        self.date_format_label.setObjectName(u"date_format_label")
        sizePolicy3.setHeightForWidth(self.date_format_label.sizePolicy().hasHeightForWidth())
        self.date_format_label.setSizePolicy(sizePolicy3)
        self.date_format_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.date_format_label, 18, 0, 1, 1)

        self.state_pin_label = QLabel(self.scrollAreaWidgetContents)
        self.state_pin_label.setObjectName(u"state_pin_label")
        sizePolicy3.setHeightForWidth(self.state_pin_label.sizePolicy().hasHeightForWidth())
        self.state_pin_label.setSizePolicy(sizePolicy3)
        self.state_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.state_pin_label, 23, 0, 1, 1)

        self.cam2_date_format = QLineEdit(self.scrollAreaWidgetContents)
        self.cam2_date_format.setObjectName(u"cam2_date_format")

        self.gridLayout_5.addWidget(self.cam2_date_format, 18, 2, 1, 1)

        self.data_path_label = QLabel(self.scrollAreaWidgetContents)
        self.data_path_label.setObjectName(u"data_path_label")
        sizePolicy3.setHeightForWidth(self.data_path_label.sizePolicy().hasHeightForWidth())
        self.data_path_label.setSizePolicy(sizePolicy3)
        self.data_path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.data_path_label, 3, 0, 1, 1)

        self.cam3_post_trig_len = QSpinBox(self.scrollAreaWidgetContents)
        self.cam3_post_trig_len.setObjectName(u"cam3_post_trig_len")
        sizePolicy2.setHeightForWidth(self.cam3_post_trig_len.sizePolicy().hasHeightForWidth())
        self.cam3_post_trig_len.setSizePolicy(sizePolicy2)
        self.cam3_post_trig_len.setMaximum(1000)

        self.gridLayout_5.addWidget(self.cam3_post_trig_len, 12, 3, 1, 1)

        self.cam2_state_comm_pin = QSpinBox(self.scrollAreaWidgetContents)
        self.cam2_state_comm_pin.setObjectName(u"cam2_state_comm_pin")
        sizePolicy2.setHeightForWidth(self.cam2_state_comm_pin.sizePolicy().hasHeightForWidth())
        self.cam2_state_comm_pin.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam2_state_comm_pin, 19, 2, 1, 1)

        self.cam3_trig_wait = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.cam3_trig_wait.setObjectName(u"cam3_trig_wait")
        sizePolicy2.setHeightForWidth(self.cam3_trig_wait.sizePolicy().hasHeightForWidth())
        self.cam3_trig_wait.setSizePolicy(sizePolicy2)
        self.cam3_trig_wait.setMaximum(1000.000000000000000)

        self.gridLayout_5.addWidget(self.cam3_trig_wait, 9, 3, 1, 1)

        self.cam2_config_path = QLineEdit(self.scrollAreaWidgetContents)
        self.cam2_config_path.setObjectName(u"cam2_config_path")

        self.gridLayout_5.addWidget(self.cam2_config_path, 2, 2, 1, 1)

        self.cam3_ip_addr = QLineEdit(self.scrollAreaWidgetContents)
        self.cam3_ip_addr.setObjectName(u"cam3_ip_addr")

        self.gridLayout_5.addWidget(self.cam3_ip_addr, 4, 3, 1, 1)

        self.cam1_buffer_len = QSpinBox(self.scrollAreaWidgetContents)
        self.cam1_buffer_len.setObjectName(u"cam1_buffer_len")
        sizePolicy2.setHeightForWidth(self.cam1_buffer_len.sizePolicy().hasHeightForWidth())
        self.cam1_buffer_len.setSizePolicy(sizePolicy2)
        self.cam1_buffer_len.setMinimum(1)
        self.cam1_buffer_len.setMaximum(1000)

        self.gridLayout_5.addWidget(self.cam1_buffer_len, 11, 1, 1, 1)

        self.cam2_ip_addr = QLineEdit(self.scrollAreaWidgetContents)
        self.cam2_ip_addr.setObjectName(u"cam2_ip_addr")

        self.gridLayout_5.addWidget(self.cam2_ip_addr, 4, 2, 1, 1)

        self.trig_pin_label = QLabel(self.scrollAreaWidgetContents)
        self.trig_pin_label.setObjectName(u"trig_pin_label")
        sizePolicy3.setHeightForWidth(self.trig_pin_label.sizePolicy().hasHeightForWidth())
        self.trig_pin_label.setSizePolicy(sizePolicy3)
        self.trig_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.trig_pin_label, 24, 0, 1, 1)

        self.cam1_trig_pin = QSpinBox(self.scrollAreaWidgetContents)
        self.cam1_trig_pin.setObjectName(u"cam1_trig_pin")
        sizePolicy2.setHeightForWidth(self.cam1_trig_pin.sizePolicy().hasHeightForWidth())
        self.cam1_trig_pin.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam1_trig_pin, 24, 1, 1, 1)

        self.cam3_label = QLabel(self.scrollAreaWidgetContents)
        self.cam3_label.setObjectName(u"cam3_label")
        sizePolicy4.setHeightForWidth(self.cam3_label.sizePolicy().hasHeightForWidth())
        self.cam3_label.setSizePolicy(sizePolicy4)
        self.cam3_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.cam3_label, 0, 3, 1, 1)

        self.cam1_mode = QSpinBox(self.scrollAreaWidgetContents)
        self.cam1_mode.setObjectName(u"cam1_mode")
        sizePolicy2.setHeightForWidth(self.cam1_mode.sizePolicy().hasHeightForWidth())
        self.cam1_mode.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam1_mode, 5, 1, 1, 1)

        self.cam_spacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.cam_spacer, 25, 0, 1, 4)

        self.cam2_trig_enbl_pin = QSpinBox(self.scrollAreaWidgetContents)
        self.cam2_trig_enbl_pin.setObjectName(u"cam2_trig_enbl_pin")
        sizePolicy2.setHeightForWidth(self.cam2_trig_enbl_pin.sizePolicy().hasHeightForWidth())
        self.cam2_trig_enbl_pin.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam2_trig_enbl_pin, 21, 2, 1, 1)

        self.trig_latch_pin_label = QLabel(self.scrollAreaWidgetContents)
        self.trig_latch_pin_label.setObjectName(u"trig_latch_pin_label")
        sizePolicy3.setHeightForWidth(self.trig_latch_pin_label.sizePolicy().hasHeightForWidth())
        self.trig_latch_pin_label.setSizePolicy(sizePolicy3)
        self.trig_latch_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.trig_latch_pin_label, 22, 0, 1, 1)

        self.exposure_label = QLabel(self.scrollAreaWidgetContents)
        self.exposure_label.setObjectName(u"exposure_label")
        sizePolicy3.setHeightForWidth(self.exposure_label.sizePolicy().hasHeightForWidth())
        self.exposure_label.setSizePolicy(sizePolicy3)
        self.exposure_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.exposure_label, 10, 0, 1, 1)

        self.cam1_state_pin = QSpinBox(self.scrollAreaWidgetContents)
        self.cam1_state_pin.setObjectName(u"cam1_state_pin")
        sizePolicy2.setHeightForWidth(self.cam1_state_pin.sizePolicy().hasHeightForWidth())
        self.cam1_state_pin.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam1_state_pin, 23, 1, 1, 1)

        self.cam3_trig_enbl_pin = QSpinBox(self.scrollAreaWidgetContents)
        self.cam3_trig_enbl_pin.setObjectName(u"cam3_trig_enbl_pin")
        sizePolicy2.setHeightForWidth(self.cam3_trig_enbl_pin.sizePolicy().hasHeightForWidth())
        self.cam3_trig_enbl_pin.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam3_trig_enbl_pin, 21, 3, 1, 1)

        self.cam3_state_pin = QSpinBox(self.scrollAreaWidgetContents)
        self.cam3_state_pin.setObjectName(u"cam3_state_pin")
        sizePolicy2.setHeightForWidth(self.cam3_state_pin.sizePolicy().hasHeightForWidth())
        self.cam3_state_pin.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam3_state_pin, 23, 3, 1, 1)

        self.cam1_adc_threshold = QSpinBox(self.scrollAreaWidgetContents)
        self.cam1_adc_threshold.setObjectName(u"cam1_adc_threshold")
        sizePolicy2.setHeightForWidth(self.cam1_adc_threshold.sizePolicy().hasHeightForWidth())
        self.cam1_adc_threshold.setSizePolicy(sizePolicy2)
        self.cam1_adc_threshold.setMaximum(10000)

        self.gridLayout_5.addWidget(self.cam1_adc_threshold, 13, 1, 1, 1)

        self.cam1_state_comm_pin = QSpinBox(self.scrollAreaWidgetContents)
        self.cam1_state_comm_pin.setObjectName(u"cam1_state_comm_pin")
        sizePolicy2.setHeightForWidth(self.cam1_state_comm_pin.sizePolicy().hasHeightForWidth())
        self.cam1_state_comm_pin.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam1_state_comm_pin, 19, 1, 1, 1)

        self.cam3_exposure = QSpinBox(self.scrollAreaWidgetContents)
        self.cam3_exposure.setObjectName(u"cam3_exposure")
        sizePolicy2.setHeightForWidth(self.cam3_exposure.sizePolicy().hasHeightForWidth())
        self.cam3_exposure.setSizePolicy(sizePolicy2)
        self.cam3_exposure.setMaximum(10000)

        self.gridLayout_5.addWidget(self.cam3_exposure, 10, 3, 1, 1)

        self.cam2_trig_latch_pin = QSpinBox(self.scrollAreaWidgetContents)
        self.cam2_trig_latch_pin.setObjectName(u"cam2_trig_latch_pin")
        sizePolicy2.setHeightForWidth(self.cam2_trig_latch_pin.sizePolicy().hasHeightForWidth())
        self.cam2_trig_latch_pin.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam2_trig_latch_pin, 22, 2, 1, 1)

        self.cam1_pix_threshold = QSpinBox(self.scrollAreaWidgetContents)
        self.cam1_pix_threshold.setObjectName(u"cam1_pix_threshold")
        sizePolicy2.setHeightForWidth(self.cam1_pix_threshold.sizePolicy().hasHeightForWidth())
        self.cam1_pix_threshold.setSizePolicy(sizePolicy2)
        self.cam1_pix_threshold.setMaximum(100000)

        self.gridLayout_5.addWidget(self.cam1_pix_threshold, 14, 1, 1, 1)

        self.cam3_trig_pin = QSpinBox(self.scrollAreaWidgetContents)
        self.cam3_trig_pin.setObjectName(u"cam3_trig_pin")
        sizePolicy2.setHeightForWidth(self.cam3_trig_pin.sizePolicy().hasHeightForWidth())
        self.cam3_trig_pin.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam3_trig_pin, 24, 3, 1, 1)

        self.cam2_pix_threshold = QSpinBox(self.scrollAreaWidgetContents)
        self.cam2_pix_threshold.setObjectName(u"cam2_pix_threshold")
        sizePolicy2.setHeightForWidth(self.cam2_pix_threshold.sizePolicy().hasHeightForWidth())
        self.cam2_pix_threshold.setSizePolicy(sizePolicy2)
        self.cam2_pix_threshold.setMaximum(100000)

        self.gridLayout_5.addWidget(self.cam2_pix_threshold, 14, 2, 1, 1)

        self.cam_config_path_label = QLabel(self.scrollAreaWidgetContents)
        self.cam_config_path_label.setObjectName(u"cam_config_path_label")
        sizePolicy3.setHeightForWidth(self.cam_config_path_label.sizePolicy().hasHeightForWidth())
        self.cam_config_path_label.setSizePolicy(sizePolicy3)
        self.cam_config_path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.cam_config_path_label, 2, 0, 1, 1)

        self.cam1_data_path = QLineEdit(self.scrollAreaWidgetContents)
        self.cam1_data_path.setObjectName(u"cam1_data_path")

        self.gridLayout_5.addWidget(self.cam1_data_path, 3, 1, 1, 1)

        self.cam3_data_path = QLineEdit(self.scrollAreaWidgetContents)
        self.cam3_data_path.setObjectName(u"cam3_data_path")

        self.gridLayout_5.addWidget(self.cam3_data_path, 3, 3, 1, 1)

        self.cam1_ip_addr = QLineEdit(self.scrollAreaWidgetContents)
        self.cam1_ip_addr.setObjectName(u"cam1_ip_addr")

        self.gridLayout_5.addWidget(self.cam1_ip_addr, 4, 1, 1, 1)

        self.trig_wait_label = QLabel(self.scrollAreaWidgetContents)
        self.trig_wait_label.setObjectName(u"trig_wait_label")
        sizePolicy3.setHeightForWidth(self.trig_wait_label.sizePolicy().hasHeightForWidth())
        self.trig_wait_label.setSizePolicy(sizePolicy3)
        self.trig_wait_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.trig_wait_label, 9, 0, 1, 1)

        self.pix_threshold_label = QLabel(self.scrollAreaWidgetContents)
        self.pix_threshold_label.setObjectName(u"pix_threshold_label")
        sizePolicy3.setHeightForWidth(self.pix_threshold_label.sizePolicy().hasHeightForWidth())
        self.pix_threshold_label.setSizePolicy(sizePolicy3)
        self.pix_threshold_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.pix_threshold_label, 14, 0, 1, 1)

        self.cam3_date_format = QLineEdit(self.scrollAreaWidgetContents)
        self.cam3_date_format.setObjectName(u"cam3_date_format")

        self.gridLayout_5.addWidget(self.cam3_date_format, 18, 3, 1, 1)

        self.buffer_len_label = QLabel(self.scrollAreaWidgetContents)
        self.buffer_len_label.setObjectName(u"buffer_len_label")
        sizePolicy3.setHeightForWidth(self.buffer_len_label.sizePolicy().hasHeightForWidth())
        self.buffer_len_label.setSizePolicy(sizePolicy3)
        self.buffer_len_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.buffer_len_label, 11, 0, 1, 1)

        self.cam1_exposure = QSpinBox(self.scrollAreaWidgetContents)
        self.cam1_exposure.setObjectName(u"cam1_exposure")
        sizePolicy2.setHeightForWidth(self.cam1_exposure.sizePolicy().hasHeightForWidth())
        self.cam1_exposure.setSizePolicy(sizePolicy2)
        self.cam1_exposure.setMaximum(10000)

        self.gridLayout_5.addWidget(self.cam1_exposure, 10, 1, 1, 1)

        self.cam1_post_trig_len = QSpinBox(self.scrollAreaWidgetContents)
        self.cam1_post_trig_len.setObjectName(u"cam1_post_trig_len")
        sizePolicy2.setHeightForWidth(self.cam1_post_trig_len.sizePolicy().hasHeightForWidth())
        self.cam1_post_trig_len.setSizePolicy(sizePolicy2)
        self.cam1_post_trig_len.setMaximum(1000)

        self.gridLayout_5.addWidget(self.cam1_post_trig_len, 12, 1, 1, 1)

        self.cam2_post_trig_len = QSpinBox(self.scrollAreaWidgetContents)
        self.cam2_post_trig_len.setObjectName(u"cam2_post_trig_len")
        sizePolicy2.setHeightForWidth(self.cam2_post_trig_len.sizePolicy().hasHeightForWidth())
        self.cam2_post_trig_len.setSizePolicy(sizePolicy2)
        self.cam2_post_trig_len.setMaximum(1000)

        self.gridLayout_5.addWidget(self.cam2_post_trig_len, 12, 2, 1, 1)

        self.cam1_trig_enbl_pin = QSpinBox(self.scrollAreaWidgetContents)
        self.cam1_trig_enbl_pin.setObjectName(u"cam1_trig_enbl_pin")
        sizePolicy2.setHeightForWidth(self.cam1_trig_enbl_pin.sizePolicy().hasHeightForWidth())
        self.cam1_trig_enbl_pin.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam1_trig_enbl_pin, 21, 1, 1, 1)

        self.cam3_mode = QSpinBox(self.scrollAreaWidgetContents)
        self.cam3_mode.setObjectName(u"cam3_mode")
        sizePolicy2.setHeightForWidth(self.cam3_mode.sizePolicy().hasHeightForWidth())
        self.cam3_mode.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam3_mode, 5, 3, 1, 1)

        self.trig_enbl_pin_label = QLabel(self.scrollAreaWidgetContents)
        self.trig_enbl_pin_label.setObjectName(u"trig_enbl_pin_label")
        sizePolicy3.setHeightForWidth(self.trig_enbl_pin_label.sizePolicy().hasHeightForWidth())
        self.trig_enbl_pin_label.setSizePolicy(sizePolicy3)
        self.trig_enbl_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.trig_enbl_pin_label, 21, 0, 1, 1)

        self.cam1_image_format = QComboBox(self.scrollAreaWidgetContents)
        self.cam1_image_format.addItem("")
        self.cam1_image_format.addItem("")
        self.cam1_image_format.addItem("")
        self.cam1_image_format.setObjectName(u"cam1_image_format")

        self.gridLayout_5.addWidget(self.cam1_image_format, 17, 1, 1, 1)

        self.cam3_trig_latch_pin = QSpinBox(self.scrollAreaWidgetContents)
        self.cam3_trig_latch_pin.setObjectName(u"cam3_trig_latch_pin")
        sizePolicy2.setHeightForWidth(self.cam3_trig_latch_pin.sizePolicy().hasHeightForWidth())
        self.cam3_trig_latch_pin.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam3_trig_latch_pin, 22, 3, 1, 1)

        self.cam1_date_format = QLineEdit(self.scrollAreaWidgetContents)
        self.cam1_date_format.setObjectName(u"cam1_date_format")

        self.gridLayout_5.addWidget(self.cam1_date_format, 18, 1, 1, 1)

        self.cam2_mode = QSpinBox(self.scrollAreaWidgetContents)
        self.cam2_mode.setObjectName(u"cam2_mode")
        sizePolicy2.setHeightForWidth(self.cam2_mode.sizePolicy().hasHeightForWidth())
        self.cam2_mode.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam2_mode, 5, 2, 1, 1)

        self.cam1_label = QLabel(self.scrollAreaWidgetContents)
        self.cam1_label.setObjectName(u"cam1_label")
        sizePolicy4.setHeightForWidth(self.cam1_label.sizePolicy().hasHeightForWidth())
        self.cam1_label.setSizePolicy(sizePolicy4)
        self.cam1_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.cam1_label, 0, 1, 1, 1)

        self.cam3_state_comm_pin = QSpinBox(self.scrollAreaWidgetContents)
        self.cam3_state_comm_pin.setObjectName(u"cam3_state_comm_pin")
        sizePolicy2.setHeightForWidth(self.cam3_state_comm_pin.sizePolicy().hasHeightForWidth())
        self.cam3_state_comm_pin.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam3_state_comm_pin, 19, 3, 1, 1)

        self.cam2_state_pin = QSpinBox(self.scrollAreaWidgetContents)
        self.cam2_state_pin.setObjectName(u"cam2_state_pin")
        sizePolicy2.setHeightForWidth(self.cam2_state_pin.sizePolicy().hasHeightForWidth())
        self.cam2_state_pin.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam2_state_pin, 23, 2, 1, 1)

        self.cam1_config_path = QLineEdit(self.scrollAreaWidgetContents)
        self.cam1_config_path.setObjectName(u"cam1_config_path")

        self.gridLayout_5.addWidget(self.cam1_config_path, 2, 1, 1, 1)

        self.cam3_pix_threshold = QSpinBox(self.scrollAreaWidgetContents)
        self.cam3_pix_threshold.setObjectName(u"cam3_pix_threshold")
        sizePolicy2.setHeightForWidth(self.cam3_pix_threshold.sizePolicy().hasHeightForWidth())
        self.cam3_pix_threshold.setSizePolicy(sizePolicy2)
        self.cam3_pix_threshold.setMaximum(100000)

        self.gridLayout_5.addWidget(self.cam3_pix_threshold, 14, 3, 1, 1)

        self.state_comm_pin_label = QLabel(self.scrollAreaWidgetContents)
        self.state_comm_pin_label.setObjectName(u"state_comm_pin_label")
        sizePolicy3.setHeightForWidth(self.state_comm_pin_label.sizePolicy().hasHeightForWidth())
        self.state_comm_pin_label.setSizePolicy(sizePolicy3)
        self.state_comm_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.state_comm_pin_label, 19, 0, 1, 1)

        self.image_format_label = QLabel(self.scrollAreaWidgetContents)
        self.image_format_label.setObjectName(u"image_format_label")
        sizePolicy3.setHeightForWidth(self.image_format_label.sizePolicy().hasHeightForWidth())
        self.image_format_label.setSizePolicy(sizePolicy3)
        self.image_format_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.image_format_label, 17, 0, 1, 1)

        self.cam3_adc_threshold = QSpinBox(self.scrollAreaWidgetContents)
        self.cam3_adc_threshold.setObjectName(u"cam3_adc_threshold")
        sizePolicy2.setHeightForWidth(self.cam3_adc_threshold.sizePolicy().hasHeightForWidth())
        self.cam3_adc_threshold.setSizePolicy(sizePolicy2)
        self.cam3_adc_threshold.setMaximum(10000)

        self.gridLayout_5.addWidget(self.cam3_adc_threshold, 13, 3, 1, 1)

        self.cam2_exposure = QSpinBox(self.scrollAreaWidgetContents)
        self.cam2_exposure.setObjectName(u"cam2_exposure")
        sizePolicy2.setHeightForWidth(self.cam2_exposure.sizePolicy().hasHeightForWidth())
        self.cam2_exposure.setSizePolicy(sizePolicy2)
        self.cam2_exposure.setMaximum(10000)

        self.gridLayout_5.addWidget(self.cam2_exposure, 10, 2, 1, 1)

        self.cam1_trig_latch_pin = QSpinBox(self.scrollAreaWidgetContents)
        self.cam1_trig_latch_pin.setObjectName(u"cam1_trig_latch_pin")
        sizePolicy2.setHeightForWidth(self.cam1_trig_latch_pin.sizePolicy().hasHeightForWidth())
        self.cam1_trig_latch_pin.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.cam1_trig_latch_pin, 22, 1, 1, 1)

        self.cam_rc_config_path_label = QLabel(self.scrollAreaWidgetContents)
        self.cam_rc_config_path_label.setObjectName(u"cam_rc_config_path_label")
        sizePolicy3.setHeightForWidth(self.cam_rc_config_path_label.sizePolicy().hasHeightForWidth())
        self.cam_rc_config_path_label.setSizePolicy(sizePolicy3)
        self.cam_rc_config_path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.cam_rc_config_path_label, 1, 0, 1, 1)

        self.cam1_rc_config_path = QLineEdit(self.scrollAreaWidgetContents)
        self.cam1_rc_config_path.setObjectName(u"cam1_rc_config_path")

        self.gridLayout_5.addWidget(self.cam1_rc_config_path, 1, 1, 1, 1)

        self.cam2_rc_config_path = QLineEdit(self.scrollAreaWidgetContents)
        self.cam2_rc_config_path.setObjectName(u"cam2_rc_config_path")

        self.gridLayout_5.addWidget(self.cam2_rc_config_path, 1, 2, 1, 1)

        self.cam3_rc_config_path = QLineEdit(self.scrollAreaWidgetContents)
        self.cam3_rc_config_path.setObjectName(u"cam3_rc_config_path")

        self.gridLayout_5.addWidget(self.cam3_rc_config_path, 1, 3, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 1)
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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 376, 534))
        self.scrollAreaWidgetContents_3.setMaximumSize(QSize(1000, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dio_general_grid_layout = QGridLayout()
        self.dio_general_grid_layout.setSpacing(3)
        self.dio_general_grid_layout.setObjectName(u"dio_general_grid_layout")
        self.dio_general_label = QLabel(self.scrollAreaWidgetContents_3)
        self.dio_general_label.setObjectName(u"dio_general_label")
        self.dio_general_label.setFont(font1)
        self.dio_general_label.setAlignment(Qt.AlignCenter)

        self.dio_general_grid_layout.addWidget(self.dio_general_label, 0, 0, 1, 3)

        self.trigger_arduino_label = QLabel(self.scrollAreaWidgetContents_3)
        self.trigger_arduino_label.setObjectName(u"trigger_arduino_label")

        self.dio_general_grid_layout.addWidget(self.trigger_arduino_label, 2, 0, 1, 1)

        self.clock_port_edit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.clock_port_edit.setObjectName(u"clock_port_edit")

        self.dio_general_grid_layout.addWidget(self.clock_port_edit, 3, 1, 1, 1)

        self.clock_sketch_edit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.clock_sketch_edit.setObjectName(u"clock_sketch_edit")

        self.dio_general_grid_layout.addWidget(self.clock_sketch_edit, 3, 2, 1, 1)

        self.position_arduino_label = QLabel(self.scrollAreaWidgetContents_3)
        self.position_arduino_label.setObjectName(u"position_arduino_label")

        self.dio_general_grid_layout.addWidget(self.position_arduino_label, 4, 0, 1, 1)

        self.clock_arduino_label = QLabel(self.scrollAreaWidgetContents_3)
        self.clock_arduino_label.setObjectName(u"clock_arduino_label")

        self.dio_general_grid_layout.addWidget(self.clock_arduino_label, 3, 0, 1, 1)

        self.position_port_edit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.position_port_edit.setObjectName(u"position_port_edit")

        self.dio_general_grid_layout.addWidget(self.position_port_edit, 4, 1, 1, 1)

        self.position_sketch_edit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.position_sketch_edit.setObjectName(u"position_sketch_edit")

        self.dio_general_grid_layout.addWidget(self.position_sketch_edit, 4, 2, 1, 1)

        self.arduino_port_label = QLabel(self.scrollAreaWidgetContents_3)
        self.arduino_port_label.setObjectName(u"arduino_port_label")

        self.dio_general_grid_layout.addWidget(self.arduino_port_label, 1, 1, 1, 1)

        self.trigger_sketch_edit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.trigger_sketch_edit.setObjectName(u"trigger_sketch_edit")

        self.dio_general_grid_layout.addWidget(self.trigger_sketch_edit, 2, 2, 1, 1)

        self.trigger_port_edit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.trigger_port_edit.setObjectName(u"trigger_port_edit")

        self.dio_general_grid_layout.addWidget(self.trigger_port_edit, 2, 1, 1, 1)

        self.trigger_sketch_but = QToolButton(self.scrollAreaWidgetContents_3)
        self.trigger_sketch_but.setObjectName(u"trigger_sketch_but")

        self.dio_general_grid_layout.addWidget(self.trigger_sketch_but, 2, 3, 1, 1)

        self.sketch_location_label = QLabel(self.scrollAreaWidgetContents_3)
        self.sketch_location_label.setObjectName(u"sketch_location_label")

        self.dio_general_grid_layout.addWidget(self.sketch_location_label, 1, 2, 1, 2)

        self.clock_sketch_but = QToolButton(self.scrollAreaWidgetContents_3)
        self.clock_sketch_but.setObjectName(u"clock_sketch_but")

        self.dio_general_grid_layout.addWidget(self.clock_sketch_but, 3, 3, 1, 1)

        self.position_sketch_but = QToolButton(self.scrollAreaWidgetContents_3)
        self.position_sketch_but.setObjectName(u"position_sketch_but")

        self.dio_general_grid_layout.addWidget(self.position_sketch_but, 4, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.dio_general_grid_layout)

        self.dio_line = QFrame(self.scrollAreaWidgetContents_3)
        self.dio_line.setObjectName(u"dio_line")
        self.dio_line.setFrameShape(QFrame.HLine)
        self.dio_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.dio_line)

        self.fifo_grid_layout = QGridLayout()
        self.fifo_grid_layout.setSpacing(3)
        self.fifo_grid_layout.setObjectName(u"fifo_grid_layout")
        self.fifo_grid_layout.setContentsMargins(-1, 0, -1, 0)
        self.trig_latch_pins_label = QLabel(self.scrollAreaWidgetContents_3)
        self.trig_latch_pins_label.setObjectName(u"trig_latch_pins_label")
        self.trig_latch_pins_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.fifo_grid_layout.addWidget(self.trig_latch_pins_label, 2, 0, 1, 1)

        self.trig_latch_pins_edit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.trig_latch_pins_edit.setObjectName(u"trig_latch_pins_edit")

        self.fifo_grid_layout.addWidget(self.trig_latch_pins_edit, 2, 1, 1, 3)

        self.trig_reset_pin_edit = QSpinBox(self.scrollAreaWidgetContents_3)
        self.trig_reset_pin_edit.setObjectName(u"trig_reset_pin_edit")

        self.fifo_grid_layout.addWidget(self.trig_reset_pin_edit, 3, 1, 1, 1)

        self.on_time_pin_edit = QSpinBox(self.scrollAreaWidgetContents_3)
        self.on_time_pin_edit.setObjectName(u"on_time_pin_edit")

        self.fifo_grid_layout.addWidget(self.on_time_pin_edit, 4, 1, 1, 1)

        self.trig_or_pin_label = QLabel(self.scrollAreaWidgetContents_3)
        self.trig_or_pin_label.setObjectName(u"trig_or_pin_label")
        self.trig_or_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.fifo_grid_layout.addWidget(self.trig_or_pin_label, 3, 2, 1, 1)

        self.heartbeat_pin_label = QLabel(self.scrollAreaWidgetContents_3)
        self.heartbeat_pin_label.setObjectName(u"heartbeat_pin_label")
        self.heartbeat_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.fifo_grid_layout.addWidget(self.heartbeat_pin_label, 4, 2, 1, 1)

        self.heartbeat_pin_edit = QSpinBox(self.scrollAreaWidgetContents_3)
        self.heartbeat_pin_edit.setObjectName(u"heartbeat_pin_edit")
        self.heartbeat_pin_edit.setFocusPolicy(Qt.StrongFocus)

        self.fifo_grid_layout.addWidget(self.heartbeat_pin_edit, 4, 3, 1, 1)

        self.trig_reset_pin_label = QLabel(self.scrollAreaWidgetContents_3)
        self.trig_reset_pin_label.setObjectName(u"trig_reset_pin_label")
        self.trig_reset_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.fifo_grid_layout.addWidget(self.trig_reset_pin_label, 3, 0, 1, 1)

        self.trig_in_pins_label = QLabel(self.scrollAreaWidgetContents_3)
        self.trig_in_pins_label.setObjectName(u"trig_in_pins_label")
        self.trig_in_pins_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.fifo_grid_layout.addWidget(self.trig_in_pins_label, 1, 0, 1, 1)

        self.trig_in_pins_edit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.trig_in_pins_edit.setObjectName(u"trig_in_pins_edit")

        self.fifo_grid_layout.addWidget(self.trig_in_pins_edit, 1, 1, 1, 3)

        self.on_time_pin_label = QLabel(self.scrollAreaWidgetContents_3)
        self.on_time_pin_label.setObjectName(u"on_time_pin_label")
        self.on_time_pin_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.fifo_grid_layout.addWidget(self.on_time_pin_label, 4, 0, 1, 1)

        self.fifo_layout = QLabel(self.scrollAreaWidgetContents_3)
        self.fifo_layout.setObjectName(u"fifo_layout")
        self.fifo_layout.setFont(font1)
        self.fifo_layout.setAlignment(Qt.AlignCenter)

        self.fifo_grid_layout.addWidget(self.fifo_layout, 0, 0, 1, 4)

        self.trig_or_pin_edit = QSpinBox(self.scrollAreaWidgetContents_3)
        self.trig_or_pin_edit.setObjectName(u"trig_or_pin_edit")
        self.trig_or_pin_edit.setFocusPolicy(Qt.StrongFocus)

        self.fifo_grid_layout.addWidget(self.trig_or_pin_edit, 3, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.fifo_grid_layout)

        self.dio_line_3 = QFrame(self.scrollAreaWidgetContents_3)
        self.dio_line_3.setObjectName(u"dio_line_3")
        self.dio_line_3.setFrameShape(QFrame.HLine)
        self.dio_line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.dio_line_3)

        self.gate_grid_layout = QGridLayout()
        self.gate_grid_layout.setSpacing(3)
        self.gate_grid_layout.setObjectName(u"gate_grid_layout")
        self.gate_grid_layout.setContentsMargins(0, 0, -1, -1)
        self.gate_period_wave5 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave5.setObjectName(u"gate_period_wave5")
        self.gate_period_wave5.setMaximum(1000000)

        self.gate_grid_layout.addWidget(self.gate_period_wave5, 7, 2, 1, 1)

        self.gate_pin_wave1 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave1.setObjectName(u"gate_pin_wave1")

        self.gate_grid_layout.addWidget(self.gate_pin_wave1, 3, 1, 1, 1)

        self.gate_polarity_wave1 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave1.addItem("")
        self.gate_polarity_wave1.addItem("")
        self.gate_polarity_wave1.setObjectName(u"gate_polarity_wave1")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave1, 3, 5, 1, 1)

        self.gate_polarity_wave5 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave5.addItem("")
        self.gate_polarity_wave5.addItem("")
        self.gate_polarity_wave5.setObjectName(u"gate_polarity_wave5")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave5, 7, 5, 1, 1)

        self.duty_wave2 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave2.setObjectName(u"duty_wave2")
        self.duty_wave2.setMaximum(100)

        self.gate_grid_layout.addWidget(self.duty_wave2, 4, 4, 1, 1)

        self.wave1_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave1_label.setObjectName(u"wave1_label")
        self.wave1_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave1_label, 3, 0, 1, 1)

        self.wave3_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave3_label.setObjectName(u"wave3_label")
        self.wave3_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave3_label, 5, 0, 1, 1)

        self.gate_pin_label = QLabel(self.scrollAreaWidgetContents_3)
        self.gate_pin_label.setObjectName(u"gate_pin_label")
        self.gate_pin_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.gate_pin_label, 1, 1, 1, 1)

        self.gate_pin_wave6 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave6.setObjectName(u"gate_pin_wave6")

        self.gate_grid_layout.addWidget(self.gate_pin_wave6, 8, 1, 1, 1)

        self.gate_phase_wave7 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave7.setObjectName(u"gate_phase_wave7")

        self.gate_grid_layout.addWidget(self.gate_phase_wave7, 9, 3, 1, 1)

        self.gate_phase_wave1 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave1.setObjectName(u"gate_phase_wave1")
        self.gate_phase_wave1.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.gate_phase_wave1.setKeyboardTracking(True)
        self.gate_phase_wave1.setMaximum(100)

        self.gate_grid_layout.addWidget(self.gate_phase_wave1, 3, 3, 1, 1)

        self.duty_wave8 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave8.setObjectName(u"duty_wave8")
        self.duty_wave8.setMaximum(100)

        self.gate_grid_layout.addWidget(self.duty_wave8, 10, 4, 1, 1)

        self.wave4_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave4_label.setObjectName(u"wave4_label")
        self.wave4_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave4_label, 6, 0, 1, 1)

        self.duty_wave3 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave3.setObjectName(u"duty_wave3")
        self.duty_wave3.setMaximum(100)

        self.gate_grid_layout.addWidget(self.duty_wave3, 5, 4, 1, 1)

        self.gate_phase_wave4 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave4.setObjectName(u"gate_phase_wave4")

        self.gate_grid_layout.addWidget(self.gate_phase_wave4, 6, 3, 1, 1)

        self.gate_polarity_wave8 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave8.addItem("")
        self.gate_polarity_wave8.addItem("")
        self.gate_polarity_wave8.setObjectName(u"gate_polarity_wave8")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave8, 10, 5, 1, 1)

        self.gate_polarity_wave7 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave7.addItem("")
        self.gate_polarity_wave7.addItem("")
        self.gate_polarity_wave7.setObjectName(u"gate_polarity_wave7")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave7, 9, 5, 1, 1)

        self.gate_polarity_label = QLabel(self.scrollAreaWidgetContents_3)
        self.gate_polarity_label.setObjectName(u"gate_polarity_label")
        self.gate_polarity_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.gate_polarity_label, 1, 5, 1, 1)

        self.gate_period_wave4 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave4.setObjectName(u"gate_period_wave4")
        self.gate_period_wave4.setMaximum(1000000)

        self.gate_grid_layout.addWidget(self.gate_period_wave4, 6, 2, 1, 1)

        self.gate_period_wave2 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave2.setObjectName(u"gate_period_wave2")
        self.gate_period_wave2.setMaximum(1000000)

        self.gate_grid_layout.addWidget(self.gate_period_wave2, 4, 2, 1, 1)

        self.wave6_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave6_label.setObjectName(u"wave6_label")
        self.wave6_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave6_label, 8, 0, 1, 1)

        self.gate_pin_wave2 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave2.setObjectName(u"gate_pin_wave2")

        self.gate_grid_layout.addWidget(self.gate_pin_wave2, 4, 1, 1, 1)

        self.gate_period_wave9 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave9.setObjectName(u"gate_period_wave9")
        self.gate_period_wave9.setMaximum(1000000)

        self.gate_grid_layout.addWidget(self.gate_period_wave9, 11, 2, 1, 1)

        self.duty_wave4 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave4.setObjectName(u"duty_wave4")
        self.duty_wave4.setMaximum(100)

        self.gate_grid_layout.addWidget(self.duty_wave4, 6, 4, 1, 1)

        self.gate_period_wave7 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave7.setObjectName(u"gate_period_wave7")
        self.gate_period_wave7.setMaximum(1000000)

        self.gate_grid_layout.addWidget(self.gate_period_wave7, 9, 2, 1, 1)

        self.wave5_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave5_label.setObjectName(u"wave5_label")
        self.wave5_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave5_label, 7, 0, 1, 1)

        self.duty_wave6 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave6.setObjectName(u"duty_wave6")
        self.duty_wave6.setMaximum(100)

        self.gate_grid_layout.addWidget(self.duty_wave6, 8, 4, 1, 1)

        self.gate_polarity_wave2 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave2.addItem("")
        self.gate_polarity_wave2.addItem("")
        self.gate_polarity_wave2.setObjectName(u"gate_polarity_wave2")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave2, 4, 5, 1, 1)

        self.gate_phase_wave8 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave8.setObjectName(u"gate_phase_wave8")

        self.gate_grid_layout.addWidget(self.gate_phase_wave8, 10, 3, 1, 1)

        self.gate_period_wave8 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave8.setObjectName(u"gate_period_wave8")
        self.gate_period_wave8.setMaximum(1000000)

        self.gate_grid_layout.addWidget(self.gate_period_wave8, 10, 2, 1, 1)

        self.duty_wave7 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave7.setObjectName(u"duty_wave7")
        self.duty_wave7.setMaximum(100)

        self.gate_grid_layout.addWidget(self.duty_wave7, 9, 4, 1, 1)

        self.gate_phase_label = QLabel(self.scrollAreaWidgetContents_3)
        self.gate_phase_label.setObjectName(u"gate_phase_label")
        self.gate_phase_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.gate_phase_label, 1, 3, 1, 1)

        self.wave2_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave2_label.setObjectName(u"wave2_label")
        self.wave2_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave2_label, 4, 0, 1, 1)

        self.gate_phase_wave6 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave6.setObjectName(u"gate_phase_wave6")

        self.gate_grid_layout.addWidget(self.gate_phase_wave6, 8, 3, 1, 1)

        self.gate_pin_wave5 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave5.setObjectName(u"gate_pin_wave5")

        self.gate_grid_layout.addWidget(self.gate_pin_wave5, 7, 1, 1, 1)

        self.duty_wave1 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave1.setObjectName(u"duty_wave1")
        self.duty_wave1.setMaximum(100)

        self.gate_grid_layout.addWidget(self.duty_wave1, 3, 4, 1, 1)

        self.gate_phase_wave5 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave5.setObjectName(u"gate_phase_wave5")

        self.gate_grid_layout.addWidget(self.gate_phase_wave5, 7, 3, 1, 1)

        self.gate_pin_wave7 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave7.setObjectName(u"gate_pin_wave7")

        self.gate_grid_layout.addWidget(self.gate_pin_wave7, 9, 1, 1, 1)

        self.duty_wave9 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave9.setObjectName(u"duty_wave9")
        self.duty_wave9.setMaximum(100)

        self.gate_grid_layout.addWidget(self.duty_wave9, 11, 4, 1, 1)

        self.gate_pin_wave3 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave3.setObjectName(u"gate_pin_wave3")

        self.gate_grid_layout.addWidget(self.gate_pin_wave3, 5, 1, 1, 1)

        self.duty_label = QLabel(self.scrollAreaWidgetContents_3)
        self.duty_label.setObjectName(u"duty_label")
        self.duty_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.duty_label, 1, 4, 1, 1)

        self.wave7_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave7_label.setObjectName(u"wave7_label")
        self.wave7_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave7_label, 9, 0, 1, 1)

        self.gate_pin_wave4 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave4.setObjectName(u"gate_pin_wave4")

        self.gate_grid_layout.addWidget(self.gate_pin_wave4, 6, 1, 1, 1)

        self.gate_pin_wave8 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave8.setObjectName(u"gate_pin_wave8")

        self.gate_grid_layout.addWidget(self.gate_pin_wave8, 10, 1, 1, 1)

        self.wave9_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave9_label.setObjectName(u"wave9_label")
        self.wave9_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave9_label, 11, 0, 1, 1)

        self.gate_period_label = QLabel(self.scrollAreaWidgetContents_3)
        self.gate_period_label.setObjectName(u"gate_period_label")
        self.gate_period_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.gate_period_label, 1, 2, 1, 1)

        self.gate_polarity_wave4 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave4.addItem("")
        self.gate_polarity_wave4.addItem("")
        self.gate_polarity_wave4.setObjectName(u"gate_polarity_wave4")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave4, 6, 5, 1, 1)

        self.gate_period_wave1 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave1.setObjectName(u"gate_period_wave1")
        self.gate_period_wave1.setMaximum(1000000)

        self.gate_grid_layout.addWidget(self.gate_period_wave1, 3, 2, 1, 1)

        self.gate_phase_wave3 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave3.setObjectName(u"gate_phase_wave3")

        self.gate_grid_layout.addWidget(self.gate_phase_wave3, 5, 3, 1, 1)

        self.gate_polarity_wave9 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave9.addItem("")
        self.gate_polarity_wave9.addItem("")
        self.gate_polarity_wave9.setObjectName(u"gate_polarity_wave9")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave9, 11, 5, 1, 1)

        self.gate_phase_wave9 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave9.setObjectName(u"gate_phase_wave9")

        self.gate_grid_layout.addWidget(self.gate_phase_wave9, 11, 3, 1, 1)

        self.duty_wave5 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.duty_wave5.setObjectName(u"duty_wave5")
        self.duty_wave5.setMaximum(100)

        self.gate_grid_layout.addWidget(self.duty_wave5, 7, 4, 1, 1)

        self.gate_polarity_wave3 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave3.addItem("")
        self.gate_polarity_wave3.addItem("")
        self.gate_polarity_wave3.setObjectName(u"gate_polarity_wave3")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave3, 5, 5, 1, 1)

        self.gate_phase_wave2 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_phase_wave2.setObjectName(u"gate_phase_wave2")

        self.gate_grid_layout.addWidget(self.gate_phase_wave2, 4, 3, 1, 1)

        self.gate_period_wave6 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave6.setObjectName(u"gate_period_wave6")
        self.gate_period_wave6.setMaximum(1000000)

        self.gate_grid_layout.addWidget(self.gate_period_wave6, 8, 2, 1, 1)

        self.gate_period_wave3 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_period_wave3.setObjectName(u"gate_period_wave3")
        self.gate_period_wave3.setMaximum(1000000)

        self.gate_grid_layout.addWidget(self.gate_period_wave3, 5, 2, 1, 1)

        self.wave8_label = QLabel(self.scrollAreaWidgetContents_3)
        self.wave8_label.setObjectName(u"wave8_label")
        self.wave8_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gate_grid_layout.addWidget(self.wave8_label, 10, 0, 1, 1)

        self.gate_polarity_wave6 = QComboBox(self.scrollAreaWidgetContents_3)
        self.gate_polarity_wave6.addItem("")
        self.gate_polarity_wave6.addItem("")
        self.gate_polarity_wave6.setObjectName(u"gate_polarity_wave6")

        self.gate_grid_layout.addWidget(self.gate_polarity_wave6, 8, 5, 1, 1)

        self.gate_pin_wave9 = QSpinBox(self.scrollAreaWidgetContents_3)
        self.gate_pin_wave9.setObjectName(u"gate_pin_wave9")

        self.gate_grid_layout.addWidget(self.gate_pin_wave9, 11, 1, 1, 1)

        self.gate_label = QLabel(self.scrollAreaWidgetContents_3)
        self.gate_label.setObjectName(u"gate_label")
        self.gate_label.setFont(font1)
        self.gate_label.setAlignment(Qt.AlignCenter)
        self.gate_label.setMargin(0)

        self.gate_grid_layout.addWidget(self.gate_label, 0, 0, 1, 6)


        self.verticalLayout_2.addLayout(self.gate_grid_layout)

        self.dio_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.dio_spacer)

        self.dio_scroll_area.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.dio_scroll_area)

        self.tabWidget.addTab(self.dio_tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        SettingsWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(SettingsWindow)
        self.toolBar.setObjectName(u"toolBar")
        SettingsWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
#if QT_CONFIG(shortcut)
        self.config_path_label.setBuddy(self.config_path_edit)
        self.log_path_label.setBuddy(self.log_path_edit)
        self.data_dir_label.setBuddy(self.data_dir_edit)
        self.max_num_ev_label.setBuddy(self.max_ev_time_box)
        self.max_ev_time_label.setBuddy(self.max_num_ev_box)
        self.sipm_ip_addr_label.setBuddy(self.sipm_ip_addr_edit)
        self.sipm_qp_label.setBuddy(self.sipm_qp_box)
        self.sipm_bias_label.setBuddy(self.sipm_bias_box)
        self.caen_polarity_label.setBuddy(self.caen_polarity_box)
        self.caen_io_label.setBuddy(self.caen_io_box)
        self.caen_post_trig_label.setBuddy(self.caen_post_trig_box)
        self.caen_conn_label.setBuddy(self.caen_conn_box)
        self.caen_ext_trig_label.setBuddy(self.caen_ext_trig_box)
        self.caen_overlap_label.setBuddy(self.caen_overlap_box)
        self.caen_evs_label.setBuddy(self.caen_evs_box)
        self.caen_model_label.setBuddy(self.caen_model_box)
        self.caen_port_label.setBuddy(self.caen_port_box)
        self.caen_sw_trig_label.setBuddy(self.caen_sw_trig_box)
        self.caen_length_label.setBuddy(self.caen_length_box)
        self.caen_decimation_label.setBuddy(self.caen_decimation_box)
        self.caen_trigin_label.setBuddy(self.caen_trigin_box)
        self.caen_g0_enable_label.setBuddy(self.caen_g0_enable_box)
        self.caen_g0_thres_label.setBuddy(self.caen_g0_thres_box)
        self.acous_post_trig_label.setBuddy(self.acous_post_trig_box)
        self.acous_trig_delay_label.setBuddy(self.acous_trig_delay_box)
        self.acous_trig_timeout_label.setBuddy(self.acous_trig_timeout_box)
        self.acous_sample_rate_label.setBuddy(self.acous_sample_rate_box)
        self.acous_pre_trig_label.setBuddy(self.acous_pre_trig_box)
        self.acous_ch5_label.setBuddy(self.acous_enable_ch5)
        self.acous_ch2_label.setBuddy(self.acous_enable_ch2)
        self.acous_ch1_label.setBuddy(self.acous_enable_ch1)
        self.acous_ch6_label.setBuddy(self.acous_enable_ch6)
        self.acous_ch7_label.setBuddy(self.acous_enable_ch7)
        self.acous_ch3_label.setBuddy(self.acous_enable_ch3)
        self.acous_ch8_label.setBuddy(self.acous_enable_ch8)
        self.acous_ch4_label.setBuddy(self.acous_enable_ch4)
        self.mode_label.setBuddy(self.cam1_mode)
        self.ip_addr_label.setBuddy(self.cam1_ip_addr)
        self.post_trig_len_label.setBuddy(self.cam1_post_trig_len)
        self.adc_threshold_label.setBuddy(self.cam1_adc_threshold)
        self.date_format_label.setBuddy(self.cam1_date_format)
        self.state_pin_label.setBuddy(self.cam1_state_pin)
        self.data_path_label.setBuddy(self.cam1_data_path)
        self.trig_pin_label.setBuddy(self.cam1_trig_pin)
        self.trig_latch_pin_label.setBuddy(self.cam1_trig_latch_pin)
        self.exposure_label.setBuddy(self.cam1_exposure)
        self.cam_config_path_label.setBuddy(self.cam1_config_path)
        self.trig_wait_label.setBuddy(self.cam1_trig_wait)
        self.pix_threshold_label.setBuddy(self.cam1_pix_threshold)
        self.buffer_len_label.setBuddy(self.cam1_buffer_len)
        self.trig_enbl_pin_label.setBuddy(self.cam1_trig_enbl_pin)
        self.state_comm_pin_label.setBuddy(self.cam1_state_comm_pin)
        self.image_format_label.setBuddy(self.cam1_image_format)
        self.cam_rc_config_path_label.setBuddy(self.cam1_config_path)
        self.trig_latch_pins_label.setBuddy(self.trig_latch_pins_edit)
        self.trig_or_pin_label.setBuddy(self.trig_or_pin_edit)
        self.heartbeat_pin_label.setBuddy(self.heartbeat_pin_edit)
        self.trig_reset_pin_label.setBuddy(self.trig_reset_pin_edit)
        self.trig_in_pins_label.setBuddy(self.trig_in_pins_edit)
        self.on_time_pin_label.setBuddy(self.on_time_pin_edit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.sipm_scroll_area, self.acoustics_scroll_area)
        QWidget.setTabOrder(self.acoustics_scroll_area, self.cam_scroll_area)
        QWidget.setTabOrder(self.cam_scroll_area, self.dio_scroll_area)
        QWidget.setTabOrder(self.dio_scroll_area, self.sipm_ip_addr_edit)
        QWidget.setTabOrder(self.sipm_ip_addr_edit, self.sipm_bias_box)
        QWidget.setTabOrder(self.sipm_bias_box, self.sipm_qp_box)
        QWidget.setTabOrder(self.sipm_qp_box, self.caen_model_box)
        QWidget.setTabOrder(self.caen_model_box, self.caen_port_box)
        QWidget.setTabOrder(self.caen_port_box, self.caen_conn_box)
        QWidget.setTabOrder(self.caen_conn_box, self.caen_evs_box)
        QWidget.setTabOrder(self.caen_evs_box, self.caen_length_box)
        QWidget.setTabOrder(self.caen_length_box, self.caen_post_trig_box)
        QWidget.setTabOrder(self.caen_post_trig_box, self.caen_trigin_box)
        QWidget.setTabOrder(self.caen_trigin_box, self.caen_overlap_box)
        QWidget.setTabOrder(self.caen_overlap_box, self.caen_polarity_box)
        QWidget.setTabOrder(self.caen_polarity_box, self.caen_io_box)
        QWidget.setTabOrder(self.caen_io_box, self.caen_ext_trig_box)
        QWidget.setTabOrder(self.caen_ext_trig_box, self.caen_sw_trig_box)
        QWidget.setTabOrder(self.caen_sw_trig_box, self.caen_g0_enable_box)
        QWidget.setTabOrder(self.caen_g0_enable_box, self.caen_g0_thres_box)
        QWidget.setTabOrder(self.caen_g0_thres_box, self.caen_g0_trig_mask_0)
        QWidget.setTabOrder(self.caen_g0_trig_mask_0, self.caen_g0_trig_mask_1)
        QWidget.setTabOrder(self.caen_g0_trig_mask_1, self.caen_g0_trig_mask_2)
        QWidget.setTabOrder(self.caen_g0_trig_mask_2, self.caen_g0_trig_mask_3)
        QWidget.setTabOrder(self.caen_g0_trig_mask_3, self.caen_g0_trig_mask_4)
        QWidget.setTabOrder(self.caen_g0_trig_mask_4, self.caen_g0_trig_mask_5)
        QWidget.setTabOrder(self.caen_g0_trig_mask_5, self.caen_g0_trig_mask_6)
        QWidget.setTabOrder(self.caen_g0_trig_mask_6, self.caen_g0_trig_mask_7)
        QWidget.setTabOrder(self.caen_g0_trig_mask_7, self.caen_g0_acq_mask_0)
        QWidget.setTabOrder(self.caen_g0_acq_mask_0, self.caen_g0_acq_mask_1)
        QWidget.setTabOrder(self.caen_g0_acq_mask_1, self.caen_g0_acq_mask_2)
        QWidget.setTabOrder(self.caen_g0_acq_mask_2, self.caen_g0_acq_mask_3)
        QWidget.setTabOrder(self.caen_g0_acq_mask_3, self.caen_g0_acq_mask_4)
        QWidget.setTabOrder(self.caen_g0_acq_mask_4, self.caen_g0_acq_mask_5)
        QWidget.setTabOrder(self.caen_g0_acq_mask_5, self.caen_g0_acq_mask_6)
        QWidget.setTabOrder(self.caen_g0_acq_mask_6, self.caen_g0_acq_mask_7)
        QWidget.setTabOrder(self.caen_g0_acq_mask_7, self.acous_sample_rate_box)
        QWidget.setTabOrder(self.acous_sample_rate_box, self.acous_pre_trig_box)
        QWidget.setTabOrder(self.acous_pre_trig_box, self.acous_trig_timeout_box)
        QWidget.setTabOrder(self.acous_trig_timeout_box, self.acous_post_trig_box)
        QWidget.setTabOrder(self.acous_post_trig_box, self.acous_trig_delay_box)
        QWidget.setTabOrder(self.acous_trig_delay_box, self.acous_enable_ch1)
        QWidget.setTabOrder(self.acous_enable_ch1, self.acous_range_ch1)
        QWidget.setTabOrder(self.acous_range_ch1, self.acous_dc_offset_ch1)
        QWidget.setTabOrder(self.acous_dc_offset_ch1, self.acous_trig_ch1)
        QWidget.setTabOrder(self.acous_trig_ch1, self.acous_polarity_ch1)
        QWidget.setTabOrder(self.acous_polarity_ch1, self.acous_threshold_ch1)
        QWidget.setTabOrder(self.acous_threshold_ch1, self.acous_enable_ch2)
        QWidget.setTabOrder(self.acous_enable_ch2, self.acous_range_ch2)
        QWidget.setTabOrder(self.acous_range_ch2, self.acous_dc_offset_ch2)
        QWidget.setTabOrder(self.acous_dc_offset_ch2, self.acous_trig_ch2)
        QWidget.setTabOrder(self.acous_trig_ch2, self.acous_polarity_ch2)
        QWidget.setTabOrder(self.acous_polarity_ch2, self.acous_threshold_ch2)
        QWidget.setTabOrder(self.acous_threshold_ch2, self.acous_enable_ch3)
        QWidget.setTabOrder(self.acous_enable_ch3, self.acous_range_ch3)
        QWidget.setTabOrder(self.acous_range_ch3, self.acous_dc_offset_ch3)
        QWidget.setTabOrder(self.acous_dc_offset_ch3, self.acous_trig_ch3)
        QWidget.setTabOrder(self.acous_trig_ch3, self.acous_polarity_ch3)
        QWidget.setTabOrder(self.acous_polarity_ch3, self.acous_threshold_ch3)
        QWidget.setTabOrder(self.acous_threshold_ch3, self.acous_enable_ch4)
        QWidget.setTabOrder(self.acous_enable_ch4, self.acous_range_ch4)
        QWidget.setTabOrder(self.acous_range_ch4, self.acous_dc_offset_ch4)
        QWidget.setTabOrder(self.acous_dc_offset_ch4, self.acous_trig_ch4)
        QWidget.setTabOrder(self.acous_trig_ch4, self.acous_polarity_ch4)
        QWidget.setTabOrder(self.acous_polarity_ch4, self.acous_threshold_ch4)
        QWidget.setTabOrder(self.acous_threshold_ch4, self.acous_enable_ch5)
        QWidget.setTabOrder(self.acous_enable_ch5, self.acous_range_ch5)
        QWidget.setTabOrder(self.acous_range_ch5, self.acous_dc_offset_ch5)
        QWidget.setTabOrder(self.acous_dc_offset_ch5, self.acous_trig_ch5)
        QWidget.setTabOrder(self.acous_trig_ch5, self.acous_polarity_ch5)
        QWidget.setTabOrder(self.acous_polarity_ch5, self.acous_threshold_ch5)
        QWidget.setTabOrder(self.acous_threshold_ch5, self.acous_enable_ch6)
        QWidget.setTabOrder(self.acous_enable_ch6, self.acous_range_ch6)
        QWidget.setTabOrder(self.acous_range_ch6, self.acous_dc_offset_ch6)
        QWidget.setTabOrder(self.acous_dc_offset_ch6, self.acous_trig_ch6)
        QWidget.setTabOrder(self.acous_trig_ch6, self.acous_polarity_ch6)
        QWidget.setTabOrder(self.acous_polarity_ch6, self.acous_threshold_ch6)
        QWidget.setTabOrder(self.acous_threshold_ch6, self.acous_enable_ch7)
        QWidget.setTabOrder(self.acous_enable_ch7, self.acous_range_ch7)
        QWidget.setTabOrder(self.acous_range_ch7, self.acous_dc_offset_ch7)
        QWidget.setTabOrder(self.acous_dc_offset_ch7, self.acous_trig_ch7)
        QWidget.setTabOrder(self.acous_trig_ch7, self.acous_polarity_ch7)
        QWidget.setTabOrder(self.acous_polarity_ch7, self.acous_threshold_ch7)
        QWidget.setTabOrder(self.acous_threshold_ch7, self.acous_enable_ch8)
        QWidget.setTabOrder(self.acous_enable_ch8, self.acous_range_ch8)
        QWidget.setTabOrder(self.acous_range_ch8, self.acous_dc_offset_ch8)
        QWidget.setTabOrder(self.acous_dc_offset_ch8, self.acous_trig_ch8)
        QWidget.setTabOrder(self.acous_trig_ch8, self.acous_polarity_ch8)
        QWidget.setTabOrder(self.acous_polarity_ch8, self.acous_threshold_ch8)
        QWidget.setTabOrder(self.acous_threshold_ch8, self.acous_trig_ext)
        QWidget.setTabOrder(self.acous_trig_ext, self.acous_polarity_ext)
        QWidget.setTabOrder(self.acous_polarity_ext, self.acous_threshold_ext)
        QWidget.setTabOrder(self.acous_threshold_ext, self.cam1_config_path)
        QWidget.setTabOrder(self.cam1_config_path, self.cam2_config_path)
        QWidget.setTabOrder(self.cam2_config_path, self.cam3_config_path)
        QWidget.setTabOrder(self.cam3_config_path, self.cam1_data_path)
        QWidget.setTabOrder(self.cam1_data_path, self.cam2_data_path)
        QWidget.setTabOrder(self.cam2_data_path, self.cam3_data_path)
        QWidget.setTabOrder(self.cam3_data_path, self.cam1_ip_addr)
        QWidget.setTabOrder(self.cam1_ip_addr, self.cam2_ip_addr)
        QWidget.setTabOrder(self.cam2_ip_addr, self.cam3_ip_addr)
        QWidget.setTabOrder(self.cam3_ip_addr, self.cam1_mode)
        QWidget.setTabOrder(self.cam1_mode, self.cam2_mode)
        QWidget.setTabOrder(self.cam2_mode, self.cam3_mode)
        QWidget.setTabOrder(self.cam3_mode, self.cam1_trig_wait)
        QWidget.setTabOrder(self.cam1_trig_wait, self.cam2_trig_wait)
        QWidget.setTabOrder(self.cam2_trig_wait, self.cam3_trig_wait)
        QWidget.setTabOrder(self.cam3_trig_wait, self.cam1_exposure)
        QWidget.setTabOrder(self.cam1_exposure, self.cam2_exposure)
        QWidget.setTabOrder(self.cam2_exposure, self.cam3_exposure)
        QWidget.setTabOrder(self.cam3_exposure, self.cam1_buffer_len)
        QWidget.setTabOrder(self.cam1_buffer_len, self.cam2_buffer_len)
        QWidget.setTabOrder(self.cam2_buffer_len, self.cam3_buffer_len)
        QWidget.setTabOrder(self.cam3_buffer_len, self.cam1_post_trig_len)
        QWidget.setTabOrder(self.cam1_post_trig_len, self.cam2_post_trig_len)
        QWidget.setTabOrder(self.cam2_post_trig_len, self.cam3_post_trig_len)
        QWidget.setTabOrder(self.cam3_post_trig_len, self.cam1_adc_threshold)
        QWidget.setTabOrder(self.cam1_adc_threshold, self.cam2_adc_threshold)
        QWidget.setTabOrder(self.cam2_adc_threshold, self.cam3_adc_threshold)
        QWidget.setTabOrder(self.cam3_adc_threshold, self.cam1_pix_threshold)
        QWidget.setTabOrder(self.cam1_pix_threshold, self.cam2_pix_threshold)
        QWidget.setTabOrder(self.cam2_pix_threshold, self.cam3_pix_threshold)
        QWidget.setTabOrder(self.cam3_pix_threshold, self.cam1_image_format)
        QWidget.setTabOrder(self.cam1_image_format, self.cam2_image_format)
        QWidget.setTabOrder(self.cam2_image_format, self.cam3_image_format)
        QWidget.setTabOrder(self.cam3_image_format, self.cam1_date_format)
        QWidget.setTabOrder(self.cam1_date_format, self.cam2_date_format)
        QWidget.setTabOrder(self.cam2_date_format, self.cam3_date_format)
        QWidget.setTabOrder(self.cam3_date_format, self.cam1_state_comm_pin)
        QWidget.setTabOrder(self.cam1_state_comm_pin, self.cam2_state_comm_pin)
        QWidget.setTabOrder(self.cam2_state_comm_pin, self.cam3_state_comm_pin)
        QWidget.setTabOrder(self.cam3_state_comm_pin, self.cam1_trig_enbl_pin)
        QWidget.setTabOrder(self.cam1_trig_enbl_pin, self.cam2_trig_enbl_pin)
        QWidget.setTabOrder(self.cam2_trig_enbl_pin, self.cam3_trig_enbl_pin)
        QWidget.setTabOrder(self.cam3_trig_enbl_pin, self.cam1_trig_latch_pin)
        QWidget.setTabOrder(self.cam1_trig_latch_pin, self.cam2_trig_latch_pin)
        QWidget.setTabOrder(self.cam2_trig_latch_pin, self.cam3_trig_latch_pin)
        QWidget.setTabOrder(self.cam3_trig_latch_pin, self.cam1_state_pin)
        QWidget.setTabOrder(self.cam1_state_pin, self.cam2_state_pin)
        QWidget.setTabOrder(self.cam2_state_pin, self.cam3_state_pin)
        QWidget.setTabOrder(self.cam3_state_pin, self.cam1_trig_pin)
        QWidget.setTabOrder(self.cam1_trig_pin, self.cam2_trig_pin)
        QWidget.setTabOrder(self.cam2_trig_pin, self.cam3_trig_pin)
        QWidget.setTabOrder(self.cam3_trig_pin, self.trigger_port_edit)
        QWidget.setTabOrder(self.trigger_port_edit, self.trigger_sketch_edit)
        QWidget.setTabOrder(self.trigger_sketch_edit, self.clock_port_edit)
        QWidget.setTabOrder(self.clock_port_edit, self.clock_sketch_edit)
        QWidget.setTabOrder(self.clock_sketch_edit, self.position_port_edit)
        QWidget.setTabOrder(self.position_port_edit, self.position_sketch_edit)
        QWidget.setTabOrder(self.position_sketch_edit, self.trig_in_pins_edit)
        QWidget.setTabOrder(self.trig_in_pins_edit, self.trig_latch_pins_edit)
        QWidget.setTabOrder(self.trig_latch_pins_edit, self.trig_reset_pin_edit)
        QWidget.setTabOrder(self.trig_reset_pin_edit, self.trig_or_pin_edit)
        QWidget.setTabOrder(self.trig_or_pin_edit, self.on_time_pin_edit)
        QWidget.setTabOrder(self.on_time_pin_edit, self.heartbeat_pin_edit)
        QWidget.setTabOrder(self.heartbeat_pin_edit, self.gate_pin_wave1)
        QWidget.setTabOrder(self.gate_pin_wave1, self.gate_period_wave1)
        QWidget.setTabOrder(self.gate_period_wave1, self.gate_phase_wave1)
        QWidget.setTabOrder(self.gate_phase_wave1, self.duty_wave1)
        QWidget.setTabOrder(self.duty_wave1, self.gate_polarity_wave1)
        QWidget.setTabOrder(self.gate_polarity_wave1, self.gate_pin_wave2)
        QWidget.setTabOrder(self.gate_pin_wave2, self.gate_period_wave2)
        QWidget.setTabOrder(self.gate_period_wave2, self.gate_phase_wave2)
        QWidget.setTabOrder(self.gate_phase_wave2, self.duty_wave2)
        QWidget.setTabOrder(self.duty_wave2, self.gate_polarity_wave2)
        QWidget.setTabOrder(self.gate_polarity_wave2, self.gate_pin_wave3)
        QWidget.setTabOrder(self.gate_pin_wave3, self.gate_period_wave3)
        QWidget.setTabOrder(self.gate_period_wave3, self.gate_phase_wave3)
        QWidget.setTabOrder(self.gate_phase_wave3, self.duty_wave3)
        QWidget.setTabOrder(self.duty_wave3, self.gate_polarity_wave3)
        QWidget.setTabOrder(self.gate_polarity_wave3, self.gate_pin_wave4)
        QWidget.setTabOrder(self.gate_pin_wave4, self.gate_period_wave4)
        QWidget.setTabOrder(self.gate_period_wave4, self.gate_phase_wave4)
        QWidget.setTabOrder(self.gate_phase_wave4, self.duty_wave4)
        QWidget.setTabOrder(self.duty_wave4, self.gate_polarity_wave4)
        QWidget.setTabOrder(self.gate_polarity_wave4, self.gate_pin_wave5)
        QWidget.setTabOrder(self.gate_pin_wave5, self.gate_period_wave5)
        QWidget.setTabOrder(self.gate_period_wave5, self.gate_phase_wave5)
        QWidget.setTabOrder(self.gate_phase_wave5, self.duty_wave5)
        QWidget.setTabOrder(self.duty_wave5, self.gate_polarity_wave5)
        QWidget.setTabOrder(self.gate_polarity_wave5, self.gate_pin_wave6)
        QWidget.setTabOrder(self.gate_pin_wave6, self.gate_period_wave6)
        QWidget.setTabOrder(self.gate_period_wave6, self.gate_phase_wave6)
        QWidget.setTabOrder(self.gate_phase_wave6, self.duty_wave6)
        QWidget.setTabOrder(self.duty_wave6, self.gate_polarity_wave6)
        QWidget.setTabOrder(self.gate_polarity_wave6, self.gate_pin_wave7)
        QWidget.setTabOrder(self.gate_pin_wave7, self.gate_period_wave7)
        QWidget.setTabOrder(self.gate_period_wave7, self.gate_phase_wave7)
        QWidget.setTabOrder(self.gate_phase_wave7, self.duty_wave7)
        QWidget.setTabOrder(self.duty_wave7, self.gate_polarity_wave7)
        QWidget.setTabOrder(self.gate_polarity_wave7, self.gate_pin_wave8)
        QWidget.setTabOrder(self.gate_pin_wave8, self.gate_period_wave8)
        QWidget.setTabOrder(self.gate_period_wave8, self.gate_phase_wave8)
        QWidget.setTabOrder(self.gate_phase_wave8, self.duty_wave8)
        QWidget.setTabOrder(self.duty_wave8, self.gate_polarity_wave8)
        QWidget.setTabOrder(self.gate_polarity_wave8, self.gate_pin_wave9)
        QWidget.setTabOrder(self.gate_pin_wave9, self.gate_period_wave9)
        QWidget.setTabOrder(self.gate_period_wave9, self.gate_phase_wave9)
        QWidget.setTabOrder(self.gate_phase_wave9, self.duty_wave9)
        QWidget.setTabOrder(self.duty_wave9, self.gate_polarity_wave9)

        self.toolBar.addAction(self.actionClose_Window)
        self.toolBar.addAction(self.actionReloadConfig)
        self.toolBar.addAction(self.actionApply_config)
        self.toolBar.addAction(self.actionSaveConfig)

        self.retranslateUi(SettingsWindow)
        self.actionClose_Window.triggered.connect(SettingsWindow.close)
        self.actionApply_config.triggered.connect(SettingsWindow.apply_config)
        self.actionSaveConfig.triggered.connect(SettingsWindow.save_config)
        self.actionReloadConfig.triggered.connect(SettingsWindow.load_config)
        self.position_sketch_but.clicked.connect(SettingsWindow.select_position_sketch_dir)
        self.trigger_sketch_but.clicked.connect(SettingsWindow.select_trigger_sketch_dir)
        self.log_path_but.clicked.connect(SettingsWindow.select_log_path)
        self.data_dir_but.clicked.connect(SettingsWindow.select_data_dir)
        self.clock_sketch_but.clicked.connect(SettingsWindow.select_clock_sketch_dir)
        self.config_path_but.clicked.connect(SettingsWindow.select_config_path)

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
        self.log_path_label.setText(QCoreApplication.translate("SettingsWindow", u"Log Path", None))
        self.log_path_but.setText(QCoreApplication.translate("SettingsWindow", u"...", None))
        self.config_path_but.setText(QCoreApplication.translate("SettingsWindow", u"...", None))
        self.data_dir_label.setText(QCoreApplication.translate("SettingsWindow", u"Data Dir", None))
        self.data_dir_but.setText(QCoreApplication.translate("SettingsWindow", u"...", None))
        self.max_num_ev_label.setText(QCoreApplication.translate("SettingsWindow", u"Max Num of Events", None))
        self.max_ev_time_label.setText(QCoreApplication.translate("SettingsWindow", u"Max Event Time", None))
        self.max_ev_time_box.setSuffix(QCoreApplication.translate("SettingsWindow", u"s", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.general_tab), QCoreApplication.translate("SettingsWindow", u"General", None))
        self.sipm_ip_addr_label.setText(QCoreApplication.translate("SettingsWindow", u"IP Addr", None))
        self.sipm_bias_box.setSuffix(QCoreApplication.translate("SettingsWindow", u"V", None))
        self.sipm_qp_box.setSuffix(QCoreApplication.translate("SettingsWindow", u"V", None))
        self.sipm_qp_label.setText(QCoreApplication.translate("SettingsWindow", u"QP Voltage", None))
        self.sipm_bias_label.setText(QCoreApplication.translate("SettingsWindow", u"Bias Voltage", None))
        self.sipm_amp_label.setText(QCoreApplication.translate("SettingsWindow", u"SiPM Amplifier", None))
        self.caen_polarity_box.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Positive", None))
        self.caen_polarity_box.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Negative", None))

        self.caen_polarity_label.setText(QCoreApplication.translate("SettingsWindow", u"Polarity", None))
        self.caen_io_label.setText(QCoreApplication.translate("SettingsWindow", u"IO Level", None))
        self.caen_post_trig_label.setText(QCoreApplication.translate("SettingsWindow", u"Post Trig", None))
        self.caen_ext_trig_box.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Disabled", None))
        self.caen_ext_trig_box.setItemText(1, QCoreApplication.translate("SettingsWindow", u"ACQ Only", None))
        self.caen_ext_trig_box.setItemText(2, QCoreApplication.translate("SettingsWindow", u"EXT Only", None))
        self.caen_ext_trig_box.setItemText(3, QCoreApplication.translate("SettingsWindow", u"ACQ+EXT", None))

        self.caen_model_box.setItemText(0, QCoreApplication.translate("SettingsWindow", u"DT5740D", None))
        self.caen_model_box.setItemText(1, QCoreApplication.translate("SettingsWindow", u"DT5730B", None))
        self.caen_model_box.setItemText(2, QCoreApplication.translate("SettingsWindow", u"V1740D", None))

        self.caen_conn_label.setText(QCoreApplication.translate("SettingsWindow", u"Connection Type", None))
        self.caen_ext_trig_label.setText(QCoreApplication.translate("SettingsWindow", u"Ext Trig Mode", None))
        self.caen_sw_trig_box.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Disabled", None))
        self.caen_sw_trig_box.setItemText(1, QCoreApplication.translate("SettingsWindow", u"ACQ Only", None))
        self.caen_sw_trig_box.setItemText(2, QCoreApplication.translate("SettingsWindow", u"EXT Only", None))
        self.caen_sw_trig_box.setItemText(3, QCoreApplication.translate("SettingsWindow", u"ACQ+EXT", None))

        self.caen_overlap_label.setText(QCoreApplication.translate("SettingsWindow", u"Overlap Reject", None))
        self.caen_overlap_box.setText("")
        self.caen_evs_label.setText(QCoreApplication.translate("SettingsWindow", u"Evs Per Read", None))
        self.caen_io_box.setItemText(0, QCoreApplication.translate("SettingsWindow", u"TTL", None))
        self.caen_io_box.setItemText(1, QCoreApplication.translate("SettingsWindow", u"NIM", None))

        self.caen_conn_box.setItemText(0, QCoreApplication.translate("SettingsWindow", u"USB", None))
        self.caen_conn_box.setItemText(1, QCoreApplication.translate("SettingsWindow", u"PCI", None))

        self.caen_general_label.setText(QCoreApplication.translate("SettingsWindow", u"CAEN Digitizer General", None))
        self.caen_model_label.setText(QCoreApplication.translate("SettingsWindow", u"Model", None))
        self.caen_port_label.setText(QCoreApplication.translate("SettingsWindow", u"Port", None))
        self.caen_sw_trig_label.setText(QCoreApplication.translate("SettingsWindow", u"SW Trig Mode", None))
        self.caen_length_label.setText(QCoreApplication.translate("SettingsWindow", u"Record Length", None))
        self.caen_post_trig_box.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.caen_decimation_label.setText(QCoreApplication.translate("SettingsWindow", u"Decimation", None))
        self.caen_trigin_label.setText(QCoreApplication.translate("SettingsWindow", u"TRG-IN as Gate", None))
        self.caen_trigin_box.setText("")
        self.caen_decimation_box.setPrefix("")
        self.caen_g0_enable_label.setText(QCoreApplication.translate("SettingsWindow", u"Enabled", None))
        self.caen_g0_enable_box.setText("")
        self.caen_g0_label.setText(QCoreApplication.translate("SettingsWindow", u"Group 0", None))
        self.caen_g0_thres_label.setText(QCoreApplication.translate("SettingsWindow", u"Threshold", None))
        self.caen_g0_acq_mask_6.setText("")
        self.label_21.setText(QCoreApplication.translate("SettingsWindow", u"Trig Mask", None))
        self.caen_g0_trig_mask_4.setText("")
        self.caen_g0_trig_mask_1.setText("")
        self.caen_g0_acq_mask_7.setText("")
        self.caen_g0_trig_mask_0.setText("")
        self.caen_g0_acq_mask_4.setText("")
        self.label_22.setText(QCoreApplication.translate("SettingsWindow", u"Acq Mask", None))
        self.caen_g0_trig_mask_5.setText("")
        self.caen_g0_acq_mask_5.setText("")
        self.caen_g0_trig_mask_3.setText("")
        self.caen_g0_trig_mask_7.setText("")
        self.caen_g0_trig_mask_2.setText("")
        self.caen_g0_trig_mask_6.setText("")
        self.caen_g0_acq_mask_3.setText("")
        self.caen_g0_acq_mask_0.setText("")
        self.label_23.setText(QCoreApplication.translate("SettingsWindow", u"Offsets", None))
        self.caen_g0_acq_mask_2.setText("")
        self.caen_g0_acq_mask_1.setText("")
        self.label_30.setText(QCoreApplication.translate("SettingsWindow", u"Ch7", None))
        self.label_29.setText(QCoreApplication.translate("SettingsWindow", u"Ch6", None))
        self.label_28.setText(QCoreApplication.translate("SettingsWindow", u"Ch5", None))
        self.label_27.setText(QCoreApplication.translate("SettingsWindow", u"Ch4", None))
        self.label_26.setText(QCoreApplication.translate("SettingsWindow", u"Ch3", None))
        self.label_25.setText(QCoreApplication.translate("SettingsWindow", u"Ch2", None))
        self.label_24.setText(QCoreApplication.translate("SettingsWindow", u"Ch1", None))
        self.label_32.setText(QCoreApplication.translate("SettingsWindow", u"Ch0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scint_tab), QCoreApplication.translate("SettingsWindow", u"Scint", None))
        self.acous_post_trig_label.setText(QCoreApplication.translate("SettingsWindow", u"Post Trig Length", None))
        self.acous_trig_delay_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig Delay", None))
        self.acous_trig_timeout_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig Timeout", None))
        self.acous_sample_rate_label.setText(QCoreApplication.translate("SettingsWindow", u"Sample Rate", None))
        self.acous_sample_rate_box.setItemText(0, QCoreApplication.translate("SettingsWindow", u"100 MS/s", None))

        self.acous_pre_trig_label.setText(QCoreApplication.translate("SettingsWindow", u"Pre Trig Length", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"General", None))
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
        self.cam2_data_path.setText("")
        self.mode_label.setText(QCoreApplication.translate("SettingsWindow", u"Mode", None))
        self.cam2_label.setText(QCoreApplication.translate("SettingsWindow", u"Cam 2", None))
        self.cam1_trig_wait.setSuffix(QCoreApplication.translate("SettingsWindow", u"s", None))
        self.ip_addr_label.setText(QCoreApplication.translate("SettingsWindow", u"IP Address", None))
        self.post_trig_len_label.setText(QCoreApplication.translate("SettingsWindow", u"Post-Trig Length", None))
        self.cam2_trig_wait.setSuffix(QCoreApplication.translate("SettingsWindow", u"s", None))
        self.cam2_image_format.setItemText(0, QCoreApplication.translate("SettingsWindow", u"bmp", None))
        self.cam2_image_format.setItemText(1, QCoreApplication.translate("SettingsWindow", u"png", None))
        self.cam2_image_format.setItemText(2, QCoreApplication.translate("SettingsWindow", u"jpg", None))

        self.cam3_image_format.setItemText(0, QCoreApplication.translate("SettingsWindow", u"bmp", None))
        self.cam3_image_format.setItemText(1, QCoreApplication.translate("SettingsWindow", u"png", None))
        self.cam3_image_format.setItemText(2, QCoreApplication.translate("SettingsWindow", u"jpg", None))

        self.adc_threshold_label.setText(QCoreApplication.translate("SettingsWindow", u"ADC Threshold", None))
        self.date_format_label.setText(QCoreApplication.translate("SettingsWindow", u"Date Format", None))
        self.state_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"State Pin", None))
        self.data_path_label.setText(QCoreApplication.translate("SettingsWindow", u"Pi Data Path", None))
        self.cam3_trig_wait.setSuffix(QCoreApplication.translate("SettingsWindow", u"s", None))
        self.cam3_ip_addr.setText("")
        self.trig_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"Trigger Pin", None))
        self.cam3_label.setText(QCoreApplication.translate("SettingsWindow", u"Cam 3", None))
        self.trig_latch_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig Latch Pin", None))
        self.exposure_label.setText(QCoreApplication.translate("SettingsWindow", u"Exposure", None))
        self.cam_config_path_label.setText(QCoreApplication.translate("SettingsWindow", u"Pi Config Path", None))
        self.trig_wait_label.setText(QCoreApplication.translate("SettingsWindow", u"Trigger Wait", None))
        self.pix_threshold_label.setText(QCoreApplication.translate("SettingsWindow", u"Pixel Treshold", None))
        self.buffer_len_label.setText(QCoreApplication.translate("SettingsWindow", u"Buffer Length", None))
        self.trig_enbl_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig Enable Pin", None))
        self.cam1_image_format.setItemText(0, QCoreApplication.translate("SettingsWindow", u"bmp", None))
        self.cam1_image_format.setItemText(1, QCoreApplication.translate("SettingsWindow", u"png", None))
        self.cam1_image_format.setItemText(2, QCoreApplication.translate("SettingsWindow", u"jpg", None))

        self.cam1_label.setText(QCoreApplication.translate("SettingsWindow", u"Cam 1", None))
        self.cam1_config_path.setText("")
        self.state_comm_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"State Comm Pin", None))
        self.image_format_label.setText(QCoreApplication.translate("SettingsWindow", u"Image Format", None))
        self.cam_rc_config_path_label.setText(QCoreApplication.translate("SettingsWindow", u"RC Config Path", None))
        self.cam2_rc_config_path.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cam_tab), QCoreApplication.translate("SettingsWindow", u"Camera", None))
        self.dio_general_label.setText(QCoreApplication.translate("SettingsWindow", u"General", None))
        self.trigger_arduino_label.setText(QCoreApplication.translate("SettingsWindow", u"Trigger", None))
        self.position_arduino_label.setText(QCoreApplication.translate("SettingsWindow", u"Position", None))
        self.clock_arduino_label.setText(QCoreApplication.translate("SettingsWindow", u"Clock", None))
        self.arduino_port_label.setText(QCoreApplication.translate("SettingsWindow", u"Arduino Port", None))
        self.trigger_sketch_but.setText(QCoreApplication.translate("SettingsWindow", u"...", None))
        self.sketch_location_label.setText(QCoreApplication.translate("SettingsWindow", u"Sketch Location", None))
        self.clock_sketch_but.setText(QCoreApplication.translate("SettingsWindow", u"...", None))
        self.position_sketch_but.setText(QCoreApplication.translate("SettingsWindow", u"...", None))
        self.trig_latch_pins_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig Latch Pins", None))
        self.trig_or_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig Or Pin", None))
        self.heartbeat_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"Heartbeat Pin", None))
        self.trig_reset_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig Reset Pin", None))
        self.trig_in_pins_label.setText(QCoreApplication.translate("SettingsWindow", u"Trig In Pins", None))
        self.on_time_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"On-Time Pin", None))
        self.fifo_layout.setText(QCoreApplication.translate("SettingsWindow", u"Trig FIFO Arduino", None))
        self.gate_polarity_wave1.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave1.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.gate_polarity_wave5.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave5.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.duty_wave2.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.wave1_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 1", None))
        self.wave3_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 3", None))
        self.gate_pin_label.setText(QCoreApplication.translate("SettingsWindow", u"Pin", None))
        self.duty_wave8.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.wave4_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 4", None))
        self.duty_wave3.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.gate_polarity_wave8.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave8.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.gate_polarity_wave7.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave7.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.gate_polarity_label.setText(QCoreApplication.translate("SettingsWindow", u"Polarity", None))
        self.wave6_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 6", None))
        self.duty_wave4.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.wave5_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 5", None))
        self.duty_wave6.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.gate_polarity_wave2.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave2.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.duty_wave7.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.gate_phase_label.setText(QCoreApplication.translate("SettingsWindow", u"Phase", None))
        self.wave2_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 2", None))
        self.duty_wave1.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.duty_wave9.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.duty_label.setText(QCoreApplication.translate("SettingsWindow", u"Duty", None))
        self.wave7_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 7", None))
        self.wave9_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 9", None))
        self.gate_period_label.setText(QCoreApplication.translate("SettingsWindow", u"Period", None))
        self.gate_polarity_wave4.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave4.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.gate_polarity_wave9.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave9.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.duty_wave5.setSuffix(QCoreApplication.translate("SettingsWindow", u"%", None))
        self.gate_polarity_wave3.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave3.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.wave8_label.setText(QCoreApplication.translate("SettingsWindow", u"Wave 8", None))
        self.gate_polarity_wave6.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Normal", None))
        self.gate_polarity_wave6.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Reverse", None))

        self.gate_label.setText(QCoreApplication.translate("SettingsWindow", u"Gate Arduino", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dio_tab), QCoreApplication.translate("SettingsWindow", u"DIO", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"toolBar", None))
    # retranslateUi

