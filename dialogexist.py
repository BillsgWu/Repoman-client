# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogexist.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.goods = QtWidgets.QTableWidget(Dialog)
        self.goods.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.goods.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.goods.setObjectName("goods")
        self.goods.setColumnCount(7)
        self.goods.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.goods.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.goods.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.goods.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.goods.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.goods.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.goods.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.goods.setHorizontalHeaderItem(6, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "库存查询"))
        item = self.goods.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.goods.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "名称"))
        item = self.goods.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "标签"))
        item = self.goods.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "厂商"))
        item = self.goods.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "计数"))
        item = self.goods.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "下限"))
        item = self.goods.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "上限"))