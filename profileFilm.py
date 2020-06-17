# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profileFilm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(740, 454)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("images/logo3.png"))
        self.logo.setScaledContents(False)
        self.logo.setObjectName("logo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.logo)
        self.headTitle = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.headTitle.setFont(font)
        self.headTitle.setFrameShape(QtWidgets.QFrame.Panel)
        self.headTitle.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.headTitle.setObjectName("headTitle")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.headTitle)
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 8, 1, 1, 1)
        self.director = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.director.sizePolicy().hasHeightForWidth())
        self.director.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.director.setFont(font)
        self.director.setObjectName("director")
        self.gridLayout_2.addWidget(self.director, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 3, 1, 1)
        self.actors = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actors.sizePolicy().hasHeightForWidth())
        self.actors.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.actors.setFont(font)
        self.actors.setObjectName("actors")
        self.gridLayout_2.addWidget(self.actors, 9, 0, 1, 1)
        self.score = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.score.setFont(font)
        self.score.setObjectName("score")
        self.gridLayout_2.addWidget(self.score, 5, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 6, 1, 1, 1)
        self.year = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.year.setFont(font)
        self.year.setObjectName("year")
        self.gridLayout_2.addWidget(self.year, 7, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)
        self.actorsTable = QtWidgets.QTableWidget(self.widget)
        self.actorsTable.setObjectName("actorsTable")
        self.actorsTable.setColumnCount(3)
        self.actorsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.actorsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.actorsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.actorsTable.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.actorsTable, 10, 0, 1, 1)
        self.screenwriter = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenwriter.sizePolicy().hasHeightForWidth())
        self.screenwriter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.screenwriter.setFont(font)
        self.screenwriter.setObjectName("screenwriter")
        self.gridLayout_2.addWidget(self.screenwriter, 3, 0, 1, 1)
        self.composer = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.composer.sizePolicy().hasHeightForWidth())
        self.composer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.composer.setFont(font)
        self.composer.setObjectName("composer")
        self.gridLayout_2.addWidget(self.composer, 5, 0, 1, 1)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.widget)
        self.line_8 = QtWidgets.QFrame(Form)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_8)
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.headTitle.setText(_translate("Form", "Фильм"))
        self.director.setText(_translate("Form", "Режиссёр"))
        self.pushButton.setText(_translate("Form", "Редактировать"))
        self.actors.setText(_translate("Form", "Люди"))
        self.score.setText(_translate("Form", "Рейтинг"))
        self.label_9.setText(_translate("Form", "Сборы"))
        self.year.setText(_translate("Form", "Год выхода"))
        self.label_8.setText(_translate("Form", "Бюджет"))
        item = self.actorsTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Имя"))
        item = self.actorsTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Должность"))
        item = self.actorsTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Зарплата"))
        self.screenwriter.setText(_translate("Form", "Сценарист"))
        self.composer.setText(_translate("Form", "Композитор"))
