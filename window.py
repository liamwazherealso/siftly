# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sun Jan  4 01:29:11 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Siftly(object):
    def setupUi(self, Siftly):
        Siftly.setObjectName(_fromUtf8("Siftly"))
        Siftly.resize(965, 672)
        self.centralwidget = QtGui.QWidget(Siftly)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Sort = QtGui.QWidget()
        self.Sort.setObjectName(_fromUtf8("Sort"))
        self.gridLayout_3 = QtGui.QGridLayout(self.Sort)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_2 = QtGui.QLabel(self.Sort)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.sift_folder = QtGui.QLineEdit(self.Sort)
        self.sift_folder.setObjectName(_fromUtf8("sift_folder"))
        self.gridLayout_3.addWidget(self.sift_folder, 1, 0, 1, 1)
        self.sift_btn_select_folder = QtGui.QPushButton(self.Sort)
        self.sift_btn_select_folder.setObjectName(_fromUtf8("sift_btn_select_folder"))
        self.gridLayout_3.addWidget(self.sift_btn_select_folder, 1, 1, 1, 1)
        self.sift_btn = QtGui.QPushButton(self.Sort)
        self.sift_btn.setObjectName(_fromUtf8("sift_btn"))
        self.gridLayout_3.addWidget(self.sift_btn, 2, 0, 1, 2)
        self.line = QtGui.QFrame(self.Sort)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 3, 0, 1, 2)
        self.label = QtGui.QLabel(self.Sort)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 4, 0, 1, 1)
        self.sift_latest_log = QtGui.QTextBrowser(self.Sort)
        self.sift_latest_log.setObjectName(_fromUtf8("sift_latest_log"))
        self.gridLayout_3.addWidget(self.sift_latest_log, 5, 0, 1, 2)
        self.tabWidget.addTab(self.Sort, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.logs_dump = QtGui.QPushButton(self.tab)
        self.logs_dump.setObjectName(_fromUtf8("logs_dump"))
        self.verticalLayout_3.addWidget(self.logs_dump)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        Siftly.setCentralWidget(self.centralwidget)

        self.retranslateUi(Siftly)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Siftly)

    def retranslateUi(self, Siftly):
        Siftly.setWindowTitle(_translate("Siftly", "Siftly", None))
        self.label_2.setText(_translate("Siftly", "Folder to Sift", None))
        self.sift_btn_select_folder.setText(_translate("Siftly", "Select File", None))
        self.sift_btn.setText(_translate("Siftly", "Sift", None))
        self.label.setText(_translate("Siftly", "Latest Log", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Sort), _translate("Siftly", "Sort", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Siftly", "Settings", None))
        self.logs_dump.setText(_translate("Siftly", "Dump Logs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Siftly", "Logs", None))

