# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_table.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import QtCore
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget, QTableView)


class ItemModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.items = []
    
    def setItems(self, items):
        self.items = items
        self.layoutChanged.emit()


    def rowCount(self, *args, **kwargs) -> int:
        return 12
    
    def columnCount(self, *args, **kwargs) -> int:
        return 6
    
    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):

        if not index.isValid():
            return
        
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            try:
                return self.items[index.row()][index.column()]
            except IndexError:
                return None
        
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Vertical:
                return {
                    0: '1 прог.',
                    1: '2 прог.',
                    2: '3 прог.',
                    3: '4 прог.',
                    4: '5 прог.',
                    5: '6 прог.',
                    6: '...',
                    7: '1 прог.',
                    8: '2 прог.',
                    9: '3 прог.',
                    10: '4 прог.',
                    11: '5 прог.'
                }.get(section)
            elif orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                    0: 'факт. 1',
                    1: 'факт. 2',
                    2: 'факт. 3',
                    3: 'факт. 4',
                    4: 'факт. 5',
                    5: 'факт. 6'
                }.get(section)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1294, 868)
        Form.setStyleSheet(u" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #6D5BBA, stop:1 #8D58BF);\n"
"    color: #FFFFFF;\n"
"    font-family: Arial, sans-serif;")
        self.tableWidget = QTableView(Form)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 1294, 868))
        self.tableWidget.setAutoFillBackground(True)
        self.model = ItemModel()
        self.tableWidget.setModel(self.model)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

