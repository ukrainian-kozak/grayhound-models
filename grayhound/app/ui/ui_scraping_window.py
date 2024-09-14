# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scraping_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QProgressBar,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)


from datetime import date

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1234, 721)
        Form.setStyleSheet(u"/* \u0417\u0430\u0433\u0430\u043b\u044c\u043d\u0456 \u043d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u043d\u044f \u0434\u043b\u044f \u0432\u0441\u044c\u043e\u0433\u043e \u0434\u043e\u0434\u0430\u0442\u043a\u0443 */\n"
"QWidget {\n"
"    background-color: #7B1FA2;\n"
"    color: white;\n"
"    font-family: Arial, sans-serif;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u0438\u0445 \u043f\u043e\u043b\u0456\u0432 */\n"
"QLineEdit {\n"
"    background-color: #9575CD;\n"
"    border: 1px solid #D1C4E9;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043e\u043a */\n"
"QPushButton {\n"
"    background-color: #512DA8;\n"
"    border: 1px solid #9575CD;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #673AB7;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b"
                        "\u044f \u0441\u043f\u0438\u0441\u043a\u0456\u0432 */\n"
"QListView, QTreeView {\n"
"    background-color: #9575CD;\n"
"    border: 1px solid #D1C4E9;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0433\u0440\u0443\u043f\u043e\u0432\u0438\u0445 \u0431\u043b\u043e\u043a\u0456\u0432 */\n"
"QGroupBox {\n"
"    border: 1px solid #D1C4E9;\n"
"    border-radius: 4px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 3px;\n"
"    background-color: #7B1FA2;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043f\u043e\u043b\u0456\u0432 \u0434\u0430\u0442\u0438 */\n"
"QDateEdit {\n"
"    background-color: #9575CD;\n"
"    border: 1px solid #D1C4E9;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043f\u0440\u043e\u0433\u0440\u0435\u0441-\u0431\u0430\u0440\u0443 */\n"
"QProgressB"
                        "ar {\n"
"    border: 1px solid #D1C4E9;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #512DA8;\n"
"}\n"
"\n"
"/* \u0421\u043f\u0435\u0446\u0438\u0444\u0456\u0447\u043d\u0456 \u043d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u043d\u044f \u0434\u043b\u044f \u043e\u043a\u0440\u0435\u043c\u0438\u0445 \u0435\u043b\u0435\u043c\u0435\u043d\u0442\u0456\u0432 */\n"
"#apiKeyInput {\n"
"    background-color: #9575CD;\n"
"    border: 1px solid #D1C4E9;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 551, 321))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_api_key = QLabel(self.widget)
        self.label_api_key.setObjectName(u"label_api_key")

        self.verticalLayout.addWidget(self.label_api_key)

        self.line_scraping = QLineEdit(self.widget)
        self.line_scraping.setObjectName(u"line_scraping")

        self.verticalLayout.addWidget(self.line_scraping)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_scraping = QLabel(self.widget)
        self.label_scraping.setObjectName(u"label_scraping")

        self.verticalLayout_2.addWidget(self.label_scraping)

        self.date_scraping = QDateEdit(self.widget)
        self.date_scraping.setObjectName(u"date_scraping")
        self.date_scraping.setCalendarPopup(True)
        self.date_scraping.setDate(date.today())

        self.verticalLayout_2.addWidget(self.date_scraping)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rmv_date_btn = QPushButton(self.widget)
        self.rmv_date_btn.setObjectName(u"rmv_date_btn")

        self.horizontalLayout.addWidget(self.rmv_date_btn)

        self.add_date_btn = QPushButton(self.widget)
        self.add_date_btn.setObjectName(u"add_date_btn")

        self.horizontalLayout.addWidget(self.add_date_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.date_list = QListWidget(self.widget)
        self.date_list.setObjectName(u"date_list")

        self.horizontalLayout_2.addWidget(self.date_list)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(370, 510, 461, 171))
        self.verticalLayout_4 = QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scraping_btn = QPushButton(self.widget1)
        self.scraping_btn.setObjectName(u"scraping_btn")
        self.scraping_btn.setEnabled(True)
        self.scraping_btn.setFlat(False)

        self.verticalLayout_4.addWidget(self.scraping_btn)

        self.scraping_progress_bar = QProgressBar(self.widget1)
        self.scraping_progress_bar.setObjectName(u"scraping_progress_bar")
        self.scraping_progress_bar.setValue(0)

        self.verticalLayout_4.addWidget(self.scraping_progress_bar)

        self.add_date_btn.clicked.connect(self.add_date)
        self.rmv_date_btn.clicked.connect(self.remove_date)


        self.retranslateUi(Form)

        self.scraping_btn.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_api_key.setText(QCoreApplication.translate("Form", u"API KEY", None))
        self.label_scraping.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0441\u043a\u0440\u0430\u043f\u0438\u043d\u0433\u0430", None))
        self.rmv_date_btn.setText(QCoreApplication.translate("Form", u"\u0423\u0431\u0440\u0430\u0442\u044c \u0434\u0430\u0442\u0443", None))
        self.add_date_btn.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0430\u0442\u0443", None))
        self.scraping_btn.setText(QCoreApplication.translate("Form", u"\u0441\u043a\u0440\u0430\u043f\u0438\u0442\u044c!!!", None))
    # retranslateUi

    def get_date(self) -> list:
        dates = [self.date_list.item(i).text() for i in range(self.date_list.count())]
        return dates
    
    def add_date(self) -> None:
        item = QListWidgetItem(self.get_day())
        self.date_list.addItem(item)
        self.list_wgt_check()

    def remove_date(self) -> None:
        self.date_list.clear()
        self.add_date_btn.setCheckable(True)
        self.add_date_btn.setEnabled(True)

    def get_day(self) -> str:
        date_to_scrape = self.date_scraping.date().toString("yyyy-MM-dd")
        return date_to_scrape
    
    def list_wgt_check(self) -> None:
        if self.date_list.count() >= 3:
            self.add_date_btn.setCheckable(False)
            self.add_date_btn.setEnabled(False)
        else:
            self.add_date_btn.setCheckable(True)
            self.add_date_btn.setEnabled(True)
                
            

