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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QToolBar, QToolButton, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 473)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(50, 50))
        self.centralwidget.setBaseSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.start_run_but = QPushButton(self.centralwidget)
        self.start_run_but.setObjectName(u"start_run_but")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.start_run_but.sizePolicy().hasHeightForWidth())
        self.start_run_but.setSizePolicy(sizePolicy2)
        self.start_run_but.setMinimumSize(QSize(0, 50))
        self.start_run_but.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.start_run_but.setFont(font)
        self.start_run_but.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_run_but.setStyleSheet(u"QPushButton:enabled {color: rgb(0, 85, 0);}\n"
"QPushButton:disabled {color: rgb(120, 120, 120);}")

        self.verticalLayout_6.addWidget(self.start_run_but)

        self.stop_run_but = QPushButton(self.centralwidget)
        self.stop_run_but.setObjectName(u"stop_run_but")
        self.stop_run_but.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.stop_run_but.sizePolicy().hasHeightForWidth())
        self.stop_run_but.setSizePolicy(sizePolicy2)
        self.stop_run_but.setMinimumSize(QSize(0, 50))
        self.stop_run_but.setFont(font)
        self.stop_run_but.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_run_but.setStyleSheet(u"QPushButton:enabled {color: rgb(170, 0, 0);}\n"
"QPushButton:disabled {color: rgb(120, 120, 120);}")
        self.stop_run_but.setCheckable(False)

        self.verticalLayout_6.addWidget(self.stop_run_but)

        self.sw_trigger_but = QPushButton(self.centralwidget)
        self.sw_trigger_but.setObjectName(u"sw_trigger_but")
        self.sw_trigger_but.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.sw_trigger_but.sizePolicy().hasHeightForWidth())
        self.sw_trigger_but.setSizePolicy(sizePolicy2)
        self.sw_trigger_but.setMinimumSize(QSize(0, 50))
        self.sw_trigger_but.setFont(font)
        self.sw_trigger_but.setCursor(QCursor(Qt.PointingHandCursor))
        self.sw_trigger_but.setStyleSheet(u"QPushButton:enabled {color: rgb(0, 30, 100);}\n"
"QPushButton:disabled {color: rgb(120, 120, 120);}")
        self.sw_trigger_but.setCheckable(False)

        self.verticalLayout_6.addWidget(self.sw_trigger_but)

        self.run_state_label = QLabel(self.centralwidget)
        self.run_state_label.setObjectName(u"run_state_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.run_state_label.sizePolicy().hasHeightForWidth())
        self.run_state_label.setSizePolicy(sizePolicy3)
        self.run_state_label.setMinimumSize(QSize(0, 50))
        self.run_state_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.run_state_label)

        self.run_label = QLabel(self.centralwidget)
        self.run_label.setObjectName(u"run_label")
        sizePolicy2.setHeightForWidth(self.run_label.sizePolicy().hasHeightForWidth())
        self.run_label.setSizePolicy(sizePolicy2)
        self.run_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.run_label)

        self.run_edit = QLineEdit(self.centralwidget)
        self.run_edit.setObjectName(u"run_edit")
        sizePolicy2.setHeightForWidth(self.run_edit.sizePolicy().hasHeightForWidth())
        self.run_edit.setSizePolicy(sizePolicy2)
        self.run_edit.setAlignment(Qt.AlignCenter)
        self.run_edit.setReadOnly(True)
        self.run_edit.setClearButtonEnabled(False)

        self.verticalLayout_6.addWidget(self.run_edit)

        self.event_num_label = QLabel(self.centralwidget)
        self.event_num_label.setObjectName(u"event_num_label")
        sizePolicy2.setHeightForWidth(self.event_num_label.sizePolicy().hasHeightForWidth())
        self.event_num_label.setSizePolicy(sizePolicy2)
        self.event_num_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.event_num_label)

        self.event_num_edit = QLineEdit(self.centralwidget)
        self.event_num_edit.setObjectName(u"event_num_edit")
        sizePolicy2.setHeightForWidth(self.event_num_edit.sizePolicy().hasHeightForWidth())
        self.event_num_edit.setSizePolicy(sizePolicy2)
        self.event_num_edit.setAlignment(Qt.AlignCenter)
        self.event_num_edit.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.event_num_edit)

        self.event_time_label = QLabel(self.centralwidget)
        self.event_time_label.setObjectName(u"event_time_label")
        sizePolicy2.setHeightForWidth(self.event_time_label.sizePolicy().hasHeightForWidth())
        self.event_time_label.setSizePolicy(sizePolicy2)
        self.event_time_label.setLineWidth(1)
        self.event_time_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.event_time_label)

        self.event_time_edit = QLineEdit(self.centralwidget)
        self.event_time_edit.setObjectName(u"event_time_edit")
        sizePolicy2.setHeightForWidth(self.event_time_edit.sizePolicy().hasHeightForWidth())
        self.event_time_edit.setSizePolicy(sizePolicy2)
        self.event_time_edit.setAlignment(Qt.AlignCenter)
        self.event_time_edit.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.event_time_edit)

        self.run_live_time_label = QLabel(self.centralwidget)
        self.run_live_time_label.setObjectName(u"run_live_time_label")
        sizePolicy2.setHeightForWidth(self.run_live_time_label.sizePolicy().hasHeightForWidth())
        self.run_live_time_label.setSizePolicy(sizePolicy2)
        self.run_live_time_label.setLineWidth(1)
        self.run_live_time_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.run_live_time_label)

        self.run_live_time_edit = QLineEdit(self.centralwidget)
        self.run_live_time_edit.setObjectName(u"run_live_time_edit")
        sizePolicy2.setHeightForWidth(self.run_live_time_edit.sizePolicy().hasHeightForWidth())
        self.run_live_time_edit.setSizePolicy(sizePolicy2)
        self.run_live_time_edit.setAlignment(Qt.AlignCenter)
        self.run_live_time_edit.setDragEnabled(False)
        self.run_live_time_edit.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.run_live_time_edit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.tabs_widget = QTabWidget(self.centralwidget)
        self.tabs_widget.setObjectName(u"tabs_widget")
        sizePolicy.setHeightForWidth(self.tabs_widget.sizePolicy().hasHeightForWidth())
        self.tabs_widget.setSizePolicy(sizePolicy)
        self.tabs_widget.setSizeIncrement(QSize(100, 0))
        self.tabs_widget.setTabShape(QTabWidget.Rounded)
        self.tabs_widget.setDocumentMode(False)
        self.tabs_widget.setTabsClosable(False)
        self.tabs_widget.setMovable(True)
        self.general_tab = QWidget()
        self.general_tab.setObjectName(u"general_tab")
        self.verticalLayout_7 = QVBoxLayout(self.general_tab)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.general_tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 346, 402))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toolButton = QToolButton(self.scrollAreaWidgetContents_2)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_5.addWidget(self.toolButton)

        self.comment_grid = QGridLayout()
        self.comment_grid.setSpacing(3)
        self.comment_grid.setObjectName(u"comment_grid")
        self.comment_grid.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.save_comment_but = QPushButton(self.scrollAreaWidgetContents_2)
        self.save_comment_but.setObjectName(u"save_comment_but")

        self.comment_grid.addWidget(self.save_comment_but, 1, 2, 1, 1)

        self.comment_persist_box = QCheckBox(self.scrollAreaWidgetContents_2)
        self.comment_persist_box.setObjectName(u"comment_persist_box")

        self.comment_grid.addWidget(self.comment_persist_box, 1, 0, 1, 1)

        self.edit_comment_but = QPushButton(self.scrollAreaWidgetContents_2)
        self.edit_comment_but.setObjectName(u"edit_comment_but")

        self.comment_grid.addWidget(self.edit_comment_but, 1, 1, 1, 1)

        self.comment_edit = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.comment_edit.setObjectName(u"comment_edit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comment_edit.sizePolicy().hasHeightForWidth())
        self.comment_edit.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setKerning(True)
        self.comment_edit.setFont(font1)
        self.comment_edit.setFrameShape(QFrame.NoFrame)
        self.comment_edit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.comment_edit.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.comment_grid.addWidget(self.comment_edit, 0, 0, 1, 3)


        self.horizontalLayout_5.addLayout(self.comment_grid)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_6.addWidget(self.pushButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea_2)

        self.tabs_widget.addTab(self.general_tab, "")
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 346, 402))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(3)
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
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.camera_status_label.sizePolicy().hasHeightForWidth())
        self.camera_status_label.setSizePolicy(sizePolicy5)
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.next_imag_but.sizePolicy().hasHeightForWidth())
        self.next_imag_but.setSizePolicy(sizePolicy6)

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

        self.horizontalLayout_4.addWidget(self.tabs_widget)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

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
        self.stop_run_but.clicked.connect(MainWindow.stop_run_but_pressed)
        self.sw_trigger_but.clicked.connect(MainWindow.sw_trigger)

        self.tabs_widget.setCurrentIndex(0)


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
        self.stop_run_but.setText(QCoreApplication.translate("MainWindow", u"Stop Run", None))
        self.sw_trigger_but.setText(QCoreApplication.translate("MainWindow", u"SW Trigger", None))
        self.run_state_label.setText(QCoreApplication.translate("MainWindow", u"RunState", None))
        self.run_label.setText(QCoreApplication.translate("MainWindow", u"Run Num", None))
        self.run_edit.setPlaceholderText("")
        self.event_num_label.setText(QCoreApplication.translate("MainWindow", u"Event Num", None))
        self.event_time_label.setText(QCoreApplication.translate("MainWindow", u"Event Time", None))
        self.run_live_time_label.setText(QCoreApplication.translate("MainWindow", u"Run Live Time", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.save_comment_but.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.comment_persist_box.setText(QCoreApplication.translate("MainWindow", u"Remember", None))
        self.edit_comment_but.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.comment_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter run comments here.", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.general_tab), QCoreApplication.translate("MainWindow", u"General", None))
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

