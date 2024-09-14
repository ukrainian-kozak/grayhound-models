from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QStackedWidget, QMessageBox

from grayhound.app.ui.ui_side_bar import Ui_Form as SidePanelUI
from grayhound.app.ui.ui_main_window import Ui_Form as Page1UI
from grayhound.app.ui.ui_model_config import Ui_Form as Page2UI
from grayhound.app.ui.ui_table import Ui_Form as Page3UI
from grayhound.app.ui.ui_scraping_window import Ui_Form as Page4UI
from grayhound.app.ui.ui_predictions import PredictionsWindow

from grayhound.app.gh_model.predict import make_predictions
from grayhound.app.gh_model.preprocessing import pred_df_preprocessing
from grayhound.app.gh_model.convertation import load_and_convert_temp_file

from grayhound.app.main.logger import GHLogger


logger = GHLogger("main_window")

#TODO: to log it. Check if I can handle some exceptions and errors.

class SideMenu(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.ui = SidePanelUI()
        self.ui.setupUi(self)
        self.setup_connections()

    def setup_connections(self):
        self.ui.pushButton_2.clicked.connect(lambda: self.main_window.display_page(0))
        self.ui.pushButton.clicked.connect(lambda: self.main_window.display_page(1))
        self.ui.pushButton_3.clicked.connect(lambda: self.main_window.display_page(3))
        self.ui.pushButton_4.clicked.connect(lambda: self.main_window.display_page(2))

class Page(QWidget):
    def __init__(self, ui_class, parent=None):
        super().__init__(parent)
        self.ui = ui_class()
        self.ui.setupUi(self)


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        logger.debug("FUNCTION: __init__ inizializing")
        super().__init__(parent)
        self.ui_init()
        self._connect_signals()

    def ui_init(self):
        logger.debug("FUNCTION: ui_init inizializing")
        self.setWindowTitle("App")
        self.setGeometry(100, 100, 1300, 640)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout(self.central_widget)
        self.central_widget.setLayout(self.layout)

        self.side_menu = SideMenu(self)
        self.side_menu.setFixedWidth(70)
        self.layout.addWidget(self.side_menu)

        self.stack = QStackedWidget(self)
        self.layout.addWidget(self.stack)

        self.add_pages()

        self.main_page = self.stack.widget(0)
        self.scraping_page = self.stack.widget(3)
        


    def _connect_signals(self):
        logger.debug("FUNCTION: _connect_signals inizializing")
        # self.main_page.ui.train_btn.clicked.connect(self.train_model)
        # self.main_page.ui.predict_btn.clicked.connect(self.pred_data)
        self.main_page.ui.today_predict_btn.clicked.connect(self.pred_today)
        # self.scraping_page.ui.scraping_btn.clicked.connect(self.scraping)

    # def scraping(self):
    #     dates = self.scraping_page.ui.get_date()
    #     api_key = self.scraping_page.ui.line_scraping.text()
    #
    #     if not api_key:
    #         print('Рома, нужно указать API Key в разделе Scraping! (просто написать его туда)')
    #         return
    #
    #     grayhound_process = CrawlerProcess()
    #     grayhound_process.crawl(GrayhoundSpider, api_key=api_key, dates=dates)
    #     grayhound_process.start()


    def add_pages(self):
        logger.debug("FUNCTION: add_pages inizializing")
        self.pages = [
            Page(Page1UI),
            Page(Page2UI),
            Page(Page3UI),
            Page(Page4UI)
        ]

        for page_widget in self.pages:
            self.stack.addWidget(page_widget)

    def display_page(self, index):
        logger.debug(f"FUNCTION: display page\ndisplaying page with index: {index}")
        self.stack.setCurrentIndex(index)

    def show_message_box(self, message):
        logger.debug(f"FUNCTION: show_message_box\nshowing message: {message}")
        app = QApplication.instance()
        if not app:
            app = QApplication([])

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(message)
        msg_box.setWindowTitle("Message")
        msg_box.setStandardButtons(QMessageBox.Ok)

        msg_box.exec()


    def populate_model(self, predictions, results):
        data = [[None for _ in range(6)] for _ in range(12)]

        for race in range(len(predictions)):
            size = len(predictions[race])
            for position in range(size):
                predicted_rank = predictions[race][position] - 1
                actual_rank = results[race][position] - 1
                if size == 5:
                    row_index = predicted_rank + 7
                    if data[row_index][actual_rank] is None:
                        data[row_index][actual_rank] = 0
                    data[row_index][actual_rank] += 1
                else:
                    if data[predicted_rank][actual_rank] is None:
                        data[predicted_rank][actual_rank] = 0
                    data[predicted_rank][actual_rank] += 1

        self.stack.widget(2).ui.model.setItems(data)


    # def train_model(self):
    #     print('train model function')
    #     first_page = self.stack.widget(0).ui
    #     second_page = self.stack.widget(1).ui
    #
    #     start_date_train, end_date_train = first_page.get_date_train()
    #
    #     start_date_train += ' 00:00:00'
    #     end_date_train += ' 23:59:00'
    #
    #     tracks, distances, dict_dist = first_page.get_distances_train()
    #     params = second_page.get_params()
    #
    #     if not distances:
    #         self.show_message_box('Рома, ты забыл выбрать дистанцию для тренировки!!!!')
    #
    #     elif not params:
    #         self.show_message_box('Рома, ты забыл указать параметры!!!')
    #
    #     else:
    #         num_races = get_train(start_date_train, end_date_train, distances, tracks, params, dict_dist)
    #
    #         if num_races < 0:
    #             first_page.add_message(f'Уже есть обученная модель с такими параметрами, обучение прошло успешно!')
    #         else:
    #             first_page.add_message(f'Обучение произошло на {num_races} гонках')
    #
    #         train(start_date_train, end_date_train, distances, tracks, params)

    # def pred_data(self):
    #     first_page = self.stack.widget(0).ui
    #     second_page = self.stack.widget(1).ui
    #
    #     start_date_pred, end_date_pred = first_page.get_date_pred()
    #     start_date_train, end_date_train = first_page.get_date_train()
    #
    #     start_date_pred += ' 00:00:00'
    #     end_date_pred += ' 23:59:00'
    #     start_date_train += ' 00:00:00'
    #     end_date_train += ' 23:59:00'
    #
    #     tracks_p, distances_p, dict_dist = first_page.get_distances_pred()
    #     tracks_t, distances_t, _ = first_page.get_distances_train()
    #     params = second_page.get_params()
    #
    #     if not distances_p:
    #         self.show_message_box('Рома, ты забыл выбрать дистанцию для предсказаний!!!!')
    #
    #     elif not params:
    #         self.show_message_box('Рома, ты забыл указать параметры!!!')
    #
    #     else:
    #         num_races = get_test_prediction(start_date_pred, end_date_pred, distances_p, tracks_p, params, dict_dist)
    #
    #         if num_races < 0:
    #             first_page.add_message(f'Уже есть обученная модель с такими параметрами!')
    #         else:
    #             first_page.add_message(f'Результат спрогнозирован на {num_races} гонках')
    #
    #         predictions, results, _ = predict(start_date_pred, end_date_pred, start_date_train, end_date_train, distances_t, tracks_t, distances_p, tracks_p, params)
    #
    #         self.populate_model(predictions, results)


    def pred_today(self):
        dfs = pred_df_preprocessing()
        make_predictions(dfs)


    def display_predictions(self, data) -> None:
        pred_window = PredictionsWindow(data)
        pred_window.show()


    def prep_pred_window_data(self, res_x, res_y, prob) -> dict:
        df = load_and_convert_temp_file()
        data = list()

        for i, row in df.iterrows():
            names = row['names']
            time = row['time']

            arr = [res_x[i], res_y[i], prob[i], names]

            data.append({
                'title': time,
                'participants': arr
            })

        return data