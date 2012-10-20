# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youdao.ui'
#
# Created: Fri Oct 19 12:30:23 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_winMain(object):
    def setupUi(self, winMain):
        winMain.setObjectName(_fromUtf8("winMain"))
        winMain.setWindowModality(QtCore.Qt.NonModal)
        winMain.resize(156, 126)
        winMain.setMouseTracking(True)
        self.centralwidget = QtGui.QWidget(winMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.txtSend = QtGui.QLineEdit(self.centralwidget)
        self.txtSend.setGeometry(QtCore.QRect(0, 0, 101, 27))
        self.txtSend.setObjectName(_fromUtf8("txtSend"))
        self.btnSend = QtGui.QPushButton(self.centralwidget)
        self.btnSend.setGeometry(QtCore.QRect(110, 0, 41, 27))
        self.btnSend.setObjectName(_fromUtf8("btnSend"))
        self.labresult = QtGui.QLabel(self.centralwidget)
        self.labresult.setGeometry(QtCore.QRect(0, 27, 171, 101))
        self.labresult.setText(_fromUtf8(""))
        self.labresult.setObjectName(_fromUtf8("labresult"))
        winMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(winMain)
        QtCore.QMetaObject.connectSlotsByName(winMain)

    def retranslateUi(self, winMain):
        winMain.setWindowTitle(QtGui.QApplication.translate("winMain", "youdao", None, QtGui.QApplication.UnicodeUTF8))
        self.txtSend.setPlaceholderText(QtGui.QApplication.translate("winMain", "中<->英", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSend.setText(QtGui.QApplication.translate("winMain", "翻译", None, QtGui.QApplication.UnicodeUTF8))


