from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, 
    QLabel, QScrollArea, 
    QHBoxLayout, QTableWidget, QTableWidgetItem)

from datetime import date




class OnePrediction(QWidget):
    def __init__(self, title_data=None, participants_data=None) -> None:
        super().__init__()

        self.title_data = title_data
        self.participants_data = participants_data
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        if self.title_data:
            title = QLabel(f"{self.title_data['place']} - {self.title_data['time']} - {self.title_data['rank']} - {self.title_data['distance']}")
            self.layout.addWidget(title)

        self.table = QTableWidget()

        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Имя", "Кэф", "Пред. время"])

        if self.participants_data:
            self.table.setRowCount(len(self.participants_data))
            for i, row in enumerate(self.participants_data):
                for j, item in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(item))

        self.layout.addWidget(self.table)
        self.setLayout(self.layout)



class PredictionsWindow(QWidget):
    def __init__(self, predictions_data):
        super().__init__()

        self.predictions_data = predictions_data
        self.initUI()

    def initUI(self) -> None:

        date_today = date.today()

        self.setWindowTitle(f"{date_today} Предсказания")
        self.setGeometry(100, 100, 1800, 900)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.scroll_area = QScrollArea()
        self.scroll_area_widget_contents = QWidget()
        self.scroll_area_layout = QVBoxLayout()
        self.scroll_area_widget_contents.setLayout(self.scroll_area_layout)
        self.scroll_area.setWidget(self.scroll_area_widget_contents)
        self.scroll_area.setWidgetResizable(True)

        self.layout.addWidget(self.scroll_area)

        self.add_predictions()

    def add_predictions(self):
        hbxlayout = QHBoxLayout()

        for i, data in enumerate(self.predictions_data, 1):
            prediction_widget = OnePrediction(data['title'], data['participants'])
            hbxlayout.addWidget(prediction_widget)
            if i % 3 == 0 or i == len(self.predictions_data):
                self.scroll_area_layout.addLayout(hbxlayout)
                hbxlayout = QHBoxLayout()