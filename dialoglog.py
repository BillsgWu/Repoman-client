# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialoglog.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(660, 390)
        self.date = QtWidgets.QLineEdit(Dialog)
        self.date.setGeometry(QtCore.QRect(450, 360, 150, 30))
        self.date.setObjectName("date")
        self.type = QtWidgets.QComboBox(Dialog)
        self.type.setGeometry(QtCore.QRect(0, 360, 150, 30))
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.good = QtWidgets.QComboBox(Dialog)
        self.good.setGeometry(QtCore.QRect(150, 360, 150, 30))
        self.good.setObjectName("good")
        self.count = QtWidgets.QSpinBox(Dialog)
        self.count.setGeometry(QtCore.QRect(300, 360, 150, 30))
        self.count.setMaximum(2147483647)
        self.count.setObjectName("count")
        self.bquery = QtWidgets.QPushButton(Dialog)
        self.bquery.setGeometry(QtCore.QRect(600, 360, 60, 30))
        self.bquery.setObjectName("bquery")
        self.log = QtWidgets.QTableWidget(Dialog)
        self.log.setGeometry(QtCore.QRect(0, 0, 660, 360))
        self.log.setObjectName("log")
        self.log.setColumnCount(5)
        self.log.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.log.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.log.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.log.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.log.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.log.setHorizontalHeaderItem(4, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.date.setPlaceholderText(_translate("Dialog", "日期yyyy/mm/dd"))
        self.type.setItemText(0, _translate("Dialog", "全部"))
        self.type.setItemText(1, _translate("Dialog", "进库"))
        self.type.setItemText(2, _translate("Dialog", "出库"))
        self.bquery.setText(_translate("Dialog", "查询"))
        item = self.log.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.log.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "操作"))
        item = self.log.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "日期"))
        item = self.log.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "货物"))
        item = self.log.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "数量"))
