# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow_rev01.ui'
#
# Created: Tue Apr 01 22:16:02 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username = QtGui.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(20, 40, 201, 21))
        self.username.setObjectName("username")
        self.firstName = QtGui.QLineEdit(self.centralwidget)
        self.firstName.setGeometry(QtCore.QRect(20, 80, 201, 21))
        self.firstName.setObjectName("firstName")
        self.address = QtGui.QLineEdit(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(250, 80, 201, 21))
        self.address.setObjectName("address")
        self.phoneNumber = QtGui.QLineEdit(self.centralwidget)
        self.phoneNumber.setGeometry(QtCore.QRect(250, 40, 201, 21))
        self.phoneNumber.setObjectName("phoneNumber")
        self.mainTable = QtGui.QTableWidget(self.centralwidget)
        self.mainTable.setGeometry(QtCore.QRect(20, 130, 751, 391))
        self.mainTable.setObjectName("mainTable")
        self.mainTable.setColumnCount(5)
        self.mainTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(4, item)
        self.mainTable.horizontalHeader().setStretchLastSection(True)
        self.addData = QtGui.QPushButton(self.centralwidget)
        self.addData.setGeometry(QtCore.QRect(700, 80, 75, 23))
        self.addData.setObjectName("addData")
        self.removeRow = QtGui.QPushButton(self.centralwidget)
        self.removeRow.setGeometry(QtCore.QRect(700, 40, 75, 23))
        self.removeRow.setObjectName("removeRow")
        self.approved = QtGui.QCheckBox(self.centralwidget)
        self.approved.setGeometry(QtCore.QRect(470, 80, 101, 17))
        self.approved.setObjectName("approved")
        mainWindow.setCentralWidget(self.centralwidget)
        self.mainMenuBar = QtGui.QMenuBar(mainWindow)
        self.mainMenuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.mainMenuBar.setObjectName("mainMenuBar")
        self.menuFile = QtGui.QMenu(self.mainMenuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.mainMenuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtGui.QMenu(self.mainMenuBar)
        self.menuHelp.setObjectName("menuHelp")
        mainWindow.setMenuBar(self.mainMenuBar)
        self.mainStatusBar = QtGui.QStatusBar(mainWindow)
        self.mainStatusBar.setObjectName("mainStatusBar")
        mainWindow.setStatusBar(self.mainStatusBar)
        self.mainToolBar = QtGui.QToolBar(mainWindow)
        self.mainToolBar.setMovable(False)
        self.mainToolBar.setObjectName("mainToolBar")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.actionExport = QtGui.QAction(mainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionImport = QtGui.QAction(mainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExit = QtGui.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionPreferences = QtGui.QAction(mainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionAbout = QtGui.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.mainMenuBar.addAction(self.menuFile.menuAction())
        self.mainMenuBar.addAction(self.menuEdit.menuAction())
        self.mainMenuBar.addAction(self.menuHelp.menuAction())
        self.mainToolBar.addAction(self.actionImport)
        self.mainToolBar.addAction(self.actionExport)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionPreferences)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionAbout)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "PyDataMan 0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.username.setPlaceholderText(QtGui.QApplication.translate("mainWindow", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.firstName.setPlaceholderText(QtGui.QApplication.translate("mainWindow", "First Name", None, QtGui.QApplication.UnicodeUTF8))
        self.address.setPlaceholderText(QtGui.QApplication.translate("mainWindow", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.phoneNumber.setPlaceholderText(QtGui.QApplication.translate("mainWindow", "Phone Number", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("mainWindow", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("mainWindow", "First Name", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("mainWindow", "Phone Number", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTable.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("mainWindow", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTable.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("mainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.addData.setText(QtGui.QApplication.translate("mainWindow", "Add Data", None, QtGui.QApplication.UnicodeUTF8))
        self.removeRow.setText(QtGui.QApplication.translate("mainWindow", "Remove Row", None, QtGui.QApplication.UnicodeUTF8))
        self.approved.setText(QtGui.QApplication.translate("mainWindow", "User approved", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("mainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("mainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("mainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.mainToolBar.setWindowTitle(QtGui.QApplication.translate("mainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("mainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("mainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("mainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("mainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("mainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

