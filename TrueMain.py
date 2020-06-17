# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrueMain.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(794, 484)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        Form.setFont(font)
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo3.png"))
        self.logo.setScaledContents(False)
        self.logo.setObjectName("logo")
        self.gridLayout_4.addWidget(self.logo, 0, 0, 1, 1)
        self.Find = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.Find.setFont(font)
        self.Find.setObjectName("Find")
        self.gridLayout_4.addWidget(self.Find, 0, 2, 1, 1)
        self.ObjectName = QtWidgets.QLineEdit(Form)
        self.ObjectName.setMinimumSize(QtCore.QSize(0, 20))
        self.ObjectName.setText("")
        self.ObjectName.setMaxLength(32771)
        self.ObjectName.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.ObjectName.setObjectName("ObjectName")
        self.gridLayout_4.addWidget(self.ObjectName, 0, 1, 1, 1)
        self.mainTable = QtWidgets.QTabWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mainTable.setFont(font)
        self.mainTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainTable.setAutoFillBackground(False)
        self.mainTable.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.mainTable.setIconSize(QtCore.QSize(16, 16))
        self.mainTable.setElideMode(QtCore.Qt.ElideRight)
        self.mainTable.setDocumentMode(False)
        self.mainTable.setTabsClosable(False)
        self.mainTable.setMovable(False)
        self.mainTable.setTabBarAutoHide(False)
        self.mainTable.setObjectName("mainTable")
        self.Archieve = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.Archieve.setFont(font)
        self.Archieve.setObjectName("Archieve")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Archieve)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.filmTab = QtWidgets.QTableWidget(self.Archieve)
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.filmTab.setFont(font)
        self.filmTab.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.filmTab.setFrameShadow(QtWidgets.QFrame.Raised)
        self.filmTab.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.filmTab.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.filmTab.setObjectName("filmTab")
        self.filmTab.setColumnCount(9)
        self.filmTab.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.header = self.filmTab.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(8, QtWidgets.QHeaderView.Stretch)
        self.filmTab.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.filmTab.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.filmTab.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.filmTab.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.filmTab.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.filmTab.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.filmTab.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.filmTab.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.filmTab.setHorizontalHeaderItem(8, item)
        self.gridLayout_3.addWidget(self.filmTab, 1, 0, 1, 1)
        self.filmButtonsWidget = QtWidgets.QWidget(self.Archieve)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filmButtonsWidget.sizePolicy().hasHeightForWidth())
        self.filmButtonsWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.filmButtonsWidget.setFont(font)
        self.filmButtonsWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.filmButtonsWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.filmButtonsWidget.setAcceptDrops(False)
        self.filmButtonsWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.filmButtonsWidget.setObjectName("filmButtonsWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.filmButtonsWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filmCreate = QtWidgets.QToolButton(self.filmButtonsWidget)
        self.filmCreate.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filmCreate.sizePolicy().hasHeightForWidth())
        self.filmCreate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.filmCreate.setFont(font)
        self.filmCreate.setIconSize(QtCore.QSize(32, 32))
        self.filmCreate.setShortcut("")
        self.filmCreate.setCheckable(False)
        self.filmCreate.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.filmCreate.setAutoRaise(False)
        self.filmCreate.setObjectName("filmCreate")
        self.horizontalLayout.addWidget(self.filmCreate)
        self.filmEdit = QtWidgets.QToolButton(self.filmButtonsWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.filmEdit.setFont(font)
        self.filmEdit.setObjectName("filmEdit")
        self.horizontalLayout.addWidget(self.filmEdit)
        self.filmDelete = QtWidgets.QPushButton(self.filmButtonsWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setBold(False)
        font.setWeight(50)
        self.filmDelete.setFont(font)
        self.filmDelete.setObjectName("filmDelete")
        self.horizontalLayout.addWidget(self.filmDelete)
        self.gridLayout_3.addWidget(self.filmButtonsWidget, 0, 0, 1, 1)
        self.mainTable.addTab(self.Archieve, "")
        self.CreatingTab = QtWidgets.QWidget()
        self.CreatingTab.setObjectName("CreatingTab")
        self.gridLayout = QtWidgets.QGridLayout(self.CreatingTab)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.CreatingTab)
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tableWidget_2, 1, 0, 1, 1)
        self.progressButtonsWidget = QtWidgets.QWidget(self.CreatingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressButtonsWidget.sizePolicy().hasHeightForWidth())
        self.progressButtonsWidget.setSizePolicy(sizePolicy)
        self.progressButtonsWidget.setObjectName("progressButtonsWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.progressButtonsWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressEdit = QtWidgets.QToolButton(self.progressButtonsWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.progressEdit.setFont(font)
        self.progressEdit.setObjectName("progressEdit")
        self.gridLayout_2.addWidget(self.progressEdit, 0, 1, 1, 1)
        self.progressCreate = QtWidgets.QToolButton(self.progressButtonsWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.progressCreate.setFont(font)
        self.progressCreate.setObjectName("progressCreate")
        self.gridLayout_2.addWidget(self.progressCreate, 0, 0, 1, 1)
        self.progressDelete = QtWidgets.QPushButton(self.progressButtonsWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.progressDelete.setFont(font)
        self.progressDelete.setObjectName("progressDelete")
        self.gridLayout_2.addWidget(self.progressDelete, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.progressButtonsWidget, 0, 0, 1, 1)
        self.mainTable.addTab(self.CreatingTab, "")
        self.PlanTab = QtWidgets.QWidget()
        self.PlanTab.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.PlanTab.setObjectName("PlanTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.PlanTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.PlanTab)
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_3.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_3.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_3.setCornerButtonEnabled(True)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        self.gridLayout_6.addWidget(self.tableWidget_3, 1, 0, 1, 1)
        self.planButtons = QtWidgets.QWidget(self.PlanTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.planButtons.sizePolicy().hasHeightForWidth())
        self.planButtons.setSizePolicy(sizePolicy)
        self.planButtons.setObjectName("planButtons")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.planButtons)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.planCreate = QtWidgets.QToolButton(self.planButtons)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.planCreate.setFont(font)
        self.planCreate.setObjectName("planCreate")
        self.gridLayout_11.addWidget(self.planCreate, 0, 0, 1, 1)
        self.planEdit = QtWidgets.QToolButton(self.planButtons)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.planEdit.setFont(font)
        self.planEdit.setObjectName("planEdit")
        self.gridLayout_11.addWidget(self.planEdit, 0, 1, 1, 1)
        self.planDelete = QtWidgets.QPushButton(self.planButtons)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.planDelete.setFont(font)
        self.planDelete.setObjectName("planDelete")
        self.gridLayout_11.addWidget(self.planDelete, 0, 2, 1, 1)
        self.gridLayout_6.addWidget(self.planButtons, 0, 0, 1, 1)
        self.mainTable.addTab(self.PlanTab, "")
        self.PeopleTab = QtWidgets.QWidget()
        self.PeopleTab.setObjectName("PeopleTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.PeopleTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.peopleTabInTab = QtWidgets.QTabWidget(self.PeopleTab)
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.peopleTabInTab.setFont(font)
        self.peopleTabInTab.setFocusPolicy(QtCore.Qt.TabFocus)
        self.peopleTabInTab.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.peopleTabInTab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.peopleTabInTab.setAutoFillBackground(False)
        self.peopleTabInTab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.peopleTabInTab.setDocumentMode(False)
        self.peopleTabInTab.setTabsClosable(False)
        self.peopleTabInTab.setTabBarAutoHide(False)
        self.peopleTabInTab.setObjectName("peopleTabInTab")
        self.actor = QtWidgets.QWidget()
        self.actor.setObjectName("actor")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.actor)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.actorTable = QtWidgets.QTableWidget(self.actor)
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actorTable.setFont(font)
        self.actorTable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.actorTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.actorTable.setObjectName("actorTable")
        self.actorTable.setColumnCount(6)
        self.actorTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.actorTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.actorTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.actorTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.actorTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.actorTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.actorTable.setHorizontalHeaderItem(5, item)
        self.gridLayout_7.addWidget(self.actorTable, 1, 0, 1, 1)
        self.actorButtonsWidget = QtWidgets.QWidget(self.actor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actorButtonsWidget.sizePolicy().hasHeightForWidth())
        self.actorButtonsWidget.setSizePolicy(sizePolicy)
        self.actorButtonsWidget.setObjectName("actorButtonsWidget")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.actorButtonsWidget)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.actorCreate = QtWidgets.QToolButton(self.actorButtonsWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.actorCreate.setFont(font)
        self.actorCreate.setObjectName("actorCreate")
        self.gridLayout_12.addWidget(self.actorCreate, 0, 0, 1, 1)
        self.actorEdit = QtWidgets.QToolButton(self.actorButtonsWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.actorEdit.setFont(font)
        self.actorEdit.setObjectName("actorEdit")
        self.gridLayout_12.addWidget(self.actorEdit, 0, 1, 1, 1)
        self.actorDelete = QtWidgets.QPushButton(self.actorButtonsWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.actorDelete.setFont(font)
        self.actorDelete.setObjectName("actorDelete")
        self.gridLayout_12.addWidget(self.actorDelete, 0, 2, 1, 1)
        self.gridLayout_7.addWidget(self.actorButtonsWidget, 0, 0, 1, 1)
        self.peopleTabInTab.addTab(self.actor, "")
        self.director = QtWidgets.QWidget()
        self.director.setObjectName("director")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.director)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.directorTable = QtWidgets.QTableWidget(self.director)
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.directorTable.setFont(font)
        self.directorTable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.directorTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.directorTable.setObjectName("directorTable")
        self.directorTable.setColumnCount(5)
        self.directorTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.directorTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.directorTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.directorTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.directorTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.directorTable.setHorizontalHeaderItem(4, item)
        self.gridLayout_8.addWidget(self.directorTable, 1, 0, 1, 1)
        self.directorButtonsWidget = QtWidgets.QWidget(self.director)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directorButtonsWidget.sizePolicy().hasHeightForWidth())
        self.directorButtonsWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.directorButtonsWidget.setFont(font)
        self.directorButtonsWidget.setObjectName("directorButtonsWidget")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.directorButtonsWidget)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.directorEdit = QtWidgets.QToolButton(self.directorButtonsWidget)
        self.directorEdit.setObjectName("directorEdit")
        self.gridLayout_13.addWidget(self.directorEdit, 0, 1, 1, 1)
        self.directorCreate = QtWidgets.QToolButton(self.directorButtonsWidget)
        self.directorCreate.setObjectName("directorCreate")
        self.gridLayout_13.addWidget(self.directorCreate, 0, 0, 1, 1)
        self.directorDelete = QtWidgets.QPushButton(self.directorButtonsWidget)
        self.directorDelete.setObjectName("directorDelete")
        self.gridLayout_13.addWidget(self.directorDelete, 0, 2, 1, 1)
        self.gridLayout_8.addWidget(self.directorButtonsWidget, 0, 0, 1, 1)
        self.peopleTabInTab.addTab(self.director, "")
        self.screenwriter = QtWidgets.QWidget()
        self.screenwriter.setObjectName("screenwriter")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.screenwriter)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.scrnTable = QtWidgets.QTableWidget(self.screenwriter)
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.scrnTable.setFont(font)
        self.scrnTable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrnTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.scrnTable.setObjectName("scrnTable")
        self.scrnTable.setColumnCount(5)
        self.scrnTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.scrnTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.scrnTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.scrnTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.scrnTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.scrnTable.setHorizontalHeaderItem(4, item)
        self.gridLayout_9.addWidget(self.scrnTable, 1, 0, 1, 1)
        self.scrwrtButtonsWidget = QtWidgets.QWidget(self.screenwriter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrwrtButtonsWidget.sizePolicy().hasHeightForWidth())
        self.scrwrtButtonsWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.scrwrtButtonsWidget.setFont(font)
        self.scrwrtButtonsWidget.setObjectName("scrwrtButtonsWidget")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.scrwrtButtonsWidget)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.scrnCreate = QtWidgets.QToolButton(self.scrwrtButtonsWidget)
        self.scrnCreate.setObjectName("scrnCreate")
        self.gridLayout_14.addWidget(self.scrnCreate, 0, 0, 1, 1)
        self.scrnEdit = QtWidgets.QToolButton(self.scrwrtButtonsWidget)
        self.scrnEdit.setObjectName("scrnEdit")
        self.gridLayout_14.addWidget(self.scrnEdit, 0, 1, 1, 1)
        self.scrnDelete = QtWidgets.QPushButton(self.scrwrtButtonsWidget)
        self.scrnDelete.setObjectName("scrnDelete")
        self.gridLayout_14.addWidget(self.scrnDelete, 0, 2, 1, 1)
        self.gridLayout_9.addWidget(self.scrwrtButtonsWidget, 0, 0, 1, 1)
        self.peopleTabInTab.addTab(self.screenwriter, "")
        self.composer = QtWidgets.QWidget()
        self.composer.setObjectName("composer")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.composer)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.compTable = QtWidgets.QTableWidget(self.composer)
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.compTable.setFont(font)
        self.compTable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.compTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.compTable.setObjectName("compTable")
        self.compTable.setColumnCount(5)
        self.compTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.compTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.compTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.compTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.compTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.compTable.setHorizontalHeaderItem(4, item)
        self.gridLayout_10.addWidget(self.compTable, 1, 0, 1, 1)
        self.compButtonsWidg = QtWidgets.QWidget(self.composer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compButtonsWidg.sizePolicy().hasHeightForWidth())
        self.compButtonsWidg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.compButtonsWidg.setFont(font)
        self.compButtonsWidg.setObjectName("compButtonsWidg")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.compButtonsWidg)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.compCreate = QtWidgets.QToolButton(self.compButtonsWidg)
        self.compCreate.setObjectName("compCreate")
        self.gridLayout_15.addWidget(self.compCreate, 0, 0, 1, 1)
        self.compEdit = QtWidgets.QToolButton(self.compButtonsWidg)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.compEdit.setFont(font)
        self.compEdit.setObjectName("compEdit")
        self.gridLayout_15.addWidget(self.compEdit, 0, 1, 1, 1)
        self.compDelete = QtWidgets.QPushButton(self.compButtonsWidg)
        self.compDelete.setObjectName("compDelete")
        self.gridLayout_15.addWidget(self.compDelete, 0, 2, 1, 1)
        self.gridLayout_10.addWidget(self.compButtonsWidg, 0, 0, 1, 1)
        self.peopleTabInTab.addTab(self.composer, "")
        self.gridLayout_5.addWidget(self.peopleTabInTab, 0, 0, 1, 1)
        self.mainTable.addTab(self.PeopleTab, "")
        self.gridLayout_4.addWidget(self.mainTable, 3, 0, 1, 4)
        self.found = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.found.setFont(font)
        self.found.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.found.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.found.setTextFormat(QtCore.Qt.PlainText)
        self.found.setScaledContents(False)
        self.found.setObjectName("found")
        self.gridLayout_4.addWidget(self.found, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.mainTable.setCurrentIndex(0)
        self.peopleTabInTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Find.setText(_translate("Form", "Найти"))
        self.ObjectName.setPlaceholderText(_translate("Form", "Введите фильм или человека"))
        self.filmTab.setSortingEnabled(True)
        item = self.filmTab.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Название"))
        item = self.filmTab.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Сборы"))
        item = self.filmTab.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Бюджет"))
        item = self.filmTab.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Рейтинг"))
        item = self.filmTab.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Год"))
        item = self.filmTab.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Режиссер"))
        item = self.filmTab.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Сценарист"))
        item = self.filmTab.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Композитор"))
        item = self.filmTab.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Актеры"))
        self.filmCreate.setText(_translate("Form", "Создать"))
        self.filmEdit.setText(_translate("Form", "Редактировать"))
        self.filmDelete.setText(_translate("Form", "Удалить"))
        self.mainTable.setTabText(self.mainTable.indexOf(self.Archieve), _translate("Form", "Снятые фильмы"))
        self.tableWidget_2.setSortingEnabled(True)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Название"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Бюджет"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Режиссер"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Сценарист"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Композитор"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Актеры"))
        self.progressEdit.setText(_translate("Form", "Редактировать"))
        self.progressCreate.setText(_translate("Form", "Создать"))
        self.progressDelete.setText(_translate("Form", "Удалить"))
        self.mainTable.setTabText(self.mainTable.indexOf(self.CreatingTab), _translate("Form", "В производстве"))
        self.tableWidget_3.setSortingEnabled(True)
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Название"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Замысел"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Тема"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Описание"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Примерный бюджет"))
        self.planCreate.setText(_translate("Form", "Создать"))
        self.planEdit.setText(_translate("Form", "Редактировать"))
        self.planDelete.setText(_translate("Form", "Удалить"))
        self.mainTable.setTabText(self.mainTable.indexOf(self.PlanTab), _translate("Form", "Планируемые фильмы"))
        self.actorTable.setSortingEnabled(True)
        item = self.actorTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Имя"))
        item = self.actorTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "e-mail"))
        item = self.actorTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Телефон"))
        item = self.actorTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Возраст"))
        item = self.actorTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Средняя зарплата"))
        item = self.actorTable.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Фильмы"))
        self.actorCreate.setText(_translate("Form", "Создать"))
        self.actorEdit.setText(_translate("Form", "Редактировать"))
        self.actorDelete.setText(_translate("Form", "Удалить"))
        self.peopleTabInTab.setTabText(self.peopleTabInTab.indexOf(self.actor), _translate("Form", "Актёр"))
        self.directorTable.setSortingEnabled(True)
        item = self.directorTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Имя"))
        item = self.directorTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "e-mail"))
        item = self.directorTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Телефон"))
        item = self.directorTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Средняя зарплата"))
        item = self.directorTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Фильмы"))
        self.directorEdit.setText(_translate("Form", "Редактировать"))
        self.directorCreate.setText(_translate("Form", "Создать"))
        self.directorDelete.setText(_translate("Form", "Удалить"))
        self.peopleTabInTab.setTabText(self.peopleTabInTab.indexOf(self.director), _translate("Form", "Режиссер"))
        self.scrnTable.setSortingEnabled(True)
        item = self.scrnTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Имя"))
        item = self.scrnTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "e-mail"))
        item = self.scrnTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Телефон"))
        item = self.scrnTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Средняя зарплата"))
        item = self.scrnTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Фильмы"))
        self.scrnCreate.setText(_translate("Form", "Создать"))
        self.scrnEdit.setText(_translate("Form", "Редактировать"))
        self.scrnDelete.setText(_translate("Form", "Удалить"))
        self.peopleTabInTab.setTabText(self.peopleTabInTab.indexOf(self.screenwriter), _translate("Form", "Сценарист"))
        self.compTable.setSortingEnabled(True)
        item = self.compTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Имя"))
        item = self.compTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "e-mail"))
        item = self.compTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Телефон"))
        item = self.compTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Средняя зарплата"))
        item = self.compTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Фильмы"))
        self.compCreate.setText(_translate("Form", "Создать"))
        self.compEdit.setText(_translate("Form", "Редактировать"))
        self.compDelete.setText(_translate("Form", "Удалить"))
        self.peopleTabInTab.setTabText(self.peopleTabInTab.indexOf(self.composer), _translate("Form", "Композитор"))
        self.mainTable.setTabText(self.mainTable.indexOf(self.PeopleTab), _translate("Form", "Люди"))
        self.found.setText(_translate("Form", "НАЙДЕНО"))
        self.pushButton.setText(_translate("Form", "Перейти"))
