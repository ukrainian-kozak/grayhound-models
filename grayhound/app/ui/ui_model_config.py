# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_model_config.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1294, 868)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #6D5BBA, stop:1 #8D58BF);\n"
"color: #FFFFFF;\n"
"font-family: Arial, sans-serif;")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1200, 590))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 2px solid #8D58BF;\n"
"    border-radius: 10px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 3px;\n"
"    background-color: #8D58BF;\n"
"    border-radius: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0447\u0435\u043a\u0431\u043e\u043a\u0441\u043e\u0432 */\n"
"QCheckBox {\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u043a\u043e\u043c\u0431\u043e\u0431\u043e\u043a\u0441\u0430 */\n"
"QSpinBox {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #FFFFFF;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.categoria_A_label = QLabel(self.groupBox)
        self.categoria_A_label.setObjectName(u"categoria_A_label")
        self.categoria_A_label.setStyleSheet(u"QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF;\n"
"}")

        self.verticalLayout.addWidget(self.categoria_A_label)

        self.race_amount_spbox = QSpinBox(self.groupBox)
        self.race_amount_spbox.setObjectName(u"race_amount_spbox")
        self.race_amount_spbox.setMaximum(10)

        self.verticalLayout.addWidget(self.race_amount_spbox)

        self.sec_time_btn = QCheckBox(self.groupBox)
        self.sec_time_btn.setObjectName(u"sec_time_btn")

        self.verticalLayout.addWidget(self.sec_time_btn)

        self.fin_pos_btn = QCheckBox(self.groupBox)
        self.fin_pos_btn.setObjectName(u"fin_pos_btn")

        self.verticalLayout.addWidget(self.fin_pos_btn)

        self.trap_btn = QCheckBox(self.groupBox)
        self.trap_btn.setObjectName(u"trap_btn")

        self.verticalLayout.addWidget(self.trap_btn)

        self.dist_btn = QCheckBox(self.groupBox)
        self.dist_btn.setObjectName(u"dist_btn")

        self.verticalLayout.addWidget(self.dist_btn)

        self.adj_time_btn = QCheckBox(self.groupBox)
        self.adj_time_btn.setObjectName(u"adj_time_btn")

        self.verticalLayout.addWidget(self.adj_time_btn)

        self.odds_btn = QCheckBox(self.groupBox)
        self.odds_btn.setObjectName(u"odds_btn")

        self.verticalLayout.addWidget(self.odds_btn)

        self.run_time_btn = QCheckBox(self.groupBox)
        self.run_time_btn.setObjectName(u"run_time_btn")

        self.verticalLayout.addWidget(self.run_time_btn)

        self.dog_weight_btn = QCheckBox(self.groupBox)
        self.dog_weight_btn.setObjectName(u"dog_weight_btn")

        self.verticalLayout.addWidget(self.dog_weight_btn)

        self.win_time_btn = QCheckBox(self.groupBox)
        self.win_time_btn.setObjectName(u"win_time_btn")

        self.verticalLayout.addWidget(self.win_time_btn)

        self.select_all_A = QCheckBox(self.groupBox)
        self.select_all_A.setObjectName(u"select_all_A")
        self.select_all_A.checkStateChanged.connect(lambda: self.tuggle_all(1))

        self.verticalLayout.addWidget(self.select_all_A)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox1 = QGroupBox(self.widget)
        self.groupBox1.setObjectName(u"groupBox1")
        self.groupBox1.setStyleSheet(u"QGroupBox {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 2px solid #8D58BF;\n"
"    border-radius: 10px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 3px;\n"
"    background-color: #8D58BF;\n"
"    border-radius: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0447\u0435\u043a\u0431\u043e\u043a\u0441\u043e\u0432 */\n"
"QCheckBox {\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u043a\u043e\u043c\u0431\u043e\u0431\u043e\u043a\u0441\u0430 */\n"
"QSpinBox {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #FFFFFF;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.curr_race_label = QLabel(self.groupBox1)
        self.curr_race_label.setObjectName(u"curr_race_label")
        self.curr_race_label.setStyleSheet(u"QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF;\n"
"}")

        self.verticalLayout_2.addWidget(self.curr_race_label)

        self.curr_trap_btn = QCheckBox(self.groupBox1)
        self.curr_trap_btn.setObjectName(u"curr_trap_btn")

        self.verticalLayout_2.addWidget(self.curr_trap_btn)

        self.curr_dist_btn = QCheckBox(self.groupBox1)
        self.curr_dist_btn.setObjectName(u"curr_dist_btn")

        self.verticalLayout_2.addWidget(self.curr_dist_btn)

        self.curr_odds_btn = QCheckBox(self.groupBox1)
        self.curr_odds_btn.setObjectName(u"curr_odds_btn")

        self.verticalLayout_2.addWidget(self.curr_odds_btn)

        self.curr_dog_weight_btn = QCheckBox(self.groupBox1)
        self.curr_dog_weight_btn.setObjectName(u"curr_dog_weight_btn")

        self.verticalLayout_2.addWidget(self.curr_dog_weight_btn)

        self.curr_race_grade_btn = QCheckBox(self.groupBox1)
        self.curr_race_grade_btn.setObjectName(u"curr_race_grade_btn")

        self.verticalLayout_2.addWidget(self.curr_race_grade_btn)

        self.select_all_B = QCheckBox(self.groupBox1)
        self.select_all_B.setObjectName(u"select_all_B")
        self.select_all_B.checkStateChanged.connect(lambda: self.tuggle_all(2))

        self.verticalLayout_2.addWidget(self.select_all_B)


        self.horizontalLayout.addWidget(self.groupBox1)

        self.groupBox2 = QGroupBox(self.widget)
        self.groupBox2.setObjectName(u"groupBox2")
        self.groupBox2.setStyleSheet(u"QGroupBox {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 2px solid #8D58BF;\n"
"    border-radius: 10px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 3px;\n"
"    background-color: #8D58BF;\n"
"    border-radius: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0447\u0435\u043a\u0431\u043e\u043a\u0441\u043e\u0432 */\n"
"QCheckBox {\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u043a\u043e\u043c\u0431\u043e\u0431\u043e\u043a\u0441\u0430 */\n"
"QSpinBox {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #FFFFFF;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.categoria_B_label = QLabel(self.groupBox2)
        self.categoria_B_label.setObjectName(u"categoria_B_label")
        self.categoria_B_label.setStyleSheet(u"QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF;\n"
"}")

        self.verticalLayout_3.addWidget(self.categoria_B_label)

        self.fin_pos_hist_btn = QCheckBox(self.groupBox2)
        self.fin_pos_hist_btn.setObjectName(u"fin_pos_hist_btn")

        self.verticalLayout_3.addWidget(self.fin_pos_hist_btn)

        self.race_all_btn = QCheckBox(self.groupBox2)
        self.race_all_btn.setObjectName(u"race_all_btn")

        self.verticalLayout_3.addWidget(self.race_all_btn)

        self.dist_by_btn = QCheckBox(self.groupBox2)
        self.dist_by_btn.setObjectName(u"dist_by_btn")

        self.verticalLayout_3.addWidget(self.dist_by_btn)

        self.race_all_curr_dist_btn = QCheckBox(self.groupBox2)
        self.race_all_curr_dist_btn.setObjectName(u"race_all_curr_dist_btn")

        self.verticalLayout_3.addWidget(self.race_all_curr_dist_btn)

        self.fst_curr_dist_btn = QCheckBox(self.groupBox2)
        self.fst_curr_dist_btn.setObjectName(u"fst_curr_dist_btn")

        self.verticalLayout_3.addWidget(self.fst_curr_dist_btn)

        self.scd_curr_dist_btn = QCheckBox(self.groupBox2)
        self.scd_curr_dist_btn.setObjectName(u"scd_curr_dist_btn")

        self.verticalLayout_3.addWidget(self.scd_curr_dist_btn)

        self.thrd_curr_dist_btn = QCheckBox(self.groupBox2)
        self.thrd_curr_dist_btn.setObjectName(u"thrd_curr_dist_btn")

        self.verticalLayout_3.addWidget(self.thrd_curr_dist_btn)

        self.frth_curr_dist_btn = QCheckBox(self.groupBox2)
        self.frth_curr_dist_btn.setObjectName(u"frth_curr_dist_btn")

        self.verticalLayout_3.addWidget(self.frth_curr_dist_btn)

        self.ffth_curr_dist_btn = QCheckBox(self.groupBox2)
        self.ffth_curr_dist_btn.setObjectName(u"ffth_curr_dist_btn")

        self.verticalLayout_3.addWidget(self.ffth_curr_dist_btn)

        self.sxth_curr_dist_btn = QCheckBox(self.groupBox2)
        self.sxth_curr_dist_btn.setObjectName(u"sxth_curr_dist_btn")

        self.verticalLayout_3.addWidget(self.sxth_curr_dist_btn)

        self.fin_pos_curr_dist_btn = QCheckBox(self.groupBox2)
        self.fin_pos_curr_dist_btn.setObjectName(u"fin_pos_curr_dist_btn")

        self.verticalLayout_3.addWidget(self.fin_pos_curr_dist_btn)

        self.sec_time_curr_dist_btn = QCheckBox(self.groupBox2)
        self.sec_time_curr_dist_btn.setObjectName(u"sec_time_curr_dist_btn")

        self.verticalLayout_3.addWidget(self.sec_time_curr_dist_btn)

        self.dog_grade_curr_dist_btn = QCheckBox(self.groupBox2)
        self.dog_grade_curr_dist_btn.setObjectName(u"dog_grade_curr_dist_btn")

        self.verticalLayout_3.addWidget(self.dog_grade_curr_dist_btn)

        self.best_run_time_curr_dist_btn = QCheckBox(self.groupBox2)
        self.best_run_time_curr_dist_btn.setObjectName(u"best_run_time_curr_dist_btn")

        self.verticalLayout_3.addWidget(self.best_run_time_curr_dist_btn)

        self.best_sec_time_curr_dist_btn = QCheckBox(self.groupBox2)
        self.best_sec_time_curr_dist_btn.setObjectName(u"best_sec_time_curr_dist_btn")

        self.verticalLayout_3.addWidget(self.best_sec_time_curr_dist_btn)

        self.select_all_C = QCheckBox(self.groupBox2)
        self.select_all_C.setObjectName(u"select_all_C")
        self.select_all_C.checkStateChanged.connect(lambda: self.tuggle_all(3))

        self.verticalLayout_3.addWidget(self.select_all_C)


        self.horizontalLayout.addWidget(self.groupBox2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.categoria_A_label.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b-\u0432\u043e \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0445 \u0433\u043e\u043d\u043e\u043a", None))
        self.sec_time_btn.setText(QCoreApplication.translate("Form", u"Sectional_time", None))
        self.fin_pos_btn.setText(QCoreApplication.translate("Form", u"\u0424\u0438\u043d\u0438\u0448\u043d\u0430\u044f \u043f\u043e\u0437\u0438\u0446\u0438\u044f", None))
        self.trap_btn.setText(QCoreApplication.translate("Form", u"Trap", None))
        self.dist_btn.setText(QCoreApplication.translate("Form", u"\u0414\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u044f", None))
        self.adj_time_btn.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0441 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u043a\u043e\u0439", None))
        self.odds_btn.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442", None))
        self.run_time_btn.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0431\u0435\u0437 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u043a\u0438", None))
        self.dog_weight_btn.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0441 \u0441\u043e\u0431\u0430\u043a\u0438", None))
        self.win_time_btn.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0438\u0433\u0440\u0430\u0448\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f", None))
        self.select_all_A.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.curr_race_label.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0433\u043e\u043d\u043a\u0430", None))
        self.curr_trap_btn.setText(QCoreApplication.translate("Form", u"Trap", None))
        self.curr_dist_btn.setText(QCoreApplication.translate("Form", u"\u0414\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u044f", None))
        self.curr_odds_btn.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442", None))
        self.curr_dog_weight_btn.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0441 \u0441\u043e\u0431\u0430\u043a\u0438", None))
        self.curr_race_grade_btn.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0433\u043e\u043d\u043a\u0438", None))
        self.select_all_B.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.categoria_B_label.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f B", None))
        self.fin_pos_hist_btn.setText(QCoreApplication.translate("Form", u"\u0424\u0438\u043d\u0438\u0448\u043d\u0430\u044f \u043f\u043e\u0437\u0438\u0446\u0438\u044f (avg)", None))
        self.race_all_btn.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b-\u0432\u043e \u0433\u043e\u043d\u043e\u043a", None))
        self.dist_by_btn.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0441\u0442\u0430\u0432\u0430\u043d\u0438\u0435 \u043e\u0442 1-\u0433\u043e \u043c\u0435\u0441\u0442\u0430", None))
        self.race_all_curr_dist_btn.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b-\u0432\u043e \u0433\u043e\u043d\u043e\u043a \u043d\u0430 \u0434\u0430\u043d\u043d\u043e\u0439 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0438", None))
        self.fst_curr_dist_btn.setText(QCoreApplication.translate("Form", u"1-\u044b\u0445 \u043c\u0435\u0441\u0442 \u043d\u0430 \u0434\u0430\u043d\u043d\u043e\u0439 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0438", None))
        self.scd_curr_dist_btn.setText(QCoreApplication.translate("Form", u"2-\u044b\u0445 \u043c\u0435\u0441\u0442 \u043d\u0430 \u0434\u0430\u043d\u043d\u043e\u0439 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0438", None))
        self.thrd_curr_dist_btn.setText(QCoreApplication.translate("Form", u"3-\u044b\u0445 \u043c\u0435\u0441\u0442 \u043d\u0430 \u0434\u0430\u043d\u043d\u043e\u0439 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0438", None))
        self.frth_curr_dist_btn.setText(QCoreApplication.translate("Form", u"4-\u044b\u0445 \u043c\u0435\u0441\u0442 \u043d\u0430 \u0434\u0430\u043d\u043d\u043e\u0439 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0438", None))
        self.ffth_curr_dist_btn.setText(QCoreApplication.translate("Form", u"5-\u044b\u0445 \u043c\u0435\u0441\u0442 \u043d\u0430 \u0434\u0430\u043d\u043d\u043e\u0439 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0438", None))
        self.sxth_curr_dist_btn.setText(QCoreApplication.translate("Form", u"6-\u044b\u0445 \u043c\u0435\u0441\u0442 \u043d\u0430 \u0434\u0430\u043d\u043d\u043e\u0439 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0438", None))
        self.fin_pos_curr_dist_btn.setText(QCoreApplication.translate("Form", u"\u0424\u0438\u043d\u0438\u0448\u043d\u0430\u044f \u043f\u043e\u0437\u0438\u0446\u0438\u044f \u043d\u0430 \u0434\u0430\u043d\u043d\u043e\u0439 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0438 (avg)", None))
        self.sec_time_curr_dist_btn.setText(QCoreApplication.translate("Form", u"Sectional time \u043d\u0430 \u0434\u0430\u043d\u043d\u043e\u0439 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0438 (avg)", None))
        self.dog_grade_curr_dist_btn.setText(QCoreApplication.translate("Form", u"\u041e\u0446\u0435\u043d\u043a\u0430 \u0441\u043e\u0431\u0430\u043a\u0438 \u043d\u0430 \u0434\u0430\u043d\u043d\u043e\u0439 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0438", None))
        self.best_run_time_curr_dist_btn.setText(QCoreApplication.translate("Form", u"\u041b\u0443\u0447\u0448\u0435\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0430 \u0434\u0430\u043d\u043d\u043e\u0439 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0438 ", None))
        self.best_sec_time_curr_dist_btn.setText(QCoreApplication.translate("Form", u"\u041b\u0443\u0447\u0448\u0435\u0435 sectional_time \u043d\u0430 \u0434\u0430\u043d\u043d\u043e\u0439 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0438", None))
        self.select_all_C.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0441\u0435", None))
    # retranslateUi

    def tuggle_all(self, mode):
        state = True

        if mode == 1:
            if not self.select_all_A.isChecked():
                state = False
            self.sec_time_btn.setChecked(state)
            self.fin_pos_btn.setChecked(state)
            self.trap_btn.setChecked(state)
            self.dist_btn.setChecked(state)
            self.adj_time_btn.setChecked(state)
            self.odds_btn.setChecked(state)
            self.run_time_btn.setChecked(state)
            self.dog_weight_btn.setChecked(state)
            self.win_time_btn.setChecked(state)

        elif mode == 2:
            if not self.select_all_B.isChecked():
                state = False
            self.curr_trap_btn.setChecked(state)
            self.curr_dist_btn.setChecked(state)
            self.curr_odds_btn.setChecked(state)
            self.curr_dog_weight_btn.setChecked(state)
            self.curr_race_grade_btn.setChecked(state)

        elif mode == 3:
            if not self.select_all_C.isChecked():
                state = False
            self.fin_pos_hist_btn.setChecked(state)
            self.race_all_btn.setChecked(state)
            self.dist_by_btn.setChecked(state)
            self.race_all_curr_dist_btn.setChecked(state)
            self.fst_curr_dist_btn.setChecked(state)
            self.scd_curr_dist_btn.setChecked(state)
            self.thrd_curr_dist_btn.setChecked(state)
            self.frth_curr_dist_btn.setChecked(state)
            self.ffth_curr_dist_btn.setChecked(state)
            self.sxth_curr_dist_btn.setChecked(state)
            self.fin_pos_curr_dist_btn.setChecked(state)
            self.sec_time_curr_dist_btn.setChecked(state)
            self.dog_grade_curr_dist_btn.setChecked(state)
            self.best_run_time_curr_dist_btn.setChecked(state)
            self.best_sec_time_curr_dist_btn.setChecked(state)

    def get_params(self):
        num = self.race_amount_spbox.value()
        params = []

        if self.sec_time_btn.isChecked():
            for i in range(1, num + 1):
                params.append(f'Hist_Race_Sec_Time_{i}')

        if self.fin_pos_btn.isChecked():
            for i in range(1, num + 1):
                params.append(f'Hist_Race_Finish_{i}')

        if self.trap_btn.isChecked():
            for i in range(1, num + 1):
                params.append(f'Hist_Race_Trap_{i}')

        if self.dist_btn.isChecked():
            for i in range(1, num + 1):
                params.append(f'Hist_Race_Dist_{i}')

        if self.adj_time_btn.isChecked():
            for i in range(1, num + 1):
                params.append(f'Hist_Race_Adj_Time_{i}')

        if self.odds_btn.isChecked():
            for i in range(1, num + 1):
                params.append(f'Hist_Race_Odds_{i}')

        if self.run_time_btn.isChecked():
            for i in range(1, num + 1):
                params.append(f'Hist_Race_Run_Time_{i}')

        if self.dog_weight_btn.isChecked():
            for i in range(1, num + 1):
                params.append(f'Hist_Race_Dog_Weight_{i}')

        if self.win_time_btn.isChecked():
            for i in range(1, num + 1):
                params.append(f'Hist_Race_Win_Time_{i}')


        if self.curr_trap_btn.isChecked():
            params.append('Trap')
        
        if self.curr_dist_btn.isChecked():
            params.append('Dist')

        if self.curr_dog_weight_btn.isChecked():
            params.append('Dog_weight')

        if self.curr_odds_btn.isChecked():
            params.append('Odds')

        if self.curr_race_grade_btn.isChecked():
            params.append('Grade_Name')

        
        if self.fin_pos_curr_dist_btn.isChecked():
            params.append('Finish_Curr_Dist')

        if self.race_all_btn.isChecked():
            params.append('Races_All')

        if self.dist_by_btn.isChecked():
            params.append('Dist_by')

        if self.race_all_curr_dist_btn.isChecked():
            params.append('Races_Curr_Dist')

        if self.fst_curr_dist_btn.isChecked():
            params.append('Wins_Curr_Dist')

        if self.scd_curr_dist_btn.isChecked():
            params.append('Second_Curr_Dist')

        if self.thrd_curr_dist_btn.isChecked():
            params.append('Third_Curr_Dist')

        if self.frth_curr_dist_btn.isChecked():
            params.append('Fourth_Curr_Dist')

        if self.ffth_curr_dist_btn.isChecked():
            params.append('Fifth_Curr_Dist')

        if self.sxth_curr_dist_btn.isChecked():
            params.append('Sixth_Curr_Dist')

        if self.fin_pos_hist_btn.isChecked():
            params.append('Finish_All')

        if self.sec_time_curr_dist_btn.isChecked():
            params.append('Sec_Curr_Dist')

        if self.dog_grade_curr_dist_btn.isChecked():
            params.append('Grade_Curr_Dist')

        if self.best_run_time_curr_dist_btn.isChecked():
            params.append('Best_Time_Curr_Dist')

        if self.best_sec_time_curr_dist_btn.isChecked():
            params.append('Best_Sec_Time_Curr_Dist')

        return params

