# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget, QAbstractItemView)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1294, 868)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #6D5BBA, stop:1 #8D58BF);\n"
"color: #FFFFFF;\n"
"font-family: Arial, sans-serif;")
        Form.setLocale(QLocale(QLocale.Russian, QLocale.Ukraine))
        self.centralwidget = QWidget(Form)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"font-family: Noto Sans SC;")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 30, 1058, 564))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.train_frame = QFrame(self.layoutWidget)
        self.train_frame.setObjectName(u"train_frame")
        self.train_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.train_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.train_label = QLabel(self.train_frame)
        self.train_label.setObjectName(u"train_label")
        self.train_label.setStyleSheet(u"QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF;\n"
"}")

        self.verticalLayout.addWidget(self.train_label)

        self.start_date_train_wgt = QDateEdit(self.train_frame)
        self.start_date_train_wgt.setObjectName(u"start_date_train_wgt")
        self.start_date_train_wgt.setCalendarPopup(True)
        self.start_date_train_wgt.setDate(QDate.currentDate())
        self.start_date_train_wgt.setStyleSheet("QDateEdit {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #CCCCCC;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(C:/machine learning/gb_greyhound/grayhound/grayhound/grayhound/bddata/ui/icons/arrow_down.svg);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCalendarWidget {\n"
"    background-color: #6D5BBA;\n"
"    border: 1px solid #8D58BF;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: #FFFFFF;\n"
"    background-color: #8D58BF;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #A77BCE;\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"    background-color: #6D5BBA;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox {\n"
"    background: none;\n"
"    color: #FFFFFF;\n"
"    selection-background-color: #8D58BF;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button, QCalendarWidget QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border: none;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-arrow, QCalendarWidget QSpinBox::down-arrow {\n"
"    image: url(C:/machine learning/gb_greyhound/grayhound/grayhound/grayhound/bddata/ui/icons/arrow_up.svg); \n"
"    width: 10px;\n"
"    height: 10px;\n"
"}")
        
        self.verticalLayout.addWidget(self.start_date_train_wgt)

        self.end_date_train_wgt = QDateEdit(self.train_frame)
        self.end_date_train_wgt.setObjectName(u"end_date_train_wgt")
        self.end_date_train_wgt.setCalendarPopup(True)
        self.end_date_train_wgt.setDate(QDate.currentDate())
        self.end_date_train_wgt.setStyleSheet(u"QDateEdit {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #CCCCCC;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QCalendarWidget {\n"
"    background-color: #6D5BBA;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: #FFFFFF;\n"
"    background: none;\n"
"    border: none;\n"
"    margin: 0;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QCalendarW"
                        "idget QToolButton:hover {\n"
"    background-color: #8D58BF;\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"    background-color: #6D5BBA;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox {\n"
"    background: none;\n"
"    color: #FFFFFF;\n"
"    selection-background-color: #8D58BF;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button, QCalendarWidget QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border: none;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-arrow, QCalendarWidget QSpinBox::down-arrow {\n"
"    image: url(C:machine learning/gb_greyhound/grayhound/grayhound/grayhound/bddata/ui/icons/arrow_up.svg); \n"
"    width: 10px;\n"
"    height: 10px;\n"
"}")

        self.verticalLayout.addWidget(self.end_date_train_wgt)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cities_wgt_1 = QListWidget(self.train_frame)
        self.cities_wgt_1.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.cities_wgt_1.itemSelectionChanged.connect(self.on_item_selected_train)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        QListWidgetItem(self.cities_wgt_1)
        self.cities_wgt_1.setObjectName(u"cities_wgt_1")
        self.cities_wgt_1.setStyleSheet(u"QLineEdit, QComboBox, QListWidget {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    color: #FFFFFF;\n"
"}")
        self.cities_wgt_1.setAutoScroll(True)

        self.horizontalLayout.addWidget(self.cities_wgt_1)

        self.distances_wgt_1 = QListWidget(self.train_frame)
        self.distances_wgt_1.setObjectName(u"distances_wgt_1")
        self.distances_wgt_1.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.distances_wgt_1.setStyleSheet(u"QLineEdit, QComboBox, QListWidget {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    color: #FFFFFF;\n"
"}")
        self.distances_wgt_1.setAutoScroll(True)

        self.horizontalLayout.addWidget(self.distances_wgt_1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.select_all_train = QCheckBox(self.train_frame)
        self.select_all_train.setObjectName(u"select_all_train")
        self.select_all_train.setStyleSheet(u"QCheckBox {\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.select_all_train.checkStateChanged.connect(lambda: self.tuggle_all(1))

        self.select_all_train_2 = QCheckBox(self.train_frame)
        self.select_all_train_2.setObjectName(u"select_all_train_2")
        self.select_all_train_2.setStyleSheet(u"QCheckBox {\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.select_all_train_2.checkStateChanged.connect(lambda: self.tuggle_all(2))

        self.horizontalLayout_5.addWidget(self.select_all_train)
        self.horizontalLayout_5.addWidget(self.select_all_train_2)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pred_label = QLabel(self.train_frame)
        self.pred_label.setObjectName(u"pred_label")
        self.pred_label.setStyleSheet(u"QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF;\n"
"}")

        self.verticalLayout_2.addWidget(self.pred_label)

        self.start_date_pred_wgt = QDateEdit(self.train_frame)
        self.start_date_pred_wgt.setObjectName(u"start_date_pred_wgt")
        self.start_date_pred_wgt.setCalendarPopup(True)
        self.start_date_pred_wgt.setDate(QDate.currentDate())
        self.start_date_pred_wgt.setStyleSheet(u"QDateEdit {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #CCCCCC;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(C:/machine learning/gb_greyhound/grayhound/grayhound/grayhound/bddata/ui/icons/arrow_down.svg);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCalendarWidget {\n"
"    background-color: #6D5BBA;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: #FFFFFF;\n"
"    background: none;\n"
"    border: none;\n"
"    margin: 0;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QCalendarW"
                        "idget QToolButton:hover {\n"
"    background-color: #8D58BF;\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"    background-color: #6D5BBA;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox {\n"
"    background: none;\n"
"    color: #FFFFFF;\n"
"    selection-background-color: #8D58BF;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button, QCalendarWidget QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border: none;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-arrow, QCalendarWidget QSpinBox::down-arrow {\n"
"    image: url(C:/machine learning/gb_greyhound/grayhound/grayhound/grayhound/bddata/ui/icons/arrow_up.svg); \n"
"    width: 10px;\n"
"    height: 10px;\n"
"}")

        self.verticalLayout_2.addWidget(self.start_date_pred_wgt)

        self.end_date_pred_wgt = QDateEdit(self.train_frame)
        self.end_date_pred_wgt.setObjectName(u"end_date_pred_wgt")
        self.end_date_pred_wgt.setCalendarPopup(True)
        self.end_date_pred_wgt.setDate(QDate.currentDate())
        self.end_date_pred_wgt.setStyleSheet(u"QDateEdit {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #CCCCCC;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(C:/machine learning/gb_greyhound/grayhound/grayhound/grayhound/bddata/ui/icons/arrow_down.svg);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCalendarWidget {\n"
"    background-color: #6D5BBA;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: #FFFFFF;\n"
"    background: none;\n"
"    border: none;\n"
"    margin: 0;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QCalendarW"
                        "idget QToolButton:hover {\n"
"    background-color: #8D58BF;\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"    background-color: #6D5BBA;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox {\n"
"    background: none;\n"
"    color: #FFFFFF;\n"
"    selection-background-color: #8D58BF;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button, QCalendarWidget QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border: none;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-arrow, QCalendarWidget QSpinBox::down-arrow {\n"
"    image: url(C:/machine learning/gb_greyhound/grayhound/grayhound/grayhound/bddata/ui/icons/arrow_up.svg); \n"
"    width: 10px;\n"
"    height: 10px;\n"
"}")

        self.verticalLayout_2.addWidget(self.end_date_pred_wgt)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cities_2 = QListWidget(self.train_frame)
        self.cities_2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.cities_2.itemSelectionChanged.connect(self.on_item_selected_pred)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        QListWidgetItem(self.cities_2)
        self.cities_2.setObjectName(u"cities_2")
        self.cities_2.setStyleSheet(u"QLineEdit, QComboBox, QListWidget {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    color: #FFFFFF;\n"
"}")
        self.cities_2.setAutoScroll(True)

        self.horizontalLayout_2.addWidget(self.cities_2)

        self.listWidget_4 = QListWidget(self.train_frame)
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget_4.setStyleSheet(u"QLineEdit, QComboBox, QListWidget {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    color: #FFFFFF;\n"
"}")
        self.listWidget_4.setAutoScroll(True)

        self.horizontalLayout_2.addWidget(self.listWidget_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.select_all_pred = QCheckBox(self.train_frame)
        self.select_all_pred.setObjectName(u"select_all_pred")
        self.select_all_pred.setStyleSheet(u"QCheckBox {\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.select_all_pred.checkStateChanged.connect(lambda: self.tuggle_all(3))

        self.select_all_pred_2 = QCheckBox(self.train_frame)
        self.select_all_pred_2.setObjectName(u"select_all_pred_2") 
        self.select_all_pred_2.setStyleSheet(u"QCheckBox {\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.select_all_pred_2.checkStateChanged.connect(lambda: self.tuggle_all(4))

        self.horizontalLayout_6.addWidget(self.select_all_pred)
        self.horizontalLayout_6.addWidget(self.select_all_pred_2)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addWidget(self.train_frame)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.train_btn = QPushButton(self.layoutWidget)
        self.train_btn.setObjectName(u"train_btn")
        self.train_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #6D5BBA;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    color: #FFFFFF;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8D58BF;\n"
"}")

        self.horizontalLayout_4.addWidget(self.train_btn)

        self.predict_btn = QPushButton(self.layoutWidget)
        self.predict_btn.setObjectName(u"predict_btn")
        self.predict_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #6D5BBA;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    color: #FFFFFF;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8D58BF;\n"
"}")

        self.horizontalLayout_4.addWidget(self.predict_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.today_predict_btn = QPushButton(self.layoutWidget)
        self.today_predict_btn.setObjectName(u"today_predict_btn")
        self.today_predict_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #6D5BBA;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    color: #FFFFFF;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8D58BF;\n"
"}")

        self.verticalLayout_4.addWidget(self.today_predict_btn)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.info_list_wgt = QListWidget(self.layoutWidget)
        self.info_list_wgt.setObjectName(u"info_list_wgt")
        self.info_list_wgt.setStyleSheet(u"QLineEdit, QComboBox, QListWidget {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    color: #FFFFFF;\n"
"}")
        self.info_list_wgt.setSpacing(1)

        self.verticalLayout_5.addWidget(self.info_list_wgt)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.train_label.setText(QCoreApplication.translate("Form", u"\u0414\u0438\u0430\u043f\u043e\u0437\u043e\u043d \u0432\u044b\u0431\u043e\u0440\u043a\u0438", None))

        __sortingEnabled = self.cities_wgt_1.isSortingEnabled()
        self.cities_wgt_1.setSortingEnabled(False)
        ___qlistwidgetitem = self.cities_wgt_1.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"Hove", None));
        ___qlistwidgetitem1 = self.cities_wgt_1.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"Central Park", None));
        ___qlistwidgetitem2 = self.cities_wgt_1.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"Crayford", None));
        ___qlistwidgetitem3 = self.cities_wgt_1.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"Doncaster", None));
        ___qlistwidgetitem4 = self.cities_wgt_1.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Form", u"Harlow", None));
        ___qlistwidgetitem5 = self.cities_wgt_1.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Form", u"Kinsley", None));
        ___qlistwidgetitem6 = self.cities_wgt_1.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Form", u"Monmore", None));
        ___qlistwidgetitem7 = self.cities_wgt_1.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Form", u"Newcastle", None));
        ___qlistwidgetitem8 = self.cities_wgt_1.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Form", u"Nottingham", None));
        ___qlistwidgetitem9 = self.cities_wgt_1.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Form", u"Oxford", None));
        ___qlistwidgetitem10 = self.cities_wgt_1.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Form", u"Pelaw Grange", None));
        ___qlistwidgetitem11 = self.cities_wgt_1.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Form", u"Perry Barr", None));
        ___qlistwidgetitem12 = self.cities_wgt_1.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("Form", u"Romford", None));
        ___qlistwidgetitem13 = self.cities_wgt_1.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("Form", u"Sheffield", None));
        ___qlistwidgetitem14 = self.cities_wgt_1.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("Form", u"Suffolk Downs", None));
        ___qlistwidgetitem15 = self.cities_wgt_1.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("Form", u"Sunderland", None));
        ___qlistwidgetitem16 = self.cities_wgt_1.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("Form", u"Swindon", None));
        ___qlistwidgetitem17 = self.cities_wgt_1.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("Form", u"Towcester", None));
        ___qlistwidgetitem18 = self.cities_wgt_1.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("Form", u"Valley", None));
        ___qlistwidgetitem19 = self.cities_wgt_1.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("Form", u"Yarmouth", None));
        self.cities_wgt_1.setSortingEnabled(__sortingEnabled)

        self.select_all_train.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.select_all_train_2.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.pred_label.setText(QCoreApplication.translate("Form", u"\u0414\u0438\u0430\u043f\u043e\u0437\u043e\u043d \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0430\u043d\u0438\u0439", None))

        __sortingEnabled1 = self.cities_2.isSortingEnabled()
        self.cities_2.setSortingEnabled(False)
        ___qlistwidgetitem20 = self.cities_2.item(0)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("Form", u"Hove", None));
        ___qlistwidgetitem21 = self.cities_2.item(1)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("Form", u"Central Park", None));
        ___qlistwidgetitem22 = self.cities_2.item(2)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("Form", u"Crayford", None));
        ___qlistwidgetitem23 = self.cities_2.item(3)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("Form", u"Doncaster", None));
        ___qlistwidgetitem24 = self.cities_2.item(4)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("Form", u"Harlow", None));
        ___qlistwidgetitem25 = self.cities_2.item(5)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("Form", u"Kinsley", None));
        ___qlistwidgetitem26 = self.cities_2.item(6)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("Form", u"Monmore", None));
        ___qlistwidgetitem27 = self.cities_2.item(7)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("Form", u"Newcastle", None));
        ___qlistwidgetitem28 = self.cities_2.item(8)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("Form", u"Nottingham", None));
        ___qlistwidgetitem29 = self.cities_2.item(9)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("Form", u"Oxford", None));
        ___qlistwidgetitem30 = self.cities_2.item(10)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("Form", u"Pelaw Grange", None));
        ___qlistwidgetitem31 = self.cities_2.item(11)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("Form", u"Perry Barr", None));
        ___qlistwidgetitem32 = self.cities_2.item(12)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("Form", u"Romford", None));
        ___qlistwidgetitem33 = self.cities_2.item(13)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("Form", u"Sheffield", None));
        ___qlistwidgetitem34 = self.cities_2.item(14)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("Form", u"Suffolk Downs", None));
        ___qlistwidgetitem35 = self.cities_2.item(15)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("Form", u"Sunderland", None));
        ___qlistwidgetitem36 = self.cities_2.item(16)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("Form", u"Swindon", None));
        ___qlistwidgetitem37 = self.cities_2.item(17)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("Form", u"Towcester", None));
        ___qlistwidgetitem38 = self.cities_2.item(18)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("Form", u"Valley", None));
        ___qlistwidgetitem39 = self.cities_2.item(19)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("Form", u"Yarmouth", None));
        self.cities_2.setSortingEnabled(__sortingEnabled1)

        self.select_all_pred.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.select_all_pred_2.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.train_btn.setText(QCoreApplication.translate("Form", u"\u0422\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.predict_btn.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.today_predict_btn.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0430\u0442\u044c \u043d\u0430 \u0441\u0435\u0433\u043e\u0434\u043d\u044f", None))
    # retranslateUi

    def on_item_selected_train(self):
        self.distances_wgt_1.clear()

        cities = [item.text() for item in self.cities_wgt_1.selectedItems()]
        
        for i in range(0, len(cities)):
            city = cities[i]
            item = QListWidgetItem(city)
            item.setFlags(item.flags() & ~Qt.ItemIsSelectable)

            self.distances_wgt_1.addItem(item)
            distances = tracks[city]

            for dist in distances:
                dist_item = QListWidgetItem(str(dist))
                dist_item.setData(Qt.UserRole, city)
                self.distances_wgt_1.addItem(dist_item)

    def on_item_selected_pred(self):
        self.listWidget_4.clear()

        selected_items = [item.text() for item in self.cities_2.selectedItems()]
        
        for i in range(0, len(selected_items)):
            city = selected_items[i]
            item = QListWidgetItem(city)
            item.setFlags(item.flags() & ~Qt.ItemIsSelectable)

            self.listWidget_4.addItem(item)
            distances = tracks[city]

            for dist in distances:
                dist_item = QListWidgetItem(str(dist))
                dist_item.setData(Qt.UserRole, city)
                self.listWidget_4.addItem(dist_item)
        
    def tuggle_all(self, mode):
        if mode == 1:
            state = True
            if not self.select_all_train.isChecked():
                state = False
            for i in range(self.cities_wgt_1.count()):
                    item = self.cities_wgt_1.item(i)
                    item.setSelected(state)
        elif mode == 2:
            state = True
            if not self.select_all_train_2.isChecked():
                state = False
            for i in range(self.distances_wgt_1.count()):
                item = self.distances_wgt_1.item(i)
                item.setSelected(state)
        elif mode == 3:
            state = True
            if not self.select_all_pred.isChecked():
                state = False
            for i in range(self.cities_2.count()):
                item = self.cities_2.item(i)
                item.setSelected(state)
        elif mode == 4:
            state = True
            if not self.select_all_pred_2.isChecked():
                state = False
            for i in range(self.listWidget_4.count()):
                item = self.listWidget_4.item(i)
                item.setSelected(state)

    def add_message(self, message):
        if message:
            self.info_list_wgt.addItem(message)

    def get_date_train(self):
        start_date_train = self.start_date_train_wgt.date().toString("dd/MM/yyyy")
        end_date_train = self.end_date_train_wgt.date().toString("dd/MM/yyyy")

        return start_date_train, end_date_train
    
    def get_date_pred(self):
        start_date_pred = self.start_date_pred_wgt.date().toString("dd/MM/yyyy")
        end_date_pred = self.end_date_pred_wgt.date().toString("dd/MM/yyyy")

        return start_date_pred, end_date_pred
    
    
    def get_distances_train(self):
        selected_items = self.distances_wgt_1.selectedItems()
        
        distances = [item.text() for item in selected_items]
        distances_with_cities = [(item.text(), item.data(Qt.UserRole)) for item in selected_items]
        
        distances_dict = {}
        cities = []

        for distance, city in distances_with_cities:
            if city not in distances_dict:
                distances_dict[city] = []
                cities.append(city)
            distances_dict[city].append(distance)
        
        return cities, distances, distances_dict
    
    
    def get_distances_pred(self):
        selected_items = self.listWidget_4.selectedItems()
        
        distances = [item.text() for item in selected_items]
        distances_with_cities = [(item.text(), item.data(Qt.UserRole)) for item in selected_items]
        
        distances_dict = {}
        cities = []

        for distance, city in distances_with_cities:
            if city not in distances_dict:
                distances_dict[city] = []
                cities.append(city)
            distances_dict[city].append(distance)
        
        return cities, distances, distances_dict

            


    

