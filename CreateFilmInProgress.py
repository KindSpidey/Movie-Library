# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateFilmInPlan.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(778, 452)
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
        self.logo.setPixmap(QtGui.QPixmap("logo3.png"))
        self.logo.setScaledContents(False)
        self.logo.setObjectName("logo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.logo)
        self.head = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.head.setFont(font)
        self.head.setFrameShape(QtWidgets.QFrame.Panel)
        self.head.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.head.setObjectName("head")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.head)
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.planningBudgetEdit = QtWidgets.QLineEdit(self.widget)
        self.planningBudgetEdit.setObjectName("planningBudgetEdit")
        self.gridLayout_2.addWidget(self.planningBudgetEdit, 2, 2, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.saveButton.setFont(font)
        self.saveButton.setDefault(True)
        self.saveButton.setFlat(False)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_2.addWidget(self.saveButton, 8, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)
        self.ideaEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ideaEdit.sizePolicy().hasHeightForWidth())
        self.ideaEdit.setSizePolicy(sizePolicy)
        self.ideaEdit.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.ideaEdit.setFont(font)
        self.ideaEdit.setObjectName("ideaEdit")
        self.gridLayout_2.addWidget(self.ideaEdit, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 7, 0, 1, 1)
        self.titleEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleEdit.sizePolicy().hasHeightForWidth())
        self.titleEdit.setSizePolicy(sizePolicy)
        self.titleEdit.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.titleEdit.setFont(font)
        self.titleEdit.setText("")
        self.titleEdit.setObjectName("titleEdit")
        self.gridLayout_2.addWidget(self.titleEdit, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)
        self.themeEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.themeEdit.sizePolicy().hasHeightForWidth())
        self.themeEdit.setSizePolicy(sizePolicy)
        self.themeEdit.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.themeEdit.setFont(font)
        self.themeEdit.setObjectName("themeEdit")
        self.gridLayout_2.addWidget(self.themeEdit, 6, 0, 1, 1)
        self.descriptionEdit = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.descriptionEdit.setFont(font)
        self.descriptionEdit.setFrameShape(QtWidgets.QFrame.Panel)
        self.descriptionEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.gridLayout_2.addWidget(self.descriptionEdit, 8, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 1, 1, 1)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.widget)
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label)
        self.makeInProgressFilmButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.makeInProgressFilmButton.sizePolicy().hasHeightForWidth())
        self.makeInProgressFilmButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.makeInProgressFilmButton.setFont(font)
        self.makeInProgressFilmButton.setDefault(True)
        self.makeInProgressFilmButton.setObjectName("makeInProgressFilmButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.makeInProgressFilmButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.head.setText(_translate("Form", "Добавление планируемого фильма"))
        self.saveButton.setText(_translate("Form", "Сохранить"))
        self.label_2.setText(_translate("Form", "Название фильма"))
        self.label_4.setText(_translate("Form", "Замысел"))
        self.label_5.setText(_translate("Form", "Тема"))
        self.ideaEdit.setPlaceholderText(_translate("Form", "В нескольких словах, о чем фильм?"))
        self.label_7.setText(_translate("Form", "Описание"))
        self.titleEdit.setPlaceholderText(_translate("Form", "Полное название фильма"))
        self.label_8.setText(_translate("Form", "Примерный бюджет"))
        self.themeEdit.setPlaceholderText(_translate("Form", "Его этические проблемы и темы"))
        self.descriptionEdit.setPlaceholderText(_translate("Form", "Любые ваши мысли насчет картины"))
        self.label.setText(_translate("Form", "Если фильм готов к производству, его можно перенести в снимаемые фильмы"))
        self.makeInProgressFilmButton.setText(_translate("Form", "Перевести фильм в снимаемые"))
