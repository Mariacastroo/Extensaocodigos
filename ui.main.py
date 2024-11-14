# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela1.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QColumnView, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QTabWidget, QTextEdit, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(860, 621)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_Home = QPushButton(self.frame)
        self.btn_Home.setObjectName(u"btn_Home")
        self.btn_Home.setGeometry(QRect(10, 20, 75, 23))
        self.btn_tabelas = QPushButton(self.frame)
        self.btn_tabelas.setObjectName(u"btn_tabelas")
        self.btn_tabelas.setGeometry(QRect(140, 20, 75, 23))
        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setGeometry(QRect(300, 20, 75, 23))
        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setGeometry(QRect(470, 20, 75, 23))
        self.btn_outro = QPushButton(self.frame)
        self.btn_outro.setObjectName(u"btn_outro")
        self.btn_outro.setGeometry(QRect(640, 20, 75, 23))
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 60, 811, 501))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.tabWidget = QTabWidget(self.page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 761, 511))
        self.tabelas = QWidget()
        self.tabelas.setObjectName(u"tabelas")
        self.verticalLayoutWidget_2 = QWidget(self.tabelas)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(40, 80, 451, 181))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.treeWidget = QTreeWidget(self.verticalLayoutWidget_2)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_4.addWidget(self.treeWidget)

        self.verticalLayoutWidget_3 = QWidget(self.tabelas)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(40, 280, 451, 161))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.treeWidget_2 = QTreeWidget(self.verticalLayoutWidget_3)
        self.treeWidget_2.setObjectName(u"treeWidget_2")

        self.verticalLayout_5.addWidget(self.treeWidget_2)

        self.verticalLayoutWidget_4 = QWidget(self.tabelas)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(530, 90, 201, 251))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.verticalLayoutWidget_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_importar = QPushButton(self.frame_2)
        self.btn_importar.setObjectName(u"btn_importar")

        self.verticalLayout_2.addWidget(self.btn_importar)

        self.btn_gerasaida = QPushButton(self.frame_2)
        self.btn_gerasaida.setObjectName(u"btn_gerasaida")

        self.verticalLayout_2.addWidget(self.btn_gerasaida)

        self.btn_extorno = QPushButton(self.frame_2)
        self.btn_extorno.setObjectName(u"btn_extorno")

        self.verticalLayout_2.addWidget(self.btn_extorno)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.horizontalLayoutWidget = QWidget(self.tabelas)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 10, 711, 73))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout.addWidget(self.textEdit)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.tabWidget.addTab(self.tabelas, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.columnView = QColumnView(self.page_2)
        self.columnView.setObjectName(u"columnView")
        self.columnView.setGeometry(QRect(40, 20, 711, 381))
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 40, 691, 251))
        self.horizontalLayoutWidget_6 = QWidget(self.page_2)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(50, 420, 691, 41))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.horizontalLayoutWidget_6)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.label_11 = QLabel(self.horizontalLayoutWidget_6)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayoutWidget_3 = QWidget(self.page_3)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(180, 182, 371, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.textEdit_6 = QTextEdit(self.horizontalLayoutWidget_3)
        self.textEdit_6.setObjectName(u"textEdit_6")

        self.horizontalLayout_3.addWidget(self.textEdit_6)

        self.horizontalLayoutWidget_4 = QWidget(self.page_3)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(180, 252, 371, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.horizontalLayoutWidget_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.textEdit_4 = QTextEdit(self.horizontalLayoutWidget_4)
        self.textEdit_4.setObjectName(u"textEdit_4")

        self.horizontalLayout_4.addWidget(self.textEdit_4)

        self.horizontalLayoutWidget_5 = QWidget(self.page_3)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(180, 312, 371, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.textEdit_5 = QTextEdit(self.horizontalLayoutWidget_5)
        self.textEdit_5.setObjectName(u"textEdit_5")

        self.horizontalLayout_5.addWidget(self.textEdit_5)

        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(290, 20, 401, 21))
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(320, 70, 101, 16))
        self.label_12 = QLabel(self.page_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(180, 490, 47, 59))
        self.horizontalLayoutWidget_7 = QWidget(self.page_3)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(180, 100, 371, 41))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.horizontalLayoutWidget_7)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_7.addWidget(self.label_13)

        self.textEdit_3 = QTextEdit(self.horizontalLayoutWidget_7)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.horizontalLayout_7.addWidget(self.textEdit_3)

        self.horizontalLayoutWidget_2 = QWidget(self.page_3)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(300, 350, 131, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.comboBox = QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.horizontalLayoutWidget_8 = QWidget(self.page_3)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(250, 400, 241, 51))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.horizontalLayoutWidget_8)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_8.addWidget(self.label_14)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget_8)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_8.addWidget(self.pushButton_3)

        self.label_15 = QLabel(self.horizontalLayoutWidget_8)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_8.addWidget(self.label_15)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_tabelas.setText(QCoreApplication.translate("MainWindow", u"Tabelas", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre ", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.btn_outro.setText(QCoreApplication.translate("MainWindow", u"Outro", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Valor Nife", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Especie", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"quantidade ", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Cod item", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Municipio", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Serie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"1", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SAIDA", None))
        ___qtreewidgetitem1 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"usuario", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Data da importa\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Nife", None));
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u" Importar ", None))
        self.btn_gerasaida.setText(QCoreApplication.translate("MainWindow", u"Gerar saida", None))
        self.btn_extorno.setText(QCoreApplication.translate("MainWindow", u"Estorno", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"abrir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabelas), QCoreApplication.translate("MainWindow", u"TreeWiget", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:48pt;\"> Bem-vindo ao Sistema </span></p><p><span style=\" font-size:48pt;\">de gerenciamento</span></p></body></html>", None))
        self.label_10.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"cadastrar", None))
        self.label_11.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"confirma\u00e7ao de senhal", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">tela de cadastro</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Cadastro Usuario", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Nome</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>   Perfil</p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Admnistrador", None))

        self.label_14.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"cadastrar", None))
        self.label_15.setText("")
    # retranslateUi

