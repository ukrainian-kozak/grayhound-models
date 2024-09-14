# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'side_bar.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(70, 640)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 70, 640))
        self.widget.setStyleSheet(u"background-color: rgb(75, 75, 75);")

        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 61, 270))

        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(75, 75, 75);\n"
"    border: none;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(81, 81, 81)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(124, 124, 124);\n"
"}")
        icon = QIcon()
        icon.addFile("C:/machine learning/gb_greyhound/grayhound/grayhound/grayhound/bddata/ui/icons/model_training.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(32, 32))
        self.pushButton_2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(75, 75, 75);\n"
"    border: none;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(81, 81, 81)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(124, 124, 124);\n"
"}")
        icon1 = QIcon()
        icon1.addFile("C:/machine learning/gb_greyhound/grayhound/grayhound/grayhound/bddata/ui/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(32, 32))
        self.pushButton.setCheckable(True)

        self.verticalLayout_6.addWidget(self.pushButton)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(75, 75, 75);\n"
"    border: none;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(81, 81, 81)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(124, 124, 124);\n"
"}")
        icon3 = QIcon()
        icon3.addFile("C:/machine learning/gb_greyhound/grayhound/grayhound/grayhound/bddata/ui/icons/table.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(32, 32))
        self.pushButton_4.setCheckable(True)

        self.verticalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(75, 75, 75);\n"
"    border: none;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(81, 81, 81)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(124, 124, 124);\n"
"}")
        icon2 = QIcon()
        icon2.addFile("C:/machine learning/gb_greyhound/grayhound/grayhound/grayhound/bddata/ui/icons/bug.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(32, 32))
        self.pushButton_3.setCheckable(True)

        self.verticalLayout_6.addWidget(self.pushButton_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.pushButton_3.setText("")
    # retranslateUi

