import sys

from grayhound.app.ui.main_window import MainWindow
from PySide6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()        

    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()